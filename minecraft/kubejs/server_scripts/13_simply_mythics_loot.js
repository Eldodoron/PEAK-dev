// ==========================================
// PEAK EXPERT MODE — SCRIPT 13
// SIMPLY SWORDS & BOWS: HYBRID MYTHIC LOOT
// ==========================================

LootJS.modifiers((event) => {
    // ---------------------------------------------------------
    // 1. GLOBAL DROP (ULTRA RARE)
    // ---------------------------------------------------------
    // 0.10% (1 in 1000) for Runic Tablet in ANY non-vanilla chest
    event.addTableModifier(LootType.CHEST, /^(?!minecraft:).*/)
        .randomChance(0.001)
        .addLoot('simplyswords:runic_tablet');

    // 0.05% (1 in 2000) for a random Mythic Bow in ANY non-vanilla chest
    event.addTableModifier(LootType.CHEST, /^(?!minecraft:).*/)
        .randomChance(0.0005)
        .addAlternativesLoot(
            'simplybows:bee_bow/bee_bow',
            'simplybows:blossom_bow/blossom_bow',
            'simplybows:bubble_bow/bubble_bow',
            'simplybows:earth_bow/earth_bow',
            'simplybows:echo_bow/echo_bow',
            'simplybows:ice_bow/ice_bow',
            'simplybows:vine_bow/vine_bow'
        );

    // ---------------------------------------------------------
    // 2. THEMATIC HIGH-TIER DROPS (5% - 1 in 20)
    // ---------------------------------------------------------
    
    // -- ICE & FIRE: Ice Dragon Caves (Ice Bow)
    event.addTableModifier(/iceandfire:chest\/ice_dragon_.*_cave/)
        .randomChance(0.05)
        .addLoot('simplybows:ice_bow/ice_bow');

    // -- ICE & FIRE: Lightning Dragon Caves (Echo Bow)
    event.addTableModifier(/iceandfire:chest\/lightning_dragon_.*_cave/)
        .randomChance(0.05)
        .addLoot('simplybows:echo_bow/echo_bow');

    // -- ICE & FIRE: Fire Dragon Caves (Runic Tablet)
    event.addTableModifier(/iceandfire:chest\/fire_dragon_.*_cave/)
        .randomChance(0.05)
        .addLoot('simplyswords:runic_tablet');

    // -- BETTER DESERT TEMPLES: Pharaoh's Tomb (Earth Bow)
    event.addTableModifier('betterdeserttemples:chests/tomb_pharaoh')
        .randomChance(0.05)
        .addLoot('simplybows:earth_bow/earth_bow');

    // -- THE LOST CASTLE (TLC): Treasure & Hided Chests (Random Bow & Tablet)
    event.addTableModifier([
        'tlc:chests/treasure',
        'tlc:chests/hided',
        'tlc:chests/throne'
    ])
        .randomChance(0.05)
        .addLoot('simplyswords:runic_tablet');

    event.addTableModifier([
        'tlc:chests/treasure',
        'tlc:chests/hided'
    ])
        .randomChance(0.05)
        .addAlternativesLoot(
            'simplybows:vine_bow/vine_bow',
            'simplybows:blossom_bow/blossom_bow',
            'simplybows:bee_bow/bee_bow'
        );

    // -- DUNGEONS ARISE / CATACLYSM / GENERAL: Any elite/treasure chest
    // This regex catches any chest that has "treasure", "boss", or "reward" in its name across any mod!
    event.addTableModifier(/.+chests?\/.*(treasure|boss|reward).*/)
        .randomChance(0.05)
        .addLoot('simplyswords:runic_tablet');
});

console.log('[PEAK Expert Mode] Script 13: Simply Mythics Hybrid Loot Injection loaded!');
