RecipeViewerEvents.removeEntries('item', event => {
    // --- HIDE ALL INCOMPLETE SEQUENCED ASSEMBLY ITEMS ---
    // Matches any item ID from any namespace (create, create_sa, delightfulcreators, kubejs, etc.)
    // containing 'incomplete_' (e.g. kubejs:incomplete_stack_upgrade_tier_1, create_sa:incomplete_steam_engine)
    event.remove('/.*:incomplete_.*/');
});
