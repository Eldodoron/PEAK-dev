// ==========================================
// PEAK EXPERT MODE — SCRIPT 25
// HARDCODED MINIBOSS VARIANTS
// ==========================================

// ---- SECTION 1: ATTRIBUTE-ONLY MINIBOSSES ----
// These minibosses only get scaled stats + custom name.

const MINIBOSSES = {
    // === ICE AND FIRE ===
    'iceandfire:cyclops': {
        tag: 'is_alpha_cyclops',
        chance: 0.025,
        name: 'Alpha Cyclops',
        color: Text.gold,
        scale: 1.3,
        healthMult: 1.0,
        damageMult: 0.5,
        speedMult: 0.1
    },
    'iceandfire:troll': {
        tag: 'is_elder_troll',
        chance: 0.025,
        name: 'Elder Cave Troll',
        color: Text.darkGreen,
        scale: 1.4,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.0
    },
    'iceandfire:gorgon': {
        tag: 'is_matriarch_gorgon',
        chance: 0.025,
        name: 'Matriarch Gorgon',
        color: Text.darkGreen,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.1
    },
    'iceandfire:cockatrice': {
        tag: 'is_venomous_cockatrice',
        chance: 0.025,
        name: 'Venomous Cockatrice',
        color: Text.darkPurple,
        scale: 1.3,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.15
    },
    'iceandfire:hippogryph': {
        tag: 'is_warhippogryph',
        chance: 0.02,
        name: 'War Hippogryph',
        color: Text.aqua,
        scale: 1.3,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.0
    },
    'iceandfire:stymphalian_bird': {
        tag: 'is_flock_matriarch',
        chance: 0.015,
        name: 'Flock Matriarch',
        color: Text.darkRed,
        scale: 1.4,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.0
    },

    // === MOWZIE'S MOBS ===
    'mowziesmobs:frostmaw': {
        tag: 'is_mother_frostmaw',
        chance: 0.025,
        name: 'Mother Frostmaw',
        color: Text.darkRed,
        scale: 1.5,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.0
    },
    'mowziesmobs:naga': {
        tag: 'is_naga_patriarch',
        chance: 0.025,
        name: 'Naga Patriarch',
        color: Text.gold,
        scale: 1.4,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.0
    },
    'mowziesmobs:ferrous_wroughtnaut': {
        tag: 'is_ancient_wroughtnaut',
        chance: 0.025,
        name: 'Ancient Wroughtnaut',
        color: Text.darkGray,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.3,
        speedMult: 0.0
    },

    // === CATACLYSM ===
    'cataclysm:ignited_berserker': {
        tag: 'is_champion_berserker',
        chance: 0.025,
        name: 'Champion Berserker',
        color: Text.red,
        scale: 1.2,
        healthMult: 1.0,
        damageMult: 0.5,
        speedMult: 0.15
    },
    'cataclysm:koboleton': {
        tag: 'is_koboleton_warchief',
        chance: 0.025,
        name: 'Koboleton Warchief',
        color: Text.darkAqua,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.15
    },
    'cataclysm:deepling_brute': {
        tag: 'is_abyssal_champion',
        chance: 0.025,
        name: 'Abyssal Champion',
        color: Text.darkBlue,
        scale: 1.3,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.1
    },
    'cataclysm:endermaptera': {
        tag: 'is_void_horror',
        chance: 0.025,
        name: 'Void Horror',
        color: Text.darkPurple,
        scale: 1.4,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.0
    },

    // === VANILLA MINECRAFT ===
    'minecraft:wither_skeleton': {
        tag: 'is_wither_vanguard',
        chance: 0.015,
        name: 'Wither Vanguard',
        color: Text.black,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.2
    },
    'minecraft:evoker': {
        tag: 'is_supreme_evoker',
        chance: 0.025,
        name: 'Supreme Evoker',
        color: Text.darkPurple,
        scale: 1.2,
        healthMult: 2.0,
        damageMult: 0.0,
        speedMult: 0.2
    },
    'minecraft:vindicator': {
        tag: 'is_raid_champion',
        chance: 0.02,
        name: 'Raid Champion',
        color: Text.darkRed,
        scale: 1.2,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.15
    },
    'minecraft:piglin_brute': {
        tag: 'is_piglin_warlord',
        chance: 0.025,
        name: 'Piglin Warlord',
        color: Text.gold,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.1
    },
    'minecraft:ravager': {
        tag: 'is_siege_beast',
        chance: 0.025,
        name: 'Siege Beast',
        color: Text.darkGray,
        scale: 1.3,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.0
    },
    'minecraft:enderman': {
        tag: 'is_void_walker',
        chance: 0.01,
        name: 'Void Walker',
        color: Text.darkPurple,
        scale: 1.4,
        healthMult: 3.0,
        damageMult: 1.0,
        speedMult: 0.0
    },
    'minecraft:warden': {
        tag: 'is_ancient_warden',
        chance: 0.05,
        name: 'Ancient Warden',
        color: Text.darkAqua,
        scale: 1.3,
        healthMult: 1.0,
        damageMult: 0.3,
        speedMult: 0.0
    },

    // === TWILIGHT FOREST ===
    'twilightforest:minotaur': {
        tag: 'is_labyrinth_champion',
        chance: 0.025,
        name: 'Labyrinth Champion',
        color: Text.gold,
        scale: 1.3,
        healthMult: 1.5,
        damageMult: 0.5,
        speedMult: 0.1
    },
    'twilightforest:carminite_golem': {
        tag: 'is_siege_golem',
        chance: 0.025,
        name: 'Siege Golem',
        color: Text.darkRed,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.0
    },
    'twilightforest:skeleton_druid': {
        tag: 'is_archdruid',
        chance: 0.025,
        name: 'Archdruid',
        color: Text.green,
        scale: 1.2,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.15
    },

    // === DEEPER AND DARKER ===
    'deeperdarker:stalker': {
        tag: 'is_abyssal_stalker',
        chance: 0.025,
        name: 'Abyssal Stalker',
        color: Text.darkAqua,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.2
    },
    'deeperdarker:shattered': {
        tag: 'is_elder_shattered',
        chance: 0.025,
        name: 'Elder Shattered',
        color: Text.darkBlue,
        scale: 1.3,
        healthMult: 2.0,
        damageMult: 0.5,
        speedMult: 0.0
    }
};

