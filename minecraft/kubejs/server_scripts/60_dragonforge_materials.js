ServerEvents.recipes(event => {
    // Change Dragonsteel recipes to use different progression materials per dragon
    const dragonMaterials = {
        'fire': 'minecraft:netherite_ingot',
        'ice': 'mekanism:enriched_iron',
        'lightning': 'create_new_age:overcharged_iron'
    };

    Object.keys(dragonMaterials).forEach(dragon => {
        // Remove the original recipe
        event.remove({ id: `iceandfire:dragonforge/dragonsteel_${dragon}_ingot` });

        // Add the new custom recipe
        event.custom({
            "type": "iceandfire:dragonforge",
            "dragonType": dragon,
            "cookTime": 1000,
            "input": { "item": dragonMaterials[dragon] },
            "blood": { "item": `iceandfire:${dragon}_dragon_blood` },
            "result": { "id": `iceandfire:dragonsteel_${dragon}_ingot` }
        });
    });
});
