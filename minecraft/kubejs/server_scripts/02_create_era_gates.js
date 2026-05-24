// ==========================================
// PEAK EXPERT MODE — SCRIPT 02
// CREATE ERA GATES: TFMG + IE + EARLY TECH
// ==========================================
// This script handles the transition from Create into
// the industrial revolution. TFMG steel is the bridge
// between Create's kinetic world and IE's electrical world.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: TFMG AS CREATE'S INDUSTRIAL ARM
    // TFMG adds industrial processes ON TOP of Create.
    // Its steel is the first "advanced" metal.
    // ==========================================

    // TFMG's Distillery requires upgraded Create components
    // (Distillery = chemical processing = advanced)
    event.remove({ output: 'tfmg:steel_distillation_controller' });
    event.shaped('tfmg:steel_distillation_controller', [
        'BPB',
        'BCB',
        'SAS'
    ], {
        B: 'create:brass_ingot',
        P: 'create:mechanical_pump',
        C: 'create:copper_casing',
        S: '#c:ingots/steel',
        A: 'create:andesite_casing'
    });

    // TFMG's Radial Engine requires advanced Create
    // (This is TFMG's top-tier power generation)
    event.remove({ output: 'tfmg:radial_engine' });
    event.shaped('tfmg:radial_engine', [
        'SPS',
        'HMH',
        'SPS'
    ], {
        S: '#c:ingots/steel',
        P: 'create:precision_mechanism',
        H: 'tfmg:heavy_plate',
        M: 'create:shaft'
    });

    // ==========================================
    // SECTION 2: IE MACHINES NEED CREATE + TFMG
    // IE is the SECOND tech era. You can't skip Create.
    // ==========================================

    // IE Workbench (the crafting station) needs Create basics
    event.remove({ output: 'immersiveengineering:workbench' });
    event.shaped('immersiveengineering:workbench', [
        '   ',
        'AFA',
        'W W'
    ], {
        A: 'create:andesite_alloy',
        F: 'minecraft:crafting_table',
        W: '#minecraft:wooden_fences'
    });

    // IE Squeezer requires Create's Mechanical Press concept
    event.remove({ output: 'immersiveengineering:squeezer' });
    event.shaped('immersiveengineering:squeezer', [
        'PHP',
        'L L',
        'SIS'
    ], {
        P: 'tfmg:heavy_plate',
        H: 'create:mechanical_press',
        L: 'immersiveengineering:light_engineering',
        S: '#c:ingots/steel',
        I: 'create:shaft'
    });

    // IE Fermenter requires Create mixing concepts
    event.remove({ output: 'immersiveengineering:fermenter' });
    event.shaped('immersiveengineering:fermenter', [
        'PHP',
        'L L',
        'SIS'
    ], {
        P: 'tfmg:heavy_plate',
        H: 'create:mechanical_mixer',
        L: 'immersiveengineering:light_engineering',
        S: '#c:ingots/steel',
        I: 'create:brass_casing'
    });

    // IE Refinery requires TFMG + Create fluid handling
    event.remove({ output: 'immersiveengineering:refinery' });
    event.shaped('immersiveengineering:refinery', [
        'PBP',
        'HCH',
        'SDS'
    ], {
        P: 'tfmg:heavy_plate',
        B: 'create:brass_ingot',
        H: 'immersiveengineering:heavy_engineering',
        C: 'immersiveengineering:component_steel',
        S: '#c:ingots/steel',
        D: 'tfmg:steel_mechanism'
    });

    // IE Metal Press = industrial upgrade of Create's Mechanical Press
    event.remove({ output: 'immersiveengineering:metal_press' });
    event.shaped('immersiveengineering:metal_press', [
        'PHP',
        'L L',
        'SRS'
    ], {
        P: 'create:precision_mechanism',
        H: 'create:mechanical_press',
        L: 'immersiveengineering:light_engineering',
        S: '#c:ingots/steel',
        R: 'minecraft:redstone'
    });

    // IE Excavator (multiblock - requires the bucket wheel)
    // Gate this behind TFMG + Create's large-scale engineering
    event.remove({ output: 'immersiveengineering:bucket_wheel' });
    event.shaped('immersiveengineering:bucket_wheel', [
        'SHS',
        'HLH',
        'SHS'
    ], {
        S: '#c:ingots/steel',
        H: 'tfmg:heavy_plate',
        L: 'create:large_cogwheel'
    });

    // ==========================================
    // SECTION 3: IE WIRE SYSTEM REQUIRES CREATE
    // Wires are IE's backbone. The connectors need Create.
    // ==========================================

    // LV Wire Connector requires Andesite Alloy
    event.remove({ output: 'immersiveengineering:connector_lv' });
    event.shaped('2x immersiveengineering:connector_lv', [
        ' A ',
        'ACA',
        ' I '
    ], {
        A: 'create:andesite_alloy',
        C: '#c:ingots/copper',
        I: '#c:ingots/iron'
    });

    // MV Wire Connector requires Brass
    event.remove({ output: 'immersiveengineering:connector_mv' });
    event.shaped('2x immersiveengineering:connector_mv', [
        ' B ',
        'BIB',
        ' E '
    ], {
        B: 'create:brass_ingot',
        I: '#c:ingots/iron',
        E: 'create:electron_tube'
    });

    // HV Wire Connector requires Precision Mechanism
    event.remove({ output: 'immersiveengineering:connector_hv' });
    event.shaped('2x immersiveengineering:connector_hv', [
        ' P ',
        'PIP',
        ' S '
    ], {
        P: 'create:precision_mechanism',
        I: '#c:ingots/iron',
        S: '#c:ingots/steel'
    });

    // ==========================================
    // SECTION 4: IE GENERATORS NEED TFMG/CREATE
    // Power generation should feel earned
    // ==========================================

    // Dynamo (basic IE power) requires Create rotation
    event.remove({ output: 'immersiveengineering:dynamo' });
    event.shaped('immersiveengineering:dynamo', [
        ' S ',
        'SCS',
        ' L '
    ], {
        S: '#c:ingots/steel',
        C: 'immersiveengineering:component_iron',
        L: 'create:large_cogwheel'
    });

    // ==========================================
    // SECTION 5: ALLTHEMODIUM EARLY PROCESSING
    // Allthemodium ore should be processed via Create
    // for max output, encouraging Create infrastructure
    // ==========================================

    // Add Create crushing for Allthemodium ore
    event.recipes.create.crushing([
        'allthemodium:raw_allthemodium',
        CreateItem.of('allthemodium:raw_allthemodium', 0.35),
        CreateItem.of('create:experience_nugget', 0.75)
    ], 'allthemodium:allthemodium_ore');

    // ==========================================
    // SECTION 6: REMOVE DUPLICATE STEEL PATHS
    // Unify steel production: TFMG early, IE later
    // ==========================================

    // If any mod adds a trivial steel recipe that bypasses
    // TFMG/IE blast furnace, remove it
    // (Keep TFMG's Create-based steel and IE's blast furnace steel)

    // ==========================================
    // SECTION 7: CREATE NEW AGE & CREATE NUCLEAR GATES
    // These are late-Create era. They should require
    // TFMG materials before accessing nuclear/electrical power
    // ==========================================

    // Create New Age motors/generators should need TFMG steel
    // (Create New Age adds electrical generation to Create)
    // These recipes may vary by version - apply cautiously

    // Create Nuclear should require IE/TFMG components
    // (Nuclear power = very late in the Create era)

    // ==========================================
    // SECTION 8: APOTHEOSIS INTEGRATION WITH CREATE
    // Apotheosis adds enchanting upgrades. Gate behind Create.
    // ==========================================

    // Apotheosis Enchanting Table upgrades should use Create materials
    // (Enchanting is enhanced crafting = mechanical enhancement)
    
    // Apothic Spawners require significant tech investment
    // (Spawner modification is powerful - gate it properly)

    // ==========================================
    // SECTION 9: SOPHISTICATED STORAGE INTEGRATION
    // Sophisticated Backpacks tiers scale with tech progression
    // ==========================================

    // ==========================================
    // SECTION 9: SOPHISTICATED STORAGE INTEGRATION
    // Sophisticated Backpacks tiers scale with tech progression
    // ==========================================

    // --- NETHERITE PLATE REFORM ---
    // Remove easy hammer recipes
    event.remove({ output: 'alltheores:netherite_plate' });
    
    // Immersive Engineering Metal Press
    event.custom({
        type: "immersiveengineering:metal_press",
        mold: "immersiveengineering:mold_plate",
        input: { item: "minecraft:netherite_ingot" },
        result: { item: "alltheores:netherite_plate" },
        energy: 2400
    });

    // Create Compacting (requires Mechanical Press + Basin + Superheated Blaze Burner)
    event.recipes.create.compacting('alltheores:netherite_plate', 'minecraft:netherite_ingot').superheated();


    // --- REMOVE DEFAULT UPGRADE RECIPES ---
    event.remove({ id: 'sophisticatedbackpacks:upgrade_base' });
    event.remove({ id: 'sophisticatedbackpacks:magnet_upgrade' });
    event.remove({ id: 'sophisticatedbackpacks:advanced_magnet_upgrade' });
    event.remove({ id: 'sophisticatedbackpacks:filter_upgrade' });
    event.remove({ id: 'sophisticatedbackpacks:advanced_filter_upgrade' });


    // --- CREATE SEQUENCED ASSEMBLIES FOR UPGRADES ---

    // A. Upgrade Base
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "minecraft:leather" },
        "transitional_item": { "id": "kubejs:incomplete_upgrade_base" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_upgrade_base" }, { "item": "minecraft:string" }],
                "results": [{ "id": "kubejs:incomplete_upgrade_base" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_upgrade_base" }, { "item": "minecraft:iron_ingot" }],
                "results": [{ "id": "kubejs:incomplete_upgrade_base" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "kubejs:incomplete_upgrade_base" }],
                "results": [{ "id": "kubejs:incomplete_upgrade_base" }]
            }
        ],
        "results": [{ "id": "sophisticatedbackpacks:upgrade_base" }],
        "loops": 4
    });

    // F. Basic Magnet Upgrade
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:upgrade_base" },
        "transitional_item": { "id": "kubejs:incomplete_magnet_upgrade" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_magnet_upgrade" }, { "item": "alexscaves:scarlet_magnet" }],
                "results": [{ "id": "kubejs:incomplete_magnet_upgrade" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_magnet_upgrade" }, { "item": "alexscaves:azure_magnet" }],
                "results": [{ "id": "kubejs:incomplete_magnet_upgrade" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "kubejs:incomplete_magnet_upgrade" }],
                "results": [{ "id": "kubejs:incomplete_magnet_upgrade" }]
            }
        ],
        "results": [{ "id": "sophisticatedbackpacks:magnet_upgrade" }],
        "loops": 1
    });

    // G. Advanced Magnet Upgrade
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:magnet_upgrade" },
        "transitional_item": { "id": "kubejs:incomplete_advanced_magnet_upgrade" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_advanced_magnet_upgrade" }, { "item": "tfmg:electromagnetic_coil" }],
                "results": [{ "id": "kubejs:incomplete_advanced_magnet_upgrade" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_advanced_magnet_upgrade" }, { "item": "immersiveengineering:electromagnet" }],
                "results": [{ "id": "kubejs:incomplete_advanced_magnet_upgrade" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "kubejs:incomplete_advanced_magnet_upgrade" }],
                "results": [{ "id": "kubejs:incomplete_advanced_magnet_upgrade" }]
            }
        ],
        "results": [{ "id": "sophisticatedbackpacks:advanced_magnet_upgrade" }],
        "loops": 1
    });

    // H. Basic Filter Upgrade
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:upgrade_base" },
        "transitional_item": { "id": "kubejs:incomplete_filter_upgrade" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_filter_upgrade" }, { "item": "create:filter" }],
                "results": [{ "id": "kubejs:incomplete_filter_upgrade" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_filter_upgrade" }, { "item": "minecraft:paper" }],
                "results": [{ "id": "kubejs:incomplete_filter_upgrade" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "kubejs:incomplete_filter_upgrade" }],
                "results": [{ "id": "kubejs:incomplete_filter_upgrade" }]
            }
        ],
        "results": [{ "id": "sophisticatedbackpacks:filter_upgrade" }],
        "loops": 1
    });

    // I. Advanced Filter Upgrade
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:filter_upgrade" },
        "transitional_item": { "id": "kubejs:incomplete_advanced_filter_upgrade" },
        "sequence": [
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_advanced_filter_upgrade" }, { "item": "create:attribute_filter" }],
                "results": [{ "id": "kubejs:incomplete_advanced_filter_upgrade" }]
            },
            {
                "type": "create:deploying",
                "ingredients": [{ "item": "kubejs:incomplete_advanced_filter_upgrade" }, { "item": "enderio:advanced_item_filter" }],
                "results": [{ "id": "kubejs:incomplete_advanced_filter_upgrade" }]
            },
            {
                "type": "create:pressing",
                "ingredients": [{ "item": "kubejs:incomplete_advanced_filter_upgrade" }],
                "results": [{ "id": "kubejs:incomplete_advanced_filter_upgrade" }]
            }
        ],
        "results": [{ "id": "sophisticatedbackpacks:advanced_filter_upgrade" }],
        "loops": 1
    });


    // --- REMOVE DEFAULT BACKPACK RECIPES ---
    event.remove({ id: 'sophisticatedbackpacks:copper_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:iron_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:iron_backpack_from_copper' });
    event.remove({ id: 'sophisticatedbackpacks:gold_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:gold_backpack_from_iron' });
    event.remove({ id: 'sophisticatedbackpacks:diamond_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:diamond_backpack_from_gold' });
    event.remove({ id: 'sophisticatedbackpacks:netherite_backpack' });


    // --- UPGRADED BACKPACKS (Shaped Tool-Damaging Crafteos) ---

    // 0. Copper Backpack (Leather -> Copper)
    ['immersiveengineering:screwdriver', 'tfmg:screwdriver'].forEach(tool => {
        event.shaped('sophisticatedbackpacks:copper_backpack', [
            ' P ',
            'PBP',
            ' T '
        ], {
            B: 'sophisticatedbackpacks:backpack',
            P: '#c:plates/copper',
            T: tool
        }).damageIngredient(tool);
    });

    // 1a. Iron Backpack (Leather -> Iron)
    ['immersiveengineering:screwdriver', 'tfmg:screwdriver'].forEach(tool => {
        event.shaped('sophisticatedbackpacks:iron_backpack', [
            ' P ',
            'PBP',
            ' T '
        ], {
            B: 'sophisticatedbackpacks:backpack',
            P: '#c:plates/iron',
            T: tool
        }).damageIngredient(tool);
    });

    // 1b. Iron Backpack (Copper -> Iron)
    ['immersiveengineering:screwdriver', 'tfmg:screwdriver'].forEach(tool => {
        event.shaped('sophisticatedbackpacks:iron_backpack', [
            ' P ',
            'PBP',
            ' T '
        ], {
            B: 'sophisticatedbackpacks:copper_backpack',
            P: '#c:plates/iron',
            T: tool
        }).damageIngredient(tool);
    });

    // 2. Gold Backpack (Iron -> Gold)
    ['immersiveengineering:screwdriver', 'tfmg:screwdriver'].forEach(tool => {
        event.shaped('sophisticatedbackpacks:gold_backpack', [
            ' P ',
            'PBP',
            ' T '
        ], {
            B: 'sophisticatedbackpacks:iron_backpack',
            P: '#c:plates/gold',
            T: tool
        }).damageIngredient(tool);
    });

    // 3. Diamond Backpack (Gold -> Diamond)
    ['immersiveengineering:screwdriver', 'tfmg:screwdriver'].forEach(tool => {
        event.shaped('sophisticatedbackpacks:diamond_backpack', [
            ' P ',
            'PBP',
            ' T '
        ], {
            B: 'sophisticatedbackpacks:gold_backpack',
            P: 'minecraft:diamond',
            T: tool
        }).damageIngredient(tool);
    });

    // 4. Netherite Backpack (Diamond -> Netherite)
    ['immersiveengineering:screwdriver', 'tfmg:screwdriver'].forEach(tool => {
        event.shaped('sophisticatedbackpacks:netherite_backpack', [
            ' P ',
            'PBP',
            ' T '
        ], {
            B: 'sophisticatedbackpacks:diamond_backpack',
            P: 'alltheores:netherite_plate',
            T: tool
        }).damageIngredient(tool);
    });



    // --- AUTOMATED BACKPACKS (Create Sequenced Assemblies) ---
    
    // 0. Copper Backpack
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:backpack" },
        "transitional_item": { "id": "kubejs:incomplete_copper_backpack" },
        "sequence": [
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_copper_backpack" }, { "tag": "c:plates/copper" }], "results": [{ "id": "kubejs:incomplete_copper_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_copper_backpack" }, { "tag": "c:plates/copper" }], "results": [{ "id": "kubejs:incomplete_copper_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_copper_backpack" }, { "tag": "c:plates/copper" }], "results": [{ "id": "kubejs:incomplete_copper_backpack" }] },
            { "type": "create:pressing", "ingredients": [{ "item": "kubejs:incomplete_copper_backpack" }], "results": [{ "id": "kubejs:incomplete_copper_backpack" }] }
        ],
        "results": [{ "id": "sophisticatedbackpacks:copper_backpack" }],
        "loops": 1
    });

    // 1a. Iron Backpack (from Leather)
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:backpack" },
        "transitional_item": { "id": "kubejs:incomplete_iron_backpack" },
        "sequence": [
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }, { "tag": "c:plates/iron" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }, { "tag": "c:plates/iron" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }, { "tag": "c:plates/iron" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] },
            { "type": "create:pressing", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] }
        ],
        "results": [{ "id": "sophisticatedbackpacks:iron_backpack" }],
        "loops": 1
    });

    // 1b. Iron Backpack (from Copper)
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:copper_backpack" },
        "transitional_item": { "id": "kubejs:incomplete_iron_backpack" },
        "sequence": [
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }, { "tag": "c:plates/iron" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }, { "tag": "c:plates/iron" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }, { "tag": "c:plates/iron" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] },
            { "type": "create:pressing", "ingredients": [{ "item": "kubejs:incomplete_iron_backpack" }], "results": [{ "id": "kubejs:incomplete_iron_backpack" }] }
        ],
        "results": [{ "id": "sophisticatedbackpacks:iron_backpack" }],
        "loops": 1
    });

    // 2. Gold Backpack
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:iron_backpack" },
        "transitional_item": { "id": "kubejs:incomplete_gold_backpack" },
        "sequence": [
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_gold_backpack" }, { "tag": "c:plates/gold" }], "results": [{ "id": "kubejs:incomplete_gold_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_gold_backpack" }, { "tag": "c:plates/gold" }], "results": [{ "id": "kubejs:incomplete_gold_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_gold_backpack" }, { "tag": "c:plates/gold" }], "results": [{ "id": "kubejs:incomplete_gold_backpack" }] },
            { "type": "create:pressing", "ingredients": [{ "item": "kubejs:incomplete_gold_backpack" }], "results": [{ "id": "kubejs:incomplete_gold_backpack" }] }
        ],
        "results": [{ "id": "sophisticatedbackpacks:gold_backpack" }],
        "loops": 1
    });

    // 3. Diamond Backpack
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:gold_backpack" },
        "transitional_item": { "id": "kubejs:incomplete_diamond_backpack" },
        "sequence": [
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_diamond_backpack" }, { "item": "minecraft:diamond" }], "results": [{ "id": "kubejs:incomplete_diamond_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_diamond_backpack" }, { "item": "minecraft:diamond" }], "results": [{ "id": "kubejs:incomplete_diamond_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_diamond_backpack" }, { "item": "minecraft:diamond" }], "results": [{ "id": "kubejs:incomplete_diamond_backpack" }] },
            { "type": "create:pressing", "ingredients": [{ "item": "kubejs:incomplete_diamond_backpack" }], "results": [{ "id": "kubejs:incomplete_diamond_backpack" }] }
        ],
        "results": [{ "id": "sophisticatedbackpacks:diamond_backpack" }],
        "loops": 1
    });

    // 4. Netherite Backpack
    event.custom({
        "type": "create:sequenced_assembly",
        "ingredient": { "item": "sophisticatedbackpacks:diamond_backpack" },
        "transitional_item": { "id": "kubejs:incomplete_netherite_backpack" },
        "sequence": [
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_netherite_backpack" }, { "item": "alltheores:netherite_plate" }], "results": [{ "id": "kubejs:incomplete_netherite_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_netherite_backpack" }, { "item": "alltheores:netherite_plate" }], "results": [{ "id": "kubejs:incomplete_netherite_backpack" }] },
            { "type": "create:deploying", "ingredients": [{ "item": "kubejs:incomplete_netherite_backpack" }, { "item": "alltheores:netherite_plate" }], "results": [{ "id": "kubejs:incomplete_netherite_backpack" }] },
            { "type": "create:pressing", "ingredients": [{ "item": "kubejs:incomplete_netherite_backpack" }], "results": [{ "id": "kubejs:incomplete_netherite_backpack" }] }
        ],
        "results": [{ "id": "sophisticatedbackpacks:netherite_backpack" }],
        "loops": 1
    });

    // --- ENGINEER'S WORKBENCH BLUEPRINT RECIPES (Immersive Engineering) ---

    // 0. Copper Backpack Blueprint
    event.custom({
        type: "immersiveengineering:blueprint",
        inputs: [
            { tag: "c:plates/copper" },
            { tag: "c:plates/copper" },
            { tag: "c:plates/copper" },
            { tag: "c:plates/copper" },
            { item: "immersiveengineering:screwdriver" },
            { item: "immersiveengineering:hammer" }
        ],
        base_ingredient: { item: "sophisticatedbackpacks:backpack" },
        category: "components",
        result: { item: "sophisticatedbackpacks:copper_backpack" }
    });

    // 1a. Iron Backpack Blueprint (Leather -> Iron)
    event.custom({
        type: "immersiveengineering:blueprint",
        inputs: [
            { tag: "c:plates/iron" },
            { tag: "c:plates/iron" },
            { tag: "c:plates/iron" },
            { tag: "c:plates/iron" },
            { item: "immersiveengineering:screwdriver" },
            { item: "immersiveengineering:hammer" }
        ],
        base_ingredient: { item: "sophisticatedbackpacks:backpack" },
        category: "components",
        result: { item: "sophisticatedbackpacks:iron_backpack" }
    });

    // 1b. Iron Backpack Blueprint (Copper -> Iron)
    event.custom({
        type: "immersiveengineering:blueprint",
        inputs: [
            { tag: "c:plates/iron" },
            { tag: "c:plates/iron" },
            { tag: "c:plates/iron" },
            { tag: "c:plates/iron" },
            { item: "immersiveengineering:screwdriver" },
            { item: "immersiveengineering:hammer" }
        ],
        base_ingredient: { item: "sophisticatedbackpacks:copper_backpack" },
        category: "components",
        result: { item: "sophisticatedbackpacks:iron_backpack" }
    });

    // 2. Gold Backpack Blueprint
    event.custom({
        type: "immersiveengineering:blueprint",
        inputs: [
            { tag: "c:plates/gold" },
            { tag: "c:plates/gold" },
            { tag: "c:plates/gold" },
            { tag: "c:plates/gold" },
            { item: "immersiveengineering:screwdriver" },
            { item: "immersiveengineering:hammer" }
        ],
        base_ingredient: { item: "sophisticatedbackpacks:iron_backpack" },
        category: "components",
        result: { item: "sophisticatedbackpacks:gold_backpack" }
    });

    // 3. Diamond Backpack Blueprint
    event.custom({
        type: "immersiveengineering:blueprint",
        inputs: [
            { item: "minecraft:diamond" },
            { item: "minecraft:diamond" },
            { item: "minecraft:diamond" },
            { item: "minecraft:diamond" },
            { item: "immersiveengineering:screwdriver" },
            { item: "immersiveengineering:hammer" }
        ],
        base_ingredient: { item: "sophisticatedbackpacks:gold_backpack" },
        category: "components",
        result: { item: "sophisticatedbackpacks:diamond_backpack" }
    });

    // 4. Netherite Backpack Blueprint
    event.custom({
        type: "immersiveengineering:blueprint",
        inputs: [
            { item: "alltheores:netherite_plate" },
            { item: "alltheores:netherite_plate" },
            { item: "minecraft:netherite_nugget" },
            { item: "minecraft:netherite_nugget" },
            { item: "immersiveengineering:screwdriver" },
            { item: "immersiveengineering:hammer" }
        ],
        base_ingredient: { item: "sophisticatedbackpacks:diamond_backpack" },
        category: "components",
        result: { item: "sophisticatedbackpacks:netherite_backpack" }
    });

    // ==========================================
    // SECTION 10: BUILDING WANDS & UTILITY
    // Quality of life items should feel earned
    // ==========================================

    // Building Wands require Create components
    event.remove({ output: 'buildingwands:stone_wand' });
    event.shaped('buildingwands:stone_wand', [
        '  S',
        ' A ',
        'I  '
    ], {
        S: '#c:cobblestones',
        A: 'create:andesite_alloy',
        I: '#minecraft:wooden_fences'
    });

    event.remove({ output: 'buildingwands:iron_wand' });
    event.shaped('buildingwands:iron_wand', [
        '  I',
        ' B ',
        'S  '
    ], {
        I: '#c:ingots/iron',
        B: 'create:brass_ingot',
        S: '#minecraft:wooden_fences'
    });

    event.remove({ output: 'buildingwands:diamond_wand' });
    event.shaped('buildingwands:diamond_wand', [
        '  D',
        ' P ',
        'S  '
    ], {
        D: '#c:gems/diamond',
        P: 'create:precision_mechanism',
        S: '#minecraft:wooden_fences'
    });

    console.log('[PEAK Expert Mode] Script 02: Create Era Gates loaded successfully!');
});
