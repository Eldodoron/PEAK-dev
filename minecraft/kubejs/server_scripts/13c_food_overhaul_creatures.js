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
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "tag": "c:foods/bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "alexsdelight:bison_patty" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:foods/leafy_green" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "alexsdelight:bison_burger" }],
        "loops": 1
    });

    // Kangaroo Burger: Bread → Deploy kangaroo → Deploy kangaroo → Deploy lettuce
    event.remove({ id: 'alexsdelight:kangaroo_burger' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "tag": "c:foods/bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "alexsdelight:cooked_kangaroo" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "alexsdelight:cooked_kangaroo" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:foods/leafy_green" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "alexsmobs:kangaroo_burger" }],
        "loops": 1
    });

    // --- SANDWICHES (Sequenced Assembly) ---

    // Bunfungus Sandwich: Bread → Deploy bunfungus → Deploy mushrooms
    event.remove({ id: 'alexsdelight:bunfungus_sandwich' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "tag": "c:foods/bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "alexsdelight:cooked_bunfungus" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:red_mushroom_colony" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:red_mushroom_colony" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "alexsdelight:bunfungus_sandwich" }],
        "loops": 1
    });

    // Gongylidia Bruschetta: Bread → Deploy gongylidia → Deploy oil → Deploy tomato
    event.remove({ id: 'alexsdelight:gongylidia_bruschetta' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "tag": "c:foods/bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "alexsmobs:gongylidia" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "alexsmobs:fish_oil" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "alexsdelight:gongylidia_bruschetta" }],
        "loops": 1
    });

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
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:stick" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "alexsmobs:cooked_moose_ribs" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:cooked_chicken" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('farmersdelight:barbecue_stick', 2)],
        "loops": 1
    });

    // ==========================================
    // AQUACULTURE DELIGHT
    // ==========================================

    // --- SUSHI ROLLS (Sequenced Assembly) ---

    // Raw Fish Fillet Roll: Rice → Deploy raw fillet → Deploy raw fillet
    event.remove({ id: 'aquaculturedelight:raw_fish_fillet_roll' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "aquaculture:fish_fillet_raw" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "aquaculture:fish_fillet_raw" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('aquaculturedelight:raw_fish_fillet_roll', 2)],
        "loops": 1
    });

    // Fried Perch Roll: Rice → Deploy fried perch
    event.remove({ id: 'aquaculturedelight:fried_perch_roll' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "aquaculturedelight:crispy_fried_perch" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "aquaculturedelight:crispy_fried_perch" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('aquaculturedelight:fried_perch_roll', 2)],
        "loops": 1
    });

    // --- SKEWERS (Sequenced Assembly) ---

    // Catfish Barbecue: Stick → Deploy catfish → Deploy tomato → Deploy cabbage
    event.remove({ id: 'aquaculturedelight:catfish_barbecue_stick' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:stick" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:foods/raw_catfish" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/cabbage" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "aquaculturedelight:catfish_barbecue" }],
        "loops": 1
    });

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
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "oceansdelight:elder_guardian_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "oceansdelight:elder_guardian_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('oceansdelight:elder_guardian_roll', 2)],
        "loops": 1
    });

    // Fugu Roll: Rice → Deploy fugu slice
    event.remove({ id: 'oceansdelight:fugu_roll' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "oceansdelight:fugu_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "oceansdelight:fugu_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('oceansdelight:fugu_roll', 2)],
        "loops": 1
    });

    // --- WRAPS & SANDWICHES (Sequenced Assembly) ---

    // Cabbage Wrapped Elder Guardian
    event.remove({ id: 'oceansdelight:cabbage_wrapped_elder_guardian' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "oceansdelight:cooked_elder_guardian_slice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:foods/cabbage" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/onion" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "oceansdelight:cabbage_wrapped_elder_guardian" }],
        "loops": 1
    });

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
