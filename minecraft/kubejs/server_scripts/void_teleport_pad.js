// ==========================================
// PEAK EXPERT MODE — SCRIPT: VOID TELEPORT PAD
// Custom Void Gateway & Teleportation System
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // END CRAFTING TABLE: VOID TELEPORT PAD (7x7)
    // Symmetrical 8-way dihedral recipe (Tier 3)
    // ==========================================
    // P = AllTheModium Teleport Pad (Center upgraded core)
    // N = Neutron Nugget (Cardinal focal points - top ingredient)
    // S = Nether Star (Diagonal energy conduits)
    // A = Allthemodium Nugget (Outer dimensional alignment)
    // E = Ender Eye (Matrix focus)
    // L = Diamond Lattice (Avaritia structural lattice)
    // D = Polished Deepslate (Grounding frame)
    // O = Reinforced Deepslate (Corners and perimeter anchors)
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "OLAOALO",
            "LEDLDEL",
            "ADSNSDA",
            "OLNPNLO",
            "ADSNSDA",
            "LEDLDEL",
            "OLAOALO"
        ],
        key: {
            P: { item: 'allthemodium:teleport_pad' },
            N: { item: 'avaritia:neutron_nugget' },
            S: { item: 'minecraft:nether_star' },
            A: { item: 'allthemodium:allthemodium_nugget' },
            E: { item: 'minecraft:ender_eye' },
            L: { item: 'avaritia:diamond_lattice' },
            D: { item: 'minecraft:polished_deepslate' },
            O: { item: 'minecraft:reinforced_deepslate' }
        },
        result: {
            id: 'kubejs:void_teleport_pad',
            count: 1
        },
        tier: 3
    });

    console.log('[PEAK Expert Mode] Void Teleport Pad: Avaritia 7x7 End Table recipe registered.');
});

// Helper: Ensure the anchor platform exists in The Beyond at (0, 64, 0)
function ensureVoidSanctuaryPlatform(server) {
    let beyondLevel = server.getLevel('allthemodium:the_beyond');
    if (!beyondLevel) return;

    // Ensure all 4 intersection chunks around (0, 0) are forceloaded
    server.runCommandSilent('execute in allthemodium:the_beyond run forceload add -16 -16 16 16');

    // Generate 5x5 platform at Y:63
    for (let x = -2; x <= 2; x++) {
        for (let z = -2; z <= 2; z++) {
            let block = (x === 0 && z === 0) ? 'minecraft:reinforced_deepslate' : 'minecraft:polished_deepslate';
            server.runCommandSilent(`execute in allthemodium:the_beyond run setblock ${x} 63 ${z} ${block}`);
        }
    }

    // Clear air clearance around pad level and above
    server.runCommandSilent('execute in allthemodium:the_beyond run fill -1 64 -1 1 64 1 minecraft:air replace');
    server.runCommandSilent('execute in allthemodium:the_beyond run fill -2 65 -2 2 66 2 minecraft:air replace');

    // Place central return pad (replaces any prior test blocks or ATM pads)
    server.runCommandSilent('execute in allthemodium:the_beyond run setblock 0 64 0 kubejs:void_teleport_pad');

    // Place decorative soul lanterns on corners
    server.runCommandSilent('execute in allthemodium:the_beyond run setblock -2 64 -2 minecraft:soul_lantern');
    server.runCommandSilent('execute in allthemodium:the_beyond run setblock 2 64 -2 minecraft:soul_lantern');
    server.runCommandSilent('execute in allthemodium:the_beyond run setblock -2 64 2 minecraft:soul_lantern');
    server.runCommandSilent('execute in allthemodium:the_beyond run setblock 2 64 2 minecraft:soul_lantern');
}

