// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 02
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
        ' B ',
        'AFA',
        'W W'
    ], {
        B: 'create:crafting_blueprint',
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

    // --- ALLTHEORES & IMMERSIVE ENGINEERING MANUAL HAMMER NERF ---
    // Remove all recipes that use the IE Hammer to manually crush ores or make plates in a crafting table.
    // This forces players to use Create's Crushing Wheels and Presses.
    
    // Immersive Engineering Hammer (removes ALL recipes using it as input)
    event.remove({ input: 'immersiveengineering:hammer' });

    // AllTheOres Hammers (removes default shapeless recipes that glitch in Create Mixers)
    event.remove({ id: /^alltheores:crafting\/hammer\/.*/ });

    // --- ALLTHEORES PLATES REFORM ---
    // Remove ALL AllTheOres crafting table plate recipes by their exact recipe IDs
    // (These are shaped recipes using 2 hammers + 2 ingots, so input filters don't catch them)
    let allPlateMats = ['aluminum', 'brass', 'bronze', 'constantan', 'copper', 'diamond', 'electrum', 'enderium', 'gold', 'invar', 'iridium', 'iron', 'lead', 'lumium', 'netherite', 'nickel', 'osmium', 'platinum', 'signalum', 'silver', 'steel', 'tin', 'uranium', 'zinc'];
    allPlateMats.forEach(mat => {
        event.remove({ id: 'alltheores:crafting/' + mat + '/plate' });
    });

    // 1. Normal Materials (Mechanical Press - No heat)
    let normalPlates = ['aluminum', 'brass', 'bronze', 'constantan', 'copper', 'electrum', 'gold', 'invar', 'iron', 'lead', 'nickel', 'silver', 'steel', 'tin', 'uranium', 'zinc'];
    normalPlates.forEach(mat => {
        event.recipes.create.pressing('alltheores:' + mat + '_plate', { tag: 'c:ingots/' + mat });
    });

    // 2. High Tier Materials (Compacting - Heated)
    let heatedPlates = ['diamond', 'platinum', 'osmium'];
    heatedPlates.forEach(mat => {
        let inputTag = (mat === 'diamond') ? 'c:gems/' + mat : 'c:ingots/' + mat;
        event.recipes.create.compacting('alltheores:' + mat + '_plate', { tag: inputTag }).heated();
    });

    // 3. Super-Strong Materials (Compacting - Super-Heated)
    let superHeatedPlates = ['netherite', 'enderium', 'lumium', 'signalum', 'iridium'];
    superHeatedPlates.forEach(mat => {
        let inputObj = (mat === 'netherite') ? { item: 'minecraft:netherite_ingot' } : { tag: 'c:ingots/' + mat };
        event.recipes.create.compacting('alltheores:' + mat + '_plate', inputObj).superheated();
    });

    // Immersive Engineering Metal Press for Netherite (Legacy support)
    event.custom({
        type: "immersiveengineering:metal_press",
        mold: "immersiveengineering:mold_plate",
        input: { item: "minecraft:netherite_ingot" },
        result: { item: "alltheores:netherite_plate" },
        energy: 2400
    });


    // --- REMOVE DEFAULT UPGRADE RECIPES ---
    // event.remove({ id: 'sophisticatedbackpacks:upgrade_base' });
    event.remove({ id: 'sophisticatedbackpacks:magnet_upgrade' });
    event.remove({ id: 'sophisticatedbackpacks:advanced_magnet_upgrade' });
    event.remove({ id: 'sophisticatedbackpacks:filter_upgrade' });
    event.remove({ id: 'sophisticatedbackpacks:advanced_filter_upgrade' });



// ==========================================
    // SECTION 10: BUILDING WANDS & UTILITY
    // Quality of life items should feel earned
    // ==========================================

    // Building Wands require Create components
    event.remove({ output: 'wands:stone_wand' });
    event.shaped('wands:stone_wand', [
        '  S',
        ' A ',
        'I  '
    ], {
        S: '#c:cobblestones',
        A: 'create:andesite_alloy',
        I: '#minecraft:wooden_fences'
    });

    event.remove({ output: 'wands:iron_wand' });
    event.shaped('wands:iron_wand', [
        '  I',
        ' B ',
        'S  '
    ], {
        I: '#c:ingots/iron',
        B: 'create:brass_ingot',
        S: '#minecraft:wooden_fences'
    });

    event.remove({ output: 'wands:diamond_wand' });
    event.shaped('wands:diamond_wand', [
        '  D',
        ' P ',
        'S  '
    ], {
        D: '#c:gems/diamond',
        P: 'create:precision_mechanism',
        S: '#minecraft:wooden_fences'
    });

    // ==========================================
    // SECTION 9: SOPHISTICATED STORAGE INTEGRATION
    // ==========================================

    // --- SAFE TIER UPGRADES (Keep NBT/Data Components via Sequenced Assembly) ---
    // Instead of Mechanical Crafters or overriding the standard recipe (which wipes NBT), 
    // we use Sequenced Assembly. The base backpack is the transitional item, so its NBT is preserved!

    // 0. Remove Default Upgrades (they use a custom recipe type or smithing)
    // Remove by exact ID to catch standard crafting/smithing recipes
    event.remove({ id: 'sophisticatedbackpacks:copper_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:iron_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:gold_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:diamond_backpack' });
    event.remove({ id: 'sophisticatedbackpacks:netherite_backpack' });
    // Also remove the old custom types just in case
    event.remove({ output: 'sophisticatedbackpacks:copper_backpack', type: 'sophisticatedbackpacks:backpack_upgrade' });
    event.remove({ output: 'sophisticatedbackpacks:iron_backpack', type: 'sophisticatedbackpacks:backpack_upgrade' });
    event.remove({ output: 'sophisticatedbackpacks:gold_backpack', type: 'sophisticatedbackpacks:backpack_upgrade' });
    event.remove({ output: 'sophisticatedbackpacks:diamond_backpack', type: 'sophisticatedbackpacks:backpack_upgrade' });
    event.remove({ output: 'sophisticatedbackpacks:netherite_backpack', type: 'sophisticatedbackpacks:backpack_upgrade' });

    // 1. Basic -> Copper Backpack
    event.custom({
        type: 'sophisticatedbackpacks:backpack_upgrade',
        pattern: [
            ' U ',
            'PBP',
            ' T '
        ],
        key: {
            U: { item: 'sophisticatedbackpacks:upgrade_base' },
            P: { tag: 'c:plates/copper' },
            B: { item: 'sophisticatedbackpacks:backpack' },
            T: { tag: 'c:tools/screwdriver' }
        },
        result: { id: 'sophisticatedbackpacks:copper_backpack' }
    }).id('kubejs:crafting/copper_backpack');

    // 2a. Copper -> Iron Backpack
    event.custom({
        type: 'sophisticatedbackpacks:backpack_upgrade',
        pattern: [
            ' U ',
            'PBP',
            ' T '
        ],
        key: {
            U: { item: 'sophisticatedbackpacks:upgrade_base' },
            P: { tag: 'c:plates/iron' },
            B: { item: 'sophisticatedbackpacks:copper_backpack' },
            T: { tag: 'c:tools/screwdriver' }
        },
        result: { id: 'sophisticatedbackpacks:iron_backpack' }
    }).id('kubejs:crafting/iron_backpack');

    // 3. Iron -> Gold Backpack
    event.custom({
        type: 'sophisticatedbackpacks:backpack_upgrade',
        pattern: [
            ' U ',
            'PBP',
            ' T '
        ],
        key: {
            U: { item: 'sophisticatedbackpacks:upgrade_base' },
            P: { tag: 'c:plates/gold' },
            B: { item: 'sophisticatedbackpacks:iron_backpack' },
            T: { item: 'immersiveengineering:hammer' }
        },
        result: { id: 'sophisticatedbackpacks:gold_backpack' }
    }).id('kubejs:crafting/gold_backpack');

    // 4. Gold -> Diamond Backpack
    event.custom({
        type: 'sophisticatedbackpacks:backpack_upgrade',
        pattern: [
            'PGP',
            'VBV',
            'UTU'
        ],
        key: {
            P: { item: 'alltheores:diamond_plate' },
            G: { tag: 'c:storage_blocks/gold' },
            V: { item: 'create:item_vault' },
            B: { item: 'sophisticatedbackpacks:gold_backpack' },
            U: { item: 'sophisticatedbackpacks:upgrade_base' },
            T: { item: 'immersiveengineering:hammer' }
        },
        result: { id: 'sophisticatedbackpacks:diamond_backpack' }
    }).id('kubejs:crafting/diamond_backpack');

    // 5. Diamond -> Netherite Backpack
    event.custom({
        type: 'sophisticatedbackpacks:backpack_upgrade',
        pattern: [
            'PDP',
            'VBV',
            'UTU'
        ],
        key: {
            P: { item: 'alltheores:netherite_plate' },
            D: { tag: 'c:storage_blocks/diamond' },
            V: { item: 'create:item_vault' },
            B: { item: 'sophisticatedbackpacks:diamond_backpack' },
            U: { item: 'sophisticatedbackpacks:upgrade_base' },
            T: { item: 'immersiveengineering:hammer' }
        },
        result: { id: 'sophisticatedbackpacks:netherite_backpack' }
    }).id('kubejs:crafting/netherite_backpack');


    // ==========================================
    // SECTION 11: ALEX'S CAVES INTEGRATION
    // ==========================================
    
    // Remove default shapeless recipes for Neodymium Ingots
    event.remove({ output: 'alexscaves:scarlet_neodymium_ingot', input: 'alexscaves:raw_scarlet_neodymium' });
    event.remove({ output: 'alexscaves:azure_neodymium_ingot', input: 'alexscaves:raw_azure_neodymium' });

    // Scarlet Neodymium Ingot via Heated Mixing
    event.recipes.create.mixing('alexscaves:scarlet_neodymium_ingot', [
        '3x alexscaves:raw_scarlet_neodymium',
        '3x minecraft:iron_ingot'
    ]).heated().id('kubejs:mixing/scarlet_neodymium_ingot');

    // Azure Neodymium Ingot via Heated Mixing
    event.recipes.create.mixing('alexscaves:azure_neodymium_ingot', [
        '3x alexscaves:raw_azure_neodymium',
        '3x minecraft:iron_ingot'
    ]).heated().id('kubejs:mixing/azure_neodymium_ingot');


    console.log('[PEAK Expert Mode] Script 02: Create Era Gates loaded successfully!');
});

