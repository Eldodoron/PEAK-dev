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
    );

    // Also register /greenscreen directly as a convenient alias
    event.register(
        createGreenScreenNode()
            .requires(src => src.hasPermission(2))
    );
});

console.log('[PEAK Expert Mode] Script 12: Admin Commands loaded!');
