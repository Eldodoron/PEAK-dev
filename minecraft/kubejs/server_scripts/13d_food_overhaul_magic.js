// ==========================================
// PEAK EXPERT MODE — SCRIPT 13D
// FOOD OVERHAUL: VEGGIES + ARS + LENDER'S
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // VEGGIES DELIGHT
    // ==========================================

    // --- BURGERS & SANDWICHES (Sequenced Assembly) ---

    // Vegetarian Burger: Bread → Deploy patty → Deploy cabbage → Deploy tomato
    event.remove({ id: 'veggiesdelight:vegetarian_burger' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:vegetarian_burger')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'veggiesdelight:cooked_vegetarian_patty']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/cabbage' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Zucchini Sandwich: Bread → Deploy zucchini → Deploy lettuce → Deploy tomato
    event.remove({ id: 'veggiesdelight:zucchini_sandwich' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:zucchini_sandwich')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/zucchini' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Garlic Bread: Bread → Deploy roasted garlic x4
    event.remove({ id: 'veggiesdelight:garlic_bread' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:garlic_bread')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'veggiesdelight:roasted_garlic_clove']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'veggiesdelight:roasted_garlic_clove']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- WRAPS (Sequenced Assembly) ---

    // Vegetable Wrap: Dough → Deploy pepper → Deploy zucchini → Deploy greens → Deploy rice
    event.remove({ id: 'veggiesdelight:vegetable_wrap' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:vegetables_wrap')
    ], { tag: 'c:foods/dough' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'veggiesdelight:smoked_bellpepper']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'veggiesdelight:roasted_zucchini']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'farmersdelight:cooked_rice'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Uncooked Mhadjeb: Dough → Deploy onion → Deploy pepper → Deploy sauce
    event.remove({ id: 'veggiesdelight:uncooked_mhadjeb' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:uncooked_mhadjeb')
    ], { tag: 'c:foods/dough' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/onion' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/bellpepper' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'farmersdelight:tomato_sauce'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SALADS (Mixing) ---

    // Turnip Salad: Mixing
    event.remove({ id: 'veggiesdelight:turnip_salad' });
    event.recipes.create.mixing('veggiesdelight:turnip_salad', [
        { tag: 'c:foods/leafy_green' },
        { tag: 'c:crops/turnip' },
        'minecraft:bowl'
    ]);

    // --- PLATED MEALS (Heated Mixing) ---

    // Garlic Baked Cod
    event.remove({ id: 'veggiesdelight:garlic_baked_cod' });
    event.recipes.create.mixing('veggiesdelight:garlic_baked_cod', [
        { tag: 'c:foods/cooked_cod' },
        'veggiesdelight:roasted_garlic_clove',
        'veggiesdelight:roasted_garlic_clove',
        { tag: 'c:crops/onion' },
        'minecraft:bowl'
    ]).heated();

    // Garlic Rice with Cauliflower
    event.remove({ id: 'veggiesdelight:garlic_rice_with_cauliflower' });
    event.recipes.create.mixing('veggiesdelight:garlic_rice_with_cauliflower', [
        'veggiesdelight:roasted_garlic_clove',
        'veggiesdelight:roasted_cauliflower_floret',
        'veggiesdelight:roasted_cauliflower_floret',
        'farmersdelight:cooked_rice',
        'minecraft:bowl'
    ]).heated();

    // Steak and Broccoli
    event.remove({ id: 'veggiesdelight:steak_and_broccoli' });
    event.recipes.create.mixing('veggiesdelight:steak_and_broccoli', [
        'minecraft:cooked_beef',
        { tag: 'c:crops/broccoli' },
        'farmersdelight:cooked_rice',
        'minecraft:bowl'
    ]).heated();

    // Stuffed Zucchini Boat
    event.remove({ id: 'veggiesdelight:stuffed_zucchini_boat' });
    event.recipes.create.mixing('veggiesdelight:stuffed_zucchini_boat', [
        'veggiesdelight:roasted_zucchini',
        '#c:foods/cooked_beef',
        '#c:foods/milk'
    ]).heated();

    // --- DOUGH & BAKING ---

    // Vegetarian Patty: Mixing vegs into a patty
    event.remove({ id: 'veggiesdelight:vegetarian_patty' });
    event.recipes.create.mixing('veggiesdelight:raw_vegetarian_patty', [
        { tag: 'c:crops/cauliflower' },
        { tag: 'c:crops/potato' },
        { tag: 'c:crops/zucchini' },
        { tag: 'c:crops/onion' },
        { tag: 'c:crops/grain' }
    ]);

    // Sweet Potato Dough: Mixing
    event.remove({ id: 'veggiesdelight:sweet_potato_dough_from_eggs' });
    event.remove({ id: 'veggiesdelight:sweet_potato_dough_from_water' });
    event.recipes.create.mixing('veggiesdelight:sweet_potato_dough', [
        { tag: 'c:crops/sweet_potato' },
        { tag: 'c:crops/sweet_potato' },
        'minecraft:wheat',
        { tag: 'c:eggs' }
    ]);

    // Sweet Potato Cupcakes: Heated mixing
    event.remove({ id: 'veggiesdelight:sweet_potato_cupcakes' });
    event.recipes.create.mixing('veggiesdelight:sweet_potato_cupcake', [
        'veggiesdelight:sweet_potato_dough',
        '#c:eggs',
        '#c:foods/milk'
    ]).heated();

    // Fermented Garlic Honey: Mixing
    event.remove({ id: 'veggiesdelight:fermented_garlic_honey' });
    event.recipes.create.mixing('veggiesdelight:fermented_garlic_honey', [
        'veggiesdelight:garlic_clove',
        'veggiesdelight:garlic_clove',
        'veggiesdelight:garlic_clove',
        'veggiesdelight:garlic_clove',
        'minecraft:honey_bottle'
    ]);

    // --- PIES & PIZZA (Sequenced Assembly) ---

    // Sweet Potato Pie: Crust → Deploy potato → Deploy sugar → Press
    event.remove({ id: 'veggiesdelight:sweet_potato_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:sweet_potato_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'veggiesdelight:baked_sweet_potato']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:sugar']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Zucchini Quiche: Crust → Deploy zucchini → Deploy meat → Deploy milk → Press
    event.remove({ id: 'veggiesdelight:zucchini_quiche' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:zucchini_quiche')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'veggiesdelight:roasted_zucchini']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', '#c:foods/cooked_mutton']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', '#c:foods/milk']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('kubejs:incomplete_ender_eye').loops(1);

    // Vegan Pizza: Dough → Deploy sauce → Deploy pepper → Deploy veg → Deploy onion → Press
    event.remove({ id: 'veggiesdelight:vegan_pizza' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:vegan_pizza')
    ], { tag: 'c:foods/dough' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'farmersdelight:tomato_sauce']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/bellpepper' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/vegetable' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/onion' }]),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SKEWERS (Sequenced Assembly) ---

    // Turnip Mutton Skewer
    event.remove({ id: 'veggiesdelight:turnip_mutton_skewer' });
    event.recipes.create.sequenced_assembly([
        Item.of('veggiesdelight:turnip_mutton_skewer')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/cooked_mutton' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/turnip' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // ==========================================
    // ARS DELIGHT (Magic Cooking!)
    // ==========================================

    // --- MAGICAL PIES (Sequenced Assembly) ---

    // Source Berry Cookie: Heated mixing
    event.remove({ id: 'arsdelight:source_berry_cookie' });
    event.recipes.create.mixing(
        Item.of('arsdelight:source_berry_cookie', 8),
        [
            'ars_nouveau:sourceberry_bush',
            'minecraft:wheat',
            'minecraft:wheat'
        ]
    ).heated();

    // Bastion Pie: Crust → Deploy bastion → Deploy jam → Deploy sourceberry → Press
    event.remove({ id: 'arsdelight:bastion_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('arsdelight:bastion_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:bastion_pod']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'arsdelight:activated_bastion_jam']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:sourceberry_bush']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Bombegrante Pie
    event.remove({ id: 'arsdelight:bombegrante_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('arsdelight:bombegrante_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:bombegranate_pod']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'arsdelight:neutralized_bombegrante_jam']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:sourceberry_bush']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Frostaya Pie
    event.remove({ id: 'arsdelight:frostaya_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('arsdelight:frostaya_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:frostaya_pod']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'arsdelight:neutralized_frostaya_jam']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:sourceberry_bush']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Mendosteen Pie
    event.remove({ id: 'arsdelight:mendosteen_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('arsdelight:mendosteen_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:mendosteen_pod']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'arsdelight:activated_mendosteen_jam']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'ars_nouveau:sourceberry_bush']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- MAGICAL SALADS (Mechanical Crafting — arcane plating) ---

    // Wilden Salad: Requires arcane presentation
    event.remove({ id: 'arsdelight:wilden_salad' });
    event.recipes.create.mechanical_crafting('arsdelight:wilden_salad', [
        'AMA',
        'SWS',
        ' B '
    ], {
        A: 'arsdelight:arch_sauce',
        M: 'ars_nouveau:magebloom',
        S: 'ars_nouveau:sourceberry_bush',
        W: 'arsdelight:grilled_wilden_meat',
        B: 'minecraft:bowl'
    });

    // --- MAGICAL SKEWERS (Sequenced Assembly) ---

    // Chimera Skewer
    event.remove({ id: 'arsdelight:chimera_skewer' });
    event.recipes.create.sequenced_assembly([
        Item.of('arsdelight:chimera_skewer')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'arsdelight:raw_chimera' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'arsdelight:wilden_spike_powder']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/cabbage' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Wilden Skewer
    event.remove({ id: 'arsdelight:wilden_skewer' });
    event.recipes.create.sequenced_assembly([
        Item.of('arsdelight:wilden_skewer')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'arsdelight:raw_wilden_meat' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'arsdelight:wilden_spike_powder']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/cabbage' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // ==========================================
    // LENDER'S DELIGHT (Cataclysm Foods!)
    // ==========================================

    // --- SANDWICHES (Sequenced Assembly) ---

    // Amethyst Crab Sandwich
    event.remove({ id: 'lendersdelight:amethyst_crab_sandwich' });
    event.recipes.create.sequenced_assembly([
        Item.of('lendersdelight:amethyst_crab_sandwich')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'lendersdelight:cooked_amethyst_crab_meat']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Coral Chunk Sandwich
    event.remove({ id: 'lendersdelight:coral_chunk_sandwich' });
    event.recipes.create.sequenced_assembly([
        Item.of('lendersdelight:coral_chunk_sandwich')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'cataclysm:coral_chunk']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SUSHI ROLLS ---

    // Crystallized Coral Roll: Deploying
    event.remove({ id: 'lendersdelight:crystallized_coral_roll' });
    event.recipes.create.deploying(
        'lendersdelight:crystallized_coral_roll',
        ['minecraft:dried_kelp', 'cataclysm:crystallized_coral_fragments']
    );

    // Lionfish Roll: Rice → Deploy lionfish
    event.remove({ id: 'lendersdelight:lionfish_roll' });
    event.recipes.create.sequenced_assembly([
        Item.of('lendersdelight:lionfish_roll', 2)
    ], 'farmersdelight:cooked_rice', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'lendersdelight:lionfish_slice']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'lendersdelight:lionfish_slice'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- PIES ---

    // Crystallized Coral Pie
    event.remove({ id: 'lendersdelight:crystallized_coral_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('lendersdelight:crystallized_coral_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'cataclysm:crystallized_coral']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'cataclysm:crystallized_coral']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:sugar']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- FEAST BLOCKS (Mechanical Crafting) ---

    // Honey Glazed Horn: The ultimate Cataclysm feast
    event.remove({ id: 'lendersdelight:honey_glazed_horn' });
    event.recipes.create.mechanical_crafting('lendersdelight:honey_glazed_horn', [
        'SHS',
        'RMR',
        'SAS'
    ], {
        S: 'minecraft:sweet_berries',
        H: 'minecraft:honey_bottle',
        R: 'farmersdelight:rice',
        M: 'cataclysm:monstrous_horn',
        A: 'minecraft:bowl'
    });

    console.log('[PEAK Expert Mode] Script 13D: Food Overhaul - Veggies/Ars/Lender loaded!');
    console.log('==========================================');
    console.log('[PEAK Expert Mode] FOOD OVERHAUL COMPLETE!');
    console.log('All food recipes now use Create processes.');
    console.log('==========================================');
});
