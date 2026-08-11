// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 09
// CUSTOM BOSS LOOT TABLES (via EntityEvents)
// ==========================================
// Each boss drops a unique custom component that
// feeds into the Expert Mode tech tree.
// We use EntityEvents.death to ensure compatibility
// across all KubeJS versions.
// ==========================================

EntityEvents.death(event => {
    // Only process if the entity is a living mob
    if (!event.entity.isLiving()) return;

    let entityType = event.entity.type;
    let source = event.source.actual;
    
    // Only drop special items if killed by a player
    if (!source || !source.isPlayer()) return;

    // Helper function to drop items
    const dropItem = (item, min, max) => {
        let count = min;
        if (max > min) {
            count = min + Math.floor(Math.random() * (max - min + 1));
        }
        if (count > 0) {
            event.entity.block.popItem(Item.of(item, count));
        }
    };

    // ==========================================
    // MOWZIE'S MOBS BOSS DROPS
    // ==========================================

    if (entityType === 'mowziesmobs:frostmaw') {
        dropItem('kubejs:frozen_heart_core', 1, 1);
    }
    
    if (entityType === 'mowziesmobs:ferrous_wroughtnaut') {
        dropItem('kubejs:infinity_fragment', 1, 2);
    }

    // ==========================================
    // TWILIGHT FOREST BOSS DROPS
    // ==========================================

    if (entityType === 'twilightforest:naga') {
        dropItem('kubejs:infinity_fragment', 1, 1);
    }

    if (entityType === 'twilightforest:lich') {
        dropItem('kubejs:lich_phylactery', 1, 1);
        dropItem('kubejs:infinity_fragment', 1, 3);
    }

    // ==========================================
    // CATACLYSM BOSS DROPS
    // ==========================================

    if (entityType === 'cataclysm:ancient_remnant') {
        dropItem('kubejs:primordial_core', 1, 1);
        dropItem('kubejs:infinity_fragment', 2, 4);
    }

    if (entityType === 'cataclysm:ender_guardian') {
        dropItem('kubejs:void_resonator', 1, 1);
        dropItem('kubejs:infinity_fragment', 2, 5);
    }

    if (entityType === 'cataclysm:ignis') {
        dropItem('kubejs:heart_of_the_inferno', 1, 1);
        dropItem('kubejs:infinity_fragment', 3, 6);
    }

    if (entityType === 'cataclysm:the_leviathan') {
        dropItem('kubejs:abyssal_catalyst', 1, 1);
        dropItem('kubejs:infinity_fragment', 2, 5);
    }

    if (entityType === 'cataclysm:netherite_monstrosity') {
        dropItem('kubejs:netheric_core', 1, 1);
        dropItem('kubejs:infinity_fragment', 2, 4);
    }

    // ==========================================
    // WARDEN â€” THE DEEP DARK GUARDIAN
    // ==========================================

    if (entityType === 'minecraft:warden') {
        dropItem('kubejs:sculk_heart', 1, 1);
        dropItem('kubejs:infinity_fragment', 2, 4);
    }

    // ==========================================
    // ICE AND FIRE â€” STAGE 5 DRAGONS
    // ==========================================

    if (entityType === 'iceandfire:fire_dragon' || 
        entityType === 'iceandfire:ice_dragon' || 
        entityType === 'iceandfire:lightning_dragon') {
        // High stage dragons drop primordial blood
        dropItem('kubejs:primordial_dragon_blood', 1, 1);
    }

    // ==========================================
    // ENDER DRAGON & WITHER â€” VANILLA BOSSES
    // ==========================================

    if (entityType === 'minecraft:ender_dragon') {
        dropItem('kubejs:void_resonator', 1, 1);
        dropItem('kubejs:infinity_fragment', 4, 8);
    }

    if (entityType === 'minecraft:wither') {
        dropItem('kubejs:infinity_fragment', 2, 5);
    }

    // ==========================================
    // BLOCK FACTORY'S BOSSES
    // ==========================================

    if (entityType === 'block_factorys_bosses:infernal_dragon' ||
        entityType === 'block_factorys_bosses:yeti' ||
        entityType === 'block_factorys_bosses:sandworm' ||
        entityType === 'block_factorys_bosses:kraken' ||
        entityType === 'block_factorys_bosses:underworld_knight') {
        dropItem('kubejs:infinity_fragment', 1, 3);
    }

    // ==========================================
    // ARS NOUVEAU BOSS (WILDEN CHIMERA)
    // ==========================================

    if (entityType === 'ars_nouveau:wilden_boss') {
        dropItem('kubejs:infinity_fragment', 1, 3);
    }

    // ==========================================
    // ALEX'S MOBS / ALEX'S CAVES BOSSES
    // ==========================================

    if (entityType === 'alexsmobs:void_worm') {
        dropItem('kubejs:void_resonator', 1, 1);
    }

    // ==========================================
    // ONCE-PER-PLAYER ENDER EYE DROP
    // ==========================================
    // To reward exploration, players get 1 Ender Eye the FIRST time 
    // they kill each specific boss type.

    const eyeBosses = [
        // Mowzie's Mobs
        'mowziesmobs:frostmaw',
        'mowziesmobs:ferrous_wroughtnaut',
        // Twilight Forest
        'twilightforest:naga',
        'twilightforest:lich',
        'twilightforest:minoshroom',
        'twilightforest:hydra',
        'twilightforest:ur_ghast',
        'twilightforest:alpha_yeti',
        'twilightforest:snow_queen',
        'twilightforest:knight_phantom',
        // L_Ender's Cataclysm
        'cataclysm:ancient_remnant',
        'cataclysm:ender_guardian',
        'cataclysm:ignis',
        'cataclysm:the_leviathan',
        'cataclysm:netherite_monstrosity',
        'cataclysm:the_harbinger',
        // Bosses of Mass Destruction
        'bosses_of_mass_destruction:lich',
        'bosses_of_mass_destruction:obsidilith',
        'bosses_of_mass_destruction:void_blossom',
        'bosses_of_mass_destruction:gauntlet',
        // Remnant Bosses
        'remnant_bosses:armored_grub',
        'remnant_bosses:bone_tyrant',
        'remnant_bosses:remnant_ossukage',
        // Vanilla / Ice & Fire / Alex's
        'minecraft:warden',
        'minecraft:wither',
        'iceandfire:fire_dragon',
        'iceandfire:ice_dragon',
        'iceandfire:lightning_dragon',
        'alexsmobs:void_worm',
        // Block Factory's Bosses
        'block_factorys_bosses:infernal_dragon',
        'block_factorys_bosses:yeti',
        'block_factorys_bosses:sandworm',
        'block_factorys_bosses:underworld_knight',
        'block_factorys_bosses:kraken',
        // Magic Bosses
        'ars_nouveau:wilden_boss',
        'irons_spellbooks:dead_king',
        'irons_spellbooks:fire_boss'
    ];

    if (eyeBosses.includes(entityType)) {
        let pData = source.persistentData;
        let key = 'dropped_eye_' + entityType.replace(':', '_');
        if (!pData.getBoolean(key)) {
            pData.putBoolean(key, true);
            event.entity.block.popItem(Item.of('minecraft:ender_eye', 1));
            source.tell(Text.lightPurple('\u2726 You extracted an Ender Eye from defeating this powerful foe for the first time! \u2726'));
        }
    }
});

console.log('[PEAK Expert Mode] Script 09: Custom Boss Loot Drops (via EntityEvents) loaded!');
