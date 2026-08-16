// ==========================================
// PEAK EXPERT MODE — SCRIPT 14
// WAYSTONES: BREAKABILITY BALANCE
// ==========================================

// Require a Diamond Pickaxe or better to mine them successfully
ServerEvents.tags('block', event => {
    event.add('minecraft:needs_diamond_tool', /waystones:.*/);
    event.add('minecraft:mineable/pickaxe', /waystones:.*/);
    
    // Natively allow Create Wrench to pick up waystones
    event.add('create:wrench_pickup', /waystones:.*/);
});

console.log('[PEAK Expert Mode] Script 14: Waystones Balance (Diamond Pickaxe, Native Wrench Pickup) loaded!');
