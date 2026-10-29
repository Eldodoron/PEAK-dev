// ==========================================
// PEAK EXPERT MODE - SCRIPT 22
// APOTHEOSIS MASTER EXPERT POOLS
// ==========================================

// This script injects custom gear sets for Apotheosis Bosses.
// Registers custom gear set data via ServerEvents.generateData for 1.21 datapack generation.
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
                { "stack": { "id": "armoroftheages:o_yoroi_armor_head" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:anubis_armor_head" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:centurion_armor_head" }, "weight": 10 },
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
                { "stack": { "id": "armoroftheages:o_yoroi_armor_chest" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:anubis_armor_chest" }, "weight": 10 },
                { "stack": { "id": "armoroftheages:centurion_armor_chest" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:dead_gladiator_chestplate" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:evening_ghost_chestplate" }, "weight": 10 },
                { "stack": { "id": "immersive_armors:heavy_chestplate" }, "weight": 10 },
                { "stack": { "id": "ars_nouveau:arcanist_robes" }, "weight": 10 },
                { "stack": { "id": "iceandfire:armor_red_chestplate" }, "weight": 5 },
                { "stack": { "id": "iceandfire:armor_blue_chestplate" }, "weight": 5 },
                { "stack": { "id": "iceandfire:armor_silver_metal_chestplate" }, "weight": 5 }
            ],
            "leggings": [
                { "stack": { "id": "armoroftheages:o_yoroi_armor_legs" }, "weight": 10 },
                { "stack": { "id": "fantasy_armor:dead_gladiator_leggings" }, "weight": 10 },
                { "stack": { "id": "immersive_armors:heavy_leggings" }, "weight": 10 },
                { "stack": { "id": "ars_nouveau:arcanist_leggings" }, "weight": 10 },
                { "stack": { "id": "iceandfire:armor_red_leggings" }, "weight": 5 }
            ],
            "boots": [
                { "stack": { "id": "armoroftheages:o_yoroi_armor_feet" }, "weight": 10 },
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
                { "stack": { "id": "armoroftheages:o_yoroi_armor_head" }, "weight": 10 },
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
            { "stack": { "id": "simplyswords:brimstone_claymore" }, "weight": 5 },
            { "stack": { "id": "simplyswords:caelestis" }, "weight": 5 },
            { "stack": { "id": "simplyswords:emberblade" }, "weight": 5 },
            { "stack": { "id": "simplyswords:frostfall" }, "weight": 5 },
            { "stack": { "id": "simplyswords:harbinger" }, "weight": 5 },
            { "stack": { "id": "simplyswords:hearthflame" }, "weight": 5 },
            { "stack": { "id": "simplyswords:icewhisper" }, "weight": 5 },
            { "stack": { "id": "simplyswords:awakened_lichblade" }, "weight": 5 },
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

    // --- FALLEN GEMS & AFFIXES 8.9.0 COMPATIBILITY OVERRIDES ---
    // Replaces legacy fallen_gems_affixes:spell_effect gem bonuses with apotheosis:mob_effect
    // so they use AbilityCooldowns in Apotheosis 8.9.0 / Apothic Attributes 2.11.0.
    event.json('fallen_gems_affixes:extra_gem_bonuses/compat/thunderheart_fragment_boots.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "cataclysm_spellbooks" }],
        "type": "apotheosis:extra_gem_bonus",
        "gem": "fallen_gems_affixes:compat/thunderheart_fragment",
        "bonuses": [
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "boots", "types": ["apotheosis:boots"] },
                "mob_effect": "cataclysm_spellbooks:rewired_effect",
                "target": "hurt_self",
                "values": {
                    "flawed": { "duration": 140, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 200, "amplifier": 0, "cooldown": 500 },
                    "flawless": { "duration": 260, "amplifier": 1, "cooldown": 500 },
                    "perfect": { "duration": 320, "amplifier": 1, "cooldown": 500 }
                }
            }
        ]
    });

    event.json('fallen_gems_affixes:extra_gem_bonuses/compat/voidmancers_eye_boots.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "cataclysm_spellbooks" }],
        "type": "apotheosis:extra_gem_bonus",
        "gem": "fallen_gems_affixes:compat/voidmancers_eye",
        "bonuses": [
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "boots", "types": ["apotheosis:boots"] },
                "mob_effect": "cataclysm_spellbooks:abyssal_predator_effect",
                "target": "hurt_self",
                "values": {
                    "flawed": { "duration": 140, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 200, "amplifier": 1, "cooldown": 500 },
                    "flawless": { "duration": 260, "amplifier": 2, "cooldown": 500 },
                    "perfect": { "duration": 320, "amplifier": 2, "cooldown": 500 }
                }
            }
        ]
    });

    event.json('fallen_gems_affixes:gems/compat/arcane_catalyst.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "irons_spellbooks" }],
        "type": "apotheosis:gem",
        "weights": { "quality": 0, "weight": 10 },
        "dimensions": [],
        "unique": true,
        "min_purity": "flawed",
        "bonuses": [
            {
                "type": "fallen_gems_affixes:con_cat_bonus",
                "con_cat": [
                    { "modid": "irons_apothic", "category": "fallen_gems_affixes:staffs", "not_mode": true },
                    { "modid": "irons_apothic", "category": "irons_apothic:staff" }
                ],
                "bonus": {
                    "type": "apotheosis:attribute",
                    "gem_class": { "key": "staffs", "types": [] },
                    "attribute": "irons_spellbooks:evocation_spell_power",
                    "operation": "add_multiplied_total",
                    "values": { "flawed": 0.15, "normal": 0.175, "flawless": 0.2, "perfect": 0.25 }
                }
            },
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "boots", "types": ["apotheosis:boots"] },
                "mob_effect": "irons_spellbooks:rend",
                "target": "attack_target",
                "values": {
                    "flawed": { "duration": 140, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 200, "amplifier": 1, "cooldown": 500 },
                    "flawless": { "duration": 260, "amplifier": 2, "cooldown": 500 },
                    "perfect": { "duration": 320, "amplifier": 3, "cooldown": 500 }
                }
            },
            {
                "type": "apotheosis:attribute",
                "gem_class": { "key": "chestplate", "types": ["apotheosis:chestplate"] },
                "attribute": "irons_spellbooks:evocation_magic_resist",
                "operation": "add_multiplied_base",
                "values": { "flawed": 0.1, "normal": 0.125, "flawless": 0.15, "perfect": 0.2 }
            }
        ]
    });

    event.json('fallen_gems_affixes:gems/compat/divine_stone.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "irons_spellbooks" }],
        "type": "apotheosis:gem",
        "weights": { "quality": 0, "weight": 10 },
        "dimensions": [],
        "unique": true,
        "min_purity": "flawed",
        "bonuses": [
            {
                "type": "fallen_gems_affixes:con_cat_bonus",
                "con_cat": [
                    { "modid": "irons_apothic", "category": "fallen_gems_affixes:staffs", "not_mode": true },
                    { "modid": "irons_apothic", "category": "irons_apothic:staff" }
                ],
                "bonus": {
                    "type": "apotheosis:attribute",
                    "gem_class": { "key": "staffs", "types": [] },
                    "attribute": "irons_spellbooks:holy_spell_power",
                    "operation": "add_multiplied_total",
                    "values": { "flawed": 0.15, "normal": 0.175, "flawless": 0.2, "perfect": 0.25 }
                }
            },
            {
                "type": "apotheosis:attribute",
                "gem_class": { "key": "helmet", "types": ["apotheosis:helmet"] },
                "attribute": "irons_spellbooks:holy_magic_resist",
                "operation": "add_multiplied_base",
                "values": { "flawed": 0.1, "normal": 0.125, "flawless": 0.15, "perfect": 0.2 }
            },
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "leggings", "types": ["apotheosis:leggings"] },
                "mob_effect": "irons_spellbooks:guided",
                "target": "attack_self",
                "values": {
                    "flawed": { "duration": 70, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 140, "amplifier": 1, "cooldown": 500 },
                    "flawless": { "duration": 210, "amplifier": 2, "cooldown": 500 },
                    "perfect": { "duration": 280, "amplifier": 3, "cooldown": 500 }
                }
            },
            {
                "type": "fallen_gems_affixes:permanent_effect",
                "gem_class": { "key": "chestplate", "types": ["apotheosis:chestplate"] },
                "effect": "irons_spellbooks:hastened",
                "values": { "flawed": 0, "normal": 1, "flawless": 2, "perfect": 3 }
            }
        ]
    });

    event.json('fallen_gems_affixes:gems/compat/emberheart_shard.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "irons_spellbooks" }],
        "type": "apotheosis:gem",
        "weights": { "quality": 0, "weight": 10 },
        "dimensions": [],
        "unique": true,
        "min_purity": "flawed",
        "bonuses": [
            {
                "type": "fallen_gems_affixes:con_cat_bonus",
                "con_cat": [
                    { "modid": "irons_apothic", "category": "fallen_gems_affixes:staffs", "not_mode": true },
                    { "modid": "irons_apothic", "category": "irons_apothic:staff" }
                ],
                "bonus": {
                    "type": "apotheosis:attribute",
                    "gem_class": { "key": "staffs", "types": [] },
                    "attribute": "irons_spellbooks:fire_spell_power",
                    "operation": "add_multiplied_total",
                    "values": { "flawed": 0.15, "normal": 0.175, "flawless": 0.2, "perfect": 0.25 }
                }
            },
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "helmet", "types": ["apotheosis:helmet"] },
                "mob_effect": "minecraft:fire_resistance",
                "target": "hurt_self",
                "values": {
                    "flawed": { "duration": 140, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 200, "amplifier": 1, "cooldown": 500 },
                    "flawless": { "duration": 260, "amplifier": 2, "cooldown": 500 },
                    "perfect": { "duration": 320, "amplifier": 3, "cooldown": 500 }
                }
            },
            {
                "type": "apotheosis:attribute",
                "gem_class": { "key": "boots", "types": ["apotheosis:boots"] },
                "attribute": "irons_spellbooks:fire_magic_resist",
                "operation": "add_multiplied_base",
                "values": { "flawed": 0.1, "normal": 0.125, "flawless": 0.15, "perfect": 0.2 }
            }
        ]
    });

    event.json('fallen_gems_affixes:gems/compat/frostvein_crystal.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "irons_spellbooks" }],
        "type": "apotheosis:gem",
        "weights": { "quality": 0, "weight": 10 },
        "dimensions": [],
        "unique": true,
        "min_purity": "flawed",
        "bonuses": [
            {
                "type": "fallen_gems_affixes:con_cat_bonus",
                "con_cat": [
                    { "modid": "irons_apothic", "category": "fallen_gems_affixes:staffs", "not_mode": true },
                    { "modid": "irons_apothic", "category": "irons_apothic:staff" }
                ],
                "bonus": {
                    "type": "apotheosis:attribute",
                    "gem_class": { "key": "staffs", "types": [] },
                    "attribute": "irons_spellbooks:ice_spell_power",
                    "operation": "add_multiplied_total",
                    "values": { "flawed": 0.15, "normal": 0.175, "flawless": 0.2, "perfect": 0.25 }
                }
            },
            {
                "type": "apotheosis:attribute",
                "gem_class": { "key": "leggings", "types": ["apotheosis:leggings"] },
                "attribute": "irons_spellbooks:ice_magic_resist",
                "operation": "add_multiplied_base",
                "values": { "flawed": 0.1, "normal": 0.125, "flawless": 0.15, "perfect": 0.2 }
            },
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "chestplate", "types": ["apotheosis:chestplate"] },
                "mob_effect": "irons_spellbooks:chilled",
                "target": "attack_target",
                "values": {
                    "flawed": { "duration": 70, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 140, "amplifier": 1, "cooldown": 500 },
                    "flawless": { "duration": 210, "amplifier": 2, "cooldown": 500 },
                    "perfect": { "duration": 280, "amplifier": 3, "cooldown": 500 }
                }
            }
        ]
    });

    event.json('fallen_gems_affixes:gems/compat/nyxite_crystal.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "irons_spellbooks" }],
        "type": "apotheosis:gem",
        "weights": { "quality": 0, "weight": 10 },
        "dimensions": [],
        "unique": true,
        "min_purity": "flawed",
        "bonuses": [
            {
                "type": "fallen_gems_affixes:con_cat_bonus",
                "con_cat": [
                    { "modid": "irons_apothic", "category": "fallen_gems_affixes:staffs", "not_mode": true },
                    { "modid": "irons_apothic", "category": "irons_apothic:staff" }
                ],
                "bonus": {
                    "type": "apotheosis:attribute",
                    "gem_class": { "key": "staffs", "types": [] },
                    "attribute": "irons_spellbooks:ender_spell_power",
                    "operation": "add_multiplied_total",
                    "values": { "flawed": 0.15, "normal": 0.175, "flawless": 0.2, "perfect": 0.25 }
                }
            },
            {
                "type": "apotheosis:attribute",
                "gem_class": { "key": "chestplate", "types": ["apotheosis:chestplate"] },
                "attribute": "irons_spellbooks:ender_magic_resist",
                "operation": "add_multiplied_base",
                "values": { "flawed": 0.1, "normal": 0.125, "flawless": 0.15, "perfect": 0.2 }
            },
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "helmet", "types": ["apotheosis:helmet"] },
                "mob_effect": "irons_spellbooks:evasion",
                "target": "hurt_self",
                "values": {
                    "flawed": { "duration": 140, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 200, "amplifier": 1, "cooldown": 500 },
                    "flawless": { "duration": 260, "amplifier": 2, "cooldown": 500 },
                    "perfect": { "duration": 320, "amplifier": 3, "cooldown": 500 }
                }
            }
        ]
    });

    event.json('fallen_gems_affixes:gems/compat/verdanite_shard.json', {
        "neoforge:conditions": [{ "type": "neoforge:mod_loaded", "modid": "irons_spellbooks" }],
        "type": "apotheosis:gem",
        "weights": { "quality": 0, "weight": 10 },
        "dimensions": [],
        "unique": true,
        "min_purity": "flawed",
        "bonuses": [
            {
                "type": "fallen_gems_affixes:con_cat_bonus",
                "con_cat": [
                    { "modid": "irons_apothic", "category": "fallen_gems_affixes:staffs", "not_mode": true },
                    { "modid": "irons_apothic", "category": "irons_apothic:staff" }
                ],
                "bonus": {
                    "type": "apotheosis:attribute",
                    "gem_class": { "key": "staffs", "types": [] },
                    "attribute": "irons_spellbooks:nature_spell_power",
                    "operation": "add_multiplied_total",
                    "values": { "flawed": 0.15, "normal": 0.175, "flawless": 0.2, "perfect": 0.25 }
                }
            },
            {
                "type": "apotheosis:attribute",
                "gem_class": { "key": "leggings", "types": ["apotheosis:leggings"] },
                "attribute": "irons_spellbooks:nature_magic_resist",
                "operation": "add_multiplied_base",
                "values": { "flawed": 0.1, "normal": 0.125, "flawless": 0.15, "perfect": 0.2 }
            },
            {
                "type": "fallen_gems_affixes:permanent_effect",
                "gem_class": { "key": "helmet", "types": ["apotheosis:helmet"] },
                "effect": "irons_spellbooks:spider_aspect",
                "values": { "flawed": 0, "normal": 1, "flawless": 2, "perfect": 3 }
            },
            {
                "type": "apotheosis:mob_effect",
                "gem_class": { "key": "chestplate", "types": ["apotheosis:chestplate"] },
                "mob_effect": "irons_spellbooks:blight",
                "target": "attack_target",
                "values": {
                    "flawed": { "duration": 70, "amplifier": 0, "cooldown": 500 },
                    "normal": { "duration": 140, "amplifier": 1, "cooldown": 500 },
                    "flawless": { "duration": 210, "amplifier": 2, "cooldown": 500 },
                    "perfect": { "duration": 280, "amplifier": 3, "cooldown": 500 }
                }
            }
        ]
    });

    console.log('[PEAK Expert Mode] Script 22: Master Expert Pools Injected!');
});

