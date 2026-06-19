// Enforce correct weapons for Illagers to prevent broken AI
EntityEvents.spawned(event => {
    const entity = event.entity;
    
    // Pillagers ONLY know how to use Crossbows natively.
    if (entity.type === 'minecraft:pillager') {
        let mainHand = entity.getMainHandItem();
        // Allow ANY modded crossbow
        if (!mainHand.id.includes('crossbow')) {
            entity.setItemSlot('mainhand', Item.of('minecraft:crossbow'));
        }
    }
    // Vindicators ONLY know how to use melee weapons, traditionally Axes.
    else if (entity.type === 'minecraft:vindicator') {
        let mainHand = entity.getMainHandItem();
        // Allow ANY modded axe
        if (!mainHand.id.includes('axe')) {
            entity.setItemSlot('mainhand', Item.of('minecraft:iron_axe'));
        }
    }
});
