RecipeViewerEvents.removeEntries('item', event => {
    // --- HIDE CREATE STUFF & ADDITIONS COPPER EQUIPMENT ---
    // The server removes these recipes to force the use of Ice and Fire's better balanced copper equipment.
    // Hiding them from JEI prevents player confusion.
    
    let itemsToHide = [
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
    
    itemsToHide.forEach(item => {
        event.hide(item);
    });
});
