// ==========================================
// PEAK EXPERT MODE — SCRIPT 16
// RECIPES, BALANCE & ECONOMY
// ==========================================

// DIAGNOSTIC: Try different class paths
try { console.info('STAGES 1: ' + Java.loadClass('dev.latvian.mods.kubejs.data.GeneratedDataStage').values()) } catch(e) {}
try { console.info('STAGES 2: ' + Java.loadClass('dev.latvian.kubejs.data.GeneratedDataStage').values()) } catch(e) {}

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

    console.log('[PEAK Expert Mode] Script 16: Recipes loaded!');
});

// RANGED DAMAGE REBALANCE
/*
EntityEvents.hurt(event => {
    if (event.source.type === 'arrow' && event.source.actual) {
        if (event.source.actual.isPlayer()) {
            event.amount = event.amount * 1.5;
        }
    }
});
*/

// ECONOMY: WANDERING TRADER
MoreJS.wandererTrades(event => {
    event.addTrade(2, ['10x minecraft:emerald_block'], 'kubejs:infinity_fragment');
    event.addTrade(2, ['5x minecraft:emerald_block'], 'minecraft:netherite_ingot');
    event.addTrade(2, ['1x minecraft:emerald_block'], '10x minecraft:experience_bottle');
    event.addTrade(2, ['3x minecraft:emerald_block'], 'ars_nouveau:source_gem_block');
});

console.log('[PEAK Expert Mode] Script 16: Combat & Economy loaded!');
