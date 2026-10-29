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
    if (!beyondLevel) return false;

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
    return true;
}

// Helper: Calculate real surface height, accurately handling terrain, water, and existing pads
function getSurfaceY(level, x, z) {
    for (let y = 319; y > -64; y--) {
        let b = level.getBlock(x, y, z);
        if (b) {
            let bid = String(b.id);
            if (bid !== 'minecraft:air' && bid !== 'minecraft:void_air') {
                if (bid === 'kubejs:void_teleport_pad' || bid === 'minecraft:soul_lantern') {
                    return y;
                }
                return y + 1;
            }
        }
    }
    return 64;
}

// Helper: Setup communal World Spawn dais in Overworld
function setupWorldSpawnDais(server, forceRecalculate) {
    let overworld = server.getLevel('minecraft:overworld');
    if (!overworld) return null;

    let spawnPos = overworld.getSharedSpawnPos();
    let sx = spawnPos.getX();
    let sz = spawnPos.getZ();

    let sy = 64;
    let storedX = server.persistentData.getInt('sanctuary_spawn_x');
    let storedY = server.persistentData.getInt('sanctuary_spawn_y');
    let storedZ = server.persistentData.getInt('sanctuary_spawn_z');

    if (!forceRecalculate && storedX === sx && storedZ === sz && storedY > -64) {
        let floorBlock = overworld.getBlock(sx, storedY - 1, sz);
        if (floorBlock && String(floorBlock.id) === 'minecraft:reinforced_deepslate') {
            sy = storedY;
        } else {
            sy = getSurfaceY(overworld, sx, sz);
        }
    } else {
        sy = getSurfaceY(overworld, sx, sz);
    }

    // Save communal spawn pad coordinates and reset cleared state
    server.persistentData.putInt('sanctuary_spawn_x', sx);
    server.persistentData.putInt('sanctuary_spawn_y', sy);
    server.persistentData.putInt('sanctuary_spawn_z', sz);
    server.persistentData.putBoolean('sanctuary_spawn_cleared', false);
    server.persistentData.putBoolean('sanctuary_world_spawn_initialized', true);

    // If over water or fluids, build a foundation pier down into the water
    for (let dy = 1; dy <= 4; dy++) {
        for (let dx = -1; dx <= 1; dx++) {
            for (let dz = -1; dz <= 1; dz++) {
                let under = overworld.getBlock(sx + dx, sy - 1 - dy, sz + dz);
                if (under && (String(under.id).includes('water') || under.liquid)) {
                    server.runCommandSilent(`execute in minecraft:overworld run setblock ${sx + dx} ${sy - 1 - dy} ${sz + dz} minecraft:polished_deepslate`);
                }
            }
        }
    }

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

    return { x: sx, y: sy, z: sz };
}

