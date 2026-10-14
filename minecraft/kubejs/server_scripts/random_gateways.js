// ==========================================
// PEAK MODPACK — SCRIPT: RANDOM GATEWAYS
// Dynamic Overworld Gateway Spawning System
// ==========================================

const RG_DEFAULTS = {
    enabled: true,
    spawn_rate: 2,         // Daily base % and pity increment per failed roll (2%)
    spawn_day: 30,         // Guaranteed spawn threshold (30 days max)
    min_player_dist: 200,  // Minimum blocks from player
    max_player_dist: 500,  // Maximum blocks from player
    warning_seconds: 300,  // 5 minutes warning before gateway opens
    countdown_chat: true   // Broadcast countdown alerts at 200s, 100s, 20s, 5s
};

// Gateway catalog with metadata and display names
const RG_GATEWAYS = {
    'gateways:basic/slime': {
        id: 'gateways:basic/slime',
        name: 'Slime Gateway',
        color: '§a',
        hex: 0x55FF55
    },
    'gateways:basic/blaze': {
        id: 'gateways:basic/blaze',
        name: 'Blaze Gateway',
        color: '§6',
        hex: 0xFFAA00
    },
    'gateways:basic/enderman': {
        id: 'gateways:basic/enderman',
        name: 'Enderman Gateway',
        color: '§5',
        hex: 0xAA00AA
    },
    'gateways:emerald_grove': {
        id: 'gateways:emerald_grove',
        name: 'Gateway of the Emerald Grove',
        color: '§2',
        hex: 0x00AA00
    },
    'gateways:overworldian_nights': {
        id: 'gateways:overworldian_nights',
        name: 'Gateway of Overworldian Nights',
        color: '§9',
        hex: 0x5555FF
    },
    'gateways:hellish_fortress': {
        id: 'gateways:hellish_fortress',
        name: 'Gateway of the Hellish Fortress',
        color: '§4',
        hex: 0xAA0000
    },
    'gateways:endless/blaze': {
        id: 'gateways:endless/blaze',
        name: 'Endless Blaze Gateway',
        color: '§c',
        hex: 0xFF5555
    }
};

// ==========================================
// CONFIGURATION & STATE PERSISTENCE
// ==========================================

function getRGConfig(server) {
    let p = server.persistentData;
    if (!p.contains('rg_init')) {
        p.putBoolean('rg_init', true);
        p.putBoolean('rg_enabled', RG_DEFAULTS.enabled);
        p.putInt('rg_spawn_rate', RG_DEFAULTS.spawn_rate);
        p.putInt('rg_spawn_day', RG_DEFAULTS.spawn_day);
        p.putBoolean('rg_countdown_chat', RG_DEFAULTS.countdown_chat);
        p.putInt('rg_days_passed', 0);
        p.putInt('rg_current_pity', RG_DEFAULTS.spawn_rate);
    }

    return {
        enabled: p.getBoolean('rg_enabled'),
        spawn_rate: Math.max(1, p.getInt('rg_spawn_rate')),
        spawn_day: Math.max(1, p.getInt('rg_spawn_day')),
        countdown_chat: p.getBoolean('rg_countdown_chat'),
        days_passed: p.getInt('rg_days_passed'),
        current_pity: p.getInt('rg_current_pity'),
        scheduled: p.getBoolean('rg_scheduled'),
        active: p.getBoolean('rg_active')
    };
}

function isGatewayPendingOrActive(server) {
    let p = server.persistentData;
    return p.getBoolean('rg_scheduled') || p.getBoolean('rg_active');
}

// ==========================================
// DISTANCE-FROM-SPAWN SCALING LOGIC
// ==========================================

function selectGatewayForPos(overworld, targetX, targetZ) {
    let spawn = overworld.getSharedSpawnPos();
    let dist = Math.hypot(targetX - spawn.getX(), targetZ - spawn.getZ());

    let pool = [];

    if (dist < 2500) {
        // Tier 1: Near spawn (0 - 2,500 blocks)
        pool = [
            { id: 'gateways:basic/slime', weight: 50 },
            { id: 'gateways:basic/blaze', weight: 50 }
        ];
    } else if (dist < 5000) {
        // Tier 2: Mid-range (2,500 - 5,000 blocks)
        pool = [
            { id: 'gateways:basic/blaze', weight: 30 },
            { id: 'gateways:basic/enderman', weight: 35 },
            { id: 'gateways:emerald_grove', weight: 35 }
        ];
    } else if (dist < 10000) {
        // Tier 3: Far (5,000 - 10,000 blocks)
        pool = [
            { id: 'gateways:basic/enderman', weight: 20 },
            { id: 'gateways:emerald_grove', weight: 25 },
            { id: 'gateways:overworldian_nights', weight: 30 },
            { id: 'gateways:hellish_fortress', weight: 25 }
        ];
    } else {
        // Tier 4: Toughest / Endgame (> 10,000 blocks)
        // Finite hardest challenges (Endless Blaze excluded from random rotation as it never completes)
        pool = [
            { id: 'gateways:overworldian_nights', weight: 45 },
            { id: 'gateways:hellish_fortress', weight: 55 }
        ];
    }

    let totalWeight = pool.reduce((sum, item) => sum + item.weight, 0);
    let roll = Math.random() * totalWeight;
    let accumulated = 0;

    for (let item of pool) {
        accumulated += item.weight;
        if (roll <= accumulated) {
            return item.id;
        }
    }

    return pool[0].id;
}

