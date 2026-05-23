// ==========================================
// PEAK EXPERT MODE — SCRIPT 11
// END GATING (Ender Eye Sequence)
// ==========================================

ServerEvents.recipes(event => {
    // Remove all vanilla recipes for the ender eye
    event.remove({ output: 'minecraft:ender_eye' });

    // Create Sequenced Assembly for Ender Eye
    // Requires: Ender Pearl -> Blaze Powder -> Ghast Tear -> Source Gem -> Pressing
    event.recipes.create.sequenced_assembly([
        Item.of('minecraft:ender_eye')
    ], 'minecraft:ender_pearl', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:blaze_powder']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:ghast_tear']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:source_gem']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('kubejs:incomplete_ender_eye').loops(1);

    console.log('[PEAK Expert Mode] Script 11: Ender Eye Gating loaded!');
});

// Remove specific items from all chest loot tables (Strongholds, Dungeons, etc.)
LootJS.modifiers(event => {
    event.addTableModifier().removeLoot('minecraft:ender_eye');
    event.addTableModifier().removeLoot('artifacts:everlasting_beef');
    event.addTableModifier().removeLoot('artifacts:eternal_steak');
});
