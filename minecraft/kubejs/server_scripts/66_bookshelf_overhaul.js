// priority: 0
// Enchanting bookshelf overhaul.
//
// Tomes (kubejs:*book) are made at a machine or altar, then combined with themed
// blocks in a crafting table to build the specialised shelves:
//   3 themed blocks / 3 tomes / 3 themed blocks.
//
// Tome item definitions: startup_scripts/bookshelf_tomes.js
// Shelf stats: data/apothic_enchanting/enchanting_stats/wisewood_bookshelf.json

ServerEvents.recipes(event => {

    // ------------------------------------------------------------
    // Helpers
    // ------------------------------------------------------------
    function repeat(ingredient, count) {
        let list = [];
        for (let i = 0; i < count; i++) {
            list.push({ item: ingredient });
        }
        return list;
    }

    function apparatus(id, reagent, pedestals, result, sourceCost) {
        event.custom({
            type: 'ars_nouveau:enchanting_apparatus',
            keepNbtOfReagent: false,
            pedestalItems: pedestals.map(item => ({ item: item })),
            reagent: { item: reagent },
            result: { id: result, count: 1 },
            sourceCost: sourceCost
        }).id(id);
    }

    // ------------------------------------------------------------
    // Remove previous shelf recipes
    // ------------------------------------------------------------
    [
        'apothic_enchanting:stoneshelf',
        'apothic_enchanting:melonshelf',
        'apothic_enchanting:beeshelf',
        'apothic_enchanting:hellshelf',
        'apothic_enchanting:seashelf',
        'apothic_enchanting:dormant_deepshelf',
        'apothic_enchanting:endshelf',
        'apothic_enchanting:echoing_sculkshelf',
        'apothic_enchanting:soul_touched_sculkshelf'
    ].forEach(shelf => event.remove({ output: shelf }));

    // ------------------------------------------------------------
    // Tomes: Create basin (3 books -> 3 tomes)
    // ------------------------------------------------------------
    event.custom({
        type: 'create:compacting',
        ingredients: repeat('minecraft:book', 3).concat(repeat('create:andesite_alloy', 4)),
        results: [{ id: 'kubejs:stonebook', count: 3 }]
    }).id('kubejs:tome/stonebook');

    event.custom({
        type: 'create:mixing',
        ingredients: repeat('minecraft:book', 3).concat([
            { item: 'minecraft:honeycomb_block' },
            { type: 'neoforge:single', amount: 750, fluid: 'create:honey' }
        ]),
        results: [{ id: 'kubejs:beebook', count: 3 }]
    }).id('kubejs:tome/beebook');

    event.custom({
        type: 'create:compacting',
        ingredients: repeat('minecraft:book', 3)
            .concat(repeat('minecraft:cracked_deepslate_tiles', 4))
            .concat(repeat('minecraft:amethyst_shard', 2)),
        results: [{ id: 'kubejs:deepbook', count: 3 }]
    }).id('kubejs:tome/deepbook');

    // ------------------------------------------------------------
    // Tomes: Farmer's Delight cooking pot (3 books -> 3 tomes, 6 slots)
    // ------------------------------------------------------------
    event.custom({
        type: 'farmersdelight:cooking',
        experience: 1.0,
        ingredients: repeat('minecraft:book', 3).concat([
            { item: 'minecraft:glistering_melon_slice' },
            { item: 'minecraft:melon_slice' },
            { item: 'minecraft:sugar' }
        ]),
        recipe_book_tab: 'misc',
        result: { id: 'kubejs:melonbook', count: 3 }
    }).id('kubejs:tome/melonbook');

    // ------------------------------------------------------------
    // Tomes: Ars Nouveau enchanting apparatus (1 book -> 1 tome)
    // ------------------------------------------------------------
    apparatus('kubejs:tome/hellbook', 'minecraft:book', [
        'minecraft:blaze_rod',
        'minecraft:magma_cream',
        'minecraft:nether_wart'
    ], 'kubejs:hellbook', 300);

    apparatus('kubejs:tome/seabook_nautilus', 'minecraft:book', [
        'minecraft:prismarine_crystals',
        'minecraft:nautilus_shell',
        'minecraft:heart_of_the_sea'
    ], 'kubejs:seabook', 300);

    apparatus('kubejs:tome/seabook_pufferfish', 'minecraft:book', [
        'minecraft:prismarine_crystals',
        'minecraft:pufferfish',
        'minecraft:heart_of_the_sea'
    ], 'kubejs:seabook', 300);

    apparatus('kubejs:tome/endbook', 'minecraft:book', [
        'minecraft:end_stone_bricks',
        'minecraft:ender_pearl',
        'apothic_enchanting:infused_breath',
        'minecraft:chorus_fruit'
    ], 'kubejs:endbook', 1000);

    // ------------------------------------------------------------
    // Tomes: Apothic table infusion
    // ------------------------------------------------------------
    event.custom({
        type: 'apothic_enchanting:infusion',
        input: { item: 'kubejs:deepbook' },
        requirements: { eterna: 60, quanta: 40, arcana: 40 },
        result: { id: 'kubejs:sculkbook', count: 1 }
    }).id('kubejs:infusion/sculkbook');

    // Infused Breath is an ingredient of the Ender Codex, which is needed for the End Shelf.
    // The Eterna requirement is lowered from 80 to 70 so it is reachable before any End Shelf exists.
    event.remove({ id: 'apothic_enchanting:infusion/infused_breath' });
    event.custom({
        type: 'apothic_enchanting:infusion',
        input: { item: 'minecraft:dragon_breath' },
        requirements: { eterna: 70, quanta: 15, arcana: 60 },
        max_requirements: { eterna: -1, quanta: 30, arcana: -1 },
        result: { id: 'apothic_enchanting:infused_breath', count: 3 }
    }).id('kubejs:infusion/infused_breath');

    // Enchanted Precision Mechanism: Infused at max enchanting power (90 Eterna, 90 Quanta, 90 Arcana).
    event.custom({
        type: 'apothic_enchanting:infusion',
        input: { item: 'create:precision_mechanism' },
        requirements: { eterna: 90, quanta: 90, arcana: 90 },
        result: { id: 'kubejs:enchanted_precision_mechanism', count: 1 }
    }).id('kubejs:infusion/enchanted_precision_mechanism');

    // ------------------------------------------------------------
    // Shelves: 3 themed blocks / 3 tomes / 3 themed blocks
    // ------------------------------------------------------------
    event.shaped('apothic_enchanting:stoneshelf', [
        'AAA',
        'BBB',
        'AAA'
    ], {
        A: 'minecraft:polished_andesite',
        B: 'kubejs:stonebook'
    }).id('kubejs:shelf/stoneshelf');

    event.shaped('apothic_enchanting:melonshelf', [
        'AAA',
        'BBB',
        'AAA'
    ], {
        A: 'minecraft:melon',
        B: 'kubejs:melonbook'
    }).id('kubejs:shelf/melonshelf');

    event.shaped('apothic_enchanting:beeshelf', [
        'HBH',
        'TTT',
        'HBH'
    ], {
        H: 'minecraft:honeycomb',
        B: 'minecraft:beehive',
        T: 'kubejs:beebook'
    }).id('kubejs:shelf/beeshelf');

    event.shaped('apothic_enchanting:hellshelf', [
        'AAA',
        'BBB',
        'AAA'
    ], {
        A: 'minecraft:crimson_planks',
        B: 'kubejs:hellbook'
    }).id('kubejs:shelf/hellshelf');

    event.shaped('apothic_enchanting:seashelf', [
        'AAA',
        'BBB',
        'AAA'
    ], {
        A: 'minecraft:prismarine_bricks',
        B: 'kubejs:seabook'
    }).id('kubejs:shelf/seashelf');

    event.shaped('apothic_enchanting:dormant_deepshelf', [
        'AAA',
        'BBB',
        'AAA'
    ], {
        A: 'minecraft:cracked_deepslate_tiles',
        B: 'kubejs:deepbook'
    }).id('kubejs:shelf/dormant_deepshelf');

    event.shaped('apothic_enchanting:endshelf', [
        'AAA',
        'BBB',
        'AAA'
    ], {
        A: 'minecraft:end_stone_bricks',
        B: 'kubejs:endbook'
    }).id('kubejs:shelf/endshelf');

    event.shaped('apothic_enchanting:echoing_sculkshelf', [
        'STS',
        'BBB',
        'CDC'
    ], {
        S: 'minecraft:sculk',
        T: 'apothic_enchanting:warden_tendril',
        B: 'kubejs:sculkbook',
        C: 'minecraft:sculk_catalyst',
        D: 'apothic_enchanting:echoing_deepshelf'
    }).id('kubejs:shelf/echoing_sculkshelf');

    event.shaped('apothic_enchanting:soul_touched_sculkshelf', [
        'STS',
        'BBB',
        'CDC'
    ], {
        S: 'minecraft:sculk',
        T: 'apothic_enchanting:warden_tendril',
        B: 'kubejs:sculkbook',
        C: 'minecraft:sculk_catalyst',
        D: 'apothic_enchanting:soul_touched_deepshelf'
    }).id('kubejs:shelf/soul_touched_sculkshelf');

    // ------------------------------------------------------------
    // Wisewood Bookshelf: vanilla bookshelves only, so higher-tier shelves
    // can never be consumed by crafting or by the Create Wizardry filling recipe.
    // ------------------------------------------------------------
    event.remove({ id: 'irons_spellbooks:wisewood_bookshelf' });
    event.shaped(Item.of('irons_spellbooks:wisewood_bookshelf', 8), [
        'BBB',
        'BAB',
        'BBB'
    ], {
        B: 'minecraft:bookshelf',
        A: 'irons_spellbooks:arcane_essence'
    }).id('kubejs:shelf/wisewood_bookshelf');

    event.remove({ id: 'irons_spellbooks:filling/wisewood_bookshelf' });
    event.custom({
        type: 'create:filling',
        ingredients: [
            { item: 'minecraft:bookshelf' },
            { type: 'neoforge:single', amount: 10, fluid: 'create_wizardry:mana' }
        ],
        results: [{ id: 'irons_spellbooks:wisewood_bookshelf' }]
    }).id('kubejs:filling/wisewood_bookshelf');

    // ------------------------------------------------------------
    // Enchanted Brass Cube: Sub-assembly binding all eight tomes
    // ------------------------------------------------------------
    event.shaped('kubejs:enchanted_brass_cube', [
        'ABC',
        'DEF',
        'GHI'
    ], {
        A: 'kubejs:stonebook',
        B: 'kubejs:melonbook',
        C: 'kubejs:beebook',
        D: 'kubejs:hellbook',
        E: 'create_sa:brass_cube',
        F: 'kubejs:seabook',
        G: 'kubejs:deepbook',
        H: 'kubejs:sculkbook',
        I: 'kubejs:endbook'
    }).id('kubejs:crafting/enchanted_brass_cube');

    // ------------------------------------------------------------
    // Brass Bookshelf: 2x sequenced assembly on the Enchanted Brass Cube
    // ------------------------------------------------------------
    const incompleteBrass = 'create_enchantment_industry:incomplete_brass_bookshelf';

    const apokineticsGems = [
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:conveyance', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:equilibrium', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:extension', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:flowing', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:frostwork', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:ignition', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:impact', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:momentum', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:precision', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:rupture', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:velocity', 'apotheosis:purity': 'perfect' }),
        Item.of('apotheosis:gem', { 'apotheosis:gem': 'apokinetics:yielding', 'apotheosis:purity': 'perfect' })
    ];

    event.remove({ id: 'create_enchantment_industry:sequenced_assembly/brass_bookshelf' });
    event.recipes.create.sequenced_assembly(
        ['create_enchantment_industry:brass_bookshelf'],
        'kubejs:enchanted_brass_cube',
        [
            event.recipes.createFilling(incompleteBrass, [incompleteBrass, Fluid.of('create_wizardry:mana', 250)]),
            event.recipes.createDeploying(incompleteBrass, [incompleteBrass, 'create:brass_casing']),
            event.recipes.createDeploying(incompleteBrass, [incompleteBrass, 'create:electron_tube']),
            event.recipes.createDeploying(incompleteBrass, [incompleteBrass, 'create:sequenced_gearshift']),
            event.recipes.createDeploying(incompleteBrass, [incompleteBrass, 'kubejs:enchanted_precision_mechanism']),
            event.recipes.createDeploying(incompleteBrass, [incompleteBrass, apokineticsGems]),
            event.recipes.createDeploying(incompleteBrass, [incompleteBrass, 'create_enchantment_industry:super_enchanting_template']),
            event.recipes.createFilling(incompleteBrass, [incompleteBrass, Fluid.of('create_enchantment_industry:experience', 250)])
        ]
    ).transitionalItem(incompleteBrass).loops(2).id('kubejs:sequenced_assembly/brass_bookshelf');

    // ------------------------------------------------------------
    // Creative Bookshelf: 9x9 Avaritia extreme crafting
    //   N = Neutron Ingot            C = Crystal Matrix Ingot
    //   I = Infinity Ingot           X = Infinity Catalyst
    //   W = Wisewood Bookshelf       B = Brass Bookshelf
    //   H = Blazing Hellshelf        S = Heart Seashelf
    //   E = Echoing Sculkshelf       D = Draconic End Shelf
    // ------------------------------------------------------------
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            'NNNNNNNNN',
            'NCCCXCCCN',
            'NCHCCCSCN',
            'NCCWIWCCN',
            'NXCIBICXN',
            'NCCWIWCCN',
            'NCECCCDCN',
            'NCCCXCCCN',
            'NNNNNNNNN'
        ],
        key: {
            N: { item: 'avaritia:neutron_ingot' },
            C: { item: 'avaritia:crystal_matrix_ingot' },
            I: { item: 'avaritia:infinity_ingot' },
            X: { item: 'avaritia:infinity_catalyst' },
            W: { item: 'irons_spellbooks:wisewood_bookshelf' },
            B: { item: 'create_enchantment_industry:brass_bookshelf' },
            H: { item: 'apothic_enchanting:blazing_hellshelf' },
            S: { item: 'apothic_enchanting:heart_seashelf' },
            E: { item: 'apothic_enchanting:echoing_sculkshelf' },
            D: { item: 'apothic_enchanting:draconic_endshelf' }
        },
        result: { id: 'create_enchantment_industry:creative_bookshelf', count: 1 },
        tier: 4
    }).id('kubejs:shelf/creative_bookshelf');

    console.log('[PEAK Expert Mode] Script 66: Bookshelf overhaul loaded!');
});