// Register all attribute-only minibosses
EntityEvents.spawned(event => {
    const { entity, server } = event;
    if (!entity || !entity.living) return;

    let config = MINIBOSSES[entity.type];
    if (!config) return;

    // Ignore non-natural spawns (spawners, tech farms, eggs) unless forced via command tag
    let forceTag = 'force_' + config.tag.replace('is_', '');
    let isForced = entity.tags.contains(forceTag);
    let reason = event.spawnReason ? String(event.spawnReason) : '';
    if (reason && reason !== 'NATURAL' && !isForced) return;

    // Roll chance OR bypass if forced
    if (Math.random() > config.chance && !isForced) return;

    // Mark as mutated
    entity.tags.add(config.tag);

    // Custom Name
    entity.customName = config.color(config.name).bold();
    entity.customNameVisible = true;

    // Modify Attributes
    if (config.scale !== 1.0) {
        server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.scale base set ${config.scale}`);
    }
    if (config.healthMult > 0.0) {
        server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.max_health modifier add peak:${config.tag}_health ${config.healthMult} add_multiplied_base`);
    }
    if (config.damageMult > 0.0) {
        server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.attack_damage modifier add peak:${config.tag}_damage ${config.damageMult} add_multiplied_base`);
    }
    if (config.speedMult > 0.0) {
        server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.movement_speed modifier add peak:${config.tag}_speed ${config.speedMult} add_multiplied_base`);
    }

    // Heal to new max health
    server.scheduleInTicks(1, callback => {
        if (entity && entity.isAlive()) {
            entity.setHealth(entity.maxHealth);
        }
    });

    console.log(`[PEAK Expert Mode] A ${config.name} has spawned at ${entity.x}, ${entity.y}, ${entity.z}!`);
});


