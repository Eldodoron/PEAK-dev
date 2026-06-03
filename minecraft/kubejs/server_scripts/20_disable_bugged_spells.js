// ==========================================
// PEAK EXPERT MODE - SCRIPT 20
// DISABLE BUGGED SPELLS (Traveloptics)
// ==========================================

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

// Remove the bugged scrolls directly from the player's inventory
PlayerEvents.inventoryChanged('irons_spellbooks:scroll', event => {
    let item = event.item;
    if (item.nbt) {
        let nbtString = item.nbt.toString();
        if (nbtString.includes('traveloptics:cursed_revenants') || nbtString.includes('traveloptics:call_forth_the_dead_king')) {
            item.count = 0;
            event.player.tell(Text.red("âŒ Se ha eliminado un pergamino buggeado de tu inventario para proteger el servidor."));
        }
    }
});

// Also prevent right clicks just in case
ItemEvents.rightClicked('irons_spellbooks:scroll', event => {
    let item = event.item;
    if (item.nbt) {
        let nbtString = item.nbt.toString();
        if (nbtString.includes('traveloptics:cursed_revenants') || nbtString.includes('traveloptics:call_forth_the_dead_king')) {
            event.cancel();
            item.count = 0; // Destroy it
            if (event.player) {
                event.player.tell(Text.red("âŒ Este pergamino ha sido destruido porque causa crasheos en el servidor."));
            }
        }
    }
});
