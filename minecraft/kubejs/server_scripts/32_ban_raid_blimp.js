ServerEvents.recipes(event => {
    // Prevent player blimp crafting
    event.remove({ output: 'raidsenhanced:player_blimp' });
});

LootJS.modifiers(event => {
    // Remove player blimp and blimp parts from loot tables
    event.addTableModifier(LootType.ENTITY, LootType.CHEST, LootType.BLOCK)
        .removeLoot('raidsenhanced:player_blimp')
        .removeLoot('raidsenhanced:blimp_parts');
});

// Discard player blimp entity on spawn or chunk load
EntityEvents.spawned('raidsenhanced:player_blimp', event => {
    event.cancel();
    if (event.entity) {
        event.entity.discard();
    }
});

// Prevent mounting player blimp entity and discard on mount attempt
NativeEvents.onEvent('net.neoforged.neoforge.event.entity.EntityMountEvent', event => {
    if (event.isMounting()) {
        try {
            let mounted = event.getEntityBeingMounted();
            if (mounted && mounted.getType() == 'raidsenhanced:player_blimp') {
                event.setCanceled(true);
                mounted.discard();
            }
        } catch (err) {}
    }
});

// Prevent interacting with player blimp entity and discard on right-click
ItemEvents.entityInteracted(event => {
    if (event.target && event.target.type == 'raidsenhanced:player_blimp') {
        event.cancel();
        try {
            event.target.discard();
        } catch (err) {}
    }
});

// Prevent using or placing player blimp item
ItemEvents.rightClicked('raidsenhanced:player_blimp', event => {
    event.cancel();
    if (event.item) {
        event.item.count = 0;
    }
});

// Clear player blimp item if present in player inventory
PlayerEvents.inventoryChanged('raidsenhanced:player_blimp', event => {
    if (event.item) {
        event.item.count = 0;
    }
});