// Helper: Setup communal World Spawn dais in Overworld
function setupWorldSpawnDais(server) {
    let overworld = server.getLevel('minecraft:overworld');
    if (!overworld) return;

    let spawnPos = overworld.getSharedSpawnPos();
    let sx = spawnPos.getX();
    let sz = spawnPos.getZ();

    // Calculate the real surface height at world spawn
    let sy = 64;
    try {
        let Heightmap = Java.loadClass('net.minecraft.world.level.levelgen.Heightmap');
        sy = overworld.getHeight(Heightmap.Types.MOTION_BLOCKING_NO_LEAVES, sx, sz);
    } catch (e) {
        // Fallback: scan downward from world ceiling to find top surface
        for (let y = 319; y > -64; y--) {
            let b = overworld.getBlock(sx, y, sz);
            if (b) {
                let bid = String(b.id);
                if (bid !== 'minecraft:air' && bid !== 'minecraft:void_air') {
                    sy = y + 1;
                    break;
                }
            }
        }
    }

    // Save communal spawn pad coordinates
    server.persistentData.putInt('sanctuary_spawn_x', sx);
    server.persistentData.putInt('sanctuary_spawn_y', sy);
    server.persistentData.putInt('sanctuary_spawn_z', sz);

    // 3x3 platform around spawn
    for (let dx = -1; dx <= 1; dx++) {
        for (let dz = -1; dz <= 1; dz++) {
            let px = sx + dx;
            let pz = sz + dz;
            let block = (dx === 0 && dz === 0) ? 'minecraft:reinforced_deepslate' : 'minecraft:polished_deepslate';
            server.runCommandSilent(`execute in minecraft:overworld run setblock ${px} ${sy - 1} ${pz} ${block}`);
            server.runCommandSilent(`execute in minecraft:overworld run setblock ${px} ${sy} ${pz} minecraft:air`);
            server.runCommandSilent(`execute in minecraft:overworld run setblock ${px} ${sy + 1} ${pz} minecraft:air`);
        }
    }

    // Place the communal Void Teleport Pad in center
    server.runCommandSilent(`execute in minecraft:overworld run setblock ${sx} ${sy} ${sz} kubejs:void_teleport_pad`);

    // Corner lanterns
    server.runCommandSilent(`execute in minecraft:overworld run setblock ${sx - 1} ${sy} ${sz - 1} minecraft:soul_lantern`);
    server.runCommandSilent(`execute in minecraft:overworld run setblock ${sx + 1} ${sy} ${sz - 1} minecraft:soul_lantern`);
    server.runCommandSilent(`execute in minecraft:overworld run setblock ${sx - 1} ${sy} ${sz + 1} minecraft:soul_lantern`);
    server.runCommandSilent(`execute in minecraft:overworld run setblock ${sx + 1} ${sy} ${sz + 1} minecraft:soul_lantern`);
}

// Helper: Check if a given block is one of the communal non-dropping pads
function isCommunalPad(block) {
    let dim = String(block.level.dimension);
    if (dim.includes('the_beyond')) {
        return block.x === 0 && block.y === 64 && block.z === 0;
    }
    if (dim.includes('overworld')) {
        let server = block.level.server;
        if (server.persistentData.getBoolean('sanctuary_spawn_cleared')) {
            return false;
        }
        let sx = server.persistentData.getInt('sanctuary_spawn_x');
        let sy = server.persistentData.getInt('sanctuary_spawn_y');
        let sz = server.persistentData.getInt('sanctuary_spawn_z');
        if (sx && sy && sz) {
            return block.x === sx && block.y === sy && block.z === sz;
        }
        let overworld = server.getLevel('minecraft:overworld');
        if (overworld) {
            let spawn = overworld.getSharedSpawnPos();
            return block.x === spawn.getX() && block.z === spawn.getZ();
        }
    }
    return false;
}

