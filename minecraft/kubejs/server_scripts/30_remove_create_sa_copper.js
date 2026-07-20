ServerEvents.recipes(event => {
    // --- REMOVE CREATE STUFF & ADDITIONS COPPER EQUIPMENT ---
    // The user wants to force the use of Ice and Fire's copper equipment because it is better balanced.
    // We only remove the basic tools and armor, keeping the jetpack and exoskeleton.
    
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
