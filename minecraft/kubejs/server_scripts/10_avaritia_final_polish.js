// ==========================================
// PEAK EXPERT MODE — SCRIPT 10
// RE-AVARITIA + CUSTOM DROP RECIPES + FINAL POLISH
// ==========================================
// This is the FINAL script.
// The Infinity Catalyst is THE ultimate achievement.
// It requires materials from EVERY era, dimension,
// magic system, and boss in the entire modpack.
//
// Custom boss drop items are woven into recipes
// throughout the tech tree, giving bosses PURPOSE.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: CUSTOM BOSS DROP RECIPES
    // Each custom drop has a specific use in the tech tree.
    // ALL of these are crafted on the SCULK CRAFTING TABLE
    // (avaritia:shaped_table, tier: 1) because they are
    // endgame recipes. They also work in Mechanical Crafters!
    // ==========================================

    // --- FROZEN HEART CORE (Frostmaw) ---
    // Used in PneumaticCraft Advanced Air Compressor upgrade
    event.remove({ output: 'pneumaticcraft:advanced_air_compressor' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "SPS",
            "FCF",
            "SES"
        ],
        key: {
            S: { tag: 'c:ingots/steel' },
            P: { item: 'create:precision_mechanism' },
            F: { item: 'kubejs:frozen_heart_core' },
            C: { item: 'pneumaticcraft:air_compressor' },
            E: { item: 'immersiveengineering:heavy_engineering' }
        },
        result: { id: 'pneumaticcraft:advanced_air_compressor', count: 1 },
        tier: 1
    });

    // --- VOID RESONATOR (Ender Guardian / Void Worm) ---
    // Used in AE2 ME Controller (dimensional void tech)
    event.remove({ output: 'ae2:controller' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "ECE",
            "VMV",
            "ECE"
        ],
        key: {
            E: { item: 'ae2:engineering_processor' },
            C: { item: 'ae2:fluix_crystal' },
            V: { item: 'kubejs:void_resonator' },
            M: { item: 'enderio:ensouled_chassis' }
        },
        result: { id: 'ae2:controller', count: 1 },
        tier: 1
    });

    // --- PRIMORDIAL CORE (Ancient Remnant) ---
    // Used in Draconic Evolution Wyvern Core
    event.remove({ output: 'draconicevolution:wyvern_core' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "SDS",
            "PCE",
            "SDS"
        ],
        key: {
            S: { item: 'deeperdarker:soul_crystal' },
            D: { item: 'draconicevolution:draconium_ingot' },
            P: { item: 'kubejs:primordial_core' },
            C: { item: 'enderio:ensouled_chassis' },
            E: { item: 'mekanism:elite_control_circuit' }
        },
        result: { id: 'draconicevolution:wyvern_core', count: 1 },
        tier: 1
    });

    // --- SCULK HEART (Warden) ---
    // Used in Draconic Wyvern Energy Core
    event.remove({ output: 'draconicevolution:wyvern_energy_core' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "DSD",
            "WNW",
            "DSD"
        ],
        key: {
            D: { item: 'draconicevolution:draconium_ingot' },
            S: { item: 'kubejs:sculk_heart' },
            W: { item: 'deeperdarker:reinforced_echo_shard' },
            N: { item: 'minecraft:nether_star' }
        },
        result: { id: 'draconicevolution:wyvern_energy_core', count: 1 },
        tier: 1
    });

    // --- ABYSSAL CATALYST (Leviathan) ---
    // Used in Ender IO Industrial Machine Chassis
    event.remove({ output: 'enderio:ensouled_chassis' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "SES",
            "ACA",
            "SES"
        ],
        key: {
            S: { item: 'enderio:soularium_ingot' },
            E: { item: 'mekanism:elite_control_circuit' },
            A: { item: 'kubejs:abyssal_catalyst' },
            C: { item: 'enderio:void_chassis' }
        },
        result: { id: 'enderio:ensouled_chassis', count: 1 },
        tier: 1
    });

    // --- NETHERIC CORE (Netherite Monstrosity) ---
    // Used in Mekanism SPS Casing
    event.remove({ output: 'mekanism:sps_casing' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "ASA",
            "SNS",
            "ASA"
        ],
        key: {
            A: { item: 'mekanism:alloy_reinforced' },
            S: { tag: 'c:ingots/steel' },
            N: { item: 'kubejs:netheric_core' }
        },
        result: { id: 'mekanism:sps_casing', count: 1 },
        tier: 1
    });

    // --- PRIMORDIAL DRAGON BLOOD (Stage 5 IAF Dragons) ---
    // Used in Draconic Evolution Awakened Draconium
    // (This stays as Create Mixing — superheated process)
    event.remove({ output: 'draconicevolution:awakened_draconium_ingot' });
    event.recipes.create.mixing(
        'draconicevolution:awakened_draconium_ingot',
        [
            'draconicevolution:draconium_ingot',
            'draconicevolution:draconium_ingot',
            'kubejs:primordial_dragon_blood',
            'minecraft:nether_star'
        ]
    ).superheated();

    // --- LICH PHYLACTERY (Twilight Forest Lich) ---
    // Used in Iron's Spellbooks Legendary Ink
    event.remove({ output: 'irons_spellbooks:legendary_ink' });
    event.custom({
        type: 'avaritia:shapeless_table',
        ingredients: [
            { item: 'irons_spellbooks:epic_ink' },
            { item: 'kubejs:lich_phylactery' },
            { item: 'ars_nouveau:wilden_spike' },
            { item: 'minecraft:nether_star' }
        ],
        result: { id: 'irons_spellbooks:legendary_ink', count: 1 },
        tier: 1
    });

    // ==========================================
    // SECTION 2: CULINARY SINGULARITY
    // The ultimate mastery of gastronomy.
    // ==========================================

    event.recipes.create.mechanical_crafting('kubejs:culinary_singularity', [
        'THR',
        'CKP',
        'EAL'
    ], {
        T: 'twilightdelight:meef_wellington_block',   // Twilight Forest feast
        H: 'mynethersdelight:roast_stuffed_hoglin',   // Nether feast (COOKED)
        R: 'oceansdelight:stuffed_squid',             // Ocean feast
        C: 'twilightdelight:lily_chicken_block',      // Twilight chicken feast
        K: 'farmersdelight:honey_glazed_ham_block',   // Overworld feast 2
        P: 'farmersdelight:stuffed_pumpkin_block',    // Overworld feast 3
        E: 'artifacts:eternal_steak',                 // Infinite food mastery
        A: 'avaritia:endless_cake',                   // Avaritia endgame
        L: 'lendersdelight:honey_glazed_horn'         // Cataclysm feast
    });

    // ==========================================
    // SECTION 3: CHAOS ESSENCE PROCESSING
    // Chaos Shards from the Chaos Guardian can be
    // processed into Chaos Essence via Create
    // ==========================================

    event.recipes.create.crushing([
        '2x kubejs:chaos_essence'
    ], 'draconicevolution:chaos_shard');

    // ==========================================
    // SECTION 3: AVARITIA — THE INFINITY CATALYST
    // Uses the NATIVE avaritia:infinity_catalyst recipe type.
    // This is a special recipe type that shows in the
    // Catalyst JEI page and requires ALL singularities
    // PLUS our custom boss drops.
    // ==========================================

    // Remove the default Infinity Catalyst recipes
    event.remove({ output: 'avaritia:infinity_catalyst' });
    event.remove({ id: 'avaritia:infinity_catalyst' });
    event.remove({ id: 'avaritia:infinity_catalyst_eternal' });

    // THE INFINITY CATALYST — Expert Mode Edition
    // Uses the native avaritia:infinity_catalyst recipe type
    // Now requires boss drops + avaritia materials + cross-mod endgame items
    event.custom({
        type: 'avaritia:infinity_catalyst',
        ingredients: [
            { item: 'avaritia:crystal_matrix_ingot' },   // Avaritia core material
            { item: 'avaritia:neutron_ingot' },           // Avaritia neutronium
            { item: 'avaritia:endest_pearl' },            // Avaritia endgame pearl
            { item: 'kubejs:heart_of_the_inferno' },      // Boss: Ignis (Cataclysm)
            { item: 'kubejs:void_resonator' },            // Boss: Ender Guardian
            { item: 'kubejs:primordial_core' },           // Boss: Ancient Remnant
            { item: 'kubejs:chaos_essence' },             // Draconic Evolution Chaos Guardian
            { item: 'kubejs:sculk_heart' },               // Boss: The Warden
            { item: 'kubejs:primordial_dragon_blood' },   // Boss: Stage 5 Dragons (Ice & Fire)
            { item: 'iceandfire:dragonsteel_fire_ingot' },// Ice and Fire dragon forge
            { item: 'mekanism:pellet_antimatter' },       // Mekanism nuclear peak
            { item: 'allthemodium:unobtainium_ingot' },   // AllTheModium endgame
            { item: 'ars_nouveau:source_gem_block' },     // Ars Nouveau magic peak
            { item: 'draconicevolution:awakened_draconium_ingot' }, // Draconic Evo
            { item: 'minecraft:nether_star' },             // Wither boss
            { item: 'kubejs:culinary_singularity' }        // Mastery of all foods
        ]
    });

    // ==========================================
    // SECTION 4: INFINITY INGOT — 9x9 EXTREME CRAFTING TABLE
    // The absolute FINAL material in the entire game.
    // Must be crafted on the Extreme Crafting Table.
    // Uses the native avaritia:shaped_table recipe type.
    // ==========================================

    // Remove the default Infinity Ingot recipe
    event.remove({ output: 'avaritia:infinity_ingot' });
    event.remove({ id: 'avaritia:infinity_ingot' });

    // THE INFINITY INGOT — Expert Mode Edition (9x9 Extreme Table)
    // Pattern layout:
    //   N = Neutron Ingot (border)
    //   C = Crystal Matrix Ingot (inner frame)
    //   X = Infinity Catalyst (center cross)
    //   D = Awakened Draconium (accents)
    //   H = Heart of the Inferno (corners)
    //   V = Void Resonator (cardinal points)
    //   E = Chaos Essence (inner ring)
    //   A = Antimatter Pellet (mid-ring)
    //   U = Unobtainium (true center)
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "NNNNNNNNN",
            "NHCCCCCHN",
            "NCADXDACN",
            "NCDEVDECN",
            "NCXVUVXCN",
            "NCDEVDECN",
            "NCADXDACN",
            "NHCCCCCHN",
            "NNNNNNNNN"
        ],
        key: {
            N: { item: 'avaritia:neutron_ingot' },
            C: { item: 'avaritia:crystal_matrix_ingot' },
            X: { item: 'avaritia:infinity_catalyst' },
            D: { item: 'draconicevolution:awakened_draconium_ingot' },
            H: { item: 'kubejs:heart_of_the_inferno' },
            V: { item: 'kubejs:void_resonator' },
            E: { item: 'kubejs:chaos_essence' },
            A: { item: 'mekanism:pellet_antimatter' },
            U: { item: 'allthemodium:unobtainium_ingot' }
        },
        result: {
            id: 'avaritia:infinity_ingot',
            count: 1
        },
        tier: 4
    });

    // ==========================================
    // SECTION 6: INFINITY FRAGMENT EXCHANGE
    // Infinity Fragments from bosses can be traded up
    // for endgame materials, creating a "boss currency"
    // ==========================================

    // 16 Infinity Fragments → 1 Nether Star
    // (Alternative to Wither farming)
    event.shapeless('minecraft:nether_star', [
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment'
    ]);

    // 4 Infinity Fragments → 1 Netherite Scrap
    event.shapeless('minecraft:netherite_scrap', [
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment'
    ]);

    // 8 Infinity Fragments → 1 Draconium Ingot
    event.shapeless('draconicevolution:draconium_ingot', [
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment',
        'kubejs:infinity_fragment', 'kubejs:infinity_fragment'
    ]);

    // ==========================================
    // SECTION 7: FINAL POLISH — ADDITIONAL GATES
    // Miscellaneous recipes that round out the pack
    // ==========================================

    // --- BEACON requires tech + magic ---
    event.remove({ output: 'minecraft:beacon' });
    event.shaped('minecraft:beacon', [
        'GGG',
        'GSG',
        'OOO'
    ], {
        G: '#c:glass_blocks',
        S: 'minecraft:nether_star',
        O: 'enderio:dark_steel_ingot'
    });

    // --- RESPAWN ANCHOR needs soul tech ---
    event.remove({ output: 'minecraft:respawn_anchor' });
    event.shaped('minecraft:respawn_anchor', [
        'CCC',
        'GSG',
        'CCC'
    ], {
        C: 'minecraft:crying_obsidian',
        G: 'minecraft:glowstone',
        S: 'malum:soul_stained_steel_ingot'
    });

    // --- END CRYSTAL crafting needs magic ---
    event.remove({ output: 'minecraft:end_crystal' });
    event.shaped('minecraft:end_crystal', [
        'GEG',
        'ESE',
        'GTG'
    ], {
        G: '#c:glass_blocks',
        E: 'minecraft:ender_eye',
        S: 'ars_nouveau:source_gem_block',
        T: 'minecraft:ghast_tear'
    });

    // --- CONDUIT (ocean power) needs Undergarden ---
    event.remove({ output: 'minecraft:conduit' });
    event.shaped('minecraft:conduit', [
        'NSN',
        'SHS',
        'NSN'
    ], {
        N: 'minecraft:nautilus_shell',
        S: 'undergarden:froststeel_ingot',
        H: 'minecraft:heart_of_the_sea'
    });

    // --- LODESTONE needs Create brass ---
    event.remove({ output: 'minecraft:lodestone' });
    event.shaped('minecraft:lodestone', [
        'BBB',
        'BNB',
        'BBB'
    ], {
        B: 'create:brass_block',
        N: 'minecraft:netherite_ingot'
    });

    // --- ENDER CHEST needs Ender IO tech ---
    event.remove({ output: 'minecraft:ender_chest' });
    event.shaped('minecraft:ender_chest', [
        'OPO',
        'OEO',
        'OPO'
    ], {
        O: 'minecraft:obsidian',
        P: 'enderio:pulsating_crystal',
        E: 'minecraft:ender_eye'
    });

    // --- ENCHANTING TABLE needs Ars Nouveau ---
    event.remove({ output: 'minecraft:enchanting_table' });
    event.shaped('minecraft:enchanting_table', [
        ' B ',
        'DSD',
        'OOO'
    ], {
        B: 'minecraft:book',
        D: '#c:gems/diamond',
        S: 'ars_nouveau:source_gem',
        O: 'minecraft:obsidian'
    });

    // --- BREWING STAND needs Iron's Spellbooks ---
    event.remove({ output: 'minecraft:brewing_stand' });
    event.shaped('minecraft:brewing_stand', [
        ' R ',
        'BSB',
        'CCC'
    ], {
        R: 'minecraft:blaze_rod',
        B: 'create:brass_ingot',
        S: 'ars_nouveau:source_gem',
        C: '#c:cobblestones'
    });

    // --- ANVIL needs Create ---
    event.remove({ output: 'minecraft:anvil' });
    event.shaped('minecraft:anvil', [
        'III',
        ' A ',
        'IAI'
    ], {
        I: 'minecraft:iron_block',
        A: 'create:andesite_alloy'
    });

    // --- INFINITY FOOD (Artifacts) ---
    // Craftable instead of finding in chests
    event.shaped('artifacts:everlasting_beef', [
        'FFF',
        'FBF',
        'FFF'
    ], {
        F: 'kubejs:infinity_fragment',
        B: 'minecraft:beef'
    });

    event.shaped('artifacts:eternal_steak', [
        'FFF',
        'FSF',
        'FFF'
    ], {
        F: 'kubejs:infinity_fragment',
        S: 'minecraft:cooked_beef'
    });

    event.shaped('relics:infinity_ham', [
        'FFF',
        'FHF',
        'FFF'
    ], {
        F: 'kubejs:infinity_fragment',
        H: 'minecraft:porkchop'
    });

    console.log('[PEAK Expert Mode] Script 10: Re-Avaritia + Final Polish loaded!');
    console.log('==========================================');
    console.log('[PEAK Expert Mode] ALL SCRIPTS LOADED!');
    console.log('The PEAK Expert Mode tech tree is ACTIVE.');
    console.log('Create → TFMG → IE → PneumaticCraft → Mekanism');
    console.log('→ Ender IO → AE2 → Draconic → Re-Avaritia');
    console.log('Magic: Ars Nouveau → Iron Spells → Malum → Vampirism');
    console.log('Dimensions: Twilight Forest, Undergarden, Alex Caves, Deeper Darker');
    console.log('==========================================');
});