// ==========================================
// SURFACE RAYCASTING & POSITIONING
// ==========================================

function findSurfacePos(level, originX, originZ, minRadius, maxRadius) {
    let Heightmap = Java.loadClass('net.minecraft.world.level.levelgen.Heightmap');
    let minBuildHeight = level.getMinBuildHeight ? level.getMinBuildHeight() : -64;
    let attempts = 25;

    for (let i = 0; i < attempts; i++) {
        let angle = Math.random() * Math.PI * 2;
        let dist = minRadius + Math.random() * (maxRadius - minRadius);
        let x = Math.floor(originX + dist * Math.cos(angle));
        let z = Math.floor(originZ + dist * Math.sin(angle));

        let topY = 64;
        try {
            topY = level.getHeight(Heightmap.Types.MOTION_BLOCKING_NO_LEAVES, x, z);
        } catch (e) {
            topY = 64;
        }

        if (topY <= minBuildHeight) {
            topY = 64;
        }

        // Search downward slightly if needed to find solid ground
        for (let checkY = topY; checkY >= Math.max(minBuildHeight + 2, topY - 12); checkY--) {
            let ground = level.getBlock(x, checkY - 1, z);
            let space1 = level.getBlock(x, checkY, z);
            let space2 = level.getBlock(x, checkY + 1, z);

            if (ground && space1 && space2) {
                let gid = String(ground.id);
                let s1 = String(space1.id);
                let s2 = String(space2.id);

                let isSolid = gid !== 'minecraft:air' && !gid.includes('air') && !gid.includes('water') && !gid.includes('lava') && !ground.liquid;
                let isClear = (s1 === 'minecraft:air' || s1.includes('air')) && (s2 === 'minecraft:air' || s2.includes('air'));

                if (isSolid && isClear) {
                    return { x: x, y: checkY, z: z };
                }
            }
        }
    }

    // Direct fallback position if all attempts fail (e.g. wide ocean/archipelago)
    let angle = Math.random() * Math.PI * 2;
    let x = Math.floor(originX + minRadius * Math.cos(angle));
    let z = Math.floor(originZ + minRadius * Math.sin(angle));
    let y = 64;
    try {
        y = Math.max(60, level.getHeight(Heightmap.Types.MOTION_BLOCKING_NO_LEAVES, x, z));
    } catch (e) {
        y = 64;
    }

    // Safety fallback: build a 5x5 cobblestone platform if ground is liquid or air
    let groundBlock = level.getBlock(x, y - 1, z);
    let gid = groundBlock ? String(groundBlock.id) : '';
    if (!groundBlock || groundBlock.liquid || gid.includes('air') || gid.includes('water') || gid.includes('lava')) {
        let srv = level.getServer ? level.getServer() : level.server;
        let dim = String(level.dimension.location ? level.dimension.location() : level.dimension);
        if (srv) {
            srv.runCommandSilent(`execute in ${dim} run fill ${x - 2} ${y - 1} ${z - 2} ${x + 2} ${y - 1} ${z + 2} minecraft:cobblestone`);
            srv.runCommandSilent(`execute in ${dim} run fill ${x - 2} ${y} ${z - 2} ${x + 2} ${y + 2} ${z + 2} minecraft:air replace minecraft:water`);
            srv.runCommandSilent(`execute in ${dim} run fill ${x - 2} ${y} ${z - 2} ${x + 2} ${y + 2} ${z + 2} minecraft:air replace minecraft:lava`);
        }
    }

    return { x: x, y: y, z: z };
}

// ==========================================
// FTB CHUNKS FORCELOAD INTEGRATION
// ==========================================

function forceLoadGatewayChunk(server, level, x, y, z, player) {
    try {
        let FTBChunksAPI = Java.loadClass('dev.ftb.mods.ftbchunks.api.FTBChunksAPI').api();
        let ChunkDimPos = Java.loadClass('dev.ftb.mods.ftblibrary.math.ChunkDimPos');

        let manager = FTBChunksAPI.getManager();
        let chunkX = Math.floor(x) >> 4;
        let chunkZ = Math.floor(z) >> 4;
        let chunkPos = new ChunkDimPos(level.dimension, chunkX, chunkZ);
        let source = server.createCommandSourceStack();

        let existingChunk = manager.getChunk(chunkPos);
        if (existingChunk) {
            let ownerTeamData = existingChunk.getTeamData();
            ownerTeamData.forceLoad(source, chunkPos, false);
            return {
                action: 'half',
                teamId: ownerTeamData.getTeam().getTeamId().toString(),
                x: chunkX,
                z: chunkZ,
                dim: String(level.dimension.location ? level.dimension.location() : level.dimension)
            };
        } else if (player) {
            let targetTeamData = manager.getOrCreateData(player);
            targetTeamData.claim(source, chunkPos, false);
            targetTeamData.forceLoad(source, chunkPos, false);
            return {
                action: 'full',
                teamId: targetTeamData.getTeam().getTeamId().toString(),
                x: chunkX,
                z: chunkZ,
                dim: String(level.dimension.location ? level.dimension.location() : level.dimension)
            };
        }
    } catch (e) {
        console.error(`[PEAK RandomGateway] FTB Chunks force-loading notice: ${e}`);
    }
    return null;
}

