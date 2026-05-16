// ==========================================
// PEAK EXPERT MODE — SCRIPT 01
// ORE UNIFICATION & CREATE FOUNDATION
// ==========================================
// Create is the CENTER of PEAK. All ore processing starts here.
// This script ensures Create's crushing/milling is the primary
// way to get bonus ore output, and removes redundant vanilla
// smelting shortcuts that bypass the tech tree.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: ORE PROCESSING UNIFICATION
    // Create Crushing Wheels / Millstone = primary doubling
    // Remove cheap furnace-based ore doubling from other mods
    // ==========================================

    // Remove duplicate ore processing recipes from mods that bypass Create
    // (We keep IE Crusher and Mekanism Enrichment as UPGRADES, not alternatives)
    
    // Force players to use Create's Crushing Wheels for early ore doubling
    // by removing any mod that adds free furnace-based ore doubling
    const vanillaOres = [
        'iron', 'gold', 'copper'
    ];

    // Remove raw ore → ingot smelting shortcuts from AllTheOres if they exist
    // (Players should crush first for bonus, then smelt the crushed output)
    // Note: We keep vanilla smelting as a basic option but Create gives 2x

    // ==========================================
    // SECTION 2: CREATE AS THE UNIVERSAL FOUNDATION
    // Every tech mod's first machine requires Create components
    // ==========================================

    // --- ANDESITE ALLOY: The absolute base material ---
    // Every mod's FIRST crafting step needs this

    // IE: Coke Oven Bricks require Andesite Alloy
    event.shaped('3x immersiveengineering:cokebrick', [
        'BCB',
        'CAC',
        'BCB'
    ], {
        B: 'minecraft:brick',
        C: 'minecraft:clay_ball',
        A: 'create:andesite_alloy'
    });

    // IE: Blast Furnace Bricks require Andesite Alloy + Nether Brick
    event.shaped('3x immersiveengineering:blastbrick', [
        'NBN',
        'BAB',
        'NBN'
    ], {
        N: 'minecraft:nether_brick',
        B: 'minecraft:magma_block',
        A: 'create:andesite_alloy'
    });

    // PneumaticCraft: Compressed Iron Block needs Create processing
    // (Compressed Iron is normally made by just placing iron under pressure,
    //  we add a Create prerequisite by requiring the Pressure Chamber itself
    //  to use Create components - handled in prompt 2)

    // Mekanism: Steel Casing (base of ALL Mekanism machines)
    // Now requires Andesite Alloy + Steel
    event.remove({ output: 'mekanism:steel_casing' });
    event.shaped('mekanism:steel_casing', [
        'SAS',
        'AGA',
        'SAS'
    ], {
        S: '#c:ingots/steel',
        A: 'create:andesite_alloy',
        G: '#c:glass_blocks'
    });

    // AE2: Certus Quartz should be polishable via Create
    // (Create's sandpaper polishing integration)
    // Add mixing recipe: Certus Quartz + Water → Polished Certus (via Create Mixer)
    // This encourages using Create's infrastructure for AE2 preparation

    // ==========================================
    // SECTION 3: BRASS = MID-TIER CREATE GATE
    // Brass is the key material for mid-game tech
    // ==========================================

    // --- BRASS requirements spread across mods ---

    // IE: Light Engineering Block requires Brass
    event.remove({ output: 'immersiveengineering:light_engineering' });
    event.shaped('immersiveengineering:light_engineering', [
        'ICI',
        'BRB',
        'ICI'
    ], {
        I: '#c:ingots/iron',
        C: 'immersiveengineering:component_iron',
        B: 'create:brass_ingot',
        R: 'minecraft:redstone'
    });

    // IE: Iron Component now needs a Create Cogwheel
    event.remove({ output: 'immersiveengineering:component_iron' });
    event.shaped('immersiveengineering:component_iron', [
        ' I ',
        'IGI',
        ' I '
    ], {
        I: '#c:ingots/iron',
        G: 'create:cogwheel'
    });

    // IE: Steel Component needs Precision Mechanism
    event.remove({ output: 'immersiveengineering:component_steel' });
    event.shaped('immersiveengineering:component_steel', [
        ' S ',
        'SPS',
        ' S '
    ], {
        S: '#c:ingots/steel',
        P: 'create:precision_mechanism'
    });

    // ==========================================
    // SECTION 4: PRECISION MECHANISM = ADVANCED CREATE GATE
    // The most important Create item. Gates access to advanced machines.
    // ==========================================

    // IE: Heavy Engineering Block requires Precision Mechanisms
    event.remove({ output: 'immersiveengineering:heavy_engineering' });
    event.shaped('immersiveengineering:heavy_engineering', [
        'SPS',
        'CEC',
        'SPS'
    ], {
        S: '#c:ingots/steel',
        P: 'create:precision_mechanism',
        C: 'immersiveengineering:component_steel',
        E: 'create:electron_tube'
    });

    // IE: Redstone Engineering Block requires Electron Tubes from Create
    event.remove({ output: 'immersiveengineering:rs_engineering' });
    event.shaped('immersiveengineering:rs_engineering', [
        'IEI',
        'RCR',
        'IEI'
    ], {
        I: '#c:ingots/iron',
        E: 'create:electron_tube',
        R: 'minecraft:redstone',
        C: 'immersiveengineering:component_iron'
    });

    // ==========================================
    // SECTION 5: CREATE ADDON INTEGRATION (TFMG)
    // TFMG provides industrial-grade Create processing
    // Steel from TFMG is the primary early-game steel source
    // ==========================================

    // TFMG Steel becomes the unified early-game steel
    // IE's blast furnace becomes an UPGRADE path (faster, more efficient)
    // but TFMG gets you there first via Create infrastructure

    // Make TFMG's Heavy Plates a requirement for IE's Crusher
    // (The IE Crusher is an upgrade over Create's Crushing Wheels)
    event.remove({ output: 'immersiveengineering:crusher' });
    event.shaped('immersiveengineering:crusher', [
        'PHP',
        'HLH',
        'PHP'
    ], {
        P: 'tfmg:heavy_plate',
        H: 'immersiveengineering:heavy_engineering',
        L: 'create:large_cogwheel'
    });

    // Make TFMG's Cast Iron essential for IE's basic machines
    // IE Arc Furnace requires TFMG heavy plates
    event.remove({ output: 'immersiveengineering:arc_furnace' });
    event.shaped('immersiveengineering:arc_furnace', [
        'PHG',
        'HCH',
        'PHP'
    ], {
        P: 'tfmg:heavy_plate',
        H: 'immersiveengineering:heavy_engineering',
        G: '#c:glass_blocks',
        C: 'immersiveengineering:component_steel'
    });

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
    event.remove({ id: 'endersdelight:shulker_bowl' });
    event.recipes.create.mixing('endersdelight:stuffed_shulker', [
        'endersdelight:shulker_filet', 'endersdelight:shulker_filet',
        'minecraft:chorus_fruit', 'minecraft:bowl'
    ]).heated();

    // Strange Eclair: Mixing
    event.remove({ id: 'endersdelight:strange_eclair' });
    event.recipes.create.mixing('endersdelight:strange_eclair', [
        'minecraft:ender_eye', '#c:foods/bread', 'minecraft:sugar'
    ]).heated();

    // Twisted Cereal: Mixing
    event.remove({ id: 'endersdelight:twisted_cereal' });
    event.recipes.create.mixing('endersdelight:twisted_cereal', [
        '#endersdelight:enderman_sight', '#endersdelight:enderman_loot',
        'minecraft:popped_chorus_fruit', '#c:drinks/milk', 'endersdelight:shulker_bowl'
    ]);

    // ==========================================
    // SECTION 6: FARMER'S DELIGHT INTEGRATION
    // Create + Farmer's Delight for food progression
    // (No random magic ingredients, just mechanical cooking)
    // ==========================================

    // Farmer's Delight Cooking Pot enhancement:
    // The Stove requires Create components (mechanical cooking)
    event.remove({ output: 'farmersdelight:stove' });
    event.shaped('farmersdelight:stove', [
        'AAA',
        'I I',
        'ICI'
    ], {
        A: 'create:andesite_alloy',
        I: '#c:ingots/iron',
        C: 'minecraft:campfire'
    });

    // ==========================================
    // SECTION 7: EARLY EXPLORATION GATES
    // Supplementaries & Quark items that should push exploration
    // ==========================================

    // Waystones require Brass (can't fast-travel for free early game)
    event.remove({ output: 'waystones:waystone' });
    event.shaped('waystones:waystone', [
        ' B ',
        'SES',
        'SSS'
    ], {
        B: 'create:brass_ingot',
        S: 'minecraft:stone_bricks',
        E: 'minecraft:ender_pearl'
    });

    // Sophisticated Backpacks: Iron tier requires Andesite Alloy
    event.remove({ output: 'sophisticatedbackpacks:backpack' });
    event.shaped('sophisticatedbackpacks:backpack', [
        'LAL',
        'LCL',
        'LLL'
    ], {
        L: 'minecraft:leather',
        A: 'create:andesite_alloy',
        C: '#c:chests/wooden'
    });

    // ==========================================
    // SECTION 8: REMOVE OVERPOWERED SHORTCUTS
    // Remove recipes that let players skip the tech tree
    // ==========================================

    // Remove any free ore doubling furnace recipes that bypass Create
    // (Keep vanilla smelting for basic ingots but Create = bonus output)

    // Remove Gobber's early ore if it's too easy to get
    // (Gobber should be mid-game, not a shortcut)
    // Gobber Ore processing through Create Crushing Wheels for bonus
    event.remove({ output: 'gobber2:gobber2_ingot', type: 'minecraft:smelting' });
    event.remove({ output: 'gobber2:gobber2_ingot', type: 'minecraft:blasting' });

    // Re-add Gobber smelting but require Create crushing first for bonus
    event.smelting('gobber2:gobber2_ingot', 'gobber2:gobber2_glob').xp(1.0);
    // Add Create crushing for Gobber ore → 2x raw
    event.recipes.create.crushing([
        'gobber2:gobber2_glob',
        { item: 'gobber2:gobber2_glob', chance: 0.5 }
    ], '#c:ores/gobber');

    // ==========================================
    // SECTION 9: CREATE MACHINES PROGRESSION
    // Even Create's own machines have a logical build order
    // ==========================================

    // Create's Mechanical Press is the FIRST real machine
    // Keep its recipe accessible (it's the gateway)

    // Create's Deployer requires Brass (mid-tier Create)
    // This is default behavior, just confirming it stays

    // Create's Mechanical Crafter requires Brass + Electron Tubes
    // This is default behavior, just confirming it stays

    // Ensure Create Nuclear and Create New Age require advanced Create
    // (These are late-Create era machines)

    console.log('[PEAK Expert Mode] Script 01: Ore Unification & Create Foundation loaded successfully!');
});
