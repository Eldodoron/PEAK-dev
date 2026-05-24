// ==========================================
// PEAK EXPERT MODE — SCRIPT 11
// END GATING (Ender Eye Sequence)
// ==========================================

ServerEvents.recipes(event => {
    // Remove all vanilla recipes for the ender eye
    event.remove({ output: 'minecraft:ender_eye' });

    // Create Sequenced Assembly for Ender Eye
    // Requires: Ender Pearl -> Blaze Powder -> Ghast Tear -> Source Gem -> Pressing
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:ender_pearl" },
        "transitional_item": { "id": "kubejs:incomplete_ender_eye" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:blaze_powder" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:ghast_tear" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:source_gem" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            }
        ],
        "results": [{ "id": "minecraft:ender_eye" }],
        "loops": 1
    });

    console.log('[PEAK Expert Mode] Script 11: Ender Eye Gating loaded!');
});

// Remove specific items from all chest loot tables (Strongholds, Dungeons, etc.)
LootJS.modifiers(event => {
    event.addLootTableModifier(/.*/).removeLoot('minecraft:ender_eye');
    event.addLootTableModifier(/.*/).removeLoot('artifacts:everlasting_beef');
    event.addLootTableModifier(/.*/).removeLoot('artifacts:eternal_steak');
});
