RecipeViewerEvents.removeEntries('item', event => {
    // --- HIDE BANNED & DISABLED ITEMS FROM JEI ---
    const bannedItems = [
        // Banned Raid Blimps
        'raidsenhanced:player_blimp',
        '',

        // Create SA Copper Equipment (Disabled in favor of Ice & Fire copper gear)
        'create_sa:copper_helmet',
        'create_sa:copper_chestplate',
        'create_sa:copper_leggings',
        'create_sa:copper_boots',
        'create_sa:copper_sword',
        'create_sa:copper_pickaxe',
        'create_sa:copper_axe',
        'create_sa:copper_shovel',
        'create_sa:copper_hoe'
    ];

    bannedItems.forEach(item => event.remove(item));
});
