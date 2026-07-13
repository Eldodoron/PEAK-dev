// ==========================================
// PEAK EXPERT MODE — SCRIPT 21
// BACKPACK UPGRADE OVERHAUL
// Uses KubeJS-Create addon API (sequenced_assembly)
// for 1.21.1 NeoForge compatibility
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // STEP 1: REMOVE ALL DEFAULT RECIPES
    // ==========================================
    const removals = [
        'sophisticatedbackpacks:pickup_upgrade',
        'sophisticatedbackpacks:restock_upgrade',
        'sophisticatedbackpacks:deposit_upgrade',
        'sophisticatedbackpacks:refill_upgrade',
        'sophisticatedbackpacks:smelting_upgrade',
        'sophisticatedbackpacks:smoking_upgrade',
        'sophisticatedbackpacks:blasting_upgrade',
        'sophisticatedbackpacks:compacting_upgrade',
        'sophisticatedbackpacks:void_upgrade',
        'sophisticatedbackpacks:feeding_upgrade',
        'sophisticatedbackpacks:jukebox_upgrade',
        'sophisticatedbackpacks:crafting_upgrade',
        'sophisticatedbackpacks:stonecutter_upgrade',
        'sophisticatedbackpacks:anvil_upgrade',
        'sophisticatedbackpacks:smithing_upgrade',
        'sophisticatedbackpacks:tank_upgrade',
        'sophisticatedbackpacks:battery_upgrade',
        'sophisticatedbackpacks:tool_swapper_upgrade',
        'sophisticatedbackpacks:pump_upgrade',
        'sophisticatedbackpacks:stack_upgrade_starter_tier',
        'sophisticatedbackpacks:filter_upgrade',
        'sophisticatedbackpacks:magnet_upgrade',
        'sophisticatedbackpacks:advanced_pickup_upgrade',
        'sophisticatedbackpacks:advanced_restock_upgrade',
        'sophisticatedbackpacks:advanced_deposit_upgrade',
        'sophisticatedbackpacks:advanced_refill_upgrade',
        'sophisticatedbackpacks:auto_smelting_upgrade',
        'sophisticatedbackpacks:auto_smoking_upgrade',
        'sophisticatedbackpacks:auto_blasting_upgrade',
        'sophisticatedbackpacks:advanced_compacting_upgrade',
        'sophisticatedbackpacks:advanced_void_upgrade',
        'sophisticatedbackpacks:advanced_feeding_upgrade',
        'sophisticatedbackpacks:advanced_filter_upgrade',
        'sophisticatedbackpacks:advanced_magnet_upgrade',
        'sophisticatedbackpacks:advanced_jukebox_upgrade',
        'sophisticatedbackpacks:advanced_tool_swapper_upgrade',
        'sophisticatedbackpacks:advanced_pump_upgrade',
        'sophisticatedbackpacks:xp_pump_upgrade',
        'sophisticatedbackpacks:alchemy_upgrade',
        'sophisticatedbackpacks:advanced_alchemy_upgrade',
        'sophisticatedbackpacks:stack_upgrade_tier_1',
        'sophisticatedbackpacks:stack_upgrade_tier_2',
        'sophisticatedbackpacks:stack_upgrade_tier_3',
        'sophisticatedbackpacks:stack_upgrade_tier_4',
        'sophisticatedbackpacks:stack_upgrade_omega_tier',
        'backpack_allthemodium_upgrade:stack_upgrade_tier_5',
        'backpack_allthemodium_upgrade:stack_upgrade_tier_6',
        'backpack_allthemodium_upgrade:stack_upgrade_tier_7',
        'sophisticatedbackpacks:inception_upgrade',
        'sophisticatedbackpacks:everlasting_upgrade',
    ];
    removals.forEach(id => event.remove({ output: id }));

    // ==========================================
    // STEP 2: SEQUENCED ASSEMBLY RECIPES
    // Using the KubeJS-Create addon API
    // Format: event.recipes.create.sequenced_assembly(result, ingredient, sequence)
    //         .transitionalItem(transitional).loops(n).id('...')
    // ==========================================

    // Helper shorthand
    const sa = event.recipes.create;

    // --- BASIC UPGRADES (base: upgrade_base, loops: 3) ---

    sa.sequenced_assembly('sophisticatedbackpacks:pickup_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_pickup_upgrade', ['kubejs:incomplete_pickup_upgrade', 'create:andesite_funnel']),
        sa.deploying('kubejs:incomplete_pickup_upgrade', ['kubejs:incomplete_pickup_upgrade', 'minecraft:hopper']),
        sa.pressing('kubejs:incomplete_pickup_upgrade', 'kubejs:incomplete_pickup_upgrade')
    ]).transitionalItem('kubejs:incomplete_pickup_upgrade').loops(3).id('kubejs:sequenced_assembly/pickup_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:restock_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_restock_upgrade', ['kubejs:incomplete_restock_upgrade', 'create:andesite_tunnel']),
        sa.deploying('kubejs:incomplete_restock_upgrade', ['kubejs:incomplete_restock_upgrade', 'minecraft:chest']),
        sa.pressing('kubejs:incomplete_restock_upgrade', 'kubejs:incomplete_restock_upgrade')
    ]).transitionalItem('kubejs:incomplete_restock_upgrade').loops(3).id('kubejs:sequenced_assembly/restock_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:deposit_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_deposit_upgrade', ['kubejs:incomplete_deposit_upgrade', 'create:chute']),
        sa.deploying('kubejs:incomplete_deposit_upgrade', ['kubejs:incomplete_deposit_upgrade', 'minecraft:piston']),
        sa.pressing('kubejs:incomplete_deposit_upgrade', 'kubejs:incomplete_deposit_upgrade')
    ]).transitionalItem('kubejs:incomplete_deposit_upgrade').loops(3).id('kubejs:sequenced_assembly/deposit_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:refill_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_refill_upgrade', ['kubejs:incomplete_refill_upgrade', 'minecraft:dropper']),
        sa.deploying('kubejs:incomplete_refill_upgrade', ['kubejs:incomplete_refill_upgrade', 'minecraft:dispenser']),
        sa.pressing('kubejs:incomplete_refill_upgrade', 'kubejs:incomplete_refill_upgrade')
    ]).transitionalItem('kubejs:incomplete_refill_upgrade').loops(3).id('kubejs:sequenced_assembly/refill_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:smelting_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_smelting_upgrade', ['kubejs:incomplete_smelting_upgrade', 'minecraft:furnace']),
        sa.deploying('kubejs:incomplete_smelting_upgrade', ['kubejs:incomplete_smelting_upgrade', 'minecraft:coal_block']),
        sa.pressing('kubejs:incomplete_smelting_upgrade', 'kubejs:incomplete_smelting_upgrade')
    ]).transitionalItem('kubejs:incomplete_smelting_upgrade').loops(3).id('kubejs:sequenced_assembly/smelting_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:smoking_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_smoking_upgrade', ['kubejs:incomplete_smoking_upgrade', 'minecraft:smoker']),
        sa.deploying('kubejs:incomplete_smoking_upgrade', ['kubejs:incomplete_smoking_upgrade', 'minecraft:coal_block']),
        sa.pressing('kubejs:incomplete_smoking_upgrade', 'kubejs:incomplete_smoking_upgrade')
    ]).transitionalItem('kubejs:incomplete_smoking_upgrade').loops(3).id('kubejs:sequenced_assembly/smoking_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:blasting_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_blasting_upgrade', ['kubejs:incomplete_blasting_upgrade', 'minecraft:blast_furnace']),
        sa.deploying('kubejs:incomplete_blasting_upgrade', ['kubejs:incomplete_blasting_upgrade', 'minecraft:coal_block']),
        sa.pressing('kubejs:incomplete_blasting_upgrade', 'kubejs:incomplete_blasting_upgrade')
    ]).transitionalItem('kubejs:incomplete_blasting_upgrade').loops(3).id('kubejs:sequenced_assembly/blasting_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:compacting_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_compacting_upgrade', ['kubejs:incomplete_compacting_upgrade', 'minecraft:piston']),
        sa.deploying('kubejs:incomplete_compacting_upgrade', ['kubejs:incomplete_compacting_upgrade', 'create:mechanical_press']),
        sa.pressing('kubejs:incomplete_compacting_upgrade', 'kubejs:incomplete_compacting_upgrade')
    ]).transitionalItem('kubejs:incomplete_compacting_upgrade').loops(3).id('kubejs:sequenced_assembly/compacting_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:void_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_void_upgrade', ['kubejs:incomplete_void_upgrade', 'minecraft:obsidian']),
        sa.deploying('kubejs:incomplete_void_upgrade', ['kubejs:incomplete_void_upgrade', 'minecraft:ender_pearl']),
        sa.pressing('kubejs:incomplete_void_upgrade', 'kubejs:incomplete_void_upgrade')
    ]).transitionalItem('kubejs:incomplete_void_upgrade').loops(3).id('kubejs:sequenced_assembly/void_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:feeding_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_feeding_upgrade', ['kubejs:incomplete_feeding_upgrade', 'minecraft:golden_carrot']),
        sa.deploying('kubejs:incomplete_feeding_upgrade', ['kubejs:incomplete_feeding_upgrade', 'minecraft:golden_apple']),
        sa.pressing('kubejs:incomplete_feeding_upgrade', 'kubejs:incomplete_feeding_upgrade')
    ]).transitionalItem('kubejs:incomplete_feeding_upgrade').loops(3).id('kubejs:sequenced_assembly/feeding_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:jukebox_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_jukebox_upgrade', ['kubejs:incomplete_jukebox_upgrade', 'minecraft:note_block']),
        sa.deploying('kubejs:incomplete_jukebox_upgrade', ['kubejs:incomplete_jukebox_upgrade', 'minecraft:jukebox']),
        sa.pressing('kubejs:incomplete_jukebox_upgrade', 'kubejs:incomplete_jukebox_upgrade')
    ]).transitionalItem('kubejs:incomplete_jukebox_upgrade').loops(3).id('kubejs:sequenced_assembly/jukebox_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:crafting_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_crafting_upgrade', ['kubejs:incomplete_crafting_upgrade', 'minecraft:crafting_table']),
        sa.deploying('kubejs:incomplete_crafting_upgrade', ['kubejs:incomplete_crafting_upgrade', 'create:mechanical_crafter']),
        sa.pressing('kubejs:incomplete_crafting_upgrade', 'kubejs:incomplete_crafting_upgrade')
    ]).transitionalItem('kubejs:incomplete_crafting_upgrade').loops(3).id('kubejs:sequenced_assembly/crafting_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:stonecutter_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_stonecutter_upgrade', ['kubejs:incomplete_stonecutter_upgrade', 'minecraft:stonecutter']),
        sa.deploying('kubejs:incomplete_stonecutter_upgrade', ['kubejs:incomplete_stonecutter_upgrade', 'create:mechanical_saw']),
        sa.pressing('kubejs:incomplete_stonecutter_upgrade', 'kubejs:incomplete_stonecutter_upgrade')
    ]).transitionalItem('kubejs:incomplete_stonecutter_upgrade').loops(3).id('kubejs:sequenced_assembly/stonecutter_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:anvil_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_anvil_upgrade', ['kubejs:incomplete_anvil_upgrade', 'minecraft:anvil']),
        sa.deploying('kubejs:incomplete_anvil_upgrade', ['kubejs:incomplete_anvil_upgrade', 'minecraft:iron_block']),
        sa.pressing('kubejs:incomplete_anvil_upgrade', 'kubejs:incomplete_anvil_upgrade')
    ]).transitionalItem('kubejs:incomplete_anvil_upgrade').loops(3).id('kubejs:sequenced_assembly/anvil_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:smithing_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_smithing_upgrade', ['kubejs:incomplete_smithing_upgrade', 'minecraft:smithing_table']),
        sa.deploying('kubejs:incomplete_smithing_upgrade', ['kubejs:incomplete_smithing_upgrade', 'minecraft:iron_block']),
        sa.pressing('kubejs:incomplete_smithing_upgrade', 'kubejs:incomplete_smithing_upgrade')
    ]).transitionalItem('kubejs:incomplete_smithing_upgrade').loops(3).id('kubejs:sequenced_assembly/smithing_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:tank_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_tank_upgrade', ['kubejs:incomplete_tank_upgrade', 'create:fluid_tank']),
        sa.deploying('kubejs:incomplete_tank_upgrade', ['kubejs:incomplete_tank_upgrade', 'minecraft:glass']),
        sa.pressing('kubejs:incomplete_tank_upgrade', 'kubejs:incomplete_tank_upgrade')
    ]).transitionalItem('kubejs:incomplete_tank_upgrade').loops(3).id('kubejs:sequenced_assembly/tank_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:battery_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_battery_upgrade', ['kubejs:incomplete_battery_upgrade', 'minecraft:redstone_block']),
        sa.deploying('kubejs:incomplete_battery_upgrade', ['kubejs:incomplete_battery_upgrade', 'minecraft:gold_ingot']),
        sa.pressing('kubejs:incomplete_battery_upgrade', 'kubejs:incomplete_battery_upgrade')
    ]).transitionalItem('kubejs:incomplete_battery_upgrade').loops(3).id('kubejs:sequenced_assembly/battery_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:tool_swapper_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_tool_swapper_upgrade', ['kubejs:incomplete_tool_swapper_upgrade', 'minecraft:iron_pickaxe']),
        sa.deploying('kubejs:incomplete_tool_swapper_upgrade', ['kubejs:incomplete_tool_swapper_upgrade', 'minecraft:iron_sword']),
        sa.pressing('kubejs:incomplete_tool_swapper_upgrade', 'kubejs:incomplete_tool_swapper_upgrade')
    ]).transitionalItem('kubejs:incomplete_tool_swapper_upgrade').loops(3).id('kubejs:sequenced_assembly/tool_swapper_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:pump_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_pump_upgrade', ['kubejs:incomplete_pump_upgrade', 'create:mechanical_pump']),
        sa.deploying('kubejs:incomplete_pump_upgrade', ['kubejs:incomplete_pump_upgrade', 'minecraft:iron_block']),
        sa.pressing('kubejs:incomplete_pump_upgrade', 'kubejs:incomplete_pump_upgrade')
    ]).transitionalItem('kubejs:incomplete_pump_upgrade').loops(3).id('kubejs:sequenced_assembly/pump_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:stack_upgrade_starter_tier', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_stack_upgrade_starter_tier', ['kubejs:incomplete_stack_upgrade_starter_tier', 'minecraft:iron_block']),
        sa.deploying('kubejs:incomplete_stack_upgrade_starter_tier', ['kubejs:incomplete_stack_upgrade_starter_tier', 'minecraft:copper_block']),
        sa.pressing('kubejs:incomplete_stack_upgrade_starter_tier', 'kubejs:incomplete_stack_upgrade_starter_tier')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_starter_tier').loops(3).id('kubejs:sequenced_assembly/stack_upgrade_starter_tier');

    // Filter Upgrade: basic uses EnderIO basic item filter (not paper/iron bars)
    sa.sequenced_assembly('sophisticatedbackpacks:filter_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_filter_upgrade', ['kubejs:incomplete_filter_upgrade', 'enderio:basic_item_filter']),
        sa.deploying('kubejs:incomplete_filter_upgrade', ['kubejs:incomplete_filter_upgrade', 'create:filter']),
        sa.pressing('kubejs:incomplete_filter_upgrade', 'kubejs:incomplete_filter_upgrade')
    ]).transitionalItem('kubejs:incomplete_filter_upgrade').loops(1).id('kubejs:sequenced_assembly/filter_upgrade');

    // Magnet Upgrade: uses Alex's Caves magnets, not iron+redstone
    sa.sequenced_assembly('sophisticatedbackpacks:magnet_upgrade', 'sophisticatedbackpacks:filter_upgrade', [
        sa.deploying('kubejs:incomplete_magnet_upgrade', ['kubejs:incomplete_magnet_upgrade', 'alexscaves:scarlet_magnet']),
        sa.deploying('kubejs:incomplete_magnet_upgrade', ['kubejs:incomplete_magnet_upgrade', 'alexscaves:azure_magnet']),
        sa.pressing('kubejs:incomplete_magnet_upgrade', 'kubejs:incomplete_magnet_upgrade')
    ]).transitionalItem('kubejs:incomplete_magnet_upgrade').loops(1).id('kubejs:sequenced_assembly/magnet_upgrade');

    // --- ADVANCED UPGRADES (loops: 4) ---

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_pickup_upgrade', 'sophisticatedbackpacks:pickup_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_pickup_upgrade', ['kubejs:incomplete_advanced_pickup_upgrade', 'create:brass_funnel']),
        sa.deploying('kubejs:incomplete_advanced_pickup_upgrade', ['kubejs:incomplete_advanced_pickup_upgrade', 'mekanism:basic_control_circuit']),
        sa.pressing('kubejs:incomplete_advanced_pickup_upgrade', 'kubejs:incomplete_advanced_pickup_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_pickup_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_pickup_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_restock_upgrade', 'sophisticatedbackpacks:restock_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_restock_upgrade', ['kubejs:incomplete_advanced_restock_upgrade', 'create:brass_tunnel']),
        sa.deploying('kubejs:incomplete_advanced_restock_upgrade', ['kubejs:incomplete_advanced_restock_upgrade', 'mekanism:basic_control_circuit']),
        sa.pressing('kubejs:incomplete_advanced_restock_upgrade', 'kubejs:incomplete_advanced_restock_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_restock_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_restock_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_deposit_upgrade', 'sophisticatedbackpacks:deposit_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_deposit_upgrade', ['kubejs:incomplete_advanced_deposit_upgrade', 'pneumaticcraft:omnidirectional_hopper']),
        sa.deploying('kubejs:incomplete_advanced_deposit_upgrade', ['kubejs:incomplete_advanced_deposit_upgrade', 'mekanism:basic_control_circuit']),
        sa.pressing('kubejs:incomplete_advanced_deposit_upgrade', 'kubejs:incomplete_advanced_deposit_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_deposit_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_deposit_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_refill_upgrade', 'sophisticatedbackpacks:refill_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_refill_upgrade', ['kubejs:incomplete_advanced_refill_upgrade', 'create:brass_tunnel']),
        sa.deploying('kubejs:incomplete_advanced_refill_upgrade', ['kubejs:incomplete_advanced_refill_upgrade', 'pneumaticcraft:printed_circuit_board']),
        sa.pressing('kubejs:incomplete_advanced_refill_upgrade', 'kubejs:incomplete_advanced_refill_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_refill_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_refill_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:auto_smelting_upgrade', 'sophisticatedbackpacks:smelting_upgrade', [
        sa.deploying('kubejs:incomplete_auto_smelting_upgrade', ['kubejs:incomplete_auto_smelting_upgrade', 'create:blaze_burner']),
        sa.deploying('kubejs:incomplete_auto_smelting_upgrade', ['kubejs:incomplete_auto_smelting_upgrade', 'pneumaticcraft:printed_circuit_board']),
        sa.pressing('kubejs:incomplete_auto_smelting_upgrade', 'kubejs:incomplete_auto_smelting_upgrade')
    ]).transitionalItem('kubejs:incomplete_auto_smelting_upgrade').loops(4).id('kubejs:sequenced_assembly/auto_smelting_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:auto_smoking_upgrade', 'sophisticatedbackpacks:smoking_upgrade', [
        sa.deploying('kubejs:incomplete_auto_smoking_upgrade', ['kubejs:incomplete_auto_smoking_upgrade', 'create:blaze_burner']),
        sa.deploying('kubejs:incomplete_auto_smoking_upgrade', ['kubejs:incomplete_auto_smoking_upgrade', 'pneumaticcraft:printed_circuit_board']),
        sa.pressing('kubejs:incomplete_auto_smoking_upgrade', 'kubejs:incomplete_auto_smoking_upgrade')
    ]).transitionalItem('kubejs:incomplete_auto_smoking_upgrade').loops(4).id('kubejs:sequenced_assembly/auto_smoking_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:auto_blasting_upgrade', 'sophisticatedbackpacks:blasting_upgrade', [
        sa.deploying('kubejs:incomplete_auto_blasting_upgrade', ['kubejs:incomplete_auto_blasting_upgrade', 'create:blaze_burner']),
        sa.deploying('kubejs:incomplete_auto_blasting_upgrade', ['kubejs:incomplete_auto_blasting_upgrade', 'pneumaticcraft:printed_circuit_board']),
        sa.pressing('kubejs:incomplete_auto_blasting_upgrade', 'kubejs:incomplete_auto_blasting_upgrade')
    ]).transitionalItem('kubejs:incomplete_auto_blasting_upgrade').loops(4).id('kubejs:sequenced_assembly/auto_blasting_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_compacting_upgrade', 'sophisticatedbackpacks:compacting_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_compacting_upgrade', ['kubejs:incomplete_advanced_compacting_upgrade', 'pneumaticcraft:air_compressor']),
        sa.deploying('kubejs:incomplete_advanced_compacting_upgrade', ['kubejs:incomplete_advanced_compacting_upgrade', 'mekanism:advanced_control_circuit']),
        sa.pressing('kubejs:incomplete_advanced_compacting_upgrade', 'kubejs:incomplete_advanced_compacting_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_compacting_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_compacting_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_void_upgrade', 'sophisticatedbackpacks:void_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_void_upgrade', ['kubejs:incomplete_advanced_void_upgrade', 'alexscaves:raygun']),
        sa.deploying('kubejs:incomplete_advanced_void_upgrade', ['kubejs:incomplete_advanced_void_upgrade', 'minecraft:end_crystal']),
        sa.pressing('kubejs:incomplete_advanced_void_upgrade', 'kubejs:incomplete_advanced_void_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_void_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_void_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_feeding_upgrade', 'sophisticatedbackpacks:feeding_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_feeding_upgrade', ['kubejs:incomplete_advanced_feeding_upgrade', 'ars_nouveau:source_gem']),
        sa.deploying('kubejs:incomplete_advanced_feeding_upgrade', ['kubejs:incomplete_advanced_feeding_upgrade', 'minecraft:enchanted_golden_apple']),
        sa.pressing('kubejs:incomplete_advanced_feeding_upgrade', 'kubejs:incomplete_advanced_feeding_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_feeding_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_feeding_upgrade');

    // Advanced Filter: uses EnderIO advanced_item_filter (remove mekanism circuit)
    sa.sequenced_assembly('sophisticatedbackpacks:advanced_filter_upgrade', 'sophisticatedbackpacks:filter_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_filter_upgrade', ['kubejs:incomplete_advanced_filter_upgrade', 'create:attribute_filter']),
        sa.deploying('kubejs:incomplete_advanced_filter_upgrade', ['kubejs:incomplete_advanced_filter_upgrade', 'enderio:advanced_item_filter']),
        sa.pressing('kubejs:incomplete_advanced_filter_upgrade', 'kubejs:incomplete_advanced_filter_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_filter_upgrade').loops(1).id('kubejs:sequenced_assembly/advanced_filter_upgrade');

    // Advanced Magnet: uses electromagnetic coil + IE electromagnet (no nether star)
    sa.sequenced_assembly('sophisticatedbackpacks:advanced_magnet_upgrade', 'sophisticatedbackpacks:magnet_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_magnet_upgrade', ['kubejs:incomplete_advanced_magnet_upgrade', 'tfmg:electromagnetic_coil']),
        sa.deploying('kubejs:incomplete_advanced_magnet_upgrade', ['kubejs:incomplete_advanced_magnet_upgrade', 'immersiveengineering:electromagnet']),
        sa.pressing('kubejs:incomplete_advanced_magnet_upgrade', 'kubejs:incomplete_advanced_magnet_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_magnet_upgrade').loops(1).id('kubejs:sequenced_assembly/advanced_magnet_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_jukebox_upgrade', 'sophisticatedbackpacks:jukebox_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_jukebox_upgrade', ['kubejs:incomplete_advanced_jukebox_upgrade', 'minecraft:jukebox']),
        sa.deploying('kubejs:incomplete_advanced_jukebox_upgrade', ['kubejs:incomplete_advanced_jukebox_upgrade', 'mekanism:basic_control_circuit']),
        sa.pressing('kubejs:incomplete_advanced_jukebox_upgrade', 'kubejs:incomplete_advanced_jukebox_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_jukebox_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_jukebox_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_tool_swapper_upgrade', 'sophisticatedbackpacks:tool_swapper_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_tool_swapper_upgrade', ['kubejs:incomplete_advanced_tool_swapper_upgrade', 'minecraft:diamond_pickaxe']),
        sa.deploying('kubejs:incomplete_advanced_tool_swapper_upgrade', ['kubejs:incomplete_advanced_tool_swapper_upgrade', 'mekanism:advanced_control_circuit']),
        sa.pressing('kubejs:incomplete_advanced_tool_swapper_upgrade', 'kubejs:incomplete_advanced_tool_swapper_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_tool_swapper_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_tool_swapper_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_pump_upgrade', 'sophisticatedbackpacks:pump_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_pump_upgrade', ['kubejs:incomplete_advanced_pump_upgrade', 'create:mechanical_pump']),
        sa.deploying('kubejs:incomplete_advanced_pump_upgrade', ['kubejs:incomplete_advanced_pump_upgrade', 'mekanism:advanced_control_circuit']),
        sa.pressing('kubejs:incomplete_advanced_pump_upgrade', 'kubejs:incomplete_advanced_pump_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_pump_upgrade').loops(4).id('kubejs:sequenced_assembly/advanced_pump_upgrade');

    // --- SPECIAL UPGRADES ---

    sa.sequenced_assembly('sophisticatedbackpacks:xp_pump_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_xp_pump_upgrade', ['kubejs:incomplete_xp_pump_upgrade', 'create_enchantment_industry:experience_hatch']),
        sa.deploying('kubejs:incomplete_xp_pump_upgrade', ['kubejs:incomplete_xp_pump_upgrade', 'ars_nouveau:experience_gem']),
        sa.pressing('kubejs:incomplete_xp_pump_upgrade', 'kubejs:incomplete_xp_pump_upgrade')
    ]).transitionalItem('kubejs:incomplete_xp_pump_upgrade').loops(4).id('kubejs:sequenced_assembly/xp_pump_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:alchemy_upgrade', 'sophisticatedbackpacks:upgrade_base', [
        sa.deploying('kubejs:incomplete_alchemy_upgrade', ['kubejs:incomplete_alchemy_upgrade', 'ars_nouveau:potion_flask']),
        sa.deploying('kubejs:incomplete_alchemy_upgrade', ['kubejs:incomplete_alchemy_upgrade', 'ars_nouveau:source_gem']),
        sa.pressing('kubejs:incomplete_alchemy_upgrade', 'kubejs:incomplete_alchemy_upgrade')
    ]).transitionalItem('kubejs:incomplete_alchemy_upgrade').loops(4).id('kubejs:sequenced_assembly/alchemy_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:advanced_alchemy_upgrade', 'sophisticatedbackpacks:alchemy_upgrade', [
        sa.deploying('kubejs:incomplete_advanced_alchemy_upgrade', ['kubejs:incomplete_advanced_alchemy_upgrade', 'ars_nouveau:source_gem']),
        sa.deploying('kubejs:incomplete_advanced_alchemy_upgrade', ['kubejs:incomplete_advanced_alchemy_upgrade', 'minecraft:nether_star']),
        sa.pressing('kubejs:incomplete_advanced_alchemy_upgrade', 'kubejs:incomplete_advanced_alchemy_upgrade')
    ]).transitionalItem('kubejs:incomplete_advanced_alchemy_upgrade').loops(5).id('kubejs:sequenced_assembly/advanced_alchemy_upgrade');

    // --- STACK UPGRADES (progressive tiers) ---

    sa.sequenced_assembly('sophisticatedbackpacks:stack_upgrade_tier_1', 'sophisticatedbackpacks:stack_upgrade_starter_tier', [
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_1', ['kubejs:incomplete_stack_upgrade_tier_1', 'minecraft:iron_block']),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_1', ['kubejs:incomplete_stack_upgrade_tier_1', 'mekanism:basic_bin']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_1', 'kubejs:incomplete_stack_upgrade_tier_1')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_tier_1').loops(2).id('kubejs:sequenced_assembly/stack_upgrade_tier_1');

    sa.sequenced_assembly('sophisticatedbackpacks:stack_upgrade_tier_2', 'sophisticatedbackpacks:stack_upgrade_tier_1', [
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_2', ['kubejs:incomplete_stack_upgrade_tier_2', 'minecraft:gold_block']),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_2', ['kubejs:incomplete_stack_upgrade_tier_2', 'mekanism:advanced_bin']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_2', 'kubejs:incomplete_stack_upgrade_tier_2')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_tier_2').loops(4).id('kubejs:sequenced_assembly/stack_upgrade_tier_2');

    sa.sequenced_assembly('sophisticatedbackpacks:stack_upgrade_tier_3', 'sophisticatedbackpacks:stack_upgrade_tier_2', [
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_3', ['kubejs:incomplete_stack_upgrade_tier_3', 'minecraft:diamond_block']),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_3', ['kubejs:incomplete_stack_upgrade_tier_3', 'mekanism:advanced_bin']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_3', 'kubejs:incomplete_stack_upgrade_tier_3')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_tier_3').loops(8).id('kubejs:sequenced_assembly/stack_upgrade_tier_3');

    sa.sequenced_assembly('sophisticatedbackpacks:stack_upgrade_tier_4', 'sophisticatedbackpacks:stack_upgrade_tier_3', [
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_4', ['kubejs:incomplete_stack_upgrade_tier_4', 'minecraft:netherite_block']),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_4', ['kubejs:incomplete_stack_upgrade_tier_4', 'mekanism:elite_bin']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_4', 'kubejs:incomplete_stack_upgrade_tier_4')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_tier_4').loops(16).id('kubejs:sequenced_assembly/stack_upgrade_tier_4');

    sa.sequenced_assembly('backpack_allthemodium_upgrade:stack_upgrade_tier_5', 'sophisticatedbackpacks:stack_upgrade_tier_4', [
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_5', ['kubejs:incomplete_stack_upgrade_tier_5', 'allthemodium:allthemodium_block']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_5', 'kubejs:incomplete_stack_upgrade_tier_5'),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_5', ['kubejs:incomplete_stack_upgrade_tier_5', 'mekanism:elite_bin']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_5', 'kubejs:incomplete_stack_upgrade_tier_5')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_tier_5').loops(32).id('kubejs:sequenced_assembly/stack_upgrade_tier_5');

    sa.sequenced_assembly('backpack_allthemodium_upgrade:stack_upgrade_tier_6', 'backpack_allthemodium_upgrade:stack_upgrade_tier_5', [
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_6', ['kubejs:incomplete_stack_upgrade_tier_6', 'allthemodium:vibranium_block']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_6', 'kubejs:incomplete_stack_upgrade_tier_6'),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_6', ['kubejs:incomplete_stack_upgrade_tier_6', 'mekanism:elite_bin']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_6', 'kubejs:incomplete_stack_upgrade_tier_6'),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_6', ['kubejs:incomplete_stack_upgrade_tier_6', 'ae2:spatial_storage_cell_2']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_6', 'kubejs:incomplete_stack_upgrade_tier_6')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_tier_6').loops(48).id('kubejs:sequenced_assembly/stack_upgrade_tier_6');

    sa.sequenced_assembly('backpack_allthemodium_upgrade:stack_upgrade_tier_7', 'backpack_allthemodium_upgrade:stack_upgrade_tier_6', [
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_7', ['kubejs:incomplete_stack_upgrade_tier_7', 'allthemodium:unobtainium_block']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_7', 'kubejs:incomplete_stack_upgrade_tier_7'),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_7', ['kubejs:incomplete_stack_upgrade_tier_7', 'mekanism:ultimate_bin']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_7', 'kubejs:incomplete_stack_upgrade_tier_7'),
        sa.deploying('kubejs:incomplete_stack_upgrade_tier_7', ['kubejs:incomplete_stack_upgrade_tier_7', 'ae2:spatial_storage_cell_16']),
        sa.pressing('kubejs:incomplete_stack_upgrade_tier_7', 'kubejs:incomplete_stack_upgrade_tier_7')
    ]).transitionalItem('kubejs:incomplete_stack_upgrade_tier_7').loops(64).id('kubejs:sequenced_assembly/stack_upgrade_tier_7');

    sa.sequenced_assembly('sophisticatedbackpacks:inception_upgrade', 'backpack_allthemodium_upgrade:stack_upgrade_tier_7', [
        sa.deploying('kubejs:incomplete_inception_upgrade', ['kubejs:incomplete_inception_upgrade', 'kubejs:anomaly_replicator']),
        sa.deploying('kubejs:incomplete_inception_upgrade', ['kubejs:incomplete_inception_upgrade', 'kubejs:infinity_fragment']),
        sa.pressing('kubejs:incomplete_inception_upgrade', 'kubejs:incomplete_inception_upgrade')
    ]).transitionalItem('kubejs:incomplete_inception_upgrade').loops(8).id('kubejs:sequenced_assembly/inception_upgrade');

    sa.sequenced_assembly('sophisticatedbackpacks:everlasting_upgrade', 'backpack_allthemodium_upgrade:stack_upgrade_tier_7', [
        sa.deploying('kubejs:incomplete_everlasting_upgrade', ['kubejs:incomplete_everlasting_upgrade', 'kubejs:draconic_scale']),
        sa.deploying('kubejs:incomplete_everlasting_upgrade', ['kubejs:incomplete_everlasting_upgrade', 'kubejs:wither_soul']),
        sa.pressing('kubejs:incomplete_everlasting_upgrade', 'kubejs:incomplete_everlasting_upgrade')
    ]).transitionalItem('kubejs:incomplete_everlasting_upgrade').loops(8).id('kubejs:sequenced_assembly/everlasting_upgrade');

    console.log('[PEAK Expert Mode] Script 21: Backpack Upgrades loaded!');
});
