// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 19
// APOTHEOSIS & MOB GEAR SETS
// ==========================================

// 1. APOTHEOSIS BOSS CUSTOM WEAPONS (NO DROPS)
ServerEvents.generateData('peak', 'mob_gear', event => {
    // Correct path for Apotheosis Boss Gear: data/apotheosis/gear_sets/pinnacle/melee/expert_weapons.json
    event.json('apothic_enchanting:gear_sets/pinnacle/melee/expert_weapons', {
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
            },
            { "stack": { "id": "simplyswords:arcanethyst", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:awakened_lichblade", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:bramblethorn", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:brimstone_claymore", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:caelestis", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:chompolotl", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:dreadtide", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:emberblade", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:emberlash", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:enigma", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:flamewind", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:frostfall", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:harbinger", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:hearthflame", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:hiveheart", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:icewhisper", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:livyatan", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:magiblade", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:magiscythe", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:magispear", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:mjolnir", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:molten_edge", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:ribboncleaver", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:shadowsting", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:soulkeeper", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:soulpyre", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:soulrender", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:soulstealer", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:stars_edge", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:stormbringer", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:storms_edge", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:sunfire", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:sword_on_a_stick", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:tempest", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:thunderbrand", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:toxic_longsword", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:twisted_blade", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:watcher_claymore", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:watching_warglaive", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:waxweaver", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:whisperwind", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:wickpiercer", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplyswords:wraithfang", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:ascended_idol", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:black_pearl", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:blade_of_the_grotesque", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:boas_fang", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:brassturn", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:cindergorge", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:culterex", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:darksent", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:deaths_eyrie", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:earthshatter", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:exedrill", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:glimmerstep", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:grandfrost", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:great_slither", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:holylight", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:jester_penetrate", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:lustrous_moxie", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:matterbane", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:mimicry", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:molten_flare", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:myrmedge", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:perforiscus", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:revvengine", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:ruptured_idol", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:ruyi_jingu_bang", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:serpentine_valour", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:smouldering_ruin", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:soul_foreseer", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:stasis", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:tarnished_idol", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:the_blood_harvester", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:the_pan", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:the_vessel_breach", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:tidebreaker", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:timekeeper", "count": 1 }, "weight": 5, "drop_chance": 0.0 },
            { "stack": { "id": "simplymore:vipers_call", "count": 1 }, "weight": 5, "drop_chance": 0.0 }
        ],
        "offhands": [],
        "helmets": [],
        "chestplates": [],
        "leggings": [],
        "boots": [],
        "tags": ["apothic_enchanting:melee"]
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


    if (Platform.isLoaded('armoroftheages')) {
        helmets.push('armoroftheages:anubis_armor_head', 'armoroftheages:centurion_armor_head', 'armoroftheages:holy_armor_head', 'armoroftheages:o_yoroi_armor_head');
        chestplates.push('armoroftheages:anubis_armor_chest', 'armoroftheages:centurion_armor_chest', 'armoroftheages:holy_armor_chest', 'armoroftheages:o_yoroi_armor_chest');
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

    // Safely extract the biome ID to prevent KubeJS Either/Left wrapper crashes
    let currentBiomeId = { namespace: 'minecraft', path: 'plains', toString: function() { return 'minecraft:plains'; } };
    try {
        let biomeHolder = entity.level.getBiome(entity.blockPosition());
        if (biomeHolder.unwrapKey && biomeHolder.unwrapKey().isPresent()) {
            currentBiomeId = biomeHolder.unwrapKey().get().location();
        } else if (biomeHolder.unwrap && biomeHolder.unwrap().left().isPresent()) {
            currentBiomeId = biomeHolder.unwrap().left().get().location();
        }
    } catch(e) {}

    // Alex's Caves Logic: ONLY in Alex's Caves biomes
    if (Platform.isLoaded('alexscaves') && currentBiomeId.namespace == 'alexscaves') {
        helmets.push('alexscaves:diving_helmet', 'alexscaves:primordial_helmet', 'alexscaves:magnetic_helmet');
        chestplates.push('alexscaves:diving_chestplate', 'alexscaves:primordial_chestplate', 'alexscaves:magnetic_chestplate');
        bows.push('alexscaves:dreadbow');
    }

    // Deeper and Darker Logic: ONLY in Deep Dark or Otherside
    if (Platform.isLoaded('deeperdarker')) {
        var dimId = entity.level.dimension.toString();
        var biomeStr = currentBiomeId.toString();
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
        let trimData = { material: "minecraft:gold", pattern: "minecraft:ward" };
        entity.setItemSlot('head', helm.with('minecraft:trim', trimData));
        entity.setItemSlot('chest', chest.with('minecraft:trim', trimData));
        
        if (entity.type == 'minecraft:skeleton' || entity.type == 'minecraft:stray' || entity.type == 'minecraft:pillager') {
            let bowId = bows[Math.floor(Math.random() * bows.length)];
            entity.setItemSlot('mainhand', Item.of(bowId));
        }

        entity.setDropChance('head', 0.05);
        entity.setDropChance('chest', 0.05);
    }});

