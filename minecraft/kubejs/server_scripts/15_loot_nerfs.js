// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 15
// LOOT NERFS & QUALITY OF LIFE
// ==========================================

LootJS.modifiers(event => {
    // ==========================================
    // NERF 1: SLIME/MAGMA CUBE SPLITTING EXPLOIT
    // Slimes split into tiny slimes, causing them to 
    // drop absurd amounts of Malum spirits.
    // We completely remove these drops from them.
    // ==========================================
    let overpoweredDrops = [

        'malum:sacred_spirit',
        'malum:wicked_spirit',
        'malum:arcane_spirit',
        'malum:earthen_spirit',
        'malum:infernal_spirit',
        'malum:aerial_spirit',
        'malum:aqueous_spirit'
    ];

    event.addEntityModifier('minecraft:slime').removeLoot(overpoweredDrops);
    event.addEntityModifier('minecraft:magma_cube').removeLoot(overpoweredDrops);
    
    // Also nerf silverfish and endermites since they spawn in swarms
    event.addEntityModifier('minecraft:silverfish').removeLoot(overpoweredDrops);
    event.addEntityModifier('minecraft:endermite').removeLoot(overpoweredDrops);

    // ==========================================
    // PURGE INTERNAL MOB-BEHAVIOR ENCHANTMENT BOOKS
    // Removes leaked internal boss traits from all loot tables
    // ==========================================
    event.addTableModifier(/.*/)
        .modifyLoot(Item.of('minecraft:enchanted_book'), item => {
            let comp = item.getComponents().toString();
            if (comp.includes('nova_structures:shulker_boss') || 
                comp.includes('nova_structures:shulker_miniboss') || 
                comp.includes('nova_structures:boss_behaviour')) {
                return Item.empty;
            }
            return item;
        });

    console.log('[PEAK Expert Mode] Script 15: Loot Nerfs loaded!');
});
