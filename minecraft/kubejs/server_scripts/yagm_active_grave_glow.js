// ==========================================
// PEAK SERVER SCRIPT - YAGM ACTIVE GRAVE GLOW
// Event-driven glowing outline visible through walls strictly for active player graves.
// Decorative graves placed by players do not receive the glowing outline.
// ==========================================

const GLOW_TAG = 'yagm_grave_glow';
const GLOW_COLOR = 5636095; // Spectral cyan (0x55FFFF)

const activeGraveGlows = new Map();

let GraveDataManager = null;
let BlockPos = null;
let gravesField = null;

function initReflection() {
    if (GraveDataManager) return;
    try {
        GraveDataManager = Java.loadClass('it.hurts.sskirillss.yagm.data.gravedata.GraveDataManager');
        BlockPos = Java.loadClass('net.minecraft.core.BlockPos');
        gravesField = GraveDataManager.class.getDeclaredField('graves');
        gravesField.setAccessible(true);
    } catch (e) {
        // Reflection unavailable, event-based fallback will handle graves
    }
}

function getActiveGravePositions(serverLevel) {
    initReflection();
    let positions = [];
    if (!gravesField) return positions;
    try {
        let manager = GraveDataManager.get(serverLevel);
        if (!manager) return positions;
        let map = gravesField.get(manager);
        if (!map) return positions;
        let iter = map.values().iterator();
        while (iter.hasNext()) {
            let tag = iter.next();
            if (tag.contains('BlockPos', 4)) {
                positions.push(BlockPos.of(tag.getLong('BlockPos')));
            }
        }
    } catch (e) {}
    return positions;
}

function spawnDisplay(server, dim, x, y, z, blockId, facing, half) {
    let props = [];
    if (facing) props.push(`facing:"${facing}"`);
    if (half) props.push(`half:"${half}"`);
    let propsStr = props.length > 0 ? `,Properties:{${props.join(',')}}` : '';

    let cmd = `execute in ${dim} run summon minecraft:block_display ${x} ${y} ${z} {Tags:["${GLOW_TAG}"],Glowing:1b,glow_color_override:${GLOW_COLOR},block_state:{Name:"${blockId}"${propsStr}},transformation:{scale:[1.004f,1.004f,1.004f],translation:[-0.002f,-0.002f,-0.002f]}}`;
    server.runCommandSilent(cmd);
}

function spawnGlowAt(server, level, pos) {
    if (!level.isLoaded(pos)) return;

    let block = level.getBlock(pos);
    if (!block.id.startsWith('yagm:') || !block.id.includes('grave')) return;

    let be = level.getBlockEntity(pos);
    if (!be || be.isDecorative()) return;

    let dim = String(level.dimension.location ? level.dimension.location() : level.dimension);
    let posKey = `${dim}@${pos.x},${pos.y},${pos.z}`;
    if (activeGraveGlows.has(posKey)) return;

    let props = block.properties;
    let facing = props && props.facing ? props.facing : null;
    let half = props && props.half ? props.half : null;

    spawnDisplay(server, dim, pos.x, pos.y, pos.z, block.id, facing, half);
    activeGraveGlows.set(posKey, { dim: dim, x: pos.x, y: pos.y, z: pos.z });

    // For double-height graves (lower half), also spawn glow display for upper half
    if (half === 'lower') {
        let upperPos = pos.above();
        let upperBlock = level.getBlock(upperPos);
        if (upperBlock.id.startsWith('yagm:')) {
            let upperKey = `${dim}@${upperPos.x},${upperPos.y},${upperPos.z}`;
            spawnDisplay(server, dim, upperPos.x, upperPos.y, upperPos.z, upperBlock.id, facing, 'upper');
            activeGraveGlows.set(upperKey, { dim: dim, x: upperPos.x, y: upperPos.y, z: upperPos.z });
        }
    }
}

function removeGlowAt(level, pos) {
    let dim = String(level.dimension.location ? level.dimension.location() : level.dimension);
    let posKey = `${dim}@${pos.x},${pos.y},${pos.z}`;
    activeGraveGlows.delete(posKey);

    let upperKey = `${dim}@${pos.x},${pos.y + 1},${pos.z}`;
    activeGraveGlows.delete(upperKey);

    let AABB = Java.loadClass('net.minecraft.world.phys.AABB');
    let box = new AABB(pos.x - 0.5, pos.y - 0.5, pos.z - 0.5, pos.x + 1.5, pos.y + 2.5, pos.z + 1.5);
    let entities = level.getEntities(null, box);
    for (let i = 0; i < entities.length; i++) {
        let e = entities[i];
        if (e.tags.contains(GLOW_TAG)) {
            e.discard();
        }
    }
}

