// ==========================================
// PEAK EXPERT MODE — SCRIPT 18
// BOSS DROP DUPLICATOR (Anomaly Replicator)
// ==========================================

const BOSS_DROPS_TO_DUPLICATE = [
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
    'undergarden:forgotten_ingot',
    'cataclysm:void_core'
];

ServerEvents.recipes(event => {
    // 1. Crafting the Anomaly Replicator
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
    BOSS_DROPS_TO_DUPLICATE.forEach(drop => {
        // Output exactly 1x to bypass max stack limits.
        // The replicator item is kept in the grid using native keepIngredient() if supported,
        // but we will continue to use the event fallback to ensure it works across all NeoForge builds.
        event.shapeless(drop, [
            drop, 
            Item.of('kubejs:anomaly_replicator'), // Strong NBT matching helps avoid shift-click dupes
            'mekanism:pellet_antimatter'
        ]).keepIngredient('kubejs:anomaly_replicator'); // Modern KubeJS method to leave item in grid!
    });

    console.log('[PEAK Expert Mode] Script 18: Boss Duplicator loaded!');
});

// Give the 2nd copy of the duplicated item
ItemEvents.crafted(event => {
    // Guard clause: O(1) performance check. Very fast.
    if (!BOSS_DROPS_TO_DUPLICATE.includes(event.item.id)) return;

    let usedReplicator = false;
    event.inventory.allItems.forEach(item => {
        if (item.id === 'kubejs:anomaly_replicator') {
            usedReplicator = true;
        }
    });
    
    if (usedReplicator && event.player) {
        // Give the 2nd duplicated copy of the item.
        // In KubeJS, .give() safely drops the item at the player's feet if their inventory is full.
        event.player.give(event.item.id);
    }
});
