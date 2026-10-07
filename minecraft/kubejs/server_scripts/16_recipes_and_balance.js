// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 16
// RECIPES, BALANCE & ECONOMY
// ==========================================

ServerEvents.recipes(event => {
    // MALUM: HALLOWED GOLD REWORK
    event.remove({ id: 'malum:spirit_infusion/hallowed_gold_ingot' });
    event.remove({ type: 'create:mixing', output: 'malum:hallowed_gold_ingot' });
    event.remove({ type: 'create:mixing', output: '#c:ingots/hallowed_gold' }); // 1.21 uses #c instead of #forge sometimes
    event.custom({
        type: 'malum:spirit_infusion',
        input: { item: 'minecraft:gold_block' },
        extraInputs: [
            { item: 'minecraft:glowstone_dust', count: 4 }
        ],
        spirits: [
            { type: 'malum:sacred', count: 4 },
            { type: 'malum:arcane', count: 2 }
        ],
        result: { id: 'malum:hallowed_gold_ingot', count: 9 }
    });

    // NORTHSTAR: MARS IRON ORE CRUSHING RESTORATION
    event.remove({ id: 'northstar:crushing/mars_iron_ore' });
    event.remove({ id: 'northstar:crushing/mars_deep_iron_ore' });

    event.recipes.create.crushing([
        '1x northstar:raw_martian_iron_ore',
        CreateItem.of('northstar:raw_martian_iron_ore', 0.75),
        CreateItem.of('create:experience_nugget', 0.75),
        CreateItem.of('northstar:mars_stone', 0.125)
    ], 'northstar:mars_iron_ore').processingTime(250).id('northstar:crushing/mars_iron_ore');

    event.recipes.create.crushing([
        '2x northstar:raw_martian_iron_ore',
        CreateItem.of('northstar:raw_martian_iron_ore', 0.25),
        CreateItem.of('create:experience_nugget', 0.75),
        CreateItem.of('northstar:mars_deep_stone', 0.125)
    ], 'northstar:mars_deep_iron_ore').processingTime(350).id('northstar:crushing/mars_deep_iron_ore');

    // Elytra duplication
    event.shapeless('minecraft:elytra', ['minecraft:elytra', 'dragonloot:dragon_scale'])
        .keepIngredient('minecraft:elytra')
        .id('kubejs:elytra_duplication');

    // Dragon scale unification conversion
    event.shapeless('dragonloot:dragon_scale', 'kubejs:draconic_scale').id('kubejs:draconic_scale_to_dragonloot');

    console.log('[PEAK Expert Mode] Script 16: Recipes loaded!');
});

// RANGED DAMAGE REBALANCE
/*
EntityEvents.beforeHurt(event => {
    if (event.source.type === 'arrow' && event.source.actual) {
        if (event.source.actual.isPlayer()) {
            event.damage = event.damage * 1.5;
        }
    }
});
*/

// ECONOMY: WANDERING TRADER
MoreJS.wandererTrades(event => {
    event.removeTrades({ output: 'minecraft:ender_eye' });

    event.addTrade(2, ['10x minecraft:emerald_block'], 'kubejs:infinity_fragment');
    event.addTrade(2, ['5x minecraft:emerald_block'], 'minecraft:netherite_ingot');
    event.addTrade(2, ['1x minecraft:emerald_block'], '10x minecraft:experience_bottle');
    event.addTrade(2, ['3x minecraft:emerald_block'], 'ars_nouveau:source_gem_block');
});

console.log('[PEAK Expert Mode] Script 16: Combat & Economy loaded!');
