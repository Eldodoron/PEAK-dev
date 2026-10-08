// ==========================================
// PEAK EXPERT MODE — SCRIPT 12
// ADMIN COMMANDS
// ==========================================

ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event;

    function buildGreenScreen(ctx, width, length, height) {
        let source = ctx.source;
        let player = source.player;
        let server = source.server;

        if (!player) {
            source.sendFailure(Text.red('This command can only be executed by a player.'));
            return 0;
        }

        // Clamp dimensions to safe bounds (3 to 200 blocks)
        width = Math.max(3, Math.min(width || 30, 200));
        length = Math.max(3, Math.min(length || width, 200));
        height = Math.max(3, Math.min(height || 15, 100));

        let px = Math.floor(player.x);
        let py = Math.floor(player.y);
        let pz = Math.floor(player.z);

        let halfW = Math.floor(width / 2);
        let halfL = Math.floor(length / 2);

        let x1 = px - halfW;
        let x2 = px + halfW;
        let y1 = py;
        let y2 = py + height;
        let z1 = pz - halfL;
        let z2 = pz + halfL;

        // 1. Generate outer box (Floor, Ceiling, 4 Walls)
        server.runCommandSilent(`fill ${x1} ${y1} ${z1} ${x2} ${y1} ${z2} kubejs:green_screen replace`);
        server.runCommandSilent(`fill ${x1} ${y2} ${z1} ${x2} ${y2} ${z2} kubejs:green_screen replace`);
        server.runCommandSilent(`fill ${x1} ${y1} ${z1} ${x2} ${y2} ${z1} kubejs:green_screen replace`);
        server.runCommandSilent(`fill ${x1} ${y1} ${z2} ${x2} ${y2} ${z2} kubejs:green_screen replace`);
        server.runCommandSilent(`fill ${x1} ${y1} ${z1} ${x1} ${y2} ${z2} kubejs:green_screen replace`);
        server.runCommandSilent(`fill ${x2} ${y1} ${z1} ${x2} ${y2} ${z2} kubejs:green_screen replace`);

        // 2. Clear interior space with air safely in vertical slices
        let innerX1 = x1 + 1;
        let innerX2 = x2 - 1;
        let innerY1 = y1 + 1;
        let innerY2 = y2 - 1;
        let innerZ1 = z1 + 1;
        let innerZ2 = z2 - 1;

        if (innerX1 <= innerX2 && innerY1 <= innerY2 && innerZ1 <= innerZ2) {
            let sliceH = 8;
            for (let currY = innerY1; currY <= innerY2; currY += sliceH) {
                let nextY = Math.min(currY + sliceH - 1, innerY2);
                server.runCommandSilent(`fill ${innerX1} ${currY} ${innerZ1} ${innerX2} ${nextY} ${innerZ2} minecraft:air replace`);
            }
        }

        // 3. Center player inside the room
        server.runCommandSilent(`tp ${player.username} ${px + 0.5} ${py + 1.0} ${pz + 0.5}`);

        player.tell(Text.green(`🎬 Green Screen Room successfully generated! (${width}x${length}x${height} blocks)`));
        return 1;
    }

    function clearGreenScreen(ctx, size) {
        let source = ctx.source;
        let player = source.player;
        let server = source.server;

        if (!player) return 0;

        let s = Math.max(3, Math.min(size || 35, 200));
        let half = Math.floor(s / 2);
        let px = Math.floor(player.x);
        let py = Math.floor(player.y);
        let pz = Math.floor(player.z);

        let x1 = px - half;
        let x2 = px + half;
        let y1 = Math.max(-64, py - 5);
        let y2 = Math.min(320, py + 35);
        let z1 = pz - half;
        let z2 = pz + half;

        server.runCommandSilent(`fill ${x1} ${y1} ${z1} ${x2} ${y2} ${z2} minecraft:air replace kubejs:green_screen`);
        player.tell(Text.yellow(`🧹 Green Screen blocks cleared in a ${s}x${s} area.`));
        return 1;
    }

    function createGreenScreenNode() {
        return Commands.literal('greenscreen')
            .executes(ctx => buildGreenScreen(ctx, 30, 30, 15))
            .then(Commands.literal('clear')
                .executes(ctx => clearGreenScreen(ctx, 35))
                .then(Commands.argument('radius', Arguments.INTEGER.create(event))
                    .executes(ctx => clearGreenScreen(ctx, Arguments.INTEGER.getResult(ctx, 'radius')))
                )
            )
            .then(Commands.argument('size', Arguments.INTEGER.create(event))
                .executes(ctx => {
                    let s = Arguments.INTEGER.getResult(ctx, 'size');
                    let h = Math.max(4, Math.floor(s / 2));
                    return buildGreenScreen(ctx, s, s, h);
                })
                .then(Commands.argument('height', Arguments.INTEGER.create(event))
                    .executes(ctx => {
                        let s = Arguments.INTEGER.getResult(ctx, 'size');
                        let h = Arguments.INTEGER.getResult(ctx, 'height');
                        return buildGreenScreen(ctx, s, s, h);
                    })
                    .then(Commands.argument('length', Arguments.INTEGER.create(event))
                        .executes(ctx => {
                            let w = Arguments.INTEGER.getResult(ctx, 'size');
                            let h = Arguments.INTEGER.getResult(ctx, 'height');
                            let l = Arguments.INTEGER.getResult(ctx, 'length');
                            return buildGreenScreen(ctx, w, l, h);
                        })
                    )
                )
            );
    }

    // Register /peak command with all subcommands
    event.register(
        Commands.literal('peak')
            .requires(src => src.hasPermission(2))
            .then(createGreenScreenNode())
            .then(Commands.literal('reset_eyes')
                .executes(ctx => {
                    let source = ctx.source;
                    let target = source.player;
                    
                    if (target) {
                        const bossList = [
                            'block_factorys_bosses:infernal_dragon',
                            'block_factorys_bosses:yeti',
                            'block_factorys_bosses:sandworm',
                            'block_factorys_bosses:underworld_knight',
                            'block_factorys_bosses:kraken',
                            'cataclysm:ender_golem',
                            'cataclysm:ender_guardian',
                            'cataclysm:ignis',
                            'cataclysm:netherite_monstrosity',
                            'cataclysm:the_harbinger',
                            'cataclysm:the_leviathan',
                            'cataclysm:wadjet',
                            'mowziesmobs:frostmaw',
                            'mowziesmobs:wroughtnaut',
                            'mowziesmobs:umvuthi',
                            'alexscaves:luxtructosaurus',
                            'alexscaves:hullbreaker',
                            'alexscaves:tremorzilla',
                            'alexscaves:forsaken',
                            'minecraft:ender_dragon',
                            'minecraft:wither',
                            'minecraft:elder_guardian',
                            'minecraft:warden'
                        ];
                        
                        bossList.forEach(bossId => {
                            let key = 'dropped_eye_' + bossId.replace(':', '_');
                            target.persistentData.remove(key);
                        });
                        
                        target.tell(Text.green('✅ Reset ALL Boss Eye drops for yourself. You can now get the first-kill drops again.'));
                    }
                    return 1;
                })
                .then(Commands.argument('boss_id', Arguments.GREEDY_STRING.create(event))
                    .suggests((ctx, builder) => {
                        const bossList = [
                            'block_factorys_bosses:infernal_dragon',
                            'block_factorys_bosses:yeti',
                            'block_factorys_bosses:sandworm',
                            'block_factorys_bosses:underworld_knight',
                            'block_factorys_bosses:kraken',
                            'cataclysm:ender_golem',
                            'cataclysm:ender_guardian',
                            'cataclysm:ignis',
                            'cataclysm:netherite_monstrosity',
                            'cataclysm:the_harbinger',
                            'cataclysm:the_leviathan',
                            'cataclysm:wadjet',
                            'mowziesmobs:frostmaw',
                            'mowziesmobs:wroughtnaut',
                            'mowziesmobs:umvuthi',
                            'alexscaves:luxtructosaurus',
                            'alexscaves:hullbreaker',
                            'alexscaves:tremorzilla',
                            'alexscaves:forsaken',
                            'minecraft:ender_dragon',
                            'minecraft:wither',
                            'minecraft:elder_guardian',
                            'minecraft:warden'
                        ];
                        bossList.forEach(id => builder.suggest(id));
                        return builder.buildFuture();
                    })
                    .executes(ctx => {
                        let source = ctx.source;
                        let target = source.player;
                        
                        if (target) {
                            let bossId = Arguments.GREEDY_STRING.getResult(ctx, 'boss_id');
                            let key = 'dropped_eye_' + bossId.replace(':', '_');
                            
                            target.persistentData.remove(key);
                            
                            target.tell(Text.green('✅ Reset Boss Eye drop for: ' + bossId));
                        }
                        return 1;
                    })
                )
            )
            .then(Commands.literal('spawn_animals')
                .executes(ctx => spawnAnimals(ctx))
            )
            .then(createPadCommandNode())
            .then(Commands.literal('regenerate_pad')
                .executes(ctx => regenerateOverworldPad(ctx))
                .then(Commands.literal('overworld').executes(ctx => regenerateOverworldPad(ctx)))
                .then(Commands.literal('beyond').executes(ctx => regenerateBeyondPad(ctx)))
                .then(Commands.literal('all').executes(ctx => regenerateAllPads(ctx)))
            )
    );

    function spawnAnimals(ctx) {
        let source = ctx.source;
        let player = source.player;
        let server = source.server;

        if (!player) {
            source.sendFailure(Text.red('This command can only be executed by a player.'));
            return 0;
        }

        const animals = [
            'minecraft:pig',
            'minecraft:cow',
            'minecraft:chicken',
            'minecraft:sheep',
            'minecraft:horse',
            'minecraft:donkey',
            'minecraft:mule',
            'minecraft:cat',
            'minecraft:ocelot',
            'minecraft:wolf',
            'minecraft:parrot',
            'minecraft:rabbit',
            'minecraft:fox',
            'minecraft:goat',
            'minecraft:llama',
            'minecraft:panda',
            'minecraft:polar_bear',
            'minecraft:bee',
            'minecraft:frog',
            'minecraft:armadillo',
            'minecraft:sniffer',
            'minecraft:camel'
        ];

        let px = player.x;
        let py = player.y;
        let pz = player.z;
        let radius = 3.5;
        let angleStep = (2 * Math.PI) / animals.length;

        animals.forEach((animalId, index) => {
            let angle = index * angleStep;
            let spawnX = (px + Math.cos(angle) * radius).toFixed(2);
            let spawnZ = (pz + Math.sin(angle) * radius).toFixed(2);
            server.runCommandSilent(`execute in ${player.level.dimension} run summon ${animalId} ${spawnX} ${py} ${spawnZ}`);
        });

        player.tell(Text.green(`✅ Spawned ${animals.length} common animals around you!`));
        return 1;
    }

    // Also register /spawnanimals directly as a convenient alias
    event.register(
        Commands.literal('spawnanimals')
            .requires(src => src.hasPermission(2))
            .executes(ctx => spawnAnimals(ctx))
    );

    // Also register /greenscreen directly as a convenient alias
    event.register(
        createGreenScreenNode()
            .requires(src => src.hasPermission(2))
    );

    function regenerateOverworldPad(ctx) {
        let source = ctx.source;
        let server = source.server;
        let setupFn = global.setupWorldSpawnDais;
        if (typeof setupFn === 'function') {
            let coords = setupFn(server, false);
            if (coords) {
                server.runCommandSilent(`execute in minecraft:overworld run playsound minecraft:block.beacon.activate block @a ${coords.x} ${coords.y} ${coords.z} 1.0 1.0`);
                server.runCommandSilent(`execute in minecraft:overworld run particle minecraft:reverse_portal ${coords.x + 0.5} ${coords.y + 0.5} ${coords.z + 0.5} 0.5 0.5 0.5 0.05 60`);
                let msg = Text.green(`Overworld Void Teleport Pad dais successfully regenerated at (${coords.x}, ${coords.y}, ${coords.z}).`);
                if (source.player) {
                    source.player.tell(msg);
                } else {
                    source.sendSuccess(msg, true);
                }
                return 1;
            }
        }
        let err = Text.red('Failed to regenerate Overworld pad: generation function unavailable or overworld level missing.');
        if (source.player) source.player.tell(err);
        else source.sendFailure(err);
        return 0;
    }

    function regenerateBeyondPad(ctx) {
        let source = ctx.source;
        let server = source.server;
        let ensureFn = global.ensureVoidSanctuaryPlatform;
        if (typeof ensureFn === 'function') {
            let success = ensureFn(server);
            if (success) {
                server.runCommandSilent('execute in allthemodium:the_beyond run playsound minecraft:block.beacon.activate block @a 0 64 0 1.0 1.0');
                server.runCommandSilent('execute in allthemodium:the_beyond run particle minecraft:reverse_portal 0.5 64.5 0.5 0.5 0.5 0.5 0.05 60');
                let msg = Text.green('The Beyond anchor dais successfully regenerated at (0, 64, 0).');
                if (source.player) {
                    source.player.tell(msg);
                } else {
                    source.sendSuccess(msg, true);
                }
                return 1;
            }
        }
        let err = Text.red('Failed to regenerate The Beyond pad: dimension unavailable.');
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

        let msg = Text.gold('--- Void Teleport Pad Status ---\n')
            .append(Text.white(`Overworld Dais: (${sx}, ${sy}, ${sz}) - Status: `))
            .append(!initialized ? Text.yellow('Uninitialized') : (cleared ? Text.red('Cleared / Inactive') : Text.green('Active')))
            .append(Text.white('\nThe Beyond Anchor: (0, 64, 0) - Status: '))
            .append(Text.green('Active'));

        if (source.player) {
            source.player.tell(msg);
        } else {
            source.sendSuccess(msg, false);
        }
        return 1;
    }

    function createPadCommandNode() {
        return Commands.literal('pad')
            .executes(ctx => regenerateOverworldPad(ctx))
            .then(Commands.literal('regenerate')
                .executes(ctx => regenerateOverworldPad(ctx))
                .then(Commands.literal('overworld').executes(ctx => regenerateOverworldPad(ctx)))
                .then(Commands.literal('beyond').executes(ctx => regenerateBeyondPad(ctx)))
                .then(Commands.literal('all').executes(ctx => regenerateAllPads(ctx)))
            )
            .then(Commands.literal('info').executes(ctx => showPadInfo(ctx)));
    }

    // Direct alias for /regeneratepad
    event.register(
        Commands.literal('regeneratepad')
            .requires(src => src.hasPermission(2))
            .executes(ctx => regenerateOverworldPad(ctx))
    );
});

console.log('[PEAK Expert Mode] Script 12: Admin Commands loaded!');
