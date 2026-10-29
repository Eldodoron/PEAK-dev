// ==========================================
// PEAK EXPERT MODE — SCRIPT 67
// ALLTHEMODIUM ADVANCED METALLURGY & EXPANSION
// ==========================================
// 1. Base metal crushing (Ingots -> Base Dusts)
// 2. True Alloy Dust compounding via Create Superheated Mixer
// 3. High-tier Ingot forging via Advanced Create Addons (New Age Energiser, TFMG Electric Arc Vat, DnDesires Hydraulic Press)
// 4. Strict removal of all vanilla furnace / blasting recipes for god-tier alloys
// 5. Ultimate Alloy Tools smithing & Paxel crafting
// 6. Missing ranged & shield gear smithing
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: PURGE NONSENSICAL FURNACE SMELTING FOR GOD-TIER ALLOYS
    // High-refractory dimension-bending alloys cannot be cooked in basic stone ovens
    // ==========================================
    event.remove({ type: 'minecraft:smelting', input: '#c:dusts/allthemodium_alloys' });
    event.remove({ type: 'minecraft:blasting', input: '#c:dusts/allthemodium_alloys' });
    event.remove({ id: /^kubejs:smelting\/.*_alloy_from_dust/ });
    event.remove({ id: /^kubejs:blasting\/.*_alloy_from_dust/ });


    // ==========================================
    // SECTION 2: BASE METAL POWDER PREPARATION
    // Milled in Create Crushing Wheels to provide powders for alloy compounding
    // ==========================================
    event.recipes.create.crushing('allthemodium:allthemodium_dust', 'allthemodium:allthemodium_ingot').id('kubejs:crushing/allthemodium_ingot_to_dust');
    event.recipes.create.crushing('allthemodium:vibranium_dust', 'allthemodium:vibranium_ingot').id('kubejs:crushing/vibranium_ingot_to_dust');
    event.recipes.create.crushing('allthemodium:unobtainium_dust', 'allthemodium:unobtainium_ingot').id('kubejs:crushing/unobtainium_ingot_to_dust');


    // ==========================================
    // SECTION 3: TRUE ALLOY DUST COMPOUNDING
    // Synthesizes the actual alloy blend from parent powders + Piglich Heart + Soul Lava
    // ==========================================

    // Unobtainium-Allthemodium Alloy Dust (2x yield from 2 parent powders)
    event.recipes.create.mixing('2x allthemodium:unobtainium_allthemodium_alloy_dust', [
        'allthemodium:unobtainium_dust',
        'allthemodium:allthemodium_dust',
        'allthemodium:piglich_heart',
        Fluid.of('allthemodium:soul_lava', 250)
    ]).superheated().id('kubejs:create_mixing/unobtainium_allthemodium_alloy_dust');

    // Unobtainium-Vibranium Alloy Dust (2x yield from 2 parent powders)
    event.recipes.create.mixing('2x allthemodium:unobtainium_vibranium_alloy_dust', [
        'allthemodium:unobtainium_dust',
        'allthemodium:vibranium_dust',
        'allthemodium:piglich_heart',
        Fluid.of('allthemodium:soul_lava', 250)
    ]).superheated().id('kubejs:create_mixing/unobtainium_vibranium_alloy_dust');

    // Vibranium-Allthemodium Alloy Dust (2x yield from 2 parent powders)
    event.recipes.create.mixing('2x allthemodium:vibranium_allthemodium_alloy_dust', [
        'allthemodium:vibranium_dust',
        'allthemodium:allthemodium_dust',
        'allthemodium:piglich_heart',
        Fluid.of('allthemodium:soul_lava', 250)
    ]).superheated().id('kubejs:create_mixing/vibranium_allthemodium_alloy_dust');


    // ==========================================
    // SECTION 4: HIGH-TIER ALLOY INGOT FORGING (ADVANCED CREATE ADDONS)
    // Sintering and fusing the alloy dusts into solid ingots using heavy machinery
    // ==========================================

    const alloyDefinitions = [
        {
            id: 'unobtainium_allthemodium_alloy',
            dust: 'allthemodium:unobtainium_allthemodium_alloy_dust',
            ingot: 'allthemodium:unobtainium_allthemodium_alloy_ingot'
        },
        {
            id: 'unobtainium_vibranium_alloy',
            dust: 'allthemodium:unobtainium_vibranium_alloy_dust',
            ingot: 'allthemodium:unobtainium_vibranium_alloy_ingot'
        },
        {
            id: 'vibranium_allthemodium_alloy',
            dust: 'allthemodium:vibranium_allthemodium_alloy_dust',
            ingot: 'allthemodium:vibranium_allthemodium_alloy_ingot'
        }
    ];

    alloyDefinitions.forEach(alloy => {
        // 1. Create: New Age Electrical Sintering (Depot lightning discharge)
        event.custom({
            type: 'create_new_age:energising',
            energy_needed: 500000,
            ingredients: [{ item: alloy.dust }],
            results: [{ id: alloy.ingot }]
        }).id(`kubejs:energising/${alloy.id}_ingot`);

        // 2. TFMG Electric Arc Furnace (Firebrick Chemical Vat + 3x Graphite Electrodes)
        event.custom({
            type: 'tfmg:vat_machine_recipe',
            allowed_vat_types: ['tfmg:firebrick_lined_vat'],
            ingredients: [
                { item: alloy.dust },
                { type: 'neoforge:single', amount: 250, fluid: 'allthemodium:soul_lava' }
            ],
            machines: [
                'tfmg:graphite_electrode',
                'tfmg:graphite_electrode',
                'tfmg:graphite_electrode'
            ],
            min_size: 1,
            processing_time: 100,
            results: [{ id: alloy.ingot }]
        }).id(`kubejs:arc_furnace/${alloy.id}_ingot`);

        // 3. Dreams & Desires Hydraulic Press (High-pressure hydraulic compaction)
        event.custom({
            type: 'dndesires:hydraulic_compacting',
            heat_requirement: 'superheated',
            ingredients: [
                { item: alloy.dust },
                { type: 'neoforge:single', amount: 250, fluid: 'allthemodium:soul_lava' }
            ],
            results: [{ id: alloy.ingot }]
        }).id(`kubejs:hydraulic_compacting/${alloy.id}_ingot`);

        // 4. Closed-loop recycling: Crushing the ingot returns 1x alloy dust
        event.recipes.create.crushing(alloy.dust, alloy.ingot).id(`kubejs:crushing/${alloy.id}_dust`);
    });

    // Direct Electric Arc Ingot Smelting in TFMG Vat (Alternate heavy industry path)
    event.custom({
        type: 'tfmg:vat_machine_recipe',
        allowed_vat_types: ['tfmg:firebrick_lined_vat'],
        ingredients: [
            { item: 'allthemodium:unobtainium_ingot' },
            { item: 'allthemodium:allthemodium_ingot' },
            { item: 'allthemodium:piglich_heart' },
            { type: 'neoforge:single', amount: 250, fluid: 'allthemodium:soul_lava' }
        ],
        machines: [
            'tfmg:graphite_electrode',
            'tfmg:graphite_electrode',
            'tfmg:graphite_electrode'
        ],
        min_size: 1,
        processing_time: 120,
        results: [{ id: 'allthemodium:unobtainium_allthemodium_alloy_ingot' }]
    }).id('kubejs:arc_furnace/direct_unobtainium_allthemodium_alloy_ingot');

    event.custom({
        type: 'tfmg:vat_machine_recipe',
        allowed_vat_types: ['tfmg:firebrick_lined_vat'],
        ingredients: [
            { item: 'allthemodium:unobtainium_ingot' },
            { item: 'allthemodium:vibranium_ingot' },
            { item: 'allthemodium:piglich_heart' },
            { type: 'neoforge:single', amount: 250, fluid: 'allthemodium:soul_lava' }
        ],
        machines: [
            'tfmg:graphite_electrode',
            'tfmg:graphite_electrode',
            'tfmg:graphite_electrode'
        ],
        min_size: 1,
        processing_time: 120,
        results: [{ id: 'allthemodium:unobtainium_vibranium_alloy_ingot' }]
    }).id('kubejs:arc_furnace/direct_unobtainium_vibranium_alloy_ingot');

    event.custom({
        type: 'tfmg:vat_machine_recipe',
        allowed_vat_types: ['tfmg:firebrick_lined_vat'],
        ingredients: [
            { item: 'allthemodium:vibranium_ingot' },
            { item: 'allthemodium:allthemodium_ingot' },
            { item: 'allthemodium:piglich_heart' },
            { type: 'neoforge:single', amount: 250, fluid: 'allthemodium:soul_lava' }
        ],
        machines: [
            'tfmg:graphite_electrode',
            'tfmg:graphite_electrode',
            'tfmg:graphite_electrode'
        ],
        min_size: 1,
        processing_time: 120,
        results: [{ id: 'allthemodium:vibranium_allthemodium_alloy_ingot' }]
    }).id('kubejs:arc_furnace/direct_vibranium_allthemodium_alloy_ingot');


    // ==========================================
    // SECTION 5: MISSING RANGED & DEFENSIVE GEAR
    // Smithing table upgrades preserving enchantments
    // ==========================================

    // Allthemodium Bow
    event.smithing(
        'allthemodium:allthemodium_bow',
        'allthemodium:allthemodium_upgrade_smithing_template',
        'minecraft:bow',
        'allthemodium:allthemodium_ingot'
    ).id('kubejs:smithing/allthemodium_bow');

    // Unobtainium Crossbow
    event.smithing(
        'allthemodium:unobtainium_crossbow',
        'allthemodium:unobtainium_upgrade_smithing_template',
        'minecraft:crossbow',
        'allthemodium:unobtainium_ingot'
    ).id('kubejs:smithing/unobtainium_crossbow');

    // Vibranium Shield
    event.smithing(
        'allthemodium:vibranium_shield',
        'allthemodium:vibranium_upgrade_smithing_template',
        'minecraft:shield',
        'allthemodium:vibranium_ingot'
    ).id('kubejs:smithing/vibranium_shield');


    // ==========================================
    // SECTION 6: ULTIMATE ALLOY TOOLS
    // Smithing Unobtainium tools with ATM Alloy ingots
    // ==========================================

    // Alloy Pickaxe
    event.smithing(
        'allthemodium:alloy_pick',
        'allthemodium:unobtainium_upgrade_smithing_template',
        'allthemodium:unobtainium_pickaxe',
        'allthemodium:unobtainium_allthemodium_alloy_ingot'
    ).id('kubejs:smithing/alloy_pick');

    // Alloy Shovel
    event.smithing(
        'allthemodium:alloy_shovel',
        'allthemodium:unobtainium_upgrade_smithing_template',
        'allthemodium:unobtainium_shovel',
        'allthemodium:unobtainium_allthemodium_alloy_ingot'
    ).id('kubejs:smithing/alloy_shovel');

    // Alloy Sword
    event.smithing(
        'allthemodium:alloy_sword',
        'allthemodium:unobtainium_upgrade_smithing_template',
        'allthemodium:unobtainium_sword',
        'allthemodium:unobtainium_vibranium_alloy_ingot'
    ).id('kubejs:smithing/alloy_sword');

    // Alloy Axe
    event.smithing(
        'allthemodium:alloy_axe',
        'allthemodium:unobtainium_upgrade_smithing_template',
        'allthemodium:unobtainium_axe',
        'allthemodium:unobtainium_vibranium_alloy_ingot'
    ).id('kubejs:smithing/alloy_axe');

    // Alloy Trident
    event.smithing(
        'allthemodium:alloy_trident',
        'allthemodium:unobtainium_upgrade_smithing_template',
        'minecraft:trident',
        'allthemodium:unobtainium_vibranium_alloy_ingot'
    ).id('kubejs:smithing/alloy_trident');

    // Alloy Paxel (Iconic 3-in-1 combo tool)
    event.shaped('allthemodium:alloy_paxel', [
        'PSA',
        ' R ',
        ' R '
    ], {
        P: 'allthemodium:alloy_pick',
        S: 'allthemodium:alloy_shovel',
        A: 'allthemodium:alloy_axe',
        R: 'allthemodium:allthemodium_rod'
    }).id('kubejs:crafting/alloy_paxel');

    console.log('[PEAK Expert Mode] Script 67: AllTheModium Advanced Metallurgy loaded!');
});
