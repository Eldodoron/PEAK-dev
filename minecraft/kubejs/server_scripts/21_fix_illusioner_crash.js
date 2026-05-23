// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 21
// EMERGENCY FIX: ILLUSIONER CRASH (Friends & Foes + Apotheosis)
// ==========================================
// This script prevents a crash where named Illusioners (Apotheosis Bosses) 
// try to fire arrows using melee weapons they shouldn't have.
// ==========================================

EntityEvents.spawned('friendsandfoes:illusioner', event => {
    const { entity } = event;
    
    // Check if the entity has a weapon that isn't a bow
    let mainhand = entity.getMainHandItem();
    
    // If it's empty or not a bow/crossbow, and the entity is an illusioner, give it a bow
    // We check for common bow types.
    if (!mainhand.id.contains('bow') && !mainhand.id.contains('crossbow')) {
        entity.setItemSlot('mainhand', 'minecraft:bow');
        
        // Log it so the user knows the fix is working
        console.log(`[PEAK Fix] Corrected invalid weapon on Illusioner (${entity.customName || 'Unnamed'}) to prevent crash.`);
    }
});

// Also try to disable Illusioner from being an Apotheosis boss via data injection
ServerEvents.generateData('peak', 'apoth_fix', event => {
    // This tells Apotheosis NOT to spawn bosses of this type if possible
    event.json('apothic_enchanting:bosses/friendsandfoes/illusioner', {
        "entity": "friendsandfoes:illusioner",
        "weight": 0, // Set weight to 0 to disable
        "dimensions": [],
        "valid_gear_sets": ["apothic_enchanting:empty"]
    });
});

console.log('[PEAK Expert Mode] Script 21: Illusioner Crash Fix loaded!');

