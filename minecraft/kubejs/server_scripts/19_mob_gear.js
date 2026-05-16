// ==========================================
// PEAK EXPERT MODE — SCRIPT 19
// APOTHEOSIS & MOB GEAR SETS
// ==========================================

// 1. APOTHEOSIS BOSS CUSTOM WEAPONS (NO DROPS)
ServerEvents.generateData('peak', 'mob_gear', event => {
    // Correct path for Apotheosis Boss Gear: data/apotheosis/gear_sets/pinnacle/melee/expert_weapons.json
    event.json('apotheosis:gear_sets/pinnacle/melee/expert_weapons', {
        "weight": 200,
        "mainhands": [
            {
                "stack": { "id": "cataclysm:infernal_forge", "count": 1 },
                "weight": 20,
                "drop_chance": 0.0
            },
            {
                "stack": { "id": "cataclysm:void_forge", "count": 1 },
                "weight": 20,
                "drop_chance": 0.0
            },
            {
                "stack": { "id": "cataclysm:meat_shredder", "count": 1 },
                "weight": 20,
                "drop_chance": 0.0
            },
            {
                "stack": { "id": "cataclysm:the_incinerator", "count": 1 },
                "weight": 20,
                "drop_chance": 0.0
            },
            {
                "stack": { "id": "cataclysm:wither_assault_shoulder_weapon", "count": 1 },
                "weight": 10,
                "drop_chance": 0.0
            }
        ],
        "offhands": [],
        "helmets": [],
        "chestplates": [],
        "leggings": [],
        "boots": [],
        "tags": ["apotheosis:melee"]
    });
    
    console.log('[PEAK Expert Mode] Script 19: Boss Gear Data injected!');
});

// 2. MOB / ILLAGER CUSTOM ARMOR & TRIMS
EntityEvents.spawned(event => {
    const { entity, level, server } = event;
    if (!entity || !entity.living) return;

    // List of targets for custom gear
    const targets = [
        'minecraft:vindicator', 
        'minecraft:pillager', 
        'minecraft:evoker', 
        'minecraft:zombie', 
        'minecraft:skeleton',
        'minecraft:husk',
        'minecraft:stray'
    ];
    
    if (!targets.includes(entity.type)) return;

    // 15% chance to give them modded armor
    if (Math.random() > 0.15) return;

    // Define potential armor pieces with safety checks
    let helmets = ['minecraft:netherite_helmet', 'minecraft:diamond_helmet'];
    let chestplates = ['minecraft:netherite_chestplate', 'minecraft:diamond_chestplate'];
    let bows = ['minecraft:bow'];

    if (Platform.isLoaded('cataclysm')) {
        helmets.push('cataclysm:ignitium_helmet');
        chestplates.push('cataclysm:ignitium_chestplate');
    }
    
    if (Platform.isLoaded('iceandfire')) {
        helmets.push('iceandfire:armor_silver_metal_helmet');
        chestplates.push('iceandfire:armor_silver_metal_chestplate');
        bows.push('iceandfire:dragonbone_bow');
    }

    if (Platform.isLoaded('ars_nouveau')) {
        helmets.push('ars_nouveau:arcanist_hood');
        chestplates.push('ars_nouveau:arcanist_robes');
    }

    if (Platform.isLoaded('knightquest')) {
        helmets.push('knightquest:silver_knight_helmet', 'knightquest:iron_knight_helmet', 'knightquest:doom_helmet');
        chestplates.push('knightquest:silver_knight_chestplate', 'knightquest:iron_knight_chestplate', 'knightquest:doom_chestplate');
    }

    if (Platform.isLoaded('armoroftheages')) {
        helmets.push('armoroftheages:anubis_helmet', 'armoroftheages:centurion_helmet', 'armoroftheages:holy_helmet', 'armoroftheages:samurai_helmet');
        chestplates.push('armoroftheages:anubis_chestplate', 'armoroftheages:centurion_chestplate', 'armoroftheages:holy_chestplate', 'armoroftheages:samurai_chestplate');
    }

    if (Platform.isLoaded('fantasy_armor')) {
        helmets.push('fantasy_armor:dead_gladiator_helmet', 'fantasy_armor:evening_ghost_helmet', 'fantasy_armor:ornstein_helmet');
        chestplates.push('fantasy_armor:dead_gladiator_chestplate', 'fantasy_armor:evening_ghost_chestplate', 'fantasy_armor:ornstein_chestplate');
    }

    if (Platform.isLoaded('immersive_armors')) {
        helmets.push('immersive_armors:heavy_helmet', 'immersive_armors:divine_helmet', 'immersive_armors:bone_helmet');
        chestplates.push('immersive_armors:heavy_chestplate', 'immersive_armors:divine_chestplate', 'immersive_armors:bone_chestplate');
    }

    if (Platform.isLoaded('simplybows')) {
        bows.push('simplybows:ice_bow', 'simplybows:bee_bow', 'simplybows:echo_bow', 'simplybows:vine_bow');
    }

    if (Platform.isLoaded('twilightforest')) {
        helmets.push('twilightforest:knightmetal_helmet', 'twilightforest:ironwood_helmet');
        chestplates.push('twilightforest:knightmetal_chestplate', 'twilightforest:ironwood_chestplate');
        bows.push('twilightforest:triple_bow', 'twilightforest:seeker_bow');
    }

    // Alex's Caves Logic: ONLY in Alex's Caves biomes
    const currentBiomeId = entity.level.getBiome(entity.blockPosition()).unwrap().key().location();
    if (Platform.isLoaded('alexscaves') && currentBiomeId.namespace == 'alexscaves') {
        helmets.push('alexscaves:diving_helmet', 'alexscaves:primordial_helmet', 'alexscaves:magnetic_helmet');
        chestplates.push('alexscaves:diving_chestplate', 'alexscaves:primordial_chestplate', 'alexscaves:magnetic_chestplate');
        bows.push('alexscaves:dreadbow');
    }

    // Deeper and Darker Logic: ONLY in Deep Dark or Otherside
    if (Platform.isLoaded('deeperdarker')) {
        const dimId = entity.level.dimension.location().toString();
        const biomeStr = currentBiomeId.toString();
        if (biomeStr == 'minecraft:deep_dark' || dimId == 'deeperdarker:otherside') {
            helmets.push('deeperdarker:warden_helmet', 'deeperdarker:resonarium_helmet');
            chestplates.push('deeperdarker:warden_chestplate', 'deeperdarker:resonarium_chestplate');
        }
    }
    
    // Choose randomly
    let randomIndex = Math.floor(Math.random() * helmets.length);
    let helmId = helmets[randomIndex];
    let chestId = chestplates[randomIndex] || chestplates[0];

    let helm = Item.of(helmId);
    let chest = Item.of(chestId);

    if (!helm.empty && !chest.empty) {
        const trimData = { material: "minecraft:gold", pattern: "minecraft:ward" };
        entity.setItemSlot('head', helm.withComponent('minecraft:trim', trimData));
        entity.setItemSlot('chest', chest.withComponent('minecraft:trim', trimData));
        
        if (entity.type == 'minecraft:skeleton' || entity.type == 'minecraft:stray' || entity.type == 'minecraft:pillager') {
            let bowId = bows[Math.floor(Math.random() * bows.length)];
            entity.setItemSlot('mainhand', Item.of(bowId));
        }

        entity.setDropChance('head', 0.05);
        entity.setDropChance('chest', 0.05);
    }
});
