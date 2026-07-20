LootJS.modifiers(event => {
    // Multiply dragon scale drops by 2.5x
    event.addEntityModifier(/iceandfire:.*_dragon/)
        .modifyLoot(/iceandfire:dragonscales_.*/, item => {
            let newCount = Math.round(item.count * 2.5);
            return item.withCount(newCount);
        });
});
