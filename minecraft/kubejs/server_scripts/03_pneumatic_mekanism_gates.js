// ==========================================
// PEAK EXPERT MODE Ã¢â‚¬â€ SCRIPT 03
// PNEUMATICCRAFT & MEKANISM GATES
// (Era 3-4: Pressure Systems Ã¢â€ â€™ Nuclear Science)
// ==========================================
// PneumaticCraft bridges IE and Mekanism.
// Its PLASTIC is the single most important gate item.
// Mekanism cannot be accessed without PneumaticCraft's plastic.
// The Undergarden provides essential materials for pressure systems.
// Alex's Caves provides materials for advanced Mekanism circuits.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: PNEUMATICCRAFT Ã¢â‚¬â€ THE PRESSURE ERA
    // PneumaticCraft machines need IE + Create components
    // ==========================================

    // Air Compressor (PneumaticCraft's most basic machine)
    // Requires IE components + Create
    event.remove({ output: 'pneumaticcraft:air_compressor' });
    event.shaped('pneumaticcraft:air_compressor', [
        'IPI',
        'IGI',
        'SCS'
    ], {
        I: '#c:ingots/iron',
        P: 'create:mechanical_piston',
        G: 'immersiveengineering:component_iron',
        S: '#c:ingots/steel',
        C: 'create:cogwheel'
    });

    // Advanced Air Compressor needs IE Heavy Engineering
    event.remove({ output: 'pneumaticcraft:advanced_air_compressor' });
    event.shaped('pneumaticcraft:advanced_air_compressor', [
        'SPS',
        'HCH',
        'SES'
    ], {
        S: '#c:ingots/steel',
        P: 'create:precision_mechanism',
        H: 'immersiveengineering:heavy_engineering',
        C: 'pneumaticcraft:air_compressor',
        E: 'create:electron_tube'
    });

    // Pressure Tubes Ã¢â‚¬â€ THE BACKBONE of PneumaticCraft
    // Require Cloggrum from The Undergarden!
    // (Cloggrum is a corrosion-resistant metal = perfect for pressure tubes)
    event.remove({ output: 'pneumaticcraft:pressure_tube' });
    event.shaped('4x pneumaticcraft:pressure_tube', [
        'CIC',
        'I I',
        'CIC'
    ], {
        C: 'undergarden:cloggrum_ingot',
        I: '#c:ingots/iron'
    });

    // Advanced Pressure Tubes need Steel + Cloggrum
    event.remove({ output: 'pneumaticcraft:advanced_pressure_tube' });
    event.shaped('4x pneumaticcraft:advanced_pressure_tube', [
        'CSC',
        'S S',
        'CSC'
    ], {
        C: 'undergarden:cloggrum_ingot',
        S: '#c:ingots/steel'
    });

    // Pressure Chamber Wall needs Undergarden materials + IE
    event.remove({ output: 'pneumaticcraft:pressure_chamber_wall' });
    event.shaped('4x pneumaticcraft:pressure_chamber_wall', [
        'SCS',
        'CIC',
        'SCS'
    ], {
        S: '#c:ingots/steel',
        C: 'undergarden:cloggrum_ingot',
        I: 'immersiveengineering:component_steel'
    });

    // Pressure Chamber Glass
    event.remove({ output: 'pneumaticcraft:pressure_chamber_glass' });
    event.shaped('4x pneumaticcraft:pressure_chamber_glass', [
        'SGS',
        'GCG',
        'SGS'
    ], {
        S: '#c:ingots/steel',
        G: '#c:glass_blocks',
        C: 'undergarden:cloggrum_ingot'
    });

    // Pressure Chamber Valve
    event.remove({ output: 'pneumaticcraft:pressure_chamber_valve' });
    event.shaped('pneumaticcraft:pressure_chamber_valve', [
        'STS',
        'TCT',
        'STS'
    ], {
        S: '#c:ingots/steel',
        T: 'pneumaticcraft:pressure_tube',
        C: 'undergarden:cloggrum_ingot'
    });

    // Refinery Ã¢â‚¬â€ PneumaticCraft's oil processing
    // Requires TFMG industrial components
    event.remove({ output: 'pneumaticcraft:refinery' });
    event.shaped('pneumaticcraft:refinery', [
        'SPS',
        'HCH',
        'SBS'
    ], {
        S: '#c:ingots/steel',
        P: 'pneumaticcraft:pressure_tube',
        H: 'tfmg:heavy_plate',
        C: 'immersiveengineering:component_steel',
        B: 'create:brass_casing'
    });

    // Thermopneumatic Processing Plant
    // The machine that makes PLASTIC (the ultimate gate item)
    event.remove({ output: 'pneumaticcraft:thermopneumatic_processing_plant' });
    event.shaped('pneumaticcraft:thermopneumatic_processing_plant', [
        'SPS',
        'HBH',
        'SES'
    ], {
        S: '#c:ingots/steel',
        P: 'pneumaticcraft:pressure_tube',
        H: 'immersiveengineering:heavy_engineering',
        B: 'minecraft:blast_furnace',
        E: 'create:precision_mechanism'
    });

    // ==========================================
    // SECTION 2: ASSEMBLY SYSTEM
    // PneumaticCraft's assembly line = precision crafting
    // Required for Mekanism's circuits
    // ==========================================

    // Assembly Platform
    event.remove({ output: 'pneumaticcraft:assembly_platform' });
    event.shaped('pneumaticcraft:assembly_platform', [
        'PMP',
        'SCS',
        'SSS'
    ], {
        P: 'pneumaticcraft:pressure_tube',
        M: 'create:precision_mechanism',
        S: '#c:ingots/steel',
        C: 'immersiveengineering:component_steel'
    });

    // Assembly Drill
    event.remove({ output: 'pneumaticcraft:assembly_drill' });
    event.shaped('pneumaticcraft:assembly_drill', [
        ' D ',
        'SPS',
        'SCS'
    ], {
        D: '#c:gems/diamond',
        S: '#c:ingots/steel',
        P: 'pneumaticcraft:pressure_tube',
        C: 'create:precision_mechanism'
    });

    // Assembly Laser
    event.remove({ output: 'pneumaticcraft:assembly_laser' });
    event.shaped('pneumaticcraft:assembly_laser', [
        ' E ',
        'SPS',
        'SCS'
    ], {
        E: 'create:electron_tube',
        S: '#c:ingots/steel',
        P: 'pneumaticcraft:pressure_tube',
        C: 'create:precision_mechanism'
    });

    // Assembly Controller
    event.remove({ output: 'pneumaticcraft:assembly_controller' });
    event.shaped('pneumaticcraft:assembly_controller', [
        'EPE',
        'SPS',
        'SCS'
    ], {
        E: 'create:electron_tube',
        S: '#c:ingots/steel',
        P: 'pneumaticcraft:pressure_tube',
        C: 'immersiveengineering:rs_engineering'
    });

    // ==========================================
    // SECTION 3: MEKANISM Ã¢â‚¬â€ THE NUCLEAR ERA
    // Every Mekanism machine needs PneumaticCraft's plastic
    // and IE/Create components
    // ==========================================

    // --- BASIC CONTROL CIRCUIT (Mekanism's fundamental component) ---
    // Now requires PLASTIC from PneumaticCraft!
    event.remove({ output: 'mekanism:basic_control_circuit' });
    event.shaped('mekanism:basic_control_circuit', [
        'PPP',
        'ROR',
        'PPP'
    ], {
        P: 'pneumaticcraft:plastic',
        R: 'minecraft:redstone',
        O: 'mekanism:ingot_osmium'
    });

    // Metallurgic Infuser (Mekanism's gate machine)
    // Requires IE Treated Wood + PneumaticCraft components
    event.remove({ output: 'mekanism:metallurgic_infuser' });
    event.shaped('mekanism:metallurgic_infuser', [
        'IPI',
        'TCS',
        'IPI'
    ], {
        I: '#c:ingots/iron',
        P: 'pneumaticcraft:plastic',
        T: 'immersiveengineering:treated_wood_horizontal',
        C: 'mekanism:steel_casing',
        S: 'immersiveengineering:component_steel'
    });

    // Enrichment Chamber
    event.remove({ output: 'mekanism:enrichment_chamber' });
    event.shaped('mekanism:enrichment_chamber', [
        'APA',
        'RCR',
        'APA'
    ], {
        A: 'mekanism:alloy_infused',
        P: 'pneumaticcraft:plastic',
        R: 'minecraft:redstone',
        C: 'mekanism:steel_casing'
    });

    // Crusher (Mekanism's ore processing)
    event.remove({ output: 'mekanism:crusher' });
    event.shaped('mekanism:crusher', [
        'APA',
        'LCL',
        'APA'
    ], {
        A: 'mekanism:alloy_infused',
        P: 'pneumaticcraft:plastic',
        L: '#c:gems/lapis',
        C: 'mekanism:steel_casing'
    });

    // Energized Smelter
    event.remove({ output: 'mekanism:energized_smelter' });
    event.shaped('mekanism:energized_smelter', [
        'APA',
        'GCG',
        'APA'
    ], {
        A: 'mekanism:alloy_infused',
        P: 'pneumaticcraft:plastic',
        G: '#c:glass_blocks',
        C: 'mekanism:steel_casing'
    });

    // Chemical Oxidizer (advanced Mekanism)
    event.remove({ output: 'mekanism:chemical_oxidizer' });
    event.shaped('mekanism:chemical_oxidizer', [
        'APA',
        'HCH',
        'APA'
    ], {
        A: 'mekanism:alloy_reinforced',
        P: 'pneumaticcraft:plastic',
        H: 'immersiveengineering:heavy_engineering',
        C: 'mekanism:steel_casing'
    });

    // --- ADVANCED CONTROL CIRCUIT ---
    // Requires Alex's Caves Scarlet Neodymium!
    event.remove({ output: 'mekanism:advanced_control_circuit' });
    event.shaped('mekanism:advanced_control_circuit', [
        'PPP',
        'NAN',
        'PPP'
    ], {
        P: 'pneumaticcraft:plastic',
        N: 'alexscaves:scarlet_neodymium_ingot',
        A: 'mekanism:alloy_infused'
    });

    // --- ELITE CONTROL CIRCUIT ---
    // Requires Ender IO components (forward gate to Era 5)
    event.remove({ output: 'mekanism:elite_control_circuit' });
    event.shaped('mekanism:elite_control_circuit', [
        'PPP',
        'EAE',
        'PPP'
    ], {
        P: 'pneumaticcraft:plastic',
        E: 'minecraft:ender_pearl',
        A: 'mekanism:alloy_reinforced'
    });

    // --- ULTIMATE CONTROL CIRCUIT ---
    // Recipe uses current era materials
    event.remove({ output: 'mekanism:ultimate_control_circuit' });
    event.shaped('mekanism:ultimate_control_circuit', [
        'DPD',
        'EAE',
        'DPD'
    ], {
        D: '#c:gems/diamond',
        P: 'pneumaticcraft:plastic',
        E: 'mekanism:elite_control_circuit',
        A: 'mekanism:alloy_atomic'
    });

    // ==========================================
    // SECTION 4: UNDERGARDEN INTEGRATION
    // Cloggrum = pressure-resistant metal
    // Froststeel = refrigeration component
    // ==========================================

    // Froststeel is used in PneumaticCraft's refrigeration
    // Add Create crushing for Undergarden ores for bonus output




    // PneumaticCraft Heat Sink uses Froststeel
    // (Froststeel = cold metal = perfect for cooling)
    event.remove({ output: 'pneumaticcraft:heat_sink' });
    event.shaped('pneumaticcraft:heat_sink', [
        'FFF',
        'IPI',
        'FFF'
    ], {
        F: 'undergarden:froststeel_ingot',
        I: '#c:ingots/iron',
        P: 'pneumaticcraft:pressure_tube'
    });

    // ==========================================
    // SECTION 5: ALEX'S CAVES INTEGRATION
    // Neodymium = advanced circuits
    // Caves materials = specialized tech components
    // ==========================================

    // Alex's Caves Neodymium processing via Create





    console.log('[PEAK Expert Mode] Script 03: PneumaticCraft & Mekanism Gates loaded successfully!');
});



