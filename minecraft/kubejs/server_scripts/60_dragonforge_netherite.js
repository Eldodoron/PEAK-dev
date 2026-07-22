ServerEvents.recipes(event => {
    // Make Dragonsteel harder to craft by requiring Netherite Ingots instead of Iron Ingots
    const dragons = ['fire', 'ice', 'lightning'];

    dragons.forEach(dragon => {
        // Remove the original recipe
        event.remove({ id: `iceandfire:dragonforge/dragonsteel_${dragon}_ingot` });

        // Add the new Netherite recipe
        event.custom({
            "type": "iceandfire:dragonforge",
            "dragonType": dragon,
            "cookTime": 1000,
            "input": { "item": "minecraft:netherite_ingot" },
            "blood": { "item": `iceandfire:${dragon}_dragon_blood` },
            "result": { "id": `iceandfire:dragonsteel_${dragon}_ingot` }
        });
    });
});
