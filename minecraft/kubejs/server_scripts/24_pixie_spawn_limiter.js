// ============================================================
// 24_pixie_spawn_limiter.js
// PEAK Dev - Optimization: Ice and Fire Pixie Spawn Reduction
// ------------------------------------------------------------
// PROBLEM: Profile x9cp2EvvpA / 8A6WsMMiBM showed 51 iceandfire:pixie
//          entities in loaded chunks causing significant entity tick
//          overhead due to their flying AI and particle systems.
// FIX:     Cancel ~45% of natural pixie spawns to keep population
//          around 28 max in loaded chunks. Pixies are preserved
//          gameplay-wise but at a reasonable density.
// NOTE:    IaF pixie "size" also reduced to 3 (from 5) in iaf-common.json
//          to reduce per-entity particle emission.
// ============================================================

EntityEvents.spawned('iceandfire:pixie', event => {
    const { entity } = event;
    
    // Skip pixies already loaded from disk in saved chunks
    if (entity.persistentData.getBoolean('peak_spawn_processed')) {
        return;
    }
    
    // Mark as processed so it is not re-evaluated on subsequent chunk loads
    entity.persistentData.putBoolean('peak_spawn_processed', true);
    
    // Cancel ~45% of new natural spawns to maintain optimal population density
    if (Math.random() < 0.45) {
        event.cancel();
    }
});
