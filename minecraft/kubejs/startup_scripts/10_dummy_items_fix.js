// priority: 10

// This script registers dummy items to fix broken tags caused by mods adding non-existent items.
// If a tag JSON references a missing item without "required": false, the ENTIRE tag fails to load.
StartupEvents.registry('item', event => {
    // allthemodium references this in data/minecraft/tags/item/enchantable/bow.json
    // Since it doesn't exist, it breaks all bow enchantments (Power, Punch, Flame, Infinity).
    // Registering it as a dummy item prevents the tag from failing.
    event.create('allthemodium:allthemodium_bow');
    event.create('allthemodium:unobtainium_crossbow');
    
    // Fixes minecraft:enchantable/equippable -> c:tools/shield -> etc.
    event.create('allthemodium:vibranium_shield');
    event.create('darkermagic:whispers_staff');
});
