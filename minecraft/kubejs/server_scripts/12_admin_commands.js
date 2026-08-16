// ==========================================
// PEAK EXPERT MODE — SCRIPT 12
// ADMIN COMMANDS
// ==========================================

ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event;
    
    // Command: /peak reset_eyes [boss_id]
    // Example: /peak reset_eyes
    // Example: /peak reset_eyes block_factorys_bosses:yeti
    
    event.register(
        Commands.literal('peak')
            .requires(src => src.hasPermission(2))
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
});

console.log('[PEAK Expert Mode] Script 12: Admin Commands loaded!');