function unForceLoadGatewayChunk(server, claimInfo) {
    if (!claimInfo) return;
    try {
        let FTBChunksAPI = Java.loadClass('dev.ftb.mods.ftbchunks.api.FTBChunksAPI').api();
        let FTBTeamsAPI = Java.loadClass('dev.ftb.mods.ftbteams.api.FTBTeamsAPI').api();
        let ChunkDimPos = Java.loadClass('dev.ftb.mods.ftblibrary.math.ChunkDimPos');
        let ResourceKey = Java.loadClass('net.minecraft.resources.ResourceKey');
        let Registries = Java.loadClass('net.minecraft.core.registries.Registries');
        let ResourceLocation = Java.loadClass('net.minecraft.resources.ResourceLocation');
        let UUID = Java.loadClass('java.util.UUID');

        let manager = FTBChunksAPI.getManager();
        let teamManager = FTBTeamsAPI.getManager();
        let teamOpt = teamManager.getTeamByID(UUID.fromString(claimInfo.teamId));

        if (teamOpt.isPresent()) {
            let team = teamOpt.get();
            let teamData = manager.getOrCreateData(team);
            let dimKey = ResourceKey.create(Registries.DIMENSION, ResourceLocation.parse(claimInfo.dim));
            let chunkPos = new ChunkDimPos(dimKey, claimInfo.x, claimInfo.z);
            let source = server.createCommandSourceStack();

            teamData.unForceLoad(source, chunkPos, false);
            if (claimInfo.action === 'full') {
                teamData.unclaim(source, chunkPos, false);
            }
        }
    } catch (e) {
        console.error(`[PEAK RandomGateway] FTB Chunks un-forceload notice: ${e}`);
    }
}

// ==========================================
// GATEWAY LIFECYCLE MANAGEMENT
// ==========================================

function cancelActiveGateway(server, reason) {
    let p = server.persistentData;
    if (!p.getBoolean('rg_scheduled') && !p.getBoolean('rg_active')) {
        return false;
    }

    let claimAction = p.getString('rg_claim_action');
    let teamId = p.getString('rg_claim_team_id');
    let cx = p.getInt('rg_claim_x');
    let cz = p.getInt('rg_claim_z');
    let dim = p.getString('rg_claim_dim') || 'minecraft:overworld';

    if (claimAction && teamId) {
        unForceLoadGatewayChunk(server, {
            action: claimAction,
            teamId: teamId,
            x: cx,
            z: cz,
            dim: dim
        });
    }

    p.putBoolean('rg_scheduled', false);
    p.putBoolean('rg_active', false);
    p.remove('rg_target_tick');
    p.remove('rg_target_x');
    p.remove('rg_target_y');
    p.remove('rg_target_z');
    p.remove('rg_gate_id');
    p.remove('rg_claim_action');
    p.remove('rg_claim_team_id');
    p.remove('rg_warned_300');
    p.remove('rg_warned_200');
    p.remove('rg_warned_100');
    p.remove('rg_warned_20');
    p.remove('rg_warned_5');
    p.remove('rg_active_start_tick');

    // Reset pity if days passed has reached or exceeded max threshold to prevent infinite guaranteed rolls
    let maxDays = p.getInt('rg_spawn_day') || RG_DEFAULTS.spawn_day;
    if (p.getInt('rg_days_passed') >= maxDays) {
        p.putInt('rg_days_passed', 0);
        p.putInt('rg_current_pity', p.getInt('rg_spawn_rate') || RG_DEFAULTS.spawn_rate);
    }

    if (reason) {
        console.log(`[PEAK RandomGateway] Gateway cleared: ${reason}`);
    }
    return true;
}

function scheduleGatewayEvent(server, overworld, targetPlayer, forcedGateId, delaySeconds) {
    let px = Math.floor(targetPlayer.x);
    let pz = Math.floor(targetPlayer.z);

    let pos = findSurfacePos(overworld, px, pz, RG_DEFAULTS.min_player_dist, RG_DEFAULTS.max_player_dist);
    let gateId = forcedGateId || selectGatewayForPos(overworld, pos.x, pos.z);

    let currentGameTime = overworld.getGameTime();
    let delayTicks = (delaySeconds ? delaySeconds * 20 : (6000 + Math.floor(Math.random() * 10000)));
    let targetTick = currentGameTime + delayTicks;

    let p = server.persistentData;
    p.putBoolean('rg_scheduled', true);
    p.putBoolean('rg_active', false);
    p.putLong('rg_target_tick', targetTick);
    p.putInt('rg_target_x', pos.x);
    p.putInt('rg_target_y', pos.y);
    p.putInt('rg_target_z', pos.z);
    p.putString('rg_gate_id', gateId);
    p.putString('rg_player_uuid', targetPlayer.uuid.toString());

    p.putBoolean('rg_warned_300', false);
    p.putBoolean('rg_warned_200', false);
    p.putBoolean('rg_warned_100', false);
    p.putBoolean('rg_warned_20', false);
    p.putBoolean('rg_warned_5', false);

    // Morning alert to chat
    server.tell(Component.lightPurple("The gate will open today… but to where?"));
    server.runCommandSilent('playsound minecraft:ambient.cave ambient @a ~ ~ ~ 0.6 0.8');

    console.log(`[PEAK RandomGateway] Scheduled ${gateId} at (${pos.x}, ${pos.y}, ${pos.z}) for tick ${targetTick} (${Math.round(delayTicks / 20)}s from now)`);
}

