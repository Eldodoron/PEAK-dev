ServerEvents.recipes(event => {
    // Prevent the player from crafting the player blimp
    event.remove({ output: 'raidsenhanced:player_blimp' });
});

LootJS.modifiers(event => {
    // Completely remove the player blimp from dropping anywhere (including the Raider Blimp entity)
    event.addTableModifier(LootType.ENTITY, LootType.CHEST, LootType.BLOCK)
        .removeLoot('raidsenhanced:player_blimp');
});
