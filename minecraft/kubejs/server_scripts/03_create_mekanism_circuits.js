// ==========================================
// CREATE SEQUENCED ASSEMBLY: MEKANISM CIRCUITS
// ==========================================

ServerEvents.recipes(event => {
    const sa = event.recipes.create;

    // 1. Basic Control Circuit
    // Osmium Ingot + 2x Redstone Dust + Mechanical Press
    sa.sequenced_assembly(
        'mekanism:basic_control_circuit',
        '#c:ingots/osmium',
        [
            sa.deploying('alltheores:osmium_ingot', ['alltheores:osmium_ingot', 'minecraft:redstone']),
            sa.deploying('alltheores:osmium_ingot', ['alltheores:osmium_ingot', 'minecraft:redstone']),
            sa.pressing('alltheores:osmium_ingot', 'alltheores:osmium_ingot')
        ]
    ).transitionalItem('alltheores:osmium_ingot').loops(1).id('kubejs:sequenced_assembly/basic_control_circuit');

    // 2. Advanced Control Circuit
    // Basic Control Circuit + 2x Infused Alloy + Mechanical Press
    sa.sequenced_assembly(
        'mekanism:advanced_control_circuit',
        'mekanism:basic_control_circuit',
        [
            sa.deploying('mekanism:basic_control_circuit', ['mekanism:basic_control_circuit', 'mekanism:alloy_infused']),
            sa.deploying('mekanism:basic_control_circuit', ['mekanism:basic_control_circuit', 'mekanism:alloy_infused']),
            sa.pressing('mekanism:basic_control_circuit', 'mekanism:basic_control_circuit')
        ]
    ).transitionalItem('mekanism:basic_control_circuit').loops(1).id('kubejs:sequenced_assembly/advanced_control_circuit');

    // 3. Elite Control Circuit
    // Advanced Control Circuit + 2x Reinforced Alloy + Mechanical Press
    sa.sequenced_assembly(
        'mekanism:elite_control_circuit',
        'mekanism:advanced_control_circuit',
        [
            sa.deploying('mekanism:advanced_control_circuit', ['mekanism:advanced_control_circuit', 'mekanism:alloy_reinforced']),
            sa.deploying('mekanism:advanced_control_circuit', ['mekanism:advanced_control_circuit', 'mekanism:alloy_reinforced']),
            sa.pressing('mekanism:advanced_control_circuit', 'mekanism:advanced_control_circuit')
        ]
    ).transitionalItem('mekanism:advanced_control_circuit').loops(1).id('kubejs:sequenced_assembly/elite_control_circuit');

    // 4. Ultimate Control Circuit
    // Elite Control Circuit + 2x Atomic Alloy + Mechanical Press
    sa.sequenced_assembly(
        'mekanism:ultimate_control_circuit',
        'mekanism:elite_control_circuit',
        [
            sa.deploying('mekanism:elite_control_circuit', ['mekanism:elite_control_circuit', 'mekanism:alloy_atomic']),
            sa.deploying('mekanism:elite_control_circuit', ['mekanism:elite_control_circuit', 'mekanism:alloy_atomic']),
            sa.pressing('mekanism:elite_control_circuit', 'mekanism:elite_control_circuit')
        ]
    ).transitionalItem('mekanism:elite_control_circuit').loops(1).id('kubejs:sequenced_assembly/ultimate_control_circuit');
});
