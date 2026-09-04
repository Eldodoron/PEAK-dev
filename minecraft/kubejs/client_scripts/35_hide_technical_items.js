RecipeViewerEvents.removeEntries('item', event => {
    // --- HIDE VANILLA ADMINISTRATIVE & TECHNICAL BLOCKS ---
    const vanillaTechnical = [
        'minecraft:barrier',
        'minecraft:structure_block',
        'minecraft:structure_void',
        'minecraft:light',
        'minecraft:debug_stick',
        'minecraft:command_block',
        'minecraft:chain_command_block',
        'minecraft:repeating_command_block',
        'minecraft:command_block_minecart',
        'minecraft:jigsaw'
    ];

    // --- HIDE MOD DEBUGGERS, DUMMY & TEST ITEMS ---
    const modTechnical = [
        'ae2:debug_card',
        'ae2:debug_cube_gen',
        'ae2:debug_energy_gen',
        'ae2:debug_eraser',
        'ae2:debug_item_gen',
        'ae2:debug_meteorite_placer',
        'ae2:debug_phantom_node',
        'ae2:debug_replicator_card',
        'ars_nouveau:debug',
        'avaritia:test_sword',
        'block_factorys_bosses:placeholder',
        'citadel:debug',
        'farmersdelight:debug_pumpkin_pie',
        'iceandfire:dragon_debug_stick',
        'levelup:test_skill_orb',
        'raidsenhanced:debug_stick',
        'tfmg:debug_cinderblock'
    ];

    vanillaTechnical.forEach(item => event.remove(item));
    modTechnical.forEach(item => event.remove(item));
});
