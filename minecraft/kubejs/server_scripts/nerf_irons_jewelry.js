LootEvents.modifiers(event => {
    // 90% of the time, this modifier will activate and remove all Iron's Jewelry items
    // This effectively makes Iron's Jewelry 10x rarer without modifying its config
    event.addModifier('nerf_irons_jewelry')
        .randomChance(0.9)
        .removeLoot('@irons_jewelry');
});
