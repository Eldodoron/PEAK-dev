// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 13B
// FOOD OVERHAUL: TWILIGHT + NETHER + END
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // TWILIGHT DELIGHT
    // ==========================================

    // --- SANDWICHES & WRAPS (Sequenced Assembly) ---

    // Ghast Burger: Bread â†’ Deploy exp115 â†’ Deploy beet â†’ Deploy tomato â†’ Deploy onion
    event.remove({ id: 'twilightdelight:ghast_burger' });
    event.recipes.create.sequenced_assembly([
        Item.of('twilightdelight:ghast_burger')
    ], '#c:foods/bread', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'twilightforest:experiment_115']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', '#c:crops/beetroot']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', '#c:foods/tomato'])
    ]).transitionalItem('kubejs:incomplete_ender_eye').loops(1);

    // Hydra Burger: Bread â†’ Deploy hydra meat â†’ Deploy lettuce â†’ Deploy tomato â†’ Deploy onion
    event.remove({ id: 'twilightdelight:hydra_burger' });
    event.recipes.create.sequenced_assembly([
        Item.of('twilightdelight:hydra_burger')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'twilightdelight:hydra_meat' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/tomato' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Meef Wrap: Bread â†’ Deploy meef â†’ Deploy lettuce â†’ Deploy onion
    event.remove({ id: 'twilightdelight:meef_wrap' });
    event.recipes.create.sequenced_assembly([
        Item.of('twilightdelight:meef_wrap')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'twilightdelight:meef_cooked' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/onion' }])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Torchberry Venison Sandwich: Bread â†’ Deploy venison â†’ Deploy lettuce â†’ Deploy torchberry
    event.remove({ id: 'twilightdelight:torchberry_venison_sandwich' });
    event.recipes.create.sequenced_assembly([
        Item.of('twilightdelight:torchberry_venison_sandwich')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'twilightdelight:vension_cooked' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', { tag: 'c:foods/leafy_green' }]),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'twilightforest:torchberries'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- SALADS & SOUPS (Mixing) ---

    // Ghast Brain Salad: Mixing (cold, exotic)
    event.remove({ id: 'twilightdelight:ghast_brain_salad' });
    event.recipes.create.mixing(
        'twilightdelight:ghast_brain_salad',
        [
            'minecraft:bowl',
            { tag: 'c:foods/leafy_green' },
            { tag: 'c:foods/onion' },
            { tag: 'c:foods/tomato' },
            'twilightdelight:experiment_110',
            'twilightforest:borer_essence',
            'twilightforest:transformation_powder'
        ]
    );

    // Borer Tear Soup: Mixing
    event.remove({ id: 'twilightdelight:borer_tear_soup' });
    event.recipes.create.mixing(
        'twilightdelight:borer_tear_soup',
        [
            'minecraft:bowl',
            'minecraft:beetroot',
            'minecraft:beetroot',
            'minecraft:beetroot',
            'minecraft:beetroot',
            'twilightforest:borer_essence'
        ]
    ).heated();

    // --- COOKIES & BAKED (Heated Mixing) ---

    // Torchberry Cookie
    event.remove({ id: 'twilightdelight:torchberry_cookie' });
    event.recipes.create.mixing(
        Item.of('twilightdelight:torchberry_cookie', 8),
        [
            'twilightforest:torchberries',
            'minecraft:wheat',
            'minecraft:wheat'
        ]
    ).heated();

    // Chocolate Wafer: Pressing wafer with chocolate
    event.remove({ id: 'twilightdelight:chocolate_wafer' });
    event.recipes.create.deploying(
        'twilightdelight:chocolate_wafer',
        ['twilightforest:maze_wafer', 'minecraft:cocoa_beans']
    );

    // Maze Wafer: Mixing wheat + milk + liveroot
    event.remove({ id: 'twilightdelight:maze_wafer' });
    event.recipes.create.mixing(
        Item.of('twilightforest:maze_wafer', 12),
        [
            'minecraft:wheat',
            'minecraft:wheat',
            'minecraft:wheat',
            { tag: 'c:drinks/milk' },
            'twilightforest:liveroot'
        ]
    ).heated();

    // --- PIES (Sequenced Assembly) ---

    // Aurora Pie: Crust â†’ Deploy aurora â†’ Deploy sugar â†’ Press
    event.remove({ id: 'twilightdelight:aurora_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('twilightdelight:aurora_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'twilightforest:torchberries']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'twilightforest:torchberries']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:sugar']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Torchberry Pie: Same concept
    event.remove({ id: 'twilightdelight:torchberry_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('twilightdelight:torchberry_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'twilightforest:torchberries']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'twilightforest:torchberries']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:sugar']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- FEAST BLOCKS (Mechanical Crafting) ---

    // Meef Wellington Block: The ultimate Twilight feast
    event.remove({ id: 'twilightdelight:meef_wellington_block' });
    event.recipes.create.mechanical_crafting('twilightdelight:meef_wellington_block', [
        'BAB',
        'DCD',
        'FEF'
    ], {
        B: { tag: 'c:eggs' },
        A: 'farmersdelight:pie_crust',
        D: { tag: 'twilightdelight:meef_cooked' },
        C: 'twilightdelight:mushgloom_sauce',
        F: 'farmersdelight:bacon',
        E: 'minecraft:bowl'
    });

    // --- DRINKS (Mixing) ---

    // Glacier Ice Tea: Cold mixing
    event.remove({ id: 'twilightdelight:glacier_ice_tea' });
    event.recipes.create.mixing(
        'twilightdelight:glacier_ice_tea',
        [
            'minecraft:glass_bottle',
            'twilightforest:ice_bomb',
            'minecraft:ice',
            'twilightforest:arctic_fur',
            'minecraft:sugar'
        ]
    );

    // Twilight Spring: Cold mixing
    event.remove({ id: 'twilightdelight:twilight_spring' });
    event.recipes.create.mixing(
        'twilightdelight:twilight_spring',
        [
            'minecraft:glass_bottle',
            'twilightforest:raw_ironwood',
            'minecraft:ice'
        ]
    );

    // Berry Stick: Mixing on stick
    event.remove({ id: 'twilightdelight:berry_stick' });
    event.recipes.create.deploying(
        'twilightdelight:berry_stick',
        ['minecraft:stick', 'twilightforest:torchberries']
    );

    // --- EXPERIMENT 113 VARIANTS (Mixing) ---

    event.remove({ id: 'twilightdelight:chocolate_113' });
    event.recipes.create.mixing('twilightdelight:chocolate_113', [
        'twilightdelight:experiment_113', { tag: 'c:drinks/milk' }, 'minecraft:sugar', 'minecraft:cocoa_beans'
    ]).heated();

    event.remove({ id: 'twilightdelight:glow_113' });
    event.recipes.create.mixing('twilightdelight:glow_113', [
        'twilightdelight:experiment_113', 'twilightdelight:glowstew'
    ]);

    event.remove({ id: 'twilightdelight:honey_113' });
    event.recipes.create.mixing('twilightdelight:honey_113', [
        'twilightdelight:experiment_113', 'minecraft:honey_bottle'
    ]);

    event.remove({ id: 'twilightdelight:milky_113' });
    event.recipes.create.mixing('twilightdelight:milky_113', [
        'twilightdelight:experiment_113', { tag: 'c:drinks/milk' }, 'minecraft:sugar'
    ]);

    // ==========================================
    // MY NETHER'S DELIGHT
    // ==========================================

    // --- SANDWICHES & HOTDOGS (Sequenced Assembly) ---

    // Nether Burger: Bread â†’ Deploy loin â†’ Deploy vines â†’ Deploy fungi
    event.remove({ id: 'mynethersdelight:nether_burger' });
    event.recipes.create.sequenced_assembly([
        Item.of('mynethersdelight:nether_burger')
    ], { tag: 'c:foods/bread' }, [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'mynethersdelight:cooked_loin']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:crimson_fungus']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:warped_fungus'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Hotdog: Bread â†’ Deploy sausage
    event.remove({ id: 'mynethersdelight:hotdog' });
    event.recipes.create.deploying(
        'mynethersdelight:hotdog',
        [{ tag: 'c:foods/bread' }, 'mynethersdelight:roasted_sausage']
    );

    // Hotdog with Mixed Salad: Mixing
    event.remove({ id: 'mynethersdelight:hotdog_with_mixed_salad' });
    event.recipes.create.mixing('mynethersdelight:hotdog_with_mixed_salad', [
        'mynethersdelight:hotdog', 'mynethersdelight:hotdog', 'farmersdelight:mixed_salad'
    ]);

    // Hotdog with Nether Salad: Mixing
    event.remove({ id: 'mynethersdelight:hotdog_with_nether_salad' });
    event.recipes.create.mixing('mynethersdelight:hotdog_with_nether_salad', [
        'mynethersdelight:hotdog', 'mynethersdelight:hotdog', 'farmersdelight:nether_salad'
    ]);

    // --- NETHER PLATED MEALS (Heated Mixing) ---

    // Blue Tenderloin Steak
    event.remove({ id: 'mynethersdelight:blue_tenderloin_steak' });
    event.recipes.create.mixing('mynethersdelight:blue_tenderloin_steak', [
        'mynethersdelight:cooked_loin', 'minecraft:warped_fungus', 'minecraft:warped_fungus',
        'minecraft:warped_roots', 'farmersdelight:straw', 'minecraft:bowl'
    ]).heated();

    // Breakfast Sampler
    event.remove({ id: 'mynethersdelight:breakfast_sampler' });
    event.recipes.create.mixing('mynethersdelight:breakfast_sampler', [
        'mynethersdelight:roasted_sausage', 'mynethersdelight:roasted_sausage',
        'minecraft:honey_bottle', 'mynethersdelight:strider_egg', 'minecraft:bowl'
    ]).heated();

    // Bleeding Tartar
    event.remove({ id: 'mynethersdelight:bleeding_tartar' });
    event.recipes.create.mixing('mynethersdelight:bleeding_tartar', [
        'mynethersdelight:minced_strider', 'mynethersdelight:minced_strider', 'minecraft:bowl'
    ]);

    // Striderloaf
    event.remove({ id: 'mynethersdelight:striderloaf' });
    event.recipes.create.mixing('mynethersdelight:striderloaf', [
        'mynethersdelight:strider_slice', 'mynethersdelight:minced_strider',
        'mynethersdelight:minced_strider', 'mynethersdelight:minced_strider', 'minecraft:bowl'
    ]).heated();

    // Sizzling Pudding
    event.remove({ id: 'mynethersdelight:sizzling_pudding' });
    event.recipes.create.mixing('mynethersdelight:sizzling_pudding', [
        'mynethersdelight:ghasmati', 'minecraft:blaze_powder',
        'mynethersdelight:pepper_powder', 'minecraft:bowl'
    ]).superheated();

    // Ghast Salad
    event.remove({ id: 'mynethersdelight:ghast_salad' });
    event.recipes.create.mixing('mynethersdelight:ghast_salad', [
        { tag: 'c:foods/leafy_green' }, 'minecraft:melon_slice', 'minecraft:bowl'
    ]);

    // Rock Soup: Superheated (it's lava rock!)
    event.remove({ id: 'mynethersdelight:rock_soup' });
    event.recipes.create.mixing('mynethersdelight:rock_soup', [
        'minecraft:magma_cream', 'minecraft:magma_cream',
        'mynethersdelight:strider_egg', 'mynethersdelight:strider_egg', 'minecraft:bowl'
    ]).superheated();

    // Dried Ghast with Milk
    event.remove({ id: 'mynethersdelight:dried_ghast_with_milk' });
    event.recipes.create.mixing('mynethersdelight:dried_ghast_with_milk', [
        'mynethersdelight:ghasmati', { tag: 'c:drinks/milk' }, 'minecraft:bowl'
    ]);

    // --- SKEWERS & STICKS (Deploying) ---

    // Bacon Wrapped Sausage Stick
    event.remove({ id: 'mynethersdelight:bacon_wrapped_sausage_stick' });
    event.recipes.create.sequenced_assembly([
        Item.of('mynethersdelight:bacon-wrapped_sausage_on_a_stick')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'mynethersdelight:roasted_sausage']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'farmersdelight:cooked_bacon'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Red Loin on a Stick
    event.remove({ id: 'mynethersdelight:red_loin_on_a_stick' });
    event.recipes.create.sequenced_assembly([
        Item.of('mynethersdelight:red_loin_on_a_stick')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'mynethersdelight:cooked_loin']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:crimson_fungus']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:red_mushroom'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Spicy Skewer
    event.remove({ id: 'mynethersdelight:spicy_skewer' });
    event.recipes.create.sequenced_assembly([
        Item.of('mynethersdelight:spicy_skewer')
    ], 'minecraft:blaze_rod', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'mynethersdelight:bullet_pepper']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'mynethersdelight:bullet_pepper'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Spicy Cotton
    event.remove({ id: 'mynethersdelight:spicy_cotton' });
    event.recipes.create.sequenced_assembly([
        Item.of('mynethersdelight:spicy_cotton')
    ], 'minecraft:blaze_rod', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'mynethersdelight:ghasta']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'mynethersdelight:ghasta'])
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // --- NETHER DOUGH & BAKING (Mixing/Pressing) ---

    // Ghast Dough: Mixing ghasmati
    event.remove({ id: 'mynethersdelight:ghast_dough' });
    event.recipes.create.mixing('mynethersdelight:ghast_dough', [
        'mynethersdelight:ghasmati', 'mynethersdelight:ghasmati'
    ]);

    // Ghast Sourdough: Pressing ghast dough
    event.remove({ id: 'mynethersdelight:ghast_sourdough' });
    event.recipes.create.pressing(
        'mynethersdelight:ghast_sourdough',
        'mynethersdelight:ghast_dough'
    );

    // Burnt Roll: Superheated pressing
    event.remove({ id: 'mynethersdelight:burnt_roll' });
    event.recipes.create.mixing('mynethersdelight:burnt_roll', [
        { tag: 'c:foods/bread' }, 'minecraft:magma_cream'
    ]).superheated();

    // --- NETHER CAKES & DESSERTS ---

    // Magma Cake: Heated mixing
    event.remove({ id: 'mynethersdelight:magma_cake' });
    event.recipes.create.mixing('mynethersdelight:magma_cake_block', [
        'farmersdelight:straw', 'mynethersdelight:hot_cream',
        'minecraft:magma_cream', 'mynethersdelight:pepper_powder'
    ]).superheated();

    // Ghasta with Cream: Heated mixing
    event.remove({ id: 'mynethersdelight:ghasta_with_cream' });
    event.recipes.create.mechanical_crafting('mynethersdelight:ghasta_with_cream', [
        'MGM',
        ' B '
    ], {
        M: 'minecraft:magma_cream',
        G: 'mynethersdelight:ghasta',
        B: 'minecraft:bowl'
    });

    // Tear Popsicle: Sequenced Assembly (frozen treat)
    event.remove({ id: 'mynethersdelight:tear_popsicle' });
    event.recipes.create.sequenced_assembly([
        Item.of('mynethersdelight:tear_popsicle')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:ghast_tear']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:ice']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Hot Cream Cone: Mixing
    event.remove({ id: 'mynethersdelight:hotcream_cone' });
    event.recipes.create.mixing('mynethersdelight:hot_cream_cone', [
        'mynethersdelight:hot_cream', 'mynethersdelight:powder_cannon',
        'mynethersdelight:powder_cannon', 'mynethersdelight:powder_cannon'
    ]).heated();

    // Hot Wings Bucket: Compacting
    event.remove({ id: 'mynethersdelight:hot_wings_bucket' });
    event.recipes.create.compacting('mynethersdelight:hot_wings_bucket', [
        'mynethersdelight:hot_wings', 'mynethersdelight:hot_wings',
        'mynethersdelight:hot_wings', 'minecraft:bucket'
    ]);

    // Raw Stuffed Hoglin: Mechanical Crafting (it's a WHOLE hoglin)
    event.remove({ id: 'mynethersdelight:raw_stuffed_hoglin' });
    event.recipes.create.mechanical_crafting('mynethersdelight:raw_stuffed_hoglin', [
        'HCH',
        'FLW'
    ], {
        H: 'mynethersdelight:hoglin_hide',
        C: 'mynethersdelight:crimson_fungus_colony',
        F: 'farmersdelight:ham',
        L: 'mynethersdelight:hoglin_loin',
        W: 'mynethersdelight:warped_fungus_colony'
    });

    // Stuffed Pepper: Deploying
    event.remove({ id: 'mynethersdelight:stuffed_pepper' });
    event.recipes.create.deploying(
        'mynethersdelight:stuffed_pepper',
        ['mynethersdelight:bullet_pepper', { tag: 'c:foods/cooked_beef' }]
    );

    // ==========================================
    // ENDER'S DELIGHT
    // ==========================================

    // Chorus Pie: Sequenced Assembly
    event.remove({ id: 'endersdelight:chorus_pie' });
    event.recipes.create.sequenced_assembly([
        Item.of('endersdelight:chorus_pie')
    ], 'farmersdelight:pie_crust', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:chorus_fruit']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:chorus_fruit']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'minecraft:sugar']),
        event.recipes.create.pressing('kubejs:incomplete_ender_eye', 'kubejs:incomplete_ender_eye')
    ]).transitionalItem('farmersdelight:wheat_dough').loops(1);

    // Chorus Juice: Mixing
    event.remove({ id: 'endersdelight:chorus_juice' });
    event.recipes.create.mixing('endersdelight:chorus_juice', [
        'minecraft:chorus_fruit', 'minecraft:chorus_fruit',
        'minecraft:sugar', 'minecraft:glass_bottle'
    ]);

    // Crawling Sandwich: Sequenced Assembly
    event.remove({ id: 'endersdelight:crawling_sandwich' });
    event.recipes.create.sequenced_assembly([
        Item.of('endersdelight:crawling_sandwich')
    ], '#c:foods/bread', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'endersdelight:mite_crust']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', '#c:foods/leafy_green'])
    ]).transitionalItem('kubejs:incomplete_ender_eye').loops(1);

    // Crispy Skewer: Deploying on stick
    event.remove({ id: 'endersdelight:crispy_skewer' });
    event.recipes.create.sequenced_assembly([
        Item.of('endersdelight:crispy_skewer')
    ], 'minecraft:stick', [
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'endersdelight:mite_crust']),
        event.recipes.create.deploying('kubejs:incomplete_ender_eye', ['kubejs:incomplete_ender_eye', 'endersdelight:mite_crust'])
    ]).transitionalItem('kubejs:incomplete_ender_eye').loops(1);

    // Shulker Bowl: Heated mixing
    event.remove({ id: 'minecraft:barrier' });
    event.recipes.create.mixing('minecraft:barrier', [
        'minecraft:barrier', 'minecraft:barrier',
        'minecraft:chorus_fruit', 'minecraft:bowl'
    ]).heated();

    // Strange Eclair: Mixing
    event.remove({ id: 'minecraft:barrier' });
    event.recipes.create.mixing('minecraft:barrier', [
        'minecraft:barrier', { tag: 'c:foods/bread' }, 'minecraft:sugar'
    ]).heated();

    // Twisted Cereal: Mixing
    event.remove({ id: 'minecraft:barrier' });
    event.recipes.create.mixing('minecraft:barrier', [
        'minecraft:barrier', 'minecraft:barrier',
        { tag: 'c:drinks/milk' }, 'minecraft:bowl'
    ]);

    // Uncanny Cookies: Heated mixing
    event.remove({ id: 'endersdelight:uncanny_cookies' });
    event.recipes.create.mixing(
        Item.of('endersdelight:uncanny_cookies', 8),
        [
            'minecraft:chorus_fruit',
            { tag: 'c:crops/wheat' },
            { tag: 'c:crops/wheat' }
        ]
    ).heated();

    console.log('[PEAK Expert Mode] Script 13B: Food Overhaul - Twilight + Nether + End loaded!');
});

