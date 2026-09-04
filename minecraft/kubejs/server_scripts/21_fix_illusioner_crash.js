// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 21
// EMERGENCY FIX: ILLUSIONER CRASH (Friends & Foes + Apotheosis)
// ==========================================
// This script prevents a crash where named Illusioners (Apotheosis Bosses) 
// try to fire arrows using melee weapons they shouldn't have.
// ==========================================

const fixIllusionerWeapon = (entity) => {
    let mainhand = entity.getMainHandItem();
    if (!mainhand.id.contains('bow') && !mainhand.id.contains('crossbow')) {
        entity.setItemSlot('mainhand', 'minecraft:bow');
    }
};

EntityEvents.spawned('friendsandfoes:illusioner', event => {
    fixIllusionerWeapon(event.entity);
});

EntityEvents.spawned('minecraft:illusioner', event => {
    fixIllusionerWeapon(event.entity);
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