function spawnGatewayNow(server, overworld, customPos, customGateId, customPlayer) {
    let p = server.persistentData;
    let x = customPos ? customPos.x : p.getInt('rg_target_x');
    let y = customPos ? customPos.y : p.getInt('rg_target_y');
    let z = customPos ? customPos.z : p.getInt('rg_target_z');
    let gateId = customGateId || p.getString('rg_gate_id') || 'gateways:basic/slime';
    let gateInfo = RG_GATEWAYS[gateId] || { name: 'Gateway', color: '§d' };

    let targetPlayer = customPlayer;
    if (!targetPlayer) {
        let playerUUID = p.getString('rg_player_uuid');
        if (playerUUID) {
            targetPlayer = server.getPlayer(playerUUID);
        }
    }
    if (!targetPlayer) {
        targetPlayer = overworld.getRandomPlayer();
    }

    // Ensure solid ground beneath gateway if fluid or air
    let ground = overworld.getBlock(x, y - 1, z);
    let gid = ground ? String(ground.id) : '';
    if (!ground || ground.liquid || gid.includes('air') || gid.includes('water') || gid.includes('lava')) {
        server.runCommandSilent(`execute in minecraft:overworld run fill ${x - 2} ${y - 1} ${z - 2} ${x + 2} ${y - 1} ${z + 2} minecraft:cobblestone`);
        server.runCommandSilent(`execute in minecraft:overworld run fill ${x - 2} ${y} ${z - 2} ${x + 2} ${y + 2} ${z + 2} minecraft:air replace minecraft:water`);
        server.runCommandSilent(`execute in minecraft:overworld run fill ${x - 2} ${y} ${z - 2} ${x + 2} ${y + 2} ${z + 2} minecraft:air replace minecraft:lava`);
    }

    // Force load the chunk in FTB Chunks
    let claimData = forceLoadGatewayChunk(server, overworld, x, y, z, targetPlayer);
    if (claimData) {
        p.putString('rg_claim_action', claimData.action);
        p.putString('rg_claim_team_id', claimData.teamId);
        p.putInt('rg_claim_x', claimData.x);
        p.putInt('rg_claim_z', claimData.z);
        p.putString('rg_claim_dim', claimData.dim);
    }

    // Summon gateway entity via Gateways command
    server.runCommandSilent(`execute in minecraft:overworld run open_gateway ${x} ${y} ${z} ${gateId}`);

    // Update persistent state
    p.putBoolean('rg_scheduled', false);
    p.putBoolean('rg_active', true);
    p.putInt('rg_target_x', x);
    p.putInt('rg_target_y', y);
    p.putInt('rg_target_z', z);
    p.putString('rg_gate_id', gateId);
    p.putLong('rg_active_start_tick', overworld.getGameTime());

    // Reset pity and day counters now that gateway has spawned in world
    p.putInt('rg_days_passed', 0);
    p.putInt('rg_current_pity', p.getInt('rg_spawn_rate') || RG_DEFAULTS.spawn_rate);

    // Broadcast opening alert to chat
    server.tell(Component.red("§l[Gateways] ").append(Component.literal(`${gateInfo.name} has opened at [X: ${x}, Y: ${y}, Z: ${z}]!`)));
    server.runCommandSilent('playsound minecraft:entity.wither.spawn master @a ~ ~ ~ 0.5 1.2');

    console.log(`[PEAK RandomGateway] Gateway ${gateId} spawned at (${x}, ${y}, ${z})`);
}

// ==========================================
// SLEEP PREVENTION HOOK
// ==========================================

BlockEvents.rightClicked(event => {
    if (event.block && event.block.hasTag('minecraft:beds')) {
        let server = event.server;
        if (!server || !isGatewayPendingOrActive(server)) return;

        let overworld = server.getLevel('minecraft:overworld');
        let timeOfDay = overworld ? (overworld.getDayTime() % 24000) : 0;
        // In Vanilla Minecraft, beds only initiate sleep between ticks 12542 and 23459 (or during thunderstorms)
        let canSleepNow = (timeOfDay >= 12542 && timeOfDay <= 23459) || (overworld && overworld.isThundering());

        if (canSleepNow) {
            event.cancel();
            event.player.displayClientMessage(Component.red("A strange force prevents you from sleeping ..."), true);
            event.server.runCommandSilent(`execute at ${event.player.uuid} run playsound minecraft:block.enchantment_table.use players @p ~ ~ ~ 0.8 0.7`);
        }
    }
});

