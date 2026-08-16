// ==========================================
// PEAK EXPERT MODE — SCRIPT 14
// WAYSTONES: BREAKABILITY BALANCE
// ==========================================

// Make all Waystone blocks extremely hard to break and immune to explosions
BlockEvents.modification(event => {
    event.modify(/waystones:.*/, block => {
        block.destroySpeed = 50.0; // Obsidian hardness
        block.explosionResistance = 1200.0; // Immune to TNT/Creepers
        block.requiresTool = true;
    });
});

console.log('[PEAK Expert Mode] Script 14: Waystones Block Modification loaded!');
