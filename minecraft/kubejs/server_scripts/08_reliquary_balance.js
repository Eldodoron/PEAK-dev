// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 08
// RELIQUARY BALANCE + OVERPOWERED ITEM FIXES
// ==========================================
// The Alkahestry Tome from Reliquary can duplicate
// almost ANY item including Nether Stars. This is
// gamebreaking in an Expert Mode pack.
//
// Solution:
// 1. Make the Tome EXTREMELY expensive to craft
//    (endgame achievement, not an early shortcut)
// 2. Remove the ability to duplicate endgame items
//    (Nether Stars, Dragon Eggs, Draconium, etc.)
// 3. Keep it useful for mid-game bulk resources
//    (ores, common materials = still valuable)
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: ALKAHESTRY TOME â€” NEW RECIPE
    // This item should be a TROPHY of late-game mastery,
    // not a cheap shortcut. You need to have mastered
    // both magic AND technology to wield transmutation.
    // ==========================================

    event.remove({ output: 'reliquary:alkahestry_tome' });
    event.shaped('reliquary:alkahestry_tome', [
        'NSN',
        'PBP',
        'HAH'
    ], {
        N: 'minecraft:nether_star',
        S: 'ars_nouveau:source_gem_block',
        P: 'create:precision_mechanism',
        B: 'minecraft:book',
        H: 'malum:hallowed_gold_ingot',
        A: 'mekanism:alloy_reinforced'
    });

    // ==========================================
    // SECTION 2: REMOVE OVERPOWERED DUPLICATIONS
    // Alkahestry should NOT be able to duplicate
    // any of these endgame/progression items.
    // We remove these specific alkahestry recipes.
    // ==========================================

    // Remove duplication of Nether Stars
    event.remove({ output: 'minecraft:nether_star', type: 'reliquary:alkahestry_crafting' });
    event.remove({ input: 'minecraft:nether_star', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Dragon Eggs
    event.remove({ output: 'minecraft:dragon_egg', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Draconium
    event.remove({ output: 'draconicevolution:draconium_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'draconicevolution:awakened_draconium_ingot', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Chaos Shards
    event.remove({ output: 'draconicevolution:chaos_shard', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of AllTheModium metals
    event.remove({ output: 'allthemodium:allthemodium_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'allthemodium:vibranium_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'allthemodium:unobtainium_ingot', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Dragonsteel
    event.remove({ output: 'iceandfire:dragonsteel_fire_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'iceandfire:dragonsteel_ice_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'iceandfire:dragonsteel_lightning_ingot', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Netherite
    event.remove({ output: 'minecraft:netherite_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'minecraft:netherite_scrap', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'minecraft:ancient_debris', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of key tech components
    event.remove({ output: 'create:precision_mechanism', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'mekanism:alloy_atomic', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'mekanism:pellet_antimatter', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'ae2:singularity', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Source Gems (magic economy)
    event.remove({ output: 'ars_nouveau:source_gem_block', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Soul materials
    event.remove({ output: 'malum:soul_stained_steel_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'enderio:soularium_ingot', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Ender Pearls (too easy to break EIO)
    event.remove({ output: 'minecraft:ender_pearl', type: 'reliquary:alkahestry_crafting' });

    // Remove duplication of Wither Skeleton Skulls
    event.remove({ output: 'minecraft:wither_skeleton_skull', type: 'reliquary:alkahestry_crafting' });

    // Remove Gobber duplication
    event.remove({ output: 'gobber2:gobber2_ingot', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'gobber2:gobber2_ingot_nether', type: 'reliquary:alkahestry_crafting' });
    event.remove({ output: 'gobber2:gobber2_ingot_end', type: 'reliquary:alkahestry_crafting' });

    // ==========================================
    // SECTION 3: OTHER RELIQUARY BALANCE
    // Make other Reliquary items fit the tech tree
    // ==========================================

    // Mob Charm Fragment â€” keep accessible but require some tech
    // (Mob charms prevent mob spawning = powerful utility)

    // Holy Hand Grenade â€” needs Hallowed Gold (thematic!)
    event.remove({ output: 'reliquary:holy_hand_grenade' });
    event.shaped('reliquary:holy_hand_grenade', [
        ' G ',
        'GHG',
        ' N '
    ], {
        G: '#c:ingots/gold',
        H: 'malum:hallowed_gold_ingot',
        N: 'minecraft:tnt'
    });

    // Mercy Cross â€” needs both holy and dark materials
    event.remove({ output: 'reliquary:mercy_cross' });
    event.shaped('reliquary:mercy_cross', [
        ' H ',
        'GNG',
        ' H '
    ], {
        H: 'malum:hallowed_gold_ingot',
        G: '#c:ingots/gold',
        N: 'minecraft:nether_star'
    });

    // ==========================================
    // SECTION 4: OTHER OVERPOWERED ITEM BALANCE
    // Catch-all for items that are too easy to get
    // ==========================================

    // Elytra duplication should be expensive
    // (If any mod allows crafting Elytra, gate it)
    event.remove({ output: 'minecraft:elytra' });
    event.shaped('minecraft:elytra', [
        'PSP',
        'P P',
        'P P'
    ], {
        P: 'minecraft:phantom_membrane',
        S: 'ars_nouveau:source_gem_block'
    });

    // Shulker Box â€” needs Ender IO ender-tech
    event.remove({ output: 'minecraft:shulker_box' });
    event.shaped('minecraft:shulker_box', [
        'S',
        'C',
        'S'
    ], {
        S: 'minecraft:shulker_shell',
        C: 'enderio:pulsating_crystal'
    });

    // ==========================================
    // SECTION 5: GATEWAY TO ETERNITY INTEGRATION
    // Boss gateways should require tech investment
    // ==========================================

    // Gateway Pearls need Ender IO + magic
    event.remove({ output: 'gateways:gate_pearl' });
    event.shaped('gateways:gate_pearl', [
        'ESE',
        'SPS',
        'ESE'
    ], {
        E: 'minecraft:ender_pearl',
        S: 'ars_nouveau:source_gem',
        P: 'enderio:pulsating_crystal'
    });

    console.log('[PEAK Expert Mode] Script 08: Reliquary Balance + OP Fixes loaded!');
});

