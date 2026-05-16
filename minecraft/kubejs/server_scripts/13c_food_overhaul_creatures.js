// ==========================================
// PEAK EXPERT MODE — SCRIPT 13C
// FOOD OVERHAUL: ALEX'S + AQUACULTURE + OCEAN'S
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // ALEX'S DELIGHT
    // ==========================================

    // --- BURGERS (Sequenced Assembly) ---

    // Bison Burger: Bread → Deploy patty → Deploy lettuce → Deploy tomato
    event.remove({ id: 'alexsdelight:bison_burger' });
    event.recipes.create.sequenced_assembly([
        Item.of('alexsdelight:bison_burger')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'alexsdelight:bison_patty']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Kangaroo Burger: Bread → Deploy kangaroo → Deploy kangaroo → Deploy lettuce
    event.remove({ id: 'alexsdelight:kangaroo_burger' });
    event.recipes.create.sequenced_assembly([
        Item.of('alexsmobs:kangaroo_burger')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'alexsdelight:cooked_kangaroo' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'alexsdelight:cooked_kangaroo' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SANDWICHES (Sequenced Assembly) ---

    // Bunfungus Sandwich: Bread → Deploy bunfungus → Deploy mushrooms
    event.remove({ id: 'alexsdelight:bunfungus_sandwich' });
    event.recipes.create.sequenced_assembly([
        Item.of('alexsdelight:bunfungus_sandwich')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'alexsdelight:cooked_bunfungus']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'farmersdelight:red_mushroom_colony']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'farmersdelight:red_mushroom_colony'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Gongylidia Bruschetta: Bread → Deploy gongylidia → Deploy oil → Deploy tomato
    event.remove({ id: 'alexsdelight:gongylidia_bruschetta' });
    event.recipes.create.sequenced_assembly([
        Item.of('alexsdelight:gongylidia_bruschetta')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'alexsmobs:gongylidia']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'alexsmobs:fish_oil']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SALADS (Mixing) ---

    // Maggot Salad: Mixing
    event.remove({ id: 'alexsdelight:maggot_salad' });
    event.remove({ id: 'alexsdelight:maggot_salad_alt' });
    event.recipes.create.mixing(
        'alexsdelight:maggot_salad',
        [
            'alexsmobs:maggot',
            { tag: 'c:foods/cabbage' },
            { tag: 'c:crops/tomato' },
            { tag: 'c:crops/onion' },
            { tag: 'c:crops/beetroot' },
            'minecraft:bowl'
        ]
    );

    // --- SKEWERS (Sequenced Assembly) ---

    // Alex's Barbecue Stick: Stick → Deploy moose → Deploy chicken → Deploy vegs
    event.remove({ id: 'alexsdelight:barbecue_stick' });
    event.recipes.create.sequenced_assembly([
        Item.of('farmersdelight:barbecue_stick', 2)
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'alexsmobs:cooked_moose_ribs']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:cooked_chicken']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'farmersdelight:tomato'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // ==========================================
    // AQUACULTURE DELIGHT
    // ==========================================

    // --- SUSHI ROLLS (Sequenced Assembly) ---

    // Raw Fish Fillet Roll: Rice → Deploy raw fillet → Deploy raw fillet
    event.remove({ id: 'aquaculturedelight:raw_fish_fillet_roll' });
    event.recipes.create.sequenced_assembly([
        Item.of('aquaculturedelight:raw_fish_fillet_roll', 2)
    ], 'farmersdelight:cooked_rice', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'aquaculture:fish_fillet_raw']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'aquaculture:fish_fillet_raw'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Fried Perch Roll: Rice → Deploy fried perch
    event.remove({ id: 'aquaculturedelight:fried_perch_roll' });
    event.recipes.create.sequenced_assembly([
        Item.of('aquaculturedelight:fried_perch_roll', 2)
    ], 'farmersdelight:cooked_rice', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'aquaculturedelight:crispy_fried_perch']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'aquaculturedelight:crispy_fried_perch'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SKEWERS (Sequenced Assembly) ---

    // Catfish Barbecue: Stick → Deploy catfish → Deploy tomato → Deploy cabbage
    event.remove({ id: 'aquaculturedelight:catfish_barbecue_stick' });
    event.recipes.create.sequenced_assembly([
        Item.of('aquaculturedelight:catfish_barbecue')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/raw_catfish' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/cabbage' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- PLATED MEALS (Heated Mixing) ---

    // Fish and Chips: Heated mixing
    event.remove({ id: 'aquaculturedelight:fish_and_chips' });
    event.recipes.create.mixing(
        'aquaculturedelight:fish_and_chips',
        [
            'aquaculturedelight:crispy_fried_perch',
            'minecraft:baked_potato',
            'farmersdelight:tomato_sauce',
            'minecraft:bowl'
        ]
    ).heated();

    // Large Fish with Vegetables: Heated mixing
    event.remove({ id: 'aquaculturedelight:large_fish_with_vegetables' });
    event.recipes.create.mixing(
        'aquaculturedelight:large_fish_with_vegetables',
        [
            'aquaculture:fish_fillet_cooked',
            'aquaculture:fish_fillet_cooked',
            { tag: 'c:crops/tomato' },
            { tag: 'c:crops/onion' },
            'farmersdelight:cooked_rice',
            'minecraft:bowl'
        ]
    ).heated();

    // Turtle Meat Dish: Heated mixing
    event.remove({ id: 'aquaculturedelight:turtle_meat_dish' });
    event.recipes.create.mixing(
        'aquaculturedelight:turtle_meat_dish',
        [
            { tag: 'c:foods/cooked_turtle' },
            { tag: 'c:foods/cooked_turtle' },
            { tag: 'c:crops/cabbage' },
            'farmersdelight:pumpkin_slice',
            'minecraft:carrot',
            'minecraft:bowl'
        ]
    ).heated();

    // Crispy Nori Kelp: Mixing
    event.remove({ id: 'aquaculturedelight:crispy_nori_kelp' });
    event.recipes.create.mixing(
        'aquaculturedelight:crispy_nori_kelp',
        [
            'minecraft:dried_kelp',
            'minecraft:dried_kelp',
            'aquaculture:algae',
            'minecraft:bowl'
        ]
    );

    // --- FEAST (Mechanical Crafting) ---

    // Fish Roll Medley: Huge sushi platter
    event.remove({ id: 'aquaculturedelight:fish_roll_medley' });
    event.recipes.create.mechanical_crafting('aquaculturedelight:fish_roll_medley', [
        'SSS',
        'RRF',
        'FBA'
    ], {
        S: 'aquaculture:sushi',
        R: 'aquaculturedelight:raw_fish_fillet_roll',
        F: 'aquaculturedelight:fried_perch_roll',
        B: 'minecraft:bowl',
        A: 'aquaculturedelight:fried_perch_roll'
    });

    // ==========================================
    // OCEAN'S DELIGHT
    // ==========================================

    // --- SUSHI ROLLS (Sequenced Assembly) ---

    // Elder Guardian Roll: Rice → Deploy elder guardian slice
    event.remove({ id: 'oceansdelight:elder_guardian_roll' });
    event.recipes.create.sequenced_assembly([
        Item.of('oceansdelight:elder_guardian_roll', 2)
    ], 'farmersdelight:cooked_rice', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'oceansdelight:elder_guardian_slice']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'oceansdelight:elder_guardian_slice'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Fugu Roll: Rice → Deploy fugu slice
    event.remove({ id: 'oceansdelight:fugu_roll' });
    event.recipes.create.sequenced_assembly([
        Item.of('oceansdelight:fugu_roll', 2)
    ], 'farmersdelight:cooked_rice', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'oceansdelight:fugu_slice']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'oceansdelight:fugu_slice'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- WRAPS & SANDWICHES (Sequenced Assembly) ---

    // Cabbage Wrapped Elder Guardian
    event.remove({ id: 'oceansdelight:cabbage_wrapped_elder_guardian' });
    event.recipes.create.sequenced_assembly([
        Item.of('oceansdelight:cabbage_wrapped_elder_guardian')
    ], 'oceansdelight:cooked_elder_guardian_slice', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/cabbage' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/onion' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:crops/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SALADS (Mixing) ---

    // Seagrass Salad: Simple mixing
    event.remove({ id: 'oceansdelight:seagrass_salad' });
    event.recipes.create.mixing(
        'oceansdelight:seagrass_salad',
        [
            'minecraft:seagrass',
            'minecraft:seagrass',
            'minecraft:bowl'
        ]
    );

    // --- STUFFED DISHES (Heated Mixing / Mechanical Crafting) ---

    // Stuffed Cod: Heated mixing
    event.remove({ id: 'oceansdelight:stuffed_cod' });
    event.recipes.create.mixing(
        'oceansdelight:stuffed_cod',
        [
            'minecraft:cod',
            'minecraft:kelp',
            'minecraft:brown_mushroom',
            { tag: 'c:crops/onion' },
            { tag: 'c:crops/tomato' },
            'farmersdelight:rope'
        ]
    ).heated();

    // Stuffed Squid: Heated mixing
    event.remove({ id: 'oceansdelight:stuffed_squid' });
    event.recipes.create.mixing(
        'oceansdelight:stuffed_squid',
        [
            'oceansdelight:tentacles',
            'farmersdelight:rice',
            'minecraft:kelp'
        ]
    ).heated();

    // --- SKEWERS (Deploying) ---

    // Tentacle on a Stick
    event.remove({ id: 'oceansdelight:tentacle_on_a_stick' });
    event.recipes.create.deploying(
        'oceansdelight:tentacle_on_a_stick',
        ['minecraft:stick', 'oceansdelight:tentacles']
    );

    console.log('[PEAK Expert Mode] Script 13C: Food Overhaul - Alex/Aquaculture/Ocean loaded!');
});
