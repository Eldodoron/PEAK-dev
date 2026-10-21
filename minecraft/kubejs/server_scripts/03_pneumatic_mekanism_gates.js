// ==========================================
// PEAK EXPERT MODE — SCRIPT 03
// TFMG & MEKANISM GATES
// (Era 3-4: Heavy Industry → Nuclear Science)
// ==========================================
// TFMG (The Factory Must Grow) bridges Create, IE, and Mekanism.
// Industrial plastic sheets are the primary gate item for advanced electronics.
// Mekanism machines require TFMG plastic sheets and IE components.
// The Undergarden provides corrosion-resistant materials for pressurized piping.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: UNDERGARDEN PRESSURE & HEAT SYSTEMS
    // Cloggrum = corrosion-resistant pressure piping
    // Froststeel = thermal dissipation
    // ==========================================

    // Mekanism Basic Pressurized Tube uses Cloggrum
    event.remove({ output: 'mekanism:basic_pressurized_tube' });
    event.shaped('8x mekanism:basic_pressurized_tube', [
        'CSC',
        'G G',
        'CSC'
    ], {
        C: 'undergarden:cloggrum_ingot',
        S: '#c:ingots/steel',
        G: '#c:glass_blocks'
    });

    // Immersive Engineering Radiator uses Froststeel for thermal dissipation
    event.remove({ output: 'immersiveengineering:radiator' });
    event.shaped('4x immersiveengineering:radiator', [
        'FFF',
        'ICI',
        'FFF'
    ], {
        F: 'undergarden:froststeel_ingot',
        I: '#c:ingots/steel',
        C: 'immersiveengineering:component_steel'
    });

    // ==========================================
    // SECTION 2: MEKANISM — THE NUCLEAR ERA
    // Every Mekanism machine needs TFMG's plastic sheets
    // and IE/Create components
    // ==========================================

    // Metallurgic Infuser (Mekanism's gate machine)
    // Requires IE Treated Wood + TFMG Plastic Sheet
    event.remove({ output: 'mekanism:metallurgic_infuser' });
    event.shaped('mekanism:metallurgic_infuser', [
        'IPI',
        'TCS',
        'IPI'
    ], {
        I: '#c:ingots/iron',
        P: '#c:plates/plastic',
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
        P: '#c:plates/plastic',
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
        P: '#c:plates/plastic',
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
        P: '#c:plates/plastic',
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
        P: '#c:plates/plastic',
        H: 'immersiveengineering:heavy_engineering',
        C: 'mekanism:steel_casing'
    });

    console.log('[PEAK Expert Mode] Script 03: TFMG & Mekanism Gates loaded successfully!');
});