// ==========================================
// SERVER STARTUP / RESTORATION
// ==========================================

ServerEvents.loaded(event => {
    let server = event.server;
    server.scheduleInTicks(40, () => {
        let p = server.persistentData;
        if (!p.getBoolean('rg_active')) return;

        let overworld = server.getLevel('minecraft:overworld');
        let x = p.getInt('rg_target_x');
        let y = p.getInt('rg_target_y');
        let z = p.getInt('rg_target_z');

        let foundGateway = false;
        if (overworld) {
            try {
                let AABB = Java.loadClass('net.minecraft.world.phys.AABB');
                let box = new AABB(x - 8, y - 8, z - 8, x + 8, y + 8, z + 8);
                let GatewayEntity = Java.loadClass('dev.shadowsoffire.gateways.entity.GatewayEntity');
                let entities = overworld.getEntitiesOfClass(GatewayEntity, box);
                if (entities && !entities.isEmpty()) {
                    foundGateway = true;
                }
            } catch (e) {
                foundGateway = false;
            }
        }

        if (!foundGateway) {
            cancelActiveGateway(server, 'cleaned orphaned active gateway on startup');
        }
    });
});

// ==========================================
// GATEWAY COMPLETION & FAILURE HOOKS
// ==========================================

try {
    let GateCompleted = Java.loadClass('dev.shadowsoffire.gateways.event.GateEvent$Completed');
    NativeEvents.onEvent(GateCompleted, event => {
        let gateEntity = event.getEntity();
        if (!gateEntity) return;

        let server = gateEntity.getServer();
        if (!server) return;

        let p = server.persistentData;
        if (!p.getBoolean('rg_active')) return;

        let dim = String(gateEntity.level.dimension.location ? gateEntity.level.dimension.location() : gateEntity.level.dimension);
        if (!dim.includes('overworld')) return;

        let targetX = p.getInt('rg_target_x');
        let targetZ = p.getInt('rg_target_z');

        // Proximity verification: ensure this is our random gateway and not a player's private Gate Pearl
        let dist = Math.hypot(gateEntity.x - targetX, gateEntity.z - targetZ);
        if (dist > 12) return;

        let gateId = p.getString('rg_gate_id');
        let gateInfo = RG_GATEWAYS[gateId] || { name: 'Gateway', color: '§a' };

        server.tell(Component.green("§l[Gateways] ").append(Component.literal(`${gateInfo.name} has been conquered!`)));
        server.runCommandSilent('playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1.0 1.0');

        // Reset pity and day counters on success
        p.putInt('rg_days_passed', 0);
        p.putInt('rg_current_pity', p.getInt('rg_spawn_rate') || RG_DEFAULTS.spawn_rate);

        cancelActiveGateway(server, 'conquered');
    });
} catch (e) {
    console.error(`[PEAK RandomGateway] Could not hook GateEvent$Completed: ${e}`);
}

try {
    let GateFailed = Java.loadClass('dev.shadowsoffire.gateways.event.GateEvent$Failed');
    NativeEvents.onEvent(GateFailed, event => {
        let gateEntity = event.getEntity();
        if (!gateEntity) return;

        let server = gateEntity.getServer();
        if (!server) return;

        let p = server.persistentData;
        if (!p.getBoolean('rg_active')) return;

        let dim = String(gateEntity.level.dimension.location ? gateEntity.level.dimension.location() : gateEntity.level.dimension);
        if (!dim.includes('overworld')) return;

        let targetX = p.getInt('rg_target_x');
        let targetZ = p.getInt('rg_target_z');

        // Proximity verification: ensure this is our random gateway
        let dist = Math.hypot(gateEntity.x - targetX, gateEntity.z - targetZ);
        if (dist > 12) return;

        let gateId = p.getString('rg_gate_id');
        let gateInfo = RG_GATEWAYS[gateId] || { name: 'Gateway', color: '§c' };

        server.tell(Component.red("[Gateways] ").append(Component.literal(`${gateInfo.name} has collapsed into the void.`)));
        server.runCommandSilent('playsound minecraft:block.beacon.deactivate master @a ~ ~ ~ 0.8 0.8');

        // Reset pity and day counters on loss
        p.putInt('rg_days_passed', 0);
        p.putInt('rg_current_pity', p.getInt('rg_spawn_rate') || RG_DEFAULTS.spawn_rate);

        cancelActiveGateway(server, 'collapsed');
    });
} catch (e) {
    console.error(`[PEAK RandomGateway] Could not hook GateEvent$Failed: ${e}`);
}

// ==========================================
// MAIN SERVER TICK CYCLE
// ==========================================

