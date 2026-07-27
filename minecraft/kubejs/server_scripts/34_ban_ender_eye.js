ServerEvents.recipes(event => {
    // Ban Ender Eye crafting so players must kill bosses for them
    event.remove({ output: 'minecraft:ender_eye' });
});

LootJS.modifiers(event => {
    // Remove Ender Eye from all chest loots (structures, dungeons, etc.)
    event.addTableModifier(LootType.CHEST)
        .removeLoot('minecraft:ender_eye');
});
