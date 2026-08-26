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
        'vampirism:ring',
        'cataclysm:ring_of_grudged'
    ];

    event.add('curios:ring', allModpackRings);
    event.add('curios:rings', allModpackRings);
});
