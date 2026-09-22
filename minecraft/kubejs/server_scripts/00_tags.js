// Tag unifications
ServerEvents.tags('item', event => {
    // Unify screwdrivers
    event.add('c:tools/screwdriver', 'immersiveengineering:screwdriver');
    event.add('c:tools/screwdriver', 'tfmg:screwdriver');

    // Runes tag for recipes
    event.add('kubejs:irons_runes', [
        'irons_spellbooks:arcane_rune', 'irons_spellbooks:blank_rune', 'irons_spellbooks:blood_rune',
        'irons_spellbooks:cinderous_soul_rune', 'irons_spellbooks:cooldown_rune', 'irons_spellbooks:ender_rune',
        'irons_spellbooks:evocation_rune', 'irons_spellbooks:fire_rune', 'irons_spellbooks:holy_rune',
        'irons_spellbooks:ice_rune', 'irons_spellbooks:lightning_rune', 'irons_spellbooks:nature_rune',
        'irons_spellbooks:protection_rune'
    ]);

    // Curios ring tag integrations (explicit item lists to avoid circular references)
    const allModpackRings = [
        'irons_jewelry:ring',
        'irons_spellbooks:affinity_ring',
        'irons_spellbooks:cast_time_ring',
        'irons_spellbooks:cooldown_ring',
        'irons_spellbooks:emerald_stoneplate_ring',
        'irons_spellbooks:expulsion_ring',
        'irons_spellbooks:fireward_ring',
        'irons_spellbooks:frostward_ring',
        'irons_spellbooks:invisibility_ring',
        'irons_spellbooks:lurker_ring',
        'irons_spellbooks:mana_ring',
        'irons_spellbooks:poisonward_ring',
        'irons_spellbooks:silver_ring',
        'irons_spellbooks:visibility_ring',
        'relics:bastion_ring',
        'relics:leafy_ring',
        'relics:chorus_inhibitor',
        'morerelics:made_in_heaven',
        'morerelics:moodworm',
        'reliquified_ars_nouveau:mana_ring',
        'reliquified_ars_nouveau:ring_of_last_will',
        'reliquified_ars_nouveau:ring_of_the_spectral_walker',
        'reliquified_ars_nouveau:ring_of_thrift',
        'malum:gilded_ring',
        'malum:ornate_ring',
        'malum:ring_of_alchemical_mastery',
        'malum:ring_of_arcane_prowess',
        'malum:ring_of_curative_talent',
        'malum:ring_of_desperate_voracity',
        'malum:ring_of_echoing_arcana',
        'malum:ring_of_esoteric_spoils',
        'malum:ring_of_growing_flesh',
        'malum:ring_of_gruesome_concentration',
        'malum:ring_of_manaweaving',
        'malum:ring_of_the_demolitionist',
        'malum:ring_of_the_endless_well',
        'malum:ring_of_the_hoarder',
        'malum:ring_of_the_howling_maelstrom',
        'malum:ring_of_the_rising_edge',
        'twilightforest:knightmetal_ring',
        'the_beyond:ring_remembrance',
        'unusualend:pearlescent_ring',
        'cataclysm:ring_of_grudged'
    ];

    event.add('curios:ring', allModpackRings);
    event.add('curios:rings', allModpackRings);
});

// Boss entity tag unifications for Boss Rifts and common compat
ServerEvents.tags('entity_type', event => {
    const PEAK_BOSSES = [
        // Mowzie's Mobs
        'mowziesmobs:frostmaw',
        'mowziesmobs:ferrous_wroughtnaut',
        'mowziesmobs:umvuthi',
        'mowziesmobs:sculptor',
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
        'cataclysm:maledictus',
        'cataclysm:scylla',
        // Bosses of Mass Destruction
        'bosses_of_mass_destruction:lich',
        'bosses_of_mass_destruction:obsidilith',
        'bosses_of_mass_destruction:void_blossom',
        'bosses_of_mass_destruction:gauntlet',
        // Remnant Bosses
        'remnant_bosses:armored_grub',
        'remnant_bosses:bone_tyrant',
        'remnant_bosses:remnant_ossukage',
        // Ice & Fire
        'iceandfire:fire_dragon',
        'iceandfire:ice_dragon',
        'iceandfire:lightning_dragon',
        'iceandfire:cyclops',
        'iceandfire:gorgon',
        'iceandfire:hydra',
        // Alex's Mobs / Caves
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
        'irons_spellbooks:fire_boss',
        // Undergarden
        'undergarden:forgotten_guardian'
    ];

    event.add('c:bosses', PEAK_BOSSES);
    event.add('bossrifts:rift_bosses', PEAK_BOSSES);

    // Bosses excluded from spawning rifts
    event.add('bossrifts:boss_exception', [
        'minecraft:wither',
        'minecraft:warden'
    ]);
});