ServerEvents.tick(event => {
    let server = event.server;
    let overworld = server.getLevel('minecraft:overworld');
    if (!overworld) return;

    // Run throttled logic once every second (20 ticks)
    let gameTime = overworld.getGameTime();
    if (gameTime % 20 !== 0) return;

    let cfg = getRGConfig(server);
    let p = server.persistentData;
    let dayTime = overworld.getDayTime();
    let timeOfDay = dayTime % 24000;

    // 1. Sunrise Daily Evaluation (around tick 0 - 1200 of day cycle, i.e. morning hour)
    if (cfg.enabled && !cfg.scheduled && !cfg.active) {
        let lastCheckedDay = p.getLong('rg_last_checked_day');
        let currentDayNumber = Math.floor(dayTime / 24000);

        if (currentDayNumber !== lastCheckedDay && timeOfDay >= 0 && timeOfDay <= 1200) {
            let players = overworld.players;
            if (players && !players.isEmpty()) {
                p.putLong('rg_last_checked_day', currentDayNumber);

                let daysPassed = cfg.days_passed;
                let currentPity = cfg.current_pity;
                let maxDays = cfg.spawn_day;

                let shouldSpawn = false;
                if (daysPassed + 1 >= maxDays) {
                    shouldSpawn = true;
                } else {
                    let roll = Math.floor(Math.random() * 100) + 1;
                    if (roll <= currentPity) {
                        shouldSpawn = true;
                    }
                }

                if (shouldSpawn) {
                    let randomPlayer = players.get(Math.floor(Math.random() * players.size()));
                    scheduleGatewayEvent(server, overworld, randomPlayer, null, null);
                } else {
                    p.putInt('rg_days_passed', daysPassed + 1);
                    p.putInt('rg_current_pity', currentPity + cfg.spawn_rate);
                    console.log(`[PEAK RandomGateway] Day ${daysPassed + 1}/${maxDays}: No gate today. Pity chance raised to ${currentPity + cfg.spawn_rate}%.`);
                }
            }
        }
    }

    // 2. Scheduled Countdown & Spawning Phase (Monotonic tracking via gameTime)
    if (cfg.scheduled) {
        let targetTick = p.getLong('rg_target_tick');
        let remainingTicks = targetTick - gameTime;
        let remainingSec = Math.floor(remainingTicks / 20);

        let x = p.getInt('rg_target_x');
        let y = p.getInt('rg_target_y');
        let z = p.getInt('rg_target_z');
        let gateId = p.getString('rg_gate_id');
        let gateInfo = RG_GATEWAYS[gateId] || { name: 'Gateway', color: '§b' };

        // 300 seconds left: Initial Chat Alert & Waypoint Registration
        if (remainingSec <= 300 && !p.getBoolean('rg_warned_300')) {
            p.putBoolean('rg_warned_300', true);

            // Register FTB Chunks waypoint for all players
            server.runCommandSilent(`execute as @a run ftbchunks waypoint add "${gateInfo.name}" minecraft:overworld ${x} ${y} ${z} light_purple false`);

            // Chat notification with clickable waypoint coordinates
            let coordText = Component.literal(`§e[X: ${x}, Y: ${y}, Z: ${z}]§r`)
                .clickRunCommand(`/ftbchunks waypoint add "${gateInfo.name}" minecraft:overworld ${x} ${y} ${z} light_purple false`)
                .hover(Component.literal("§7Click to add waypoint on map"));

            server.tell(
                Component.lightPurple("[Gateways] A ").append(
                    Component.literal(`${gateInfo.color}${gateInfo.name}§d will open at `)
                ).append(coordText).append(
                    Component.literal(" in §6300§d seconds! Be ready to fight!")
                )
            );
            server.runCommandSilent('playsound minecraft:block.beacon.activate players @a ~ ~ ~ 0.8 1.0');
        }

        // Milestone chat warnings (if countdown_chat is enabled)
        if (cfg.countdown_chat) {
            if (remainingSec <= 200 && remainingSec > 100 && !p.getBoolean('rg_warned_200')) {
                p.putBoolean('rg_warned_200', true);
                server.tell(Component.lightPurple(`[Gateways] ${gateInfo.color}${gateInfo.name}§d opening at §e[${x}, ${z}]§d in §6200§d seconds!`));
            } else if (remainingSec <= 100 && remainingSec > 20 && !p.getBoolean('rg_warned_100')) {
                p.putBoolean('rg_warned_100', true);
                server.tell(Component.lightPurple(`[Gateways] ${gateInfo.color}${gateInfo.name}§d opening at §e[${x}, ${z}]§d in §6100§d seconds!`));
            } else if (remainingSec <= 20 && remainingSec > 5 && !p.getBoolean('rg_warned_20')) {
                p.putBoolean('rg_warned_20', true);
                server.tell(Component.lightPurple(`[Gateways] ${gateInfo.color}${gateInfo.name}§d opening at §e[${x}, ${z}]§d in §620§d seconds!`));
            } else if (remainingSec <= 5 && remainingSec > 0 && !p.getBoolean('rg_warned_5')) {
                p.putBoolean('rg_warned_5', true);
                server.tell(Component.red(`[Gateways] ${gateInfo.color}${gateInfo.name}§c opening in §65§c seconds!`));
            }
        }

        // Time to open the gate
        if (remainingTicks <= 0) {
            spawnGatewayNow(server, overworld, null, null, null);
        }
    }

    // 3. Watchdog Fail-Safe for Active Gateway (25 minutes max lifetime)
    if (cfg.active) {
        let startTick = p.getLong('rg_active_start_tick');
        if (startTick > 0 && (gameTime - startTick) > 30000) {
            cancelActiveGateway(server, 'timeout watchdog exceeded (25 min)');
        }
    }
});

