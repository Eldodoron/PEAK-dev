// ==========================================
// EMBOLDENED INGOT RECIPES
// Multi-path blood-infusion synthesis for ess_requiem:emboldened_ingot.
// Supported paths: Alchemist Cauldron, Create Spout/Mixing, Crafting Table.
// ==========================================

ServerEvents.recipes(event => {
    // Remove legacy cheap crafting and campfire recipes
    event.remove({ id: 'ess_requiem:emboldened_ingot' });
    event.remove({ id: 'ess_requiem:emboldned_ingot_campfire' });

    // -------------------------------------------------------------
    // 1. Iron's Spells: Alchemist Cauldron Soaking
    // Handled via datapack JSON in kubejs/data/irons_spellbooks/recipe/alchemist_cauldron/soak_emboldened_ingot.json
    // -------------------------------------------------------------

    // -------------------------------------------------------------
    // 2. Create: Spout Filling (1000 mB Blood)
    // -------------------------------------------------------------
    event.recipes.create.filling('ess_requiem:emboldened_ingot', [
        'minecraft:iron_ingot',
        Fluid.of('irons_spellbooks:blood', 1000)
    ]).id('kubejs:create/filling/emboldened_ingot');

    event.recipes.create.filling('ess_requiem:emboldened_ingot', [
        'minecraft:iron_ingot',
        Fluid.of('create_wizardry:blood', 1000)
    ]).id('kubejs:create/filling/emboldened_ingot_cw');

    // -------------------------------------------------------------
    // 3. Create: Basin Mixing (1000 mB Blood)
    // -------------------------------------------------------------
    event.recipes.create.mixing('ess_requiem:emboldened_ingot', [
        'minecraft:iron_ingot',
        Fluid.of('irons_spellbooks:blood', 1000)
    ]).id('kubejs:create/mixing/emboldened_ingot');

    event.recipes.create.mixing('ess_requiem:emboldened_ingot', [
        'minecraft:iron_ingot',
        Fluid.of('create_wizardry:blood', 1000)
    ]).id('kubejs:create/mixing/emboldened_ingot_cw');

    // -------------------------------------------------------------
    // 4. Crafting Table: 4x Blood Vials + Iron Ingot
    // -------------------------------------------------------------
    event.shapeless('ess_requiem:emboldened_ingot', [
        'minecraft:iron_ingot',
        'irons_spellbooks:blood_vial',
        'irons_spellbooks:blood_vial',
        'irons_spellbooks:blood_vial',
        'irons_spellbooks:blood_vial'
    ])
    .replaceIngredient('irons_spellbooks:blood_vial', Item.of('minecraft:glass_bottle'))
    .id('kubejs:crafting/emboldened_ingot_from_vials');

    // -------------------------------------------------------------
    // 5. Crafting Table: Blood Bucket + Iron Ingot
    // -------------------------------------------------------------
    event.shapeless('ess_requiem:emboldened_ingot', [
        'minecraft:iron_ingot',
        'create_wizardry:blood_bucket'
    ])
    .replaceIngredient('create_wizardry:blood_bucket', Item.of('minecraft:bucket'))
    .id('kubejs:crafting/emboldened_ingot_from_bucket');
});
