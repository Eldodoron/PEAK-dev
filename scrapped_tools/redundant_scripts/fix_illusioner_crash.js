// priority: -1000

// Fix Illusioner crash on spawn (lowest priority to run after Apotheosis/other mods)
EntityEvents.spawned(event => {
    const entity = event.entity;
    if (!entity || !entity.isLiving()) return;

    if (entity.type === 'minecraft:illusioner' || entity.type === 'friendsandfoes:illusioner') {
        let handItem = entity.mainHandItem;
        if (handItem && !handItem.id.includes('bow')) {
            // Force vanilla bow
            entity.equip('mainhand', 'minecraft:bow');
        }
    }
});