// ==========================================
// ADMIN COMMANDS: /peak pad & /regeneratepad
// ==========================================
ServerEvents.commandRegistry(event => {
    const { commands: Commands } = event;

    function regenerateOverworldPad(ctx) {
        let source = ctx.source;
        let server = source.server;
        let coords = setupWorldSpawnDais(server, true);
        if (coords) {
            server.runCommandSilent(`execute in minecraft:overworld run playsound minecraft:block.beacon.activate block @a ${coords.x} ${coords.y} ${coords.z} 1.0 1.0`);
            server.runCommandSilent(`execute in minecraft:overworld run particle minecraft:reverse_portal ${coords.x + 0.5} ${coords.y + 0.5} ${coords.z + 0.5} 0.5 0.5 0.5 0.05 60`);
            let msg = Component.literal(`§aOverworld Void Teleport Pad dais successfully regenerated at (${coords.x}, ${coords.y}, ${coords.z}).§r`);
            if (source.player) source.player.tell(msg);
            else source.sendSuccess(msg, true);
            return 1;
        }
        let err = Component.literal('§cFailed to regenerate Overworld pad: Overworld level not found.§r');
        if (source.player) source.player.tell(err);
        else source.sendFailure(err);
        return 0;
    }

    function regenerateBeyondPad(ctx) {
        let source = ctx.source;
        let server = source.server;
        let success = ensureVoidSanctuaryPlatform(server);
        if (success) {
            server.runCommandSilent('execute in allthemodium:the_beyond run playsound minecraft:block.beacon.activate block @a 0 64 0 1.0 1.0');
            server.runCommandSilent('execute in allthemodium:the_beyond run particle minecraft:reverse_portal 0.5 64.5 0.5 0.5 0.5 0.5 0.05 60');
            let msg = Component.literal('§aThe Beyond anchor dais successfully regenerated at (0, 64, 0).§r');
            if (source.player) source.player.tell(msg);
            else source.sendSuccess(msg, true);
            return 1;
        }
        let err = Component.literal('§cFailed to regenerate The Beyond pad: dimension unavailable.§r');
        if (source.player) source.player.tell(err);
        else source.sendFailure(err);
        return 0;
    }

    function regenerateAllPads(ctx) {
        let r1 = regenerateOverworldPad(ctx);
        let r2 = regenerateBeyondPad(ctx);
        return (r1 && r2) ? 1 : 0;
    }

    function showPadInfo(ctx) {
        let source = ctx.source;
        let server = source.server;
        let sx = server.persistentData.getInt('sanctuary_spawn_x');
        let sy = server.persistentData.getInt('sanctuary_spawn_y');
        let sz = server.persistentData.getInt('sanctuary_spawn_z');
        let cleared = server.persistentData.getBoolean('sanctuary_spawn_cleared');
        let initialized = server.persistentData.getBoolean('sanctuary_world_spawn_initialized');

        let msg = Component.literal('§6--- Void Teleport Pad Status ---\n§r')
            .append(Component.literal(`§fOverworld Dais: (${sx}, ${sy}, ${sz}) - Status: §r`))
            .append(!initialized ? Component.literal('§eUninitialized§r') : (cleared ? Component.literal('§cCleared / Inactive§r') : Component.literal('§aActive§r')))
            .append(Component.literal('§f\nThe Beyond Anchor: (0, 64, 0) - Status: §r'))
            .append(Component.literal('§aActive§r'));

        if (source.player) source.player.tell(msg);
        else source.sendSuccess(msg, false);
        return 1;
    }

    event.register(
        Commands.literal('peak')
            .requires(src => src.hasPermission(2))
            .then(Commands.literal('pad')
                .executes(ctx => regenerateOverworldPad(ctx))
                .then(Commands.literal('regenerate')
                    .executes(ctx => regenerateOverworldPad(ctx))
                    .then(Commands.literal('overworld').executes(ctx => regenerateOverworldPad(ctx)))
                    .then(Commands.literal('beyond').executes(ctx => regenerateBeyondPad(ctx)))
                    .then(Commands.literal('all').executes(ctx => regenerateAllPads(ctx)))
                )
                .then(Commands.literal('info').executes(ctx => showPadInfo(ctx)))
            )
    );
});

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
            player.displayClientMessage(Component.literal("§eThe Void anchor has been disturbed and will reform.§r"), true);
        }
    } else if (dim.includes('overworld') && isCommunalPad(block)) {
        server.persistentData.putBoolean('sanctuary_spawn_cleared', true);
        if (player) {
            player.displayClientMessage(Component.literal("§7World Spawn gateway removed.§r"), true);
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
        player.displayClientMessage(Component.literal("§7Sneak + Right-Click to use the Void Teleport Pad.§r"), true);
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

        player.displayClientMessage(Component.literal("§bReturned to previous location.§r"), true);

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

        player.displayClientMessage(Component.literal("§dTeleported to The Beyond.§r"), true);
    }

    // Cancel interaction at the end so holding items/blocks does not place or consume them
    return event.cancel();
});
