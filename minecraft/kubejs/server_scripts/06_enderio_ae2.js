// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 06
// ENDER IO + APPLIED ENERGISTICS 2
// (Era 5-5.5: Convergence of Tech & Magic â†’ Digital)
// ==========================================
// Ender IO is where technology and magic MERGE.
// Its machines use soul-based technology (Soularium
// from Malum's spirits) and ender-magic (Pulsating
// Crystals from Ars Nouveau Source).
//
// AE2 sits ABOVE Ender IO. Its digital storage and
// auto-crafting represent the ultimate automation.
// You need Ender IO's conduits and Mekanism's circuits
// before touching AE2.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: ENDER IO CORE MACHINES
    // These require Mekanism circuits + Malum soul materials
    // (Both handled in previous scripts as prerequisites)
    // ==========================================

    // --- DARK STEEL INGOT ---
    // The backbone of Ender IO. Made via Create superheated
    // mixing: Iron + Coal + Obsidian + dark magical energy
    event.remove({ output: 'enderio:dark_steel_ingot' });
    event.recipes.create.mixing(
        'enderio:dark_steel_ingot',
        [
            '#c:ingots/iron',
            'minecraft:obsidian',
            'minecraft:coal',
            'malum:hex_ash'
        ]
    ).superheated();

    // --- CONDUCTIVE ALLOY ---
    // Needs Create + IE components (electricity theme)
    event.remove({ output: 'enderio:conductive_alloy_ingot' });
    event.recipes.create.mixing(
        'enderio:conductive_alloy_ingot',
        [
            '#c:ingots/iron',
            '#c:ingots/copper',
            'minecraft:redstone',
            'create:electron_tube'
        ]
    ).heated();

    // --- ENERGETIC ALLOY ---
    // High-energy metal. Needs Mekanism enrichment.
    event.remove({ output: 'enderio:energetic_alloy_ingot' });
    event.recipes.create.mixing(
        'enderio:energetic_alloy_ingot',
        [
            '#c:ingots/gold',
            'minecraft:glowstone_dust',
            'minecraft:redstone',
            'mekanism:alloy_infused'
        ]
    ).superheated();

    // --- VIBRANT ALLOY ---
    // The pinnacle Ender IO alloy. Needs Ender + energy.
    event.remove({ output: 'enderio:vibrant_alloy_ingot' });
    event.recipes.create.mixing(
        'enderio:vibrant_alloy_ingot',
        [
            'enderio:energetic_alloy_ingot',
            'minecraft:ender_pearl',
            'ars_nouveau:source_gem',
            'mekanism:alloy_reinforced'
        ]
    ).superheated();

    // --- MACHINE CHASSIS (Standard) ---
    // The workhorse. Needs Mekanism alloys + dark steel.
    event.remove({ output: 'enderio:void_chassis' });
    event.shaped('enderio:void_chassis', [
        'DAD',
        'ACA',
        'DAD'
    ], {
        D: 'enderio:dark_steel_ingot',
        A: 'mekanism:alloy_infused',
        C: 'minecraft:iron_block'
    });

    // --- INDUSTRIAL MACHINE CHASSIS ---
    // Top-tier. Needs elite circuits + soul tech.
    event.remove({ output: 'enderio:ensouled_chassis' });
    event.shaped('enderio:ensouled_chassis', [
        'SES',
        'ECE',
        'SES'
    ], {
        S: 'enderio:soularium_ingot',
        E: 'mekanism:elite_control_circuit',
        C: 'enderio:void_chassis'
    });

    // --- ALLOY SMELTER (Ender IO's main processing machine) ---
    event.remove({ output: 'enderio:alloy_smelter' });
    event.shaped('enderio:alloy_smelter', [
        'DSD',
        'FCF',
        'DPD'
    ], {
        D: 'enderio:dark_steel_ingot',
        S: 'enderio:soularium_ingot',
        F: 'minecraft:furnace',
        C: 'enderio:void_chassis',
        P: 'mekanism:basic_control_circuit'
    });

    // --- SAG MILL (Ender IO's grinder â€” upgrade from IE/Create) ---
    event.remove({ output: 'enderio:sag_mill' });
    event.shaped('enderio:sag_mill', [
        'DFD',
        'MCM',
        'DPD'
    ], {
        D: 'enderio:dark_steel_ingot',
        F: 'minecraft:flint',
        M: 'create:millstone',
        C: 'enderio:void_chassis',
        P: 'mekanism:basic_control_circuit'
    });

    // --- CONDUIT BINDER (Essential for all conduits) ---
    // Conduits are Ender IO's killer feature. Gate them properly.
    event.remove({ output: 'enderio:conduit_binder' });
    event.recipes.create.mixing(
        '8x enderio:conduit_binder',
        [
            'minecraft:clay_ball',
            'minecraft:gravel',
            'minecraft:sand',
            'pneumaticcraft:plastic'
        ]
    ).heated();

    /*
    // --- CONDUITS (The ultimate item/fluid/energy transfer) ---
    // Energy Conduit needs IE wire concepts + Ender IO alloys
    event.remove({ output: 'enderio:energy_conduit' });
    event.shaped('8x enderio:energy_conduit', [
        'BBB',
        'EAE',
        'BBB'
    ], {
        B: 'enderio:conduit_binder',
        E: 'enderio:conductive_alloy_ingot',
        A: 'immersiveengineering:wirecoil_copper'
    });

    // Item Conduit needs PneumaticCraft tubes (item transport)
    event.remove({ output: 'enderio:item_conduit' });
    event.shaped('8x enderio:item_conduit', [
        'BBB',
        'PAP',
        'BBB'
    ], {
        B: 'enderio:conduit_binder',
        P: 'pneumaticcraft:pressure_tube',
        A: 'enderio:pulsating_crystal'
    });

    // Fluid Conduit needs Create pipes + binder
    event.remove({ output: 'enderio:fluid_conduit' });
    event.shaped('8x enderio:fluid_conduit', [
        'BBB',
        'GAG',
        'BBB'
    ], {
        B: 'enderio:conduit_binder',
        G: 'enderio:conductive_alloy_ingot',
        A: 'create:fluid_pipe'
    });

    // Ender Fluid Conduit (advanced) needs Vibrant Alloy
    event.remove({ output: 'enderio:ender_fluid_conduit' });
    event.shaped('8x enderio:ender_fluid_conduit', [
        'BBB',
        'VAV',
        'BBB'
    ], {
        B: 'enderio:conduit_binder',
        V: 'enderio:vibrant_alloy_ingot',
        A: 'enderio:fluid_conduit'
    });
    */

    // ==========================================
    // SECTION 2: APPLIED ENERGISTICS 2
    // Digital storage. Sits ABOVE Ender IO.
    // Requires Ender IO chassis + Mekanism circuits.
    // ==========================================

    // --- INSCRIBER (AE2's core crafting machine) ---
    // Needs Ender IO machine chassis + Create precision
    event.remove({ output: 'ae2:inscriber' });
    event.shaped('ae2:inscriber', [
        'IPI',
        'DCE',
        'IPI'
    ], {
        I: '#c:ingots/iron',
        P: 'create:precision_mechanism',
        D: 'enderio:dark_steel_ingot',
        C: 'enderio:void_chassis',
        E: 'create:electron_tube'
    });

    // --- ME CONTROLLER (AE2's brain) ---
    // The most important AE2 block. Needs EVERYTHING.
    event.remove({ output: 'ae2:controller' });
    event.shaped('ae2:controller', [
        'ECE',
        'CMC',
        'ECE'
    ], {
        E: 'ae2:engineering_processor',
        C: 'ae2:fluix_crystal',
        M: 'enderio:ensouled_chassis'
    });

    // --- ME DRIVE (Digital storage housing) ---
    event.remove({ output: 'ae2:drive' });
    event.shaped('ae2:drive', [
        'EPE',
        'D D',
        'EIE'
    ], {
        E: 'ae2:engineering_processor',
        P: 'enderio:pulsating_crystal',
        D: 'enderio:dark_steel_ingot',
        I: '#c:ingots/iron'
    });

    // --- ME CHEST (Simple AE2 storage) ---
    event.remove({ output: 'ae2:chest' });
    event.shaped('ae2:chest', [
        'GCG',
        'D D',
        'IMI'
    ], {
        G: '#c:glass_blocks',
        C: 'ae2:calculation_processor',
        D: 'enderio:dark_steel_ingot',
        I: '#c:ingots/iron',
        M: 'mekanism:advanced_control_circuit'
    });

    // --- MOLECULAR ASSEMBLER (Auto-crafting machine) ---
    // The pinnacle of automation. Needs everything.
    event.remove({ output: 'ae2:molecular_assembler' });
    event.shaped('ae2:molecular_assembler', [
        'ICI',
        'PAP',
        'IGI'
    ], {
        I: '#c:ingots/iron',
        C: 'ae2:calculation_processor',
        P: 'enderio:pulsating_crystal',
        A: 'create:deployer',
        G: 'enderio:void_chassis'
    });

    // --- CRAFTING UNIT ---
    event.remove({ output: 'ae2:crafting_unit' });
    event.shaped('ae2:crafting_unit', [
        'ILI',
        'CMC',
        'IEI'
    ], {
        I: '#c:ingots/iron',
        L: 'ae2:logic_processor',
        C: 'ae2:calculation_processor',
        M: 'mekanism:advanced_control_circuit',
        E: 'ae2:engineering_processor'
    });

    // --- FLUIX CRYSTAL (AE2 core material) ---
    // Made via Create mixing (mechanical crystal growth)
    event.remove({ output: 'ae2:fluix_crystal' });
    event.recipes.create.mixing(
        '2x ae2:fluix_crystal',
        [
            'ae2:certus_quartz_crystal',
            'minecraft:redstone',
            'minecraft:quartz',
            'ars_nouveau:source_gem'
        ]
    ).heated();

    // --- QUARTZ GLASS ---
    // Needs AE2 quartz dust processed through Create
    event.remove({ output: 'ae2:quartz_glass' });
    event.recipes.create.mixing(
        '4x ae2:quartz_glass',
        [
            '#c:glass_blocks',
            '#c:glass_blocks',
            'ae2:certus_quartz_dust',
            'ae2:certus_quartz_dust'
        ]
    ).heated();

    // --- ME CABLE (Network infrastructure) ---
    // Requires Ender IO conduit concepts + AE2 materials
    event.remove({ output: 'ae2:fluix_glass_cable' });
    event.shaped('6x ae2:fluix_glass_cable', [
        ' G ',
        'FEF',
        ' G '
    ], {
        G: 'ae2:quartz_glass',
        F: 'ae2:fluix_crystal',
        E: 'enderio:conductive_alloy_ingot'
    });

    console.log('[PEAK Expert Mode] Script 06: Ender IO + AE2 loaded!');
});