// ---- SECTION 2: DECEASED DRAGONSLAYER ----
// A special zombie variant wearing full matching dragonscale armor + dragonbone sword.

EntityEvents.spawned('minecraft:zombie', event => {
    const { entity, server } = event;
    if (!entity || !entity.living) return;

    // Ignore non-natural spawns (spawners, tech farms, eggs) unless forced via command tag
    let isForced = entity.tags.contains('force_deceased_dragonslayer');
    let reason = event.spawnReason ? String(event.spawnReason) : '';
    if (reason && reason !== 'NATURAL' && !isForced) return;

    // 1% chance (rare encounter)
    if (Math.random() > 0.01 && !isForced) return;

    // Mark as mutated
    entity.tags.add('is_deceased_dragonslayer');

    // Randomly pick an element: fire, ice, or lightning
    const elements = ['fire', 'ice', 'lightning'];
    const element = elements[Math.floor(Math.random() * elements.length)];

    // Define matching armor + weapon sets using real Ice and Fire item IDs
    const sets = {
        fire: {
            helmet: 'iceandfire:armor_red_helmet',
            chestplate: 'iceandfire:armor_red_chestplate',
            leggings: 'iceandfire:armor_red_leggings',
            boots: 'iceandfire:armor_red_boots',
            sword: 'iceandfire:dragonbone_sword_fire',
            name: 'Deceased Fire Dragonslayer',
            color: Text.red
        },
        ice: {
            helmet: 'iceandfire:armor_blue_helmet',
            chestplate: 'iceandfire:armor_blue_chestplate',
            leggings: 'iceandfire:armor_blue_leggings',
            boots: 'iceandfire:armor_blue_boots',
            sword: 'iceandfire:dragonbone_sword_ice',
            name: 'Deceased Ice Dragonslayer',
            color: Text.aqua
        },
        lightning: {
            helmet: 'iceandfire:armor_amethyst_helmet',
            chestplate: 'iceandfire:armor_amethyst_chestplate',
            leggings: 'iceandfire:armor_amethyst_leggings',
            boots: 'iceandfire:armor_amethyst_boots',
            sword: 'iceandfire:dragonbone_sword_lightning',
            name: 'Deceased Lightning Dragonslayer',
            color: Text.yellow
        }
    };

    let set = sets[element];

    // Custom Name
    entity.customName = set.color(set.name).bold();
    entity.customNameVisible = true;

    // Equip full matching dragonscale armor + dragonbone sword
    entity.setItemSlot('head', Item.of(set.helmet));
    entity.setItemSlot('chest', Item.of(set.chestplate));
    entity.setItemSlot('legs', Item.of(set.leggings));
    entity.setItemSlot('feet', Item.of(set.boots));
    entity.setItemSlot('mainhand', Item.of(set.sword));

    // They do NOT drop the gear (it died with them for a reason)
    entity.setDropChance('head', 0.0);
    entity.setDropChance('chest', 0.0);
    entity.setDropChance('legs', 0.0);
    entity.setDropChance('feet', 0.0);
    entity.setDropChance('mainhand', 0.0);

    // Scale + attributes: Slightly bigger, much tougher, same speed (they're undead, they shamble)
    server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.scale base set 1.15`);
    server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.max_health modifier add peak:dragonslayer_health 3.0 add_multiplied_base`);
    server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.attack_damage modifier add peak:dragonslayer_damage 1.0 add_multiplied_base`);
    server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.knockback_resistance modifier add peak:dragonslayer_kb 0.6 add_value`);
    server.runCommandSilent(`attribute ${entity.uuid} minecraft:generic.armor modifier add peak:dragonslayer_armor 10.0 add_value`);

    // Heal to new max
    server.scheduleInTicks(1, callback => {
        if (entity && entity.isAlive()) {
            entity.setHealth(entity.maxHealth);
        }
    });

    console.log(`[PEAK Expert Mode] A ${set.name} has risen at ${entity.x}, ${entity.y}, ${entity.z}!`);
});
