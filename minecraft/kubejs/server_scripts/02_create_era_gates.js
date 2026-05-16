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
    event.remove({ output: 'tfmg:distillation_tower' });
    event.shaped('tfmg:distillation_tower', [
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
        { item: 'allthemodium:raw_allthemodium', chance: 0.35 },
        { item: 'minecraft:experience_nugget', chance: 0.75 }
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

    // Iron Backpack Upgrade needs Andesite Alloy
    event.remove({ output: 'sophisticatedbackpacks:iron_upgrade' });
    event.shaped('sophisticatedbackpacks:iron_upgrade', [
        'IAI',
        'IUI',
        'III'
    ], {
        I: '#c:ingots/iron',
        A: 'create:andesite_alloy',
        U: 'sophisticatedbackpacks:upgrade_base'
    });

    // Gold Backpack Upgrade needs Brass (Create's mid-tier)
    event.remove({ output: 'sophisticatedbackpacks:gold_upgrade' });
    event.shaped('sophisticatedbackpacks:gold_upgrade', [
        'GBG',
        'GUG',
        'GGG'
    ], {
        G: '#c:ingots/gold',
        B: 'create:brass_ingot',
        U: 'sophisticatedbackpacks:iron_upgrade'
    });

    // Diamond Backpack Upgrade needs Precision Mechanism
    event.remove({ output: 'sophisticatedbackpacks:diamond_upgrade' });
    event.shaped('sophisticatedbackpacks:diamond_upgrade', [
        'DPD',
        'DUD',
        'DDD'
    ], {
        D: '#c:gems/diamond',
        P: 'create:precision_mechanism',
        U: 'sophisticatedbackpacks:gold_upgrade'
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