// ==========================================
// WORLD GENERATION & SPAWN SETUP HOOKS
// ==========================================
ServerEvents.loaded(event => {
    let server = event.server;

    // Forceload all 4 intersection chunks (-16 to 16) in The Beyond so arrival is always instant and stable
    server.runCommandSilent('execute in allthemodium:the_beyond run forceload add -16 -16 16 16');
    ensureVoidSanctuaryPlatform(server);

    let overworld = server.getLevel('minecraft:overworld');
    if (overworld && !server.persistentData.contains('sanctuary_spawn_x')) {
        let spawnPos = overworld.getSharedSpawnPos();
        server.persistentData.putInt('sanctuary_spawn_x', spawnPos.getX());
        server.persistentData.putInt('sanctuary_spawn_z', spawnPos.getZ());
    }

    if (!server.persistentData.getBoolean('sanctuary_world_spawn_initialized')) {
        setupWorldSpawnDais(server);
        server.persistentData.putBoolean('sanctuary_world_spawn_initialized', true);
        console.log('[PEAK Expert Mode] Void Teleport Pad: Communal World Spawn dais initialized.');
    }
});

// ==========================================
// COMMUNAL PAD PROTECTION & ANTI-DUPLICATION
// ==========================================

// Communal pads drop 0 items when mined, preventing duplication and sequence breaks
BlockEvents.drops('kubejs:void_teleport_pad', event => {
    if (isCommunalPad(event.block)) {
        event.cancel();
    }
});

// When broken, handle world spawn clearing and automatic void anchor regeneration
BlockEvents.broken('kubejs:void_teleport_pad', event => {
    let block = event.block;
    let server = block.level.server;
    let player = event.player;
    let dim = String(block.level.dimension);

    if (dim.includes('the_beyond') && block.x === 0 && block.y === 64 && block.z === 0) {
        // Automatic void anchor reformation so players are never stranded
        server.scheduleInTicks(20, () => {
            ensureVoidSanctuaryPlatform(server);
            server.runCommandSilent(`execute in allthemodium:the_beyond run playsound minecraft:block.beacon.activate players @a 0.5 65.0 0.5 0.9 1.1`);
            server.runCommandSilent(`execute in allthemodium:the_beyond run particle minecraft:reverse_portal 0.5 64.5 0.5 0.4 0.4 0.4 0.05 40`);
        });
        if (player) {
            player.displayClientMessage(Component.yellow("The Void anchor has been disturbed and will reform."), true);
        }
    } else if (dim.includes('overworld') && isCommunalPad(block)) {
        server.persistentData.putBoolean('sanctuary_spawn_cleared', true);
        if (player) {
            player.displayClientMessage(Component.gray("World Spawn gateway removed."), true);
        }
    }
});

