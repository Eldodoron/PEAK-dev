// ==========================================
// PEAK EXPERT MODE — SCRIPT 18
// BOSS DROP DUPLICATOR (Anomaly Replicator)
// ==========================================

ServerEvents.recipes(event => {
    // 1. Crafting the Anomaly Replicator
    // Extremely expensive, requires 1 Infinity Catalyst, 4 Antimatter Pellets, 4 Dragon Eggs
    event.recipes.create.mechanical_crafting('kubejs:anomaly_replicator', [
        ' E ',
        'CAC',
        ' E '
    ], {
        E: 'minecraft:dragon_egg',
        C: 'avaritia:infinity_catalyst',
        A: 'mekanism:pellet_antimatter'
    });

    // 2. Duplication Recipes
    // The Anomaly Replicator stays in the grid (defined in startup_scripts).
    // Cost: 1 Boss Drop + 1 Antimatter Pellet = 2 Boss Drops
    let bossDropsToDuplicate = [
        'minecraft:nether_star',
        'minecraft:dragon_egg',
        'kubejs:heart_of_the_inferno',
        'cataclysm:witherite_ingot',
        'cataclysm:ignitium_ingot',
        'cataclysm:abyssal_egg',
        'kubejs:wither_soul',
        'kubejs:draconic_scale',
        'twilightforest:fiery_blood',
        'twilightforest:naga_scale',
        'mowziesmobs:wrought_helmet',
        'mowziesmobs:naga_fang',
        'ars_nouveau:wilden_tribute',
        'undergarden:forgotten_ingot'
    ];

    bossDropsToDuplicate.forEach(drop => {
        // We use shapeless crafting to duplicate it.
        event.shapeless(`2x ${drop}`, [
            drop, 
            'kubejs:anomaly_replicator', 
            'mekanism:pellet_antimatter'
        ]);
    });

    // Special case for cataclysm:void_core (Max Stack Size: 1)
    // We output a different item or just double it if possible, 
    // but KubeJS 1.21 doesn't like 2x single-stack items in one slot.
    // So we just output it twice in a mechanical crafting table or skip it.
    event.shapeless('2x cataclysm:void_core', [
        'cataclysm:void_core', 
        'kubejs:anomaly_replicator', 
        'mekanism:pellet_antimatter'
    ]).setResult(['cataclysm:void_core', 'cataclysm:void_core']); // Try to return two stacks

    console.log('[PEAK Expert Mode] Script 18: Boss Duplicator loaded!');
});

// Give the Anomaly Replicator back to the player when they use it to craft
ItemEvents.crafted(event => {
    // If they crafted a boss drop, and the replicator was in the grid, we give it back
    // (A bit hacky, but very effective for custom un-consumable items in KubeJS 1.21)
    let usedReplicator = false;
    event.inventory.allItems.forEach(item => {
        if (item.id === 'kubejs:anomaly_replicator') {
            usedReplicator = true;
        }
    });
    
    if (usedReplicator && event.player) {
        event.player.give('kubejs:anomaly_replicator');
    }
});
