// ==========================================
// PEAK EXPERT MODE — SCRIPT 07
// DRACONIC EVOLUTION + ICE & FIRE + ALLTHEMODIUM
// (Era 6-7: The True Endgame)
// ==========================================
// Draconic Evolution has 3 tiers:
//   WYVERN  → Requires Deeper Darker + Mekanism + Ender IO
//   DRACONIC → Requires Dragonsteel + AllTheModium + Vampirism
//   CHAOTIC  → Requires Vibranium/Unobtainium + Everything
//
// Ice and Fire's Dragonsteel is the physical endgame.
// You need actual dragon forges (hard to automate!)
// but the results feed into Draconic Evolution.
//
// AllTheModium provides the dimensional mining tier:
//   Allthemodium (Overworld deep) → mid-endgame
//   Vibranium (Nether) → late endgame
//   Unobtainium (End) → final endgame
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: ICE AND FIRE INTEGRATION
    // Dragon materials are rare and powerful.
    // They feed into Draconic Evolution's mid-tiers.
    // ==========================================

    // --- DRAGON BONE PROCESSING ---
    // Dragon Bones can be crushed in Create for bone meal + rare drops
    event.recipes.create.crushing([
        '4x minecraft:bone_meal',
        'minecraft:bone_meal',
        'minecraft:blaze_powder'
    ], 'iceandfire:dragon_bone');

    // --- DRAGON BLOOD MIXING ---
    // Dragon blood + metals in Create's Mixer = enhanced alloys
    // Fire Dragon Blood + Steel = Fire-tempered Steel
    event.recipes.create.mixing(
        '2x enderio:dark_steel_ingot',
        [
            '#c:ingots/steel',
            '#c:ingots/steel',
            'iceandfire:fire_dragon_blood'
        ]
    ).superheated();

    // Ice Dragon Blood + Gold = Cryogenic Gold (enhanced Hallowed Gold)
    event.recipes.create.mixing(
        '2x malum:hallowed_gold_ingot',
        [
            '#c:ingots/gold',
            '#c:ingots/gold',
            'iceandfire:ice_dragon_blood'
        ]
    ).superheated();

    // Lightning Dragon Blood + Redstone = Supercharged circuits
    event.recipes.create.mixing(
        '2x mekanism:advanced_control_circuit',
        [
            'mekanism:basic_control_circuit',
            'mekanism:basic_control_circuit',
            'iceandfire:lightning_dragon_blood',
            'minecraft:redstone_block'
        ]
    ).superheated();

    // ==========================================
    // SECTION 2: ALLTHEMODIUM PROCESSING
    // Create is the primary processing method
    // ==========================================

    // Allthemodium processed via Create Crushing (bonus yield)
    event.recipes.create.crushing([
        'allthemodium:raw_allthemodium',
        'minecraft:raw_gold'
    ], 'allthemodium:allthemodium_ore');

    // Vibranium crushing (Nether ore)
    event.recipes.create.crushing([
        'allthemodium:raw_vibranium'
    ], 'allthemodium:vibranium_ore');

    // Unobtainium crushing (End ore — rarest)
    event.recipes.create.crushing([
        'allthemodium:raw_unobtainium',
        'minecraft:netherite_scrap'
    ], 'allthemodium:unobtainium_ore');

    // ==========================================
    // SECTION 3: DRACONIUM PROCESSING
    // Draconium is Draconic Evolution's base material.
    // Must be processed through Create for bonus.
    // ==========================================

    event.recipes.create.crushing([
        '2x draconicevolution:draconium_dust'
    ], 'draconicevolution:draconium_ore');

    // ==========================================
    // SECTION 4: DRACONIC EVOLUTION — WYVERN TIER
    // The first endgame tier. Requires:
    // - Draconium (base material)
    // - Deeper Darker materials (Warden Carapace, Soul Crystal)
    // - Mekanism Elite Circuits
    // - Ender IO Machine Chassis
    // ==========================================

    // --- WYVERN CORE ---
    // The foundation of all Wyvern-tier items
    event.remove({ output: 'draconicevolution:wyvern_core' });
    event.shaped('draconicevolution:wyvern_core', [
        'SDS',
        'ECE',
        'SDS'
    ], {
        S: 'deeperdarker:soul_crystal',
        D: 'draconicevolution:draconium_ingot',
        E: 'mekanism:elite_control_circuit',
        C: 'enderio:ensouled_chassis'
    });

    // --- WYVERN ENERGY CORE ---
    // Energy storage for Wyvern tier
    event.remove({ output: 'draconicevolution:wyvern_energy_core' });
    event.shaped('draconicevolution:wyvern_energy_core', [
        'DWD',
        'WNW',
        'DWD'
    ], {
        D: 'draconicevolution:draconium_ingot',
        W: 'deeperdarker:reinforced_echo_shard',
        N: 'minecraft:nether_star'
    });

    // ==========================================
    // SECTION 5: DRACONIC EVOLUTION — DRACONIC TIER
    // Mid-endgame. Requires:
    // - Awakened Draconium
    // - DRAGONSTEEL from Ice and Fire (the hard-to-farm gate!)
    // - Allthemodium
    // - Vampirism Pure Blood (dark sacrifice for power)
    // - AE2 Processors
    // ==========================================

    // --- AWAKENED CORE (Previously Draconic Core) ---
    event.remove({ output: 'draconicevolution:awakened_core' });
    event.shaped('draconicevolution:awakened_core', [
        'DAD',
        'AWA',
        'DAD'
    ], {
        D: 'iceandfire:dragonsteel_fire_ingot',
        A: 'allthemodium:allthemodium_ingot',
        W: 'draconicevolution:wyvern_core'
    });

    // --- AWAKENED ENERGY CORE ---
    event.remove({ output: 'draconicevolution:awakened_energy_core' });
    event.shaped('draconicevolution:awakened_energy_core', [
        'DAD',
        'AWA',
        'DAD'
    ], {
        D: 'iceandfire:dragonsteel_ice_ingot',
        A: 'allthemodium:allthemodium_ingot',
        W: 'draconicevolution:wyvern_energy_core'
    });

    // --- AWAKENED DRACONIUM ---
    // Enhanced recipe: requires dragon blood ritual
    event.remove({ output: 'draconicevolution:awakened_draconium_ingot' });
    event.recipes.create.mixing(
        'draconicevolution:awakened_draconium_ingot',
        [
            'draconicevolution:draconium_ingot',
            'draconicevolution:draconium_ingot',
            'iceandfire:fire_dragon_blood',
            'minecraft:nether_star'
        ]
    ).superheated();

    // ==========================================
    // SECTION 6: DRACONIC EVOLUTION — CHAOTIC TIER
    // The absolute endgame. Requires EVERYTHING.
    // - Chaos Shards (from Chaos Guardian boss)
    // - Vibranium + Unobtainium (AllTheModium top tiers)
    // - Every prior tech and magic system
    // ==========================================

    // --- CHAOTIC CORE ---
    event.remove({ output: 'draconicevolution:chaotic_core' });
    event.shaped('draconicevolution:chaotic_core', [
        'UVU',
        'VDV',
        'UVU'
    ], {
        U: 'allthemodium:unobtainium_ingot',
        V: 'allthemodium:vibranium_ingot',
        D: 'draconicevolution:awakened_core'
    });

    // --- CHAOTIC ENERGY CORE ---
    event.remove({ output: 'draconicevolution:chaotic_energy_core' });
    event.shaped('draconicevolution:chaotic_energy_core', [
        'UCU',
        'CDE',
        'UCU'
    ], {
        U: 'allthemodium:unobtainium_ingot',
        C: 'draconicevolution:chaos_shard',
        D: 'draconicevolution:awakened_energy_core',
        E: 'mekanism:ultimate_control_circuit'
    });

    // --- DRACONIC REACTOR ---
    // The ultimate power source. Needs everything.
    event.remove({ output: 'draconicevolution:reactor_core' });
    event.shaped('draconicevolution:reactor_core', [
        'UCU',
        'CNC',
        'UCU'
    ], {
        U: 'allthemodium:unobtainium_ingot',
        C: 'draconicevolution:chaotic_core',
        N: 'draconicevolution:chaos_shard'
    });


    // ==========================================
    // SECTION 7: GOBBER INTEGRATION
    // Gobber ores run parallel to AllTheModium
    // as a secondary progression path
    // ==========================================

    // Gobber ingots processed via Create for bonus
    event.recipes.create.crushing([
        '2x gobber2:gobber2_ore'
    ], 'gobber2:gobber2_ore');

    event.recipes.create.crushing([
        '2x gobber2:gobber2_ore_nether'
    ], 'gobber2:gobber2_ore_nether');

    event.recipes.create.crushing([
        '2x gobber2:gobber2_ore_end'
    ], 'gobber2:gobber2_ore_end');

    // Gobber tools/armor require AllTheModium counterparts
    // End Gobber Ingot needs Allthemodium to process
    event.remove({ output: 'gobber2:gobber2_ingot_end' });
    event.recipes.create.mixing(
        'gobber2:gobber2_ingot_end',
        [
            'gobber2:gobber2_ore_end',
            'allthemodium:allthemodium_nugget',
            'minecraft:netherite_scrap'
        ]
    ).superheated();

    console.log('[PEAK Expert Mode] Script 07: Draconic + IAF + AllTheModium loaded!');
});
