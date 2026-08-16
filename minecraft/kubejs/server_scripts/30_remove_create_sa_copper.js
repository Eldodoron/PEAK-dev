ServerEvents.recipes(event => {
    // --- REMOVE CREATE STUFF & ADDITIONS COPPER EQUIPMENT ---
    // Prefer Ice and Fire copper equipment for balance.
    // Only basic tools and armor are removed; jetpack and exoskeleton are retained.
    
    let itemsToRemove = [
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
    
    itemsToRemove.forEach(item => {
        event.remove({ output: item });
    });
});