// ==========================================
// TELEPORTATION INTERACTION LOGIC
// ==========================================
BlockEvents.rightClicked('kubejs:void_teleport_pad', event => {
    if (event.hand.name() !== 'MAIN_HAND') return;

    let player = event.player;
    let block = event.block;
    let server = event.server;

    // Player must sneak to activate the pad (prevents accidental warps)
    if (!player.isCrouching()) {
        player.displayClientMessage(Component.gray("Sneak + Right-Click to use the Void Teleport Pad."), true);
        return;
    }

    let dimKey = player.level.dimension;
    let currentDim = String(dimKey.location ? dimKey.location() : dimKey);
    let isVoid = currentDim.includes('the_beyond');

    let yaw = player.getYRot ? player.getYRot() : (player.yaw || 0.0);
    let pitch = player.getXRot ? player.getXRot() : (player.pitch || 0.0);

    if (isVoid) {
        // --- RETURNING FROM VOID TO PREVIOUS LOCATION ---
        let hasReturn = player.persistentData.contains('void_pad_return_x') || player.persistentData.contains('sanctuary_return_x');
        let returnDim = player.persistentData.getString('void_pad_return_dim') || player.persistentData.getString('sanctuary_return_dim');
        let targetX = player.persistentData.getDouble('void_pad_return_x') || player.persistentData.getDouble('sanctuary_return_x');
        let targetY = player.persistentData.getDouble('void_pad_return_y') || player.persistentData.getDouble('sanctuary_return_y');
        let targetZ = player.persistentData.getDouble('void_pad_return_z') || player.persistentData.getDouble('sanctuary_return_z');

        if (!returnDim || returnDim === '' || returnDim.includes('the_beyond')) {
            returnDim = 'minecraft:overworld';
        }

        let targetLevel = server.getLevel(returnDim);
        if (!targetLevel) {
            targetLevel = server.getOverworld();
            returnDim = 'minecraft:overworld';
        }

        if (!hasReturn || !targetX || !targetY || !targetZ) {
            let spawn = targetLevel.getSharedSpawnPos();
            targetX = spawn.getX() + 0.5;
            targetY = spawn.getY() + 1.0;
            targetZ = spawn.getZ() + 0.5;
        }

        // Departure effects
        server.runCommandSilent(`playsound minecraft:block.portal.travel players @a ${player.x} ${player.y} ${player.z} 0.8 1.4`);
        server.runCommandSilent(`particle minecraft:reverse_portal ${player.x} ${player.y + 1} ${player.z} 0.5 0.5 0.5 0.1 60`);

        // Teleport back to return coordinates
        try {
            player.teleportToLevel(targetLevel, targetX, targetY, targetZ, yaw, pitch);
        } catch (e) {
            server.runCommandSilent(`execute in ${returnDim} run tp ${player.username} ${targetX.toFixed(2)} ${targetY.toFixed(2)} ${targetZ.toFixed(2)}`);
        }

        // Arrival effects scheduled at destination
        server.scheduleInTicks(2, () => {
            server.runCommandSilent(`execute at ${player.uuid} run playsound minecraft:block.beacon.activate players @a ~ ~ ~ 0.9 1.2`);
            server.runCommandSilent(`execute at ${player.uuid} run particle minecraft:portal ~ ~1 ~ 0.5 0.5 0.5 0.2 50`);
        });

        player.displayClientMessage(Component.aqua("Returned to previous location."), true);

    } else {
        // --- ENTERING VOID SANCTUARY FROM OVERWORLD / OTHER ---
        // Save current coordinates and dimension (position player directly above the pad)
        player.persistentData.putDouble('void_pad_return_x', block.x + 0.5);
        player.persistentData.putDouble('void_pad_return_y', block.y + 0.25);
        player.persistentData.putDouble('void_pad_return_z', block.z + 0.5);
        player.persistentData.putString('void_pad_return_dim', currentDim);

        // Departure effects
        server.runCommandSilent(`playsound minecraft:block.end_portal.spawn players @a ${player.x} ${player.y} ${player.z} 0.8 1.2`);
        server.runCommandSilent(`particle minecraft:portal ${player.x} ${player.y + 1} ${player.z} 0.5 0.5 0.5 0.2 60`);

        // Pre-generate platform
        ensureVoidSanctuaryPlatform(server);

        let beyondLevel = server.getLevel('allthemodium:the_beyond');
        if (beyondLevel) {
            try {
                player.teleportToLevel(beyondLevel, 0.5, 64.25, 0.5, yaw, pitch);
            } catch (e) {
                server.runCommandSilent(`execute in allthemodium:the_beyond run tp ${player.username} 0.5 64.25 0.5`);
            }
        } else {
            server.runCommandSilent(`execute in allthemodium:the_beyond run tp ${player.username} 0.5 64.25 0.5`);
        }

        // Arrival effects & platform confirmation in The Beyond
        server.scheduleInTicks(1, () => {
            ensureVoidSanctuaryPlatform(server);
            server.runCommandSilent(`execute in allthemodium:the_beyond run playsound minecraft:block.beacon.activate players @a 0.5 65.0 0.5 0.9 1.1`);
            server.runCommandSilent(`execute in allthemodium:the_beyond run particle minecraft:reverse_portal 0.5 65.5 0.5 0.4 0.8 0.4 0.05 80`);
        });

        player.displayClientMessage(Component.lightPurple("Teleported to The Beyond."), true);
    }

    // Cancel interaction at the end so holding items/blocks does not place or consume them
    return event.cancel();
});
