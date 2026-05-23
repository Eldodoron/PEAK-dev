// 01_readded_recipes.js
// Re-adds purged recipes based on log analysis using native KubeJS 1.21.1 wrappers

ServerEvents.recipes(event => {

    // ==========================================
    // 1. Irons Spellbooks Create Compat (Filling)
    // ==========================================
    event.recipes.create.filling('irons_spellbooks:uncommon_ink', [
        'minecraft:glass_bottle',
        Fluid.of('irons_spellbooks:uncommon_ink', 250)
    ]).id('irons_spellbooks:create_compat/create_fill_uncommon_ink');

    event.recipes.create.filling('irons_spellbooks:invisibility_elixir', [
        'minecraft:glass_bottle',
        Fluid.of('irons_spellbooks:invisibility_elixir', 250)
    ]).id('kubejs:irons_spellbooks/create_compat/create_fill_invisibility_elixir');

    event.recipes.create.filling('irons_spellbooks:ice_venom_vial', [
        'minecraft:glass_bottle',
        Fluid.of('irons_spellbooks:ice_venom', 250)
    ]).id('kubejs:irons_spellbooks/create_compat/create_fill_ice_venom_vial');

    event.recipes.create.filling('irons_spellbooks:oakskin_elixir', [
        'minecraft:glass_bottle',
        Fluid.of('irons_spellbooks:oakskin_elixir', 250)
    ]).id('kubejs:irons_spellbooks/create_compat/create_fill_oakskin_elixir');

    event.recipes.create.filling('irons_spellbooks:common_ink', [
        'minecraft:glass_bottle',
        Fluid.of('irons_spellbooks:common_ink', 250)
    ]).id('kubejs:irons_spellbooks/create_compat/create_fill_common_ink');


    // ==========================================
    // 2. Create Diesel Generators (Mixing)
    // ==========================================
    event.recipes.create.mixing(Fluid.of('createdieselgenerators:biodiesel', 200), [
        {fluidTag: 'c:ethanol', amount: 100},
        {fluidTag: 'c:plantoil', amount: 100}
    ]).id('kubejs:createdieselgenerators/biodiesel');

    event.recipes.create.mixing('createdieselgenerators:asphalt_block', [
        'minecraft:gravel',
        'minecraft:sand',
        {fluidTag: 'c:crude_oil', amount: 100}
    ]).id('kubejs:createdieselgenerators/asphalt_block');

    const concreteColors = ['pink', 'purple', 'white', 'light_gray'];
    concreteColors.forEach(color => {
        event.recipes.create.mixing(`minecraft:${color}_concrete`, [
            `minecraft:${color}_concrete_powder`,
            Fluid.of('minecraft:water', 100)
        ]).id(`kubejs:mixing_${color}_concrete`);
    });


    // ==========================================
    // 3. Create Confectionery
    // ==========================================
    event.recipes.create.mixing(Fluid.of('create_confectionery:hot_chocolate', 250), [
        'minecraft:cocoa_beans',
        {fluidTag: 'c:milk', amount: 250}
    ]).id('kubejs:create_confectionery/hot_chocolate_recipe');

    event.recipes.create.mixing(Fluid.of('create_confectionery:white_chocolate', 250), [
        'minecraft:cocoa_beans',
        'minecraft:sugar',
        {fluidTag: 'c:milk', amount: 250}
    ]).id('kubejs:create_confectionery/white_chocolate_recipe');

    event.recipes.create.mixing(Fluid.of('create_confectionery:ruby_chocolate', 250), [
        'minecraft:cocoa_beans',
        'minecraft:sweet_berries',
        {fluidTag: 'c:milk', amount: 250}
    ]).id('kubejs:create_confectionery/ruby_chocolate_recipe');

    event.recipes.create.compacting('create_confectionery:bar_of_black_chocolate', [
        Fluid.of('create_confectionery:black_chocolate', 250)
    ]).id('kubejs:create_confectionery/bar_of_black_chocolate_recipe');

    event.recipes.create.mixing('4x create_confectionery:honey_candy', [
        'minecraft:honey_bottle',
        'minecraft:sugar'
    ]).id('kubejs:create_confectionery/honey_candy_recipe');

    event.recipes.create.mixing('4x create_confectionery:candy_cane', [
        'minecraft:sugar',
        'minecraft:red_dye'
    ]).id('kubejs:create_confectionery/candy_cane_recipe');


    // ==========================================
    // 4. Create Deep Dark
    // ==========================================
    event.recipes.create.sequenced_assembly(
        [Item.of('create_deep_dark:echo_ingot').withChance(1.0)], 
        'minecraft:iron_ingot', 
        [
            event.recipes.create.deploying('create_deep_dark:incomplete_echo_ingot', ['create_deep_dark:incomplete_echo_ingot', 'minecraft:echo_shard']),
            event.recipes.create.filling('create_deep_dark:incomplete_echo_ingot', ['create_deep_dark:incomplete_echo_ingot', Fluid.of('minecraft:water', 250)])
        ]
    ).transitionalItem('create_deep_dark:incomplete_echo_ingot').loops(1).id('kubejs:create_deep_dark/sequenced_assembly_echo_ingot');

    event.recipes.create.crushing([
        'create:experience_nugget',
        Item.of('create_deep_dark:sculk_flour').withChance(0.5),
        Item.of('minecraft:sculk').withChance(0.75)
    ], 'minecraft:sculk_catalyst').id('kubejs:create/crushing_sculk_catalyst');

    event.recipes.create.crushing([
        'create:experience_nugget',
        Item.of('create_deep_dark:sculk_flour').withChance(0.5),
        Item.of('minecraft:sculk').withChance(0.75)
    ], 'minecraft:sculk_shrieker').id('kubejs:create/crushing_sculk_shrieker');

});

