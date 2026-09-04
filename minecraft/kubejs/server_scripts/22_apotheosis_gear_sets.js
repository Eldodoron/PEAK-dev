// ==========================================
// PEAK EXPERT MODE Ã¢â‚¬â€ SCRIPT 22
// APOTHEOSIS MASTER EXPERT POOLS
// ==========================================

// This script injects custom gear sets for Apotheosis Bosses.
// We use ServerEvents.generateData to ensure they are registered correctly in 1.21.
ServerEvents.generateData('peak', 'apotheosis_gear', event => {
    
    // --- MELEE EXPERT POOL ---
    const createExpertPool = (tier, weight) => {
        return {
            "weight": weight,
            "mainhands": [
                { "stack": { "id": "simplyswords:iron_longsword" }, "weight": 10 },
                { "stack": { "id": "simplyswords:diamond_katana" }, "weight": 10 },
                { "stack": { "id": "simplyswords:gold_rapier" }, "weight": 10 },
                { "stack": { "id": "simplyswords:iron_claymore" }, "weight": 10 },
                { "stack": { "id": "simplyswords:iron_glaive" }, "weight": 10 },
                { "stack": { "id": "simplymore:iron_grandsword" }, "weight": 5 },
                { "stack": { "id": "iceandfire:dragonbone_sword" }, "weight": 5 }
            ],
            "helmets": [
                { "stack": { "id": "armoroftheages:samurai_helmet" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:anubis_helmet" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:centurion_helmet" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:dead_gladiator_helmet" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:evening_ghost_helmet" }, "weight": 10 },
                { "stack": { "id": "immersive_armors:heavy_helmet" }, "weight": 10 },
                { "stack": { "id": "ars_nouveau:arcanist_hood" }, "weight": 10 },
                { "stack": { "id": "iceandfire:armor_red_helmet" }, "weight": 5 },
                { "stack": { "id": "iceandfire:armor_blue_helmet" }, "weight": 5 },
                { "stack": { "id": "iceandfire:armor_silver_metal_helmet" }, "weight": 5 },
                { "stack": { "id": "mowziesmobs:wrought_helmet", "drop_chance": 0.0 }, "weight": 5 }
            ],
            "chestplates": [
                { "stack": { "id": "armoroftheages:samurai_chestplate" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:anubis_chestplate" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:centurion_chestplate" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:dead_gladiator_chestplate" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:evening_ghost_chestplate" }, "weight": 10 },
                { "stack": { "id": "immersive_armors:heavy_chestplate" }, "weight": 10 },
                { "stack": { "id": "ars_nouveau:arcanist_robes" }, "weight": 10 },
                { "stack": { "id": "iceandfire:armor_red_chestplate" }, "weight": 5 },
                { "stack": { "id": "iceandfire:armor_blue_chestplate" }, "weight": 5 },
                { "stack": { "id": "iceandfire:armor_silver_metal_chestplate" }, "weight": 5 }
            ],
            "leggings": [
                { "stack": { "id": "armoroftheages:samurai_leggings" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:dead_gladiator_leggings" }, "weight": 10 },
                { "stack": { "id": "immersive_armors:heavy_leggings" }, "weight": 10 },
                { "stack": { "id": "ars_nouveau:arcanist_leggings" }, "weight": 10 },
                { "stack": { "id": "iceandfire:armor_red_leggings" }, "weight": 5 }
            ],
            "boots": [
                { "stack": { "id": "armoroftheages:samurai_boots" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:dead_gladiator_boots" }, "weight": 10 },
                { "stack": { "id": "immersive_armors:heavy_boots" }, "weight": 10 },
                { "stack": { "id": "ars_nouveau:arcanist_boots" }, "weight": 10 },
                { "stack": { "id": "iceandfire:armor_red_boots" }, "weight": 5 }
            ],
            "tags": ["apothic_enchanting:melee", `apothic_enchanting:${tier}`]
        };
    };

    // Inject the pool for multiple tiers
    event.json('apothic_enchanting:gear_sets/overworld/expert_pool_g1.json', createExpertPool('overworld', 100));
    event.json('apothic_enchanting:gear_sets/nether/expert_pool_g1.json', createExpertPool('nether', 100));
    event.json('apothic_enchanting:gear_sets/the_end/expert_pool_g1.json', createExpertPool('the_end', 100));

    // --- RANGED EXPERT POOL ---
    const createRangedPool = (tier, weight) => {
        return {
            "weight": weight,
            "mainhands": [
                { "stack": { "id": "simplybows:ice_bow/ice_bow" }, "weight": 10 },
                { "stack": { "id": "simplybows:bee_bow/bee_bow" }, "weight": 10 },
                { "stack": { "id": "simplybows:echo_bow/echo_bow" }, "weight": 10 },
                { "stack": { "id": "simplybows:vine_bow/vine_bow" }, "weight": 10 },
                { "stack": { "id": "simplybows:bubble_bow/bubble_bow" }, "weight": 10 },
                { "stack": { "id": "simplybows:earth_bow/earth_bow" }, "weight": 10 },
                { "stack": { "id": "iceandfire:dragonbone_bow" }, "weight": 10 }
            ],
            "helmets": [
                { "stack": { "id": "armoroftheages:samurai_helmet" }, "weight": 10 },
                { "stack": { "id": "ars_nouveau:arcanist_hood" }, "weight": 20 }
            ],
            "chestplates": [
                { "stack": { "id": "ars_nouveau:arcanist_robes" }, "weight": 20 }
            ],
            "tags": ["apothic_enchanting:ranged", `apothic_enchanting:${tier}`]
        };
    };

    event.json('apothic_enchanting:gear_sets/overworld/expert_ranged.json', createRangedPool('overworld', 80));
    event.json('apothic_enchanting:gear_sets/nether/expert_ranged.json', createRangedPool('nether', 80));
    event.json('apothic_enchanting:gear_sets/pinnacle/expert_ranged.json', createRangedPool('pinnacle', 80));

    // --- PINNACLE UNIQUES POOL ---
    event.json('apothic_enchanting:gear_sets/pinnacle/expert_uniques.json', {
        "weight": 150,
        "mainhands": [
            { "stack": { "id": "simplyswords:brimstone" }, "weight": 5 },
            { "stack": { "id": "simplyswords:caelestis" }, "weight": 5 },
            { "stack": { "id": "simplyswords:emberblade" }, "weight": 5 },
            { "stack": { "id": "simplyswords:frostfall" }, "weight": 5 },
            { "stack": { "id": "simplyswords:harbinger" }, "weight": 5 },
            { "stack": { "id": "simplyswords:hearthflame" }, "weight": 5 },
            { "stack": { "id": "simplyswords:icewhisper" }, "weight": 5 },
            { "stack": { "id": "simplyswords:lichblade" }, "weight": 5 },
            { "stack": { "id": "simplyswords:mjolnir" }, "weight": 5 },
            { "stack": { "id": "simplyswords:ribboncleaver" }, "weight": 5 },
            { "stack": { "id": "simplyswords:soulpyre" }, "weight": 5 },
            { "stack": { "id": "simplyswords:stormbringer" }, "weight": 5 },
            { "stack": { "id": "simplyswords:sunfire" }, "weight": 5 },
            { "stack": { "id": "simplyswords:thunderbrand" }, "weight": 5 },
            { "stack": { "id": "simplyswords:whisperwind" }, "weight": 5 },
            { "stack": { "id": "cataclysm:the_incinerator" }, "weight": 10 },
            { "stack": { "id": "cataclysm:void_forge" }, "weight": 10 },
            { "stack": { "id": "cataclysm:gauntlet_of_guard" }, "weight": 10 }
        ],
        "helmets": [
            { "stack": { "id": "fantasy_armor:ornstein_helmet" }, "weight": 10 },
            { "stack": { "id": "iceandfire:armor_red_helmet" }, "weight": 10 },
            { "stack": { "id": "cataclysm:ignitium_helmet" }, "weight": 10 }
        ],
        "chestplates": [
            { "stack": { "id": "fantasy_armor:ornstein_chestplate" }, "weight": 10 },
            { "stack": { "id": "cataclysm:ignitium_chestplate" }, "weight": 10 }
        ],
        "tags": ["apothic_enchanting:melee", "apothic_enchanting:pinnacle"]
    });

    console.log('[PEAK Expert Mode] Script 22: Master Expert Pools Injected!');
});

