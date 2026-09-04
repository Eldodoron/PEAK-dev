// ==========================================
// PEAK EXPERT MODE - SCRIPT 20
// DISABLE BUGGED SPELLS (Traveloptics)
// ==========================================

// NOTE: Traveloptics is temporarily disabled until release.
// All listeners are commented out below to eliminate unnecessary tick/spawn overhead.
// Uncomment when Traveloptics is re-enabled.

/*
// Prevent the entities from ever spawning. If they are spawned, remove them instantly so they don't cause the despawn crash.
EntityEvents.spawned(event => {
    let type = event.entity.type;
    if (type === 'traveloptics:summoned_elite_draugr' || 
        type === 'traveloptics:summoned_draugr' || 
        type === 'traveloptics:summoned_royal_draugr' ||
        type === 'traveloptics:enraged_dead_king') {
        event.cancel();
    }
});

// Remove bugged scrolls directly from the player's inventory
PlayerEvents.inventoryChanged('irons_spellbooks:scroll', event => {
    let item = event.item;
    let dataStr = (item.components ? item.components.toString() : '') + (item.nbt ? item.nbt.toString() : '');
    if (dataStr.includes('traveloptics:cursed_revenants') || dataStr.includes('traveloptics:call_forth_the_dead_king')) {
        item.count = 0;
        event.player.tell(Text.red("[PEAK] A bugged spell scroll was removed from your inventory to protect the server."));
    }
});

// Also prevent right clicks just in case
ItemEvents.rightClicked('irons_spellbooks:scroll', event => {
    let item = event.item;
    let dataStr = (item.components ? item.components.toString() : '') + (item.nbt ? item.nbt.toString() : '');
    if (dataStr.includes('traveloptics:cursed_revenants') || dataStr.includes('traveloptics:call_forth_the_dead_king')) {
        event.cancel();
        item.count = 0;
        if (event.player) {
            event.player.tell(Text.red("[PEAK] This spell scroll was destroyed because it causes server instability."));
        }
    }
});
*/
