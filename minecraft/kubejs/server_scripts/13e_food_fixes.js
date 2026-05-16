// ==========================================
// PEAK EXPERT MODE — SCRIPT 13E
// FOOD OVERHAUL: FIXES & MINECOLONIES
// ==========================================
// Fixes missed/broken recipe removals and adds
// MineColonies food conversions.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // FIX 1: MY NETHER'S DELIGHT — ID CORRECTIONS
    // Some recipes use subfolder IDs like crafting/name
    // ==========================================

    // Ghasta with Cream — fix the remove ID
    event.remove({ output: 'mynethersdelight:ghasta_with_cream' });

    // Raw Stuffed Hoglin — ensure removed from crafting table
    event.remove({ output: 'mynethersdelight:raw_stuffed_hoglin' });

    // Golden Egg — missed food recipe
    event.remove({ output: 'mynethersdelight:golden_egg' });
    event.recipes.create.mixing('mynethersdelight:golden_egg', [
        'minecraft:egg',
        'minecraft:gold_nugget',
        'minecraft:gold_nugget',
        'minecraft:gold_nugget',
        'minecraft:gold_nugget'
    ]).heated();

    // Hot Wings Bucket alt — remove duplicate
    event.remove({ id: 'mynethersdelight:crafting/hot_wings_bucket_alt' });

    // Magma Cake alt — remove duplicate
    event.remove({ id: 'mynethersdelight:crafting/magma_cake_alt' });

    // Chilidog alt — remove duplicate
    event.remove({ id: 'mynethersdelight:crafting/chilidog_alt' });

    // Hotcream Bucket — ensure removed
    event.remove({ output: 'mynethersdelight:hot_cream', type: 'minecraft:crafting_shapeless' });

    // Letios Compost — convert
    event.remove({ id: 'mynethersdelight:crafting/letios_compost_from_bone_alt' });
    event.remove({ id: 'mynethersdelight:crafting/letios_compost_from_rotten_flesh' });



    // ==========================================
    // MINECOLONIES FOOD RECIPES
    // Only convert crafting table recipes.
    // Colony-only recipes are left untouched.
    // ==========================================

    // Chicken Broth: Heated mixing
    event.remove({ id: 'minecolonies:chicken_broth' });
    event.recipes.create.mixing('minecolonies:chicken_broth', [
        'minecolonies:garlic',
        'minecolonies:onion',
        'minecraft:chicken',
        'minecolonies:large_water_bottle',
        'minecraft:bowl',
        'minecraft:bowl'
    ]).heated();

    // Eggdrop Soup: Heated mixing
    event.remove({ id: 'minecolonies:eggdrop_soup' });
    event.recipes.create.mixing('minecolonies:eggdrop_soup', [
        'minecolonies:onion',
        'minecolonies:onion',
        'minecraft:egg',
        'minecraft:egg',
        'minecraft:chicken',
        'minecraft:bowl'
    ]).heated();

    // Potato Soup: Heated mixing
    event.remove({ id: 'minecolonies:potato_soup' });
    event.recipes.create.mixing('minecolonies:potato_soup', [
        'minecolonies:garlic',
        'minecolonies:onion',
        'minecraft:potato',
        'minecraft:bowl',
        'minecraft:bowl'
    ]).heated();

    // Squash Soup: Heated mixing
    event.remove({ id: 'minecolonies:squash_soup' });
    event.recipes.create.mixing('minecolonies:squash_soup', [
        'minecolonies:garlic',
        'minecolonies:onion',
        'minecolonies:butternut_squash',
        'minecraft:bowl',
        'minecraft:bowl'
    ]).heated();

    // Pea Soup: Heated mixing
    event.remove({ id: 'minecolonies:pea_soup' });
    event.remove({ id: 'minecolonies:soy_pea_soup' });
    event.recipes.create.mixing('minecolonies:pea_soup', [
        'minecolonies:garlic',
        'minecolonies:onion',
        'minecolonies:peas',
        'minecolonies:large_milk_bottle',
        'minecraft:bowl',
        'minecraft:bowl'
    ]).heated();

    // Veggie Soup: Heated mixing
    event.remove({ id: 'minecolonies:veggie_soup' });
    event.recipes.create.mixing('minecolonies:veggie_soup', [
        'minecolonies:garlic',
        'minecolonies:garlic',
        'minecolonies:onion',
        'minecolonies:eggplant',
        'minecraft:carrot',
        'minecraft:bowl'
    ]).heated();

    // Apple Pie: Sequenced Assembly
    event.remove({ id: 'minecolonies:apple_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('minecolonies:apple_pie')
    ], 'minecolonies:durum', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:apple']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:apple']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:sugar']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Plain Cheesecake: Sequenced Assembly
    event.remove({ id: 'minecolonies:plain_cheesecake' });
    event.recipes.create.sequenced_assembly([
        Item.of('minecolonies:plain_cheesecake')
    ], 'minecolonies:durum', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecolonies:creamcheese']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecolonies:butter']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:egg']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Cabochis: Mixing
    event.remove({ id: 'minecolonies:cabochis' });
    event.recipes.create.mixing('minecolonies:cabochis', [
        'minecolonies:onion',
        'minecolonies:cabbage',
        'minecolonies:manchet_bread',
        'minecraft:bowl'
    ]).heated();

    // Fish & Chips: Heated mixing
    event.remove({ id: 'minecolonies:fish_n_chips' });
    event.recipes.create.mixing('minecolonies:fish_n_chips', [
        'minecolonies:garlic',
        'minecolonies:onion',
        'minecolonies:durum',
        'minecraft:potato',
        { tag: 'c:foods/raw_fish' }
    ]).heated();

    // Pierogi: Sequenced Assembly
    event.remove({ id: 'minecolonies:pierogi' });
    event.recipes.create.sequenced_assembly([
        Item.of('minecolonies:pierogi')
    ], 'minecolonies:durum', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecolonies:cheddar_cheese']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:potato']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecolonies:onion']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Cornmeal: Pressing corn
    event.remove({ id: 'minecolonies:cornmeal' });
    event.recipes.create.pressing(
        'minecolonies:cornmeal',
        'minecolonies:corn'
    );

    // Polenta: Heated mixing
    event.remove({ id: 'minecolonies:polenta' });
    event.recipes.create.mixing('minecolonies:polenta', [
        'minecolonies:cornmeal',
        'minecolonies:cornmeal',
        'minecolonies:large_water_bottle',
        'minecraft:bowl',
        'minecraft:bowl'
    ]).heated();

    // Tortillas: Pressing cornmeal flat
    event.remove({ id: 'minecolonies:tortillas' });
    event.recipes.create.pressing(
        'minecolonies:tortillas',
        'minecolonies:cornmeal'
    );

    console.log('[PEAK Expert Mode] Script 13E: Food Fixes + MineColonies loaded!');
});
