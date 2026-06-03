// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 13A
// FOOD OVERHAUL: FARMER'S DELIGHT BASE
// ==========================================
// Converts crafting table food recipes to
// Create processes (mixing, deploying, pressing,
// compacting, sequenced assembly).
// Decoration/furniture recipes are left as-is.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // CATEGORY 1: DOUGH & BASE INGREDIENTS
    // Pressing + Mixing (industrial bread-making)
    // ==========================================

    // Wheat Dough: Pressing wheat into flour, then mixing with egg
    event.remove({ id: 'farmersdelight:wheat_dough_from_egg' });
    event.recipes.create.mixing(
        Item.of('farmersdelight:wheat_dough', 3),
        [
            { tag: 'c:crops/wheat' },
            { tag: 'c:crops/wheat' },
            { tag: 'c:crops/wheat' },
            { tag: 'c:eggs' }
        ]
    );

    // Pie Crust: Pressing dough flat
    event.remove({ id: 'farmersdelight:pie_crust' });
    event.recipes.create.pressing(
        'farmersdelight:pie_crust',
        'farmersdelight:wheat_dough'
    );

    // Straw: Pressing wheat
    event.remove({ id: 'farmersdelight:straw' });
    event.recipes.create.pressing(
        'farmersdelight:straw',
        { tag: 'c:crops/wheat' }
    );

    // ==========================================
    // CATEGORY 2: SANDWICHES & WRAPS
    // Sequenced Assembly (layered construction)
    // ==========================================

    // Hamburger: Bread â†’ Deploy patty â†’ Deploy lettuce â†’ Deploy tomato â†’ Press
    event.remove({ id: 'farmersdelight:hamburger' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:beef_patty" }],
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
        "results": [{ "id": "farmersdelight:hamburger" }],
        "loops": 1
    });

    // Bacon Sandwich: Bread â†’ Deploy bacon â†’ Deploy bacon
    event.remove({ id: 'farmersdelight:bacon_sandwich' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cooked_bacon" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cooked_bacon" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "farmersdelight:bacon_sandwich" }],
        "loops": 1
    });

    // Chicken Sandwich: Bread â†’ Deploy chicken â†’ Deploy lettuce â†’ Deploy carrot
    event.remove({ id: 'farmersdelight:chicken_sandwich' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cooked_chicken_cuts" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage_leaf" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/carrot" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "farmersdelight:chicken_sandwich" }],
        "loops": 1
    });

    // Egg Sandwich: Bread â†’ Deploy fried egg â†’ Deploy fried egg
    event.remove({ id: 'farmersdelight:egg_sandwich' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:fried_egg" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:fried_egg" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "farmersdelight:egg_sandwich" }],
        "loops": 1
    });

    // Mutton Wrap: Bread â†’ Deploy mutton â†’ Deploy lettuce â†’ Deploy onion
    event.remove({ id: 'farmersdelight:mutton_wrap' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:bread" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:cooked_mutton" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cabbage_leaf" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "tag": "c:crops/onion" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "farmersdelight:mutton_wrap" }],
        "loops": 1
    });

    // ==========================================
    // CATEGORY 3: SALADS & BOWLS
    // Create Mixing (cold mixing, no heat)
    // ==========================================

    // Mixed Salad: Mixing vegetables in a bowl
    event.remove({ id: 'farmersdelight:mixed_salad' });
    event.recipes.create.mixing(
        'farmersdelight:mixed_salad',
        [
            'farmersdelight:cabbage_leaf',
            { tag: 'c:crops/tomato' },
            { tag: 'c:crops/beetroot' },
            'minecraft:bowl'
        ]
    );

    // Fruit Salad: Mixing fruits in a bowl
    event.remove({ id: 'farmersdelight:fruit_salad' });
    event.recipes.create.mixing(
        'farmersdelight:fruit_salad',
        [
            'minecraft:apple',
            'minecraft:melon_slice',
            'minecraft:sweet_berries',
            'minecraft:bowl'
        ]
    );

    // Nether Salad: Mixing nether fungi
    event.remove({ id: 'farmersdelight:nether_salad' });
    event.recipes.create.mixing(
        'farmersdelight:nether_salad',
        [
            'minecraft:crimson_fungus',
            'minecraft:warped_fungus',
            'minecraft:bowl'
        ]
    );

    // ==========================================
    // CATEGORY 4: PLATED MEALS (Bowl dishes)
    // Create Mixing (heated)
    // ==========================================

    // Bacon and Eggs: Heated mixing
    event.remove({ id: 'farmersdelight:bacon_and_eggs' });
    event.recipes.create.mixing(
        'farmersdelight:bacon_and_eggs',
        [
            'farmersdelight:cooked_bacon',
            'farmersdelight:cooked_bacon',
            'farmersdelight:fried_egg',
            'farmersdelight:fried_egg',
            'minecraft:bowl'
        ]
    ).heated();

    // Steak and Potatoes: Heated mixing
    event.remove({ id: 'farmersdelight:steak_and_potatoes' });
    event.recipes.create.mixing(
        'farmersdelight:steak_and_potatoes',
        [
            'minecraft:cooked_beef',
            'minecraft:baked_potato',
            { tag: 'c:crops/onion' },
            'farmersdelight:cooked_rice',
            'minecraft:bowl'
        ]
    ).heated();

    // Roasted Mutton Chops: Heated mixing
    event.remove({ id: 'farmersdelight:roasted_mutton_chops' });
    event.recipes.create.mixing(
        'farmersdelight:roasted_mutton_chops',
        [
            'farmersdelight:cooked_mutton_chops',
            { tag: 'c:crops/beetroot' },
            { tag: 'c:crops/tomato' },
            'farmersdelight:cooked_rice',
            'minecraft:bowl'
        ]
    ).heated();

    // Grilled Salmon: Heated mixing
    event.remove({ id: 'farmersdelight:grilled_salmon' });
    event.recipes.create.mixing(
        'farmersdelight:grilled_salmon',
        [
            'farmersdelight:cooked_salmon_slice',
            'farmersdelight:cooked_salmon_slice',
            { tag: 'c:crops/tomato' },
            'minecraft:sweet_berries',
            'minecraft:bowl'
        ]
    ).heated();

    // Stuffed Potato: Heated mixing
    event.remove({ id: 'farmersdelight:stuffed_potato' });
    event.recipes.create.mixing(
        'farmersdelight:stuffed_potato',
        [
            'minecraft:baked_potato',
            'minecraft:cooked_beef',
            'minecraft:milk_bucket'
        ]
    ).heated();

    // Barbecue Stick: Heated mixing (grilling)
    event.remove({ id: 'farmersdelight:barbecue_stick' });
    event.recipes.create.mixing(
        'farmersdelight:barbecue_stick',
        [
            'minecraft:cooked_beef',
            { tag: 'c:crops/onion' },
            { tag: 'c:crops/tomato' },
            'minecraft:stick'
        ]
    ).heated();

    // ==========================================
    // CATEGORY 5: SUSHI ROLLS
    // Sequenced Assembly (rolling technique)
    // ==========================================

    // Cod Roll: Rice â†’ Deploy cod â†’ Wrap with kelp
    event.remove({ id: 'farmersdelight:cod_roll' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cooked_cod_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:cooked_cod_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('farmersdelight:cod_roll', 2)],
        "loops": 1
    });

    // Salmon Roll: Rice â†’ Deploy salmon slices
    event.remove({ id: 'farmersdelight:salmon_roll' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:salmon_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "farmersdelight:salmon_slice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [Item.of('farmersdelight:salmon_roll', 2)],
        "loops": 1
    });

    // Kelp Roll: Shaped recipe â†’ Pressing (rolling)
    event.remove({ id: 'farmersdelight:kelp_roll' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:cooked_rice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:carrot" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:dried_kelp" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "farmersdelight:kelp_roll" }],
        "loops": 1
    });

    // ==========================================
    // CATEGORY 6: COOKIES & SWEETS
    // Create Mixing (baking)
    // ==========================================

    // Honey Cookie: Mixing
    event.remove({ id: 'farmersdelight:honey_cookie' });
    event.recipes.create.mixing(
        Item.of('farmersdelight:honey_cookie', 8),
        [
            'minecraft:honey_bottle',
            { tag: 'c:crops/wheat' },
            { tag: 'c:crops/wheat' }
        ]
    ).heated();

    // Sweet Berry Cookie: Mixing
    event.remove({ id: 'farmersdelight:sweet_berry_cookie' });
    event.recipes.create.mixing(
        Item.of('farmersdelight:sweet_berry_cookie', 8),
        [
            'minecraft:sweet_berries',
            { tag: 'c:crops/wheat' },
            { tag: 'c:crops/wheat' }
        ]
    ).heated();

    // ==========================================
    // CATEGORY 7: PIES & CHEESECAKE
    // Sequenced Assembly (layered baking)
    // ==========================================

    // Apple Pie: Crust â†’ Deploy apples â†’ Deploy sugar â†’ Press (bake)
    event.remove({ id: 'farmersdelight:apple_pie' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:apple" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:apple" }],
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
        "results": [{ "id": "farmersdelight:apple_pie" }],
        "loops": 1
    });

    // Sweet Berry Cheesecake: Crust â†’ Deploy berries â†’ Deploy milk â†’ Press
    event.remove({ id: 'farmersdelight:sweet_berry_cheesecake' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "farmersdelight:pie_crust" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:sweet_berries" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:sweet_berries" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:milk_bucket" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "farmersdelight:sweet_berry_cheesecake" }],
        "loops": 1
    });

    // ==========================================
    // CATEGORY 8: FEAST BLOCKS (the big ones!)
    // Mechanical Crafting (these are massive feasts)
    // ==========================================

    // Roast Chicken Block: The ultimate chicken feast
    event.remove({ id: 'farmersdelight:roast_chicken_block' });
    event.recipes.create.mechanical_crafting('farmersdelight:roast_chicken_block', [
        'OEB',
        'CPC',
        'RAR'
    ], {
        O: { tag: 'c:crops/onion' },
        E: { tag: 'c:eggs' },
        B: 'minecraft:bread',
        C: { tag: 'c:crops/carrot' },
        P: 'minecraft:cooked_chicken',
        R: 'minecraft:baked_potato',
        A: 'minecraft:bowl'
    });

    // Honey Glazed Ham Block: The ultimate ham feast
    event.remove({ id: 'farmersdelight:honey_glazed_ham_block' });
    event.recipes.create.mechanical_crafting('farmersdelight:honey_glazed_ham_block', [
        'SHS',
        'RGR',
        'SAS'
    ], {
        S: 'minecraft:sweet_berries',
        H: 'minecraft:honey_bottle',
        R: 'farmersdelight:cooked_rice',
        G: 'farmersdelight:smoked_ham',
        A: 'minecraft:bowl'
    });

    // Shepherd's Pie Block: The ultimate pie feast
    event.remove({ id: 'farmersdelight:shepherds_pie_block' });
    event.recipes.create.mechanical_crafting('farmersdelight:shepherds_pie_block', [
        'PMP',
        'LLL',
        'OAO'
    ], {
        P: 'minecraft:baked_potato',
        M: 'minecraft:milk_bucket',
        L: { tag: 'c:foods/cooked_mutton' },
        O: { tag: 'c:crops/onion' },
        A: 'minecraft:bowl'
    });

    // Rice Roll Medley Block
    event.remove({ id: 'farmersdelight:rice_roll_medley_block' });
    event.recipes.create.mechanical_crafting('farmersdelight:rice_roll_medley_block', [
        'KKK',
        'SSS',
        'CAC'
    ], {
        K: 'farmersdelight:kelp_roll_slice',
        S: 'farmersdelight:salmon_roll',
        C: 'farmersdelight:cod_roll',
        A: 'minecraft:bowl'
    });

    // Gleaming Salad Block
    event.remove({ id: 'farmersdelight:gleaming_salad_block' });
    event.recipes.create.mixing(
        'farmersdelight:gleaming_salad_block',
        [
            'farmersdelight:mixed_salad',
            'farmersdelight:mixed_salad',
            'minecraft:glow_berries',
            'minecraft:glow_berries',
            'minecraft:bowl'
        ]
    );

    // ==========================================
    // CATEGORY 9: DRINKS
    // Create Mixing (cold mixing/juicing)
    // ==========================================

    // Melon Juice: Mixing/pressing melon
    event.remove({ id: 'farmersdelight:melon_juice' });
    event.recipes.create.mixing(
        'farmersdelight:melon_juice',
        [
            'minecraft:melon_slice',
            'minecraft:melon_slice',
            'minecraft:melon_slice',
            'minecraft:melon_slice',
            'minecraft:sugar',
            'minecraft:glass_bottle'
        ]
    );

    // Melon Popsicle: Pressing ice with melon
    event.remove({ id: 'farmersdelight:melon_popsicle' });
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:melon_slice" },
        "transitional_item": { "id": "farmersdelight:wheat_dough" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:ice" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_ender_eye" }, { "item": "minecraft:stick" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "farmersdelight:wheat_dough" }],
                "results": [{ "id": "farmersdelight:wheat_dough" }]
            }
        ],
        "results": [{ "id": "farmersdelight:melon_popsicle" }],
        "loops": 1
    });

    // ==========================================
    // CATEGORY 10: UTILITY / COMPOST
    // Create Compacting/Mixing
    // ==========================================

    // Organic Compost from Rotten Flesh: Compacting
    event.remove({ id: 'farmersdelight:organic_compost_from_rotten_flesh' });
    event.recipes.create.compacting(
        'farmersdelight:organic_compost',
        [
            'minecraft:rotten_flesh',
            'minecraft:rotten_flesh',
            'minecraft:rotten_flesh',
            'minecraft:rotten_flesh',
            'farmersdelight:straw',
            'farmersdelight:straw',
            'minecraft:bone_meal',
            'minecraft:bone_meal',
            'minecraft:dirt'
        ]
    );

    // Organic Compost from Tree Bark: Compacting
    event.remove({ id: 'farmersdelight:organic_compost_from_tree_bark' });
    event.recipes.create.compacting(
        'farmersdelight:organic_compost',
        [
            'farmersdelight:tree_bark',
            'farmersdelight:tree_bark',
            'farmersdelight:tree_bark',
            'farmersdelight:tree_bark',
            'farmersdelight:straw',
            'farmersdelight:straw',
            'minecraft:bone_meal',
            'minecraft:bone_meal',
            'minecraft:dirt'
        ]
    );

    // Horse Feed: Mixing
    event.remove({ id: 'farmersdelight:horse_feed' });
    event.recipes.create.mixing(
        'farmersdelight:horse_feed',
        [
            'minecraft:hay_block',
            'minecraft:apple',
            'minecraft:apple',
            'minecraft:golden_carrot'
        ]
    );

    console.log('[PEAK Expert Mode] Script 13A: Food Overhaul - Farmer\'s Delight loaded!');
    console.log('  â†’ Sandwiches: Sequenced Assembly');
    console.log('  â†’ Salads/Bowls: Create Mixing');
    console.log('  â†’ Sushi: Sequenced Assembly');
    console.log('  â†’ Pies: Sequenced Assembly');
    console.log('  â†’ Feasts: Mechanical Crafting');
    console.log('  â†’ Drinks: Create Mixing');
});
