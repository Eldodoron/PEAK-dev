// ==========================================
// PEAK EXPERT MODE — SCRIPT 09
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
    
    if (entityType.includes('block_factorys_bosses')) {
        console.log('[DEBUG] A block factory boss DIED! Type: ' + entityType);
    }
    
    // Helper function to drop regular items
    const dropItem = (item, min, max) => {
        let count = min;
        if (max > min) {
            count = min + Math.floor(Math.random() * (max - min + 1));
        }
        if (count > 0) {
            let itemEntity = event.entity.block.createEntity('item');
            itemEntity.item = Item.of(item, count);
            itemEntity.mergeNbt({
                Invulnerable: 1,
                Age: -12000
            });
            itemEntity.setGlowing(true);
            itemEntity.spawn();
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
        dropItem('kubejs:infinity_fragment', 1, 3);
    }

    if (entityType === 'cataclysm:ender_guardian') {
        dropItem('kubejs:void_resonator', 1, 1);
        dropItem('kubejs:infinity_fragment', 1, 2);
    }

    if (entityType === 'cataclysm:ignis') {
        dropItem('kubejs:infernal_core', 1, 1);
        dropItem('kubejs:infinity_fragment', 1, 4);
    }

    if (entityType === 'cataclysm:the_leviathan') {
        dropItem('kubejs:abyssal_heart', 1, 1);
        dropItem('kubejs:infinity_fragment', 1, 4);
    }

    if (entityType === 'cataclysm:netherite_monstrosity') {
        dropItem('kubejs:infinity_fragment', 1, 3);
    }

    // ==========================================
    // ICE & FIRE BOSS DROPS
    // ==========================================

    if (entityType === 'iceandfire:fire_dragon' ||
        entityType === 'iceandfire:ice_dragon' ||
        entityType === 'iceandfire:lightning_dragon') {
        dropItem('kubejs:dragon_soul_gem', 1, 1);
        dropItem('kubejs:infinity_fragment', 1, 4);
    }

    // ==========================================
    // VANILLA BOSS DROPS
    // ==========================================

    if (entityType === 'minecraft:warden') {
        dropItem('kubejs:void_resonator', 1, 2);
        dropItem('kubejs:infinity_fragment', 1, 2);
    }

    if (entityType === 'minecraft:wither') {
        dropItem('kubejs:infinity_fragment', 1, 3);
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
    // ONCE-PER-PLAYER ENDER EYE DROP (PROXIMITY BASED)
    // ==========================================
    // To reward exploration, players get 1 Ender Eye the FIRST time 
    // they participate in defeating a specific unique boss.

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
        let closestPlayer = null;
        let minDistanceSq = 128 * 128; // 8 chunks radius squared
        let key = 'dropped_eye_' + entityType.replace(':', '_');
        
        // Find the closest player who has NOT received an eye from this boss yet
        let players = event.level.getPlayers();
        players.forEach(p => {
            if (p.level.dimension === event.entity.level.dimension) {
                let distSq = p.distanceToSqr(event.entity);
                if (distSq <= minDistanceSq) {
                    if (!p.persistentData.getBoolean(key)) {
                        closestPlayer = p;
                        minDistanceSq = distSq;
                    }
                }
            }
        });

        if (closestPlayer != null) {
            // Mark it as completed for this player
            closestPlayer.persistentData.putBoolean(key, true);
            
            // Spawn indestructible, 15-minute Ender Eye
            let itemEntity = event.entity.block.createEntity('item');
            itemEntity.item = Item.of('minecraft:ender_eye', 1);
            
            // Invulnerable: 1b makes it immune to lava, fire, and explosions.
            // Age: -12000 means it will take 18000 ticks (15 mins) to reach 6000 and despawn.
            itemEntity.mergeNbt({
                Invulnerable: 1,
                Age: -12000
            });
            
            // Add glowing effect so it's easy to find in the chaos
            itemEntity.setGlowing(true);
            
            itemEntity.spawn();
            
            closestPlayer.tell(Text.lightPurple('✦ You extracted a durable Ender Eye from defeating this powerful foe for the first time! ✦'));
        }
    }
});

console.log('[PEAK Expert Mode] Script 09: Custom Boss Loot Drops (via EntityEvents) loaded!');