// 1. Player death listener - spawns glow when the grave block is created
EntityEvents.death(event => {
    if (!event.entity.isPlayer()) return;
    let player = event.entity;
    let server = player.server;
    let level = player.level;
    let deathPos = player.blockPosition();

    // Allow YAGM a brief 4-tick window to place the grave in world
    server.scheduleInTicks(4, () => {
        let spawned = false;

        // A. Check CemeteryManager for exact position of last placed grave
        try {
            let CemeteryManager = Java.loadClass('it.hurts.sskirillss.yagm.structure.cemetery.CemeteryManager');
            let ResourceKeyClass = Java.loadClass('net.minecraft.resources.ResourceKey');
            let RegistriesClass = Java.loadClass('net.minecraft.core.registries.Registries');
            let ResourceLocationClass = Java.loadClass('net.minecraft.resources.ResourceLocation');
            let dim = String(level.dimension.location ? level.dimension.location() : level.dimension);
            let dimKey = ResourceKeyClass.create(RegistriesClass.DIMENSION, ResourceLocationClass.parse(dim));
            let lastGravePos = CemeteryManager.getInstance().getLastAddedGrave(dimKey);
            if (lastGravePos && level.isLoaded(lastGravePos)) {
                let block = level.getBlock(lastGravePos);
                if (block.id.startsWith('yagm:') && block.id.includes('grave')) {
                    spawnGlowAt(server, level, lastGravePos);
                    spawned = true;
                }
            }
        } catch (e) {}

        // B. Check active graves from GraveDataManager
        if (!spawned) {
            let activePositions = getActiveGravePositions(level);
            for (let i = 0; i < activePositions.length; i++) {
                let pos = activePositions[i];
                if (level.isLoaded(pos)) {
                    spawnGlowAt(server, level, pos);
                    spawned = true;
                }
            }
        }

        // C. Fallback: Search in small radius around death position
        if (!spawned) {
            for (let dx = -2; dx <= 2; dx++) {
                for (let dy = -3; dy <= 3; dy++) {
                    for (let dz = -2; dz <= 2; dz++) {
                        let checkPos = deathPos.offset(dx, dy, dz);
                        let b = level.getBlock(checkPos);
                        if (b.id.startsWith('yagm:') && b.id.includes('grave')) {
                            spawnGlowAt(server, level, checkPos);
                        }
                    }
                }
            }
        }
    });
});

// 2. Right-click listener - removes glow when player collects their items
BlockEvents.rightClicked(event => {
    let block = event.block;
    if (block.id.startsWith('yagm:') && block.id.includes('grave')) {
        let pos = block.pos;
        let level = event.level;
        event.server.scheduleInTicks(2, () => {
            let be = level.getBlockEntity(pos);
            if (!be || be.isDecorative()) {
                removeGlowAt(level, pos);
            }
        });
    }
});

// 3. Block break listener - removes glow if grave is broken
BlockEvents.broken(event => {
    let block = event.block;
    if (block.id.startsWith('yagm:') && block.id.includes('grave')) {
        removeGlowAt(event.level, block.pos);
    }
});

// 4. Player login and respawn check - syncs active graves for the player
PlayerEvents.respawned(event => {
    let player = event.player;
    let server = player.server;
    let level = player.level;
    let positions = getActiveGravePositions(level);
    for (let i = 0; i < positions.length; i++) {
        spawnGlowAt(server, level, positions[i]);
    }
});

PlayerEvents.loggedIn(event => {
    let player = event.player;
    let server = player.server;
    let level = player.level;
    let positions = getActiveGravePositions(level);
    for (let i = 0; i < positions.length; i++) {
        spawnGlowAt(server, level, positions[i]);
    }
});

// 5. Lightweight cleanup heartbeat (runs once every 100 ticks = 5 seconds)
// Exits immediately if no active graves exist, ensuring zero performance overhead
ServerEvents.tick(event => {
    if (event.server.tickCount % 100 !== 0) return;
    if (activeGraveGlows.size === 0) return;

    let server = event.server;
    let BlockPosClass = Java.loadClass('net.minecraft.core.BlockPos');
    let ResourceKeyClass = Java.loadClass('net.minecraft.resources.ResourceKey');
    let RegistriesClass = Java.loadClass('net.minecraft.core.registries.Registries');
    let ResourceLocationClass = Java.loadClass('net.minecraft.resources.ResourceLocation');

    activeGraveGlows.forEach((data, key) => {
        let level = server.getLevel(ResourceKeyClass.create(RegistriesClass.DIMENSION, ResourceLocationClass.parse(data.dim)));
        if (!level) return;

        let pos = new BlockPosClass(data.x, data.y, data.z);
        if (!level.isLoaded(pos)) return;

        let block = level.getBlock(pos);
        let be = level.getBlockEntity(pos);
        if (!be && block.properties && block.properties.half === 'upper') {
            be = level.getBlockEntity(pos.below());
        }

        if (!block.id.startsWith('yagm:') || !block.id.includes('grave') || !be || be.isDecorative()) {
            removeGlowAt(level, pos);
        }
    });
});
