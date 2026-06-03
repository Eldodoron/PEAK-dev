// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 13D
// FOOD OVERHAUL: VEGGIES + ARS + LENDER'S
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // VEGGIES DELIGHT
    // ==========================================

    // --- BURGERS & SANDWICHES (Sequenced Assembly) ---

    // Vegetarian Burger: Bread â†’ Deploy patty â†’ Deploy cabbage â†’ Deploy tomato
    event.remove({ id: 'veggiesdelight:vegetarian_burger' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "veggiesdelight:cooked_vegetarian_patty" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/cabbage" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:vegetarian_burger" }],
        "loops": 1
    });

    // Zucchini Sandwich: Bread â†’ Deploy zucchini â†’ Deploy lettuce â†’ Deploy tomato
    event.remove({ id: 'veggiesdelight:zucchini_sandwich' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/zucchini" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage_leaf" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:zucchini_sandwich" }],
        "loops": 1
    });

    // Garlic Bread: Bread â†’ Deploy roasted garlic x4
    event.remove({ id: 'veggiesdelight:garlic_bread' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "veggiesdelight:roasted_garlic_clove" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "veggiesdelight:roasted_garlic_clove" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:garlic_bread" }],
        "loops": 1
    });

    // --- WRAPS (Sequenced Assembly) ---

    // Vegetable Wrap: Dough â†’ Deploy pepper â†’ Deploy zucchini â†’ Deploy greens â†’ Deploy rice
    event.remove({ id: 'veggiesdelight:vegetable_wrap' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:wheat_dough" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "veggiesdelight:smoked_bellpepper" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "veggiesdelight:roasted_zucchini" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage_leaf" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cooked_rice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:vegetables_wrap" }],
        "loops": 1
    });

    // Uncooked Mhadjeb: Dough â†’ Deploy onion â†’ Deploy pepper â†’ Deploy sauce
    event.remove({ id: 'veggiesdelight:uncooked_mhadjeb' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:wheat_dough" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/onion" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/bellpepper" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:tomato_sauce" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:uncooked_mhadjeb" }],
        "loops": 1
    });

    // --- SALADS (Mixing) ---

    // Turnip Salad: Mixing
    event.remove({ id: 'veggiesdelight:turnip_salad' });
    event.recipes.create.mixing('veggiesdelight:turnip_salad', [
        'farmersdelight:cabbage_leaf',
        { tag: 'c:crops/turnip' },
        'minecraft:bowl'
    ]);

    // --- PLATED MEALS (Heated Mixing) ---

    // Garlic Baked Cod
    event.remove({ id: 'veggiesdelight:garlic_baked_cod' });
    event.recipes.create.mixing('veggiesdelight:garlic_baked_cod', [
        'minecraft:cooked_cod',
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
        'minecraft:cooked_beef',
        'minecraft:milk_bucket'
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
        'minecraft:milk_bucket'
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

    // Sweet Potato Pie: Crust â†’ Deploy potato â†’ Deploy sugar â†’ Press
    event.remove({ id: 'veggiesdelight:sweet_potato_pie' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "veggiesdelight:baked_sweet_potato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:sugar" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:sweet_potato_pie" }],
        "loops": 1
    });

    // Zucchini Quiche: Crust â†’ Deploy zucchini â†’ Deploy meat â†’ Deploy milk â†’ Press
    event.remove({ id: 'veggiesdelight:zucchini_quiche' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "kubejs:incomplete_ender_eye" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "veggiesdelight:roasted_zucchini" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:cooked_mutton" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:milk_bucket" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }],
                "results": [{ "id": "kubejs:incomplete_ender_eye" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:zucchini_quiche" }],
        "loops": 1
    });

    // Vegan Pizza: Dough â†’ Deploy sauce â†’ Deploy pepper â†’ Deploy veg â†’ Deploy onion â†’ Press
    event.remove({ id: 'veggiesdelight:vegan_pizza' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:wheat_dough" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:tomato_sauce" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/bellpepper" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:carrot" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/onion" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:vegan_pizza" }],
        "loops": 1
    });

    // --- SKEWERS (Sequenced Assembly) ---

    // Turnip Mutton Skewer
    event.remove({ id: 'veggiesdelight:turnip_mutton_skewer' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:stick" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:cooked_mutton" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/turnip" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "veggiesdelight:turnip_mutton_skewer" }],
        "loops": 1
    });

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

    // Bastion Pie: Crust â†’ Deploy bastion â†’ Deploy jam â†’ Deploy sourceberry â†’ Press
    event.remove({ id: 'arsdelight:bastion_pie' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:bastion_pod" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "arsdelight:activated_bastion_jam" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:sourceberry_bush" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "arsdelight:bastion_pie" }],
        "loops": 1
    });

    // Bombegrante Pie
    event.remove({ id: 'arsdelight:bombegrante_pie' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:bombegranate_pod" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "arsdelight:neutralized_bombegrante_jam" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:sourceberry_bush" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "arsdelight:bombegrante_pie" }],
        "loops": 1
    });

    // Frostaya Pie
    event.remove({ id: 'arsdelight:frostaya_pie' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:frostaya_pod" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "arsdelight:neutralized_frostaya_jam" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:sourceberry_bush" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "arsdelight:frostaya_pie" }],
        "loops": 1
    });

    // Mendosteen Pie
    event.remove({ id: 'arsdelight:mendosteen_pie' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:mendosteen_pod" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "arsdelight:activated_mendosteen_jam" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "ars_nouveau:sourceberry_bush" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "arsdelight:mendosteen_pie" }],
        "loops": 1
    });

    // --- MAGICAL SALADS (Mechanical Crafting â€” arcane plating) ---

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
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:stick" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "arsdelight:raw_chimera" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "arsdelight:wilden_spike_powder" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "arsdelight:chimera_skewer" }],
        "loops": 1
    });

    // Wilden Skewer
    event.remove({ id: 'arsdelight:wilden_skewer' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:stick" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "arsdelight:raw_wilden_meat" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "arsdelight:wilden_spike_powder" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "arsdelight:wilden_skewer" }],
        "loops": 1
    });

    // ==========================================
    // LENDER'S DELIGHT (Cataclysm Foods!)
    // ==========================================

    // --- SANDWICHES (Sequenced Assembly) ---

    // Amethyst Crab Sandwich
    event.remove({ id: 'lendersdelight:amethyst_crab_sandwich' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "lendersdelight:cooked_amethyst_crab_meat" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage_leaf" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "lendersdelight:amethyst_crab_sandwich" }],
        "loops": 1
    });

    // Coral Chunk Sandwich
    event.remove({ id: 'lendersdelight:coral_chunk_sandwich' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "cataclysm:coral_chunk" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage_leaf" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/tomato" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "lendersdelight:coral_chunk_sandwich" }],
        "loops": 1
    });

    // --- SUSHI ROLLS ---

    // Crystallized Coral Roll: Deploying
    event.remove({ id: 'lendersdelight:crystallized_coral_roll' });
    event.recipes.create.deploying(
        'lendersdelight:crystallized_coral_roll',
        ['minecraft:dried_kelp', 'cataclysm:crystallized_coral_fragments']
    );

    // Lionfish Roll: Rice â†’ Deploy lionfish
    event.remove({ id: 'lendersdelight:lionfish_roll' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "lendersdelight:lionfish_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "lendersdelight:lionfish_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('lendersdelight:lionfish_roll', 2)],
        "loops": 1
    });

    // --- PIES ---

    // Crystallized Coral Pie
    event.remove({ id: 'lendersdelight:crystallized_coral_pie' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "cataclysm:crystallized_coral" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "cataclysm:crystallized_coral" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:sugar" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "lendersdelight:crystallized_coral_pie" }],
        "loops": 1
    });

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