// ==========================================
// COMMAND REGISTRATION (/peak RandomGateway & /randomgateway)
// ==========================================

ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event;

    function attachSubcommands(builder) {
        return builder
            .executes(ctx => showStatus(ctx))
            // /peak RandomGateway true / false
            .then(Commands.literal('true').executes(ctx => setEnabled(ctx, true)))
            .then(Commands.literal('false').executes(ctx => setEnabled(ctx, false)))
            // /peak RandomGateway enabled <true|false>
            .then(Commands.literal('enabled')
                .then(Commands.argument('value', Arguments.BOOLEAN.create(event))
                    .executes(ctx => setEnabled(ctx, Arguments.BOOLEAN.getResult(ctx, 'value')))))
            // /peak RandomGateway spawn [gateway_id] (Immediately spawns the gateway)
            .then(Commands.literal('spawn')
                .executes(ctx => immediateSpawn(ctx, null))
                .then(Commands.argument('gateway', Arguments.GREEDY_STRING.create(event))
                    .suggests((ctx, b) => {
                        Object.keys(RG_GATEWAYS).forEach(id => b.suggest(id));
                        return b.buildFuture();
                    })
                    .executes(ctx => immediateSpawn(ctx, Arguments.GREEDY_STRING.getResult(ctx, 'gateway')))))
            // /peak RandomGateway schedule [gateway_id] (Queues with countdown)
            .then(Commands.literal('schedule')
                .executes(ctx => forceSchedule(ctx, null))
                .then(Commands.argument('gateway', Arguments.GREEDY_STRING.create(event))
                    .suggests((ctx, b) => {
                        Object.keys(RG_GATEWAYS).forEach(id => b.suggest(id));
                        return b.buildFuture();
                    })
                    .executes(ctx => forceSchedule(ctx, Arguments.GREEDY_STRING.getResult(ctx, 'gateway')))))
            // /peak RandomGateway spawn_rate <number>
            .then(Commands.literal('spawn_rate')
                .then(Commands.argument('rate', Arguments.INTEGER.create(event))
                    .executes(ctx => setSpawnRate(ctx, Arguments.INTEGER.getResult(ctx, 'rate')))))
            // /peak RandomGateway spawn_day <number>
            .then(Commands.literal('spawn_day')
                .then(Commands.argument('days', Arguments.INTEGER.create(event))
                    .executes(ctx => setSpawnDay(ctx, Arguments.INTEGER.getResult(ctx, 'days')))))
            // /peak RandomGateway countdown_chat <true|false>
            .then(Commands.literal('countdown_chat')
                .then(Commands.argument('value', Arguments.BOOLEAN.create(event))
                    .executes(ctx => setCountdownChat(ctx, Arguments.BOOLEAN.getResult(ctx, 'value')))))
            // /peak RandomGateway status / info
            .then(Commands.literal('status').executes(ctx => showStatus(ctx)))
            .then(Commands.literal('info').executes(ctx => showStatus(ctx)))
            // /peak RandomGateway cancel
            .then(Commands.literal('cancel').executes(ctx => cancelEvent(ctx)));
    }

    function showStatus(ctx) {
        let server = ctx.source.server;
        let cfg = getRGConfig(server);
        let p = server.persistentData;
        let overworld = server.getLevel('minecraft:overworld');
        let gameTime = overworld ? overworld.getGameTime() : 0;

        let src = ctx.source;
        src.sendSuccess(() => Component.gold("=== PEAK Random Gateways Status ==="), false);
        src.sendSuccess(() => Component.gray("Enabled: ").append(Component.literal(cfg.enabled ? "§aTrue" : "§cFalse")), false);
        src.sendSuccess(() => Component.gray("Spawn Rate (Pity Base): ").append(Component.literal(`§e${cfg.spawn_rate}%`)), false);
        src.sendSuccess(() => Component.gray("Guaranteed Spawn Threshold: ").append(Component.literal(`§e${cfg.spawn_day} days`)), false);
        src.sendSuccess(() => Component.gray("Days Passed without spawn: ").append(Component.literal(`§b${cfg.days_passed}`)), false);
        src.sendSuccess(() => Component.gray("Current Pity Chance: ").append(Component.literal(`§b${cfg.current_pity}%`)), false);
        src.sendSuccess(() => Component.gray("Chat Countdown Alerts: ").append(Component.literal(cfg.countdown_chat ? "§aEnabled" : "§cDisabled")), false);

        if (cfg.scheduled) {
            let x = p.getInt('rg_target_x');
            let y = p.getInt('rg_target_y');
            let z = p.getInt('rg_target_z');
            let gid = p.getString('rg_gate_id');
            let targetTick = p.getLong('rg_target_tick');
            let remainingSec = Math.max(0, Math.floor((targetTick - gameTime) / 20));
            src.sendSuccess(() => Component.yellow(`Status: §6Scheduled§r [${gid}] at (${x}, ${y}, ${z}) in §6${remainingSec}s`), false);
        } else if (cfg.active) {
            let x = p.getInt('rg_target_x');
            let y = p.getInt('rg_target_y');
            let z = p.getInt('rg_target_z');
            let gid = p.getString('rg_gate_id');
            src.sendSuccess(() => Component.green(`Status: §aACTIVE§r [${gid}] at (${x}, ${y}, ${z})`), false);
        } else {
            src.sendSuccess(() => Component.gray("Status: §7Idle (Awaiting morning roll)"), false);
        }
        return 1;
    }

    function setEnabled(ctx, state) {
        let server = ctx.source.server;
        server.persistentData.putBoolean('rg_enabled', state);
        ctx.source.sendSuccess(() => Component.green(`Random Gateways system is now ${state ? "ENABLED" : "DISABLED"}.`), true);
        return 1;
    }

    function setSpawnRate(ctx, rate) {
        if (rate < 1 || rate > 100) {
            ctx.source.sendFailure(Component.red("Rate must be between 1 and 100."));
            return 0;
        }
        let server = ctx.source.server;
        server.persistentData.putInt('rg_spawn_rate', rate);
        ctx.source.sendSuccess(() => Component.green(`Daily spawn rate updated to ${rate}%.`), true);
        return 1;
    }

    function setSpawnDay(ctx, days) {
        if (days < 1) {
            ctx.source.sendFailure(Component.red("Spawn day threshold must be at least 1."));
            return 0;
        }
        let server = ctx.source.server;
        server.persistentData.putInt('rg_spawn_day', days);
        ctx.source.sendSuccess(() => Component.green(`Guaranteed spawn day updated to ${days} days.`), true);
        return 1;
    }

    function setCountdownChat(ctx, value) {
        let server = ctx.source.server;
        server.persistentData.putBoolean('rg_countdown_chat', value);
        ctx.source.sendSuccess(() => Component.green(`Chat countdown alerts are now ${value ? "ENABLED" : "DISABLED"}.`), true);
        return 1;
    }

    function immediateSpawn(ctx, customGate) {
        let server = ctx.source.server;
        let overworld = server.getLevel('minecraft:overworld');
        if (!overworld) {
            ctx.source.sendFailure(Component.red("Overworld dimension not available."));
            return 0;
        }

        let player = ctx.source.player || overworld.getRandomPlayer();
        if (!player) {
            ctx.source.sendFailure(Component.red("No player available to anchor the gateway spawn."));
            return 0;
        }

        if (customGate && !RG_GATEWAYS[customGate]) {
            ctx.source.sendFailure(Component.red(`Unknown gateway id '${customGate}'. Available: ${Object.keys(RG_GATEWAYS).join(', ')}`));
            return 0;
        }

        cancelActiveGateway(server, 'force spawning immediate event');

        let px = Math.floor(player.x);
        let pz = Math.floor(player.z);
        let pos = findSurfacePos(overworld, px, pz, RG_DEFAULTS.min_player_dist, RG_DEFAULTS.max_player_dist);
        let gateId = customGate || selectGatewayForPos(overworld, pos.x, pos.z);

        spawnGatewayNow(server, overworld, pos, gateId, player);
        ctx.source.sendSuccess(() => Component.green(`Immediately spawned ${gateId} at (${pos.x}, ${pos.y}, ${pos.z}) near ${player.username}.`), true);
        return 1;
    }

    function forceSchedule(ctx, customGate) {
        let server = ctx.source.server;
        let overworld = server.getLevel('minecraft:overworld');
        if (!overworld) {
            ctx.source.sendFailure(Component.red("Overworld dimension not available."));
            return 0;
        }

        let player = ctx.source.player || overworld.getRandomPlayer();
        if (!player) {
            ctx.source.sendFailure(Component.red("No player available to anchor the gateway spawn."));
            return 0;
        }

        if (customGate && !RG_GATEWAYS[customGate]) {
            ctx.source.sendFailure(Component.red(`Unknown gateway id '${customGate}'. Available: ${Object.keys(RG_GATEWAYS).join(', ')}`));
            return 0;
        }

        cancelActiveGateway(server, 'scheduling new event');

        scheduleGatewayEvent(server, overworld, player, customGate, RG_DEFAULTS.warning_seconds);
        ctx.source.sendSuccess(() => Component.green(`Scheduled gateway countdown (300s) near ${player.username}.`), true);
        return 1;
    }

    function cancelEvent(ctx) {
        let server = ctx.source.server;
        let cleared = cancelActiveGateway(server, 'cancelled via command');
        if (cleared) {
            ctx.source.sendSuccess(() => Component.green("Active/scheduled gateway cancelled and cleaned up."), true);
        } else {
            ctx.source.sendFailure(Component.gray("No gateway event is currently active or scheduled."));
        }
        return 1;
    }

    // Register /peak RandomGateway
    event.register(
        Commands.literal('peak')
            .requires(src => src.hasPermission(2))
            .then(attachSubcommands(Commands.literal('RandomGateway')))
    );

    // Register standalone /randomgateway shortcut
    event.register(
        attachSubcommands(Commands.literal('randomgateway')
            .requires(src => src.hasPermission(2)))
    );
});
