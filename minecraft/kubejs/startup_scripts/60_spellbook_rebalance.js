// priority: 0
// Script for rebalancing Iron's Spells 'n Spellbooks maxSpells

console.log('[PEAK] Modifying Spellbook maxSpells sizes...');

ItemEvents.modification(event => {
    
    const applySpellbook = (id, maxSlots, customData) => {
        event.modify(id, item => {
            let componentData = {
                maxSpells: maxSlots,
                mustEquip: true,
                spellWheel: true,
                data: customData || []
            };
            item.set('irons_spellbooks:spell_container', componentData);
        });
    };

    // 2 SLOTS
    applySpellbook('irons_spellbooks:copper_spell_book', 2);

    // 3 SLOTS
    applySpellbook('irons_spellbooks:iron_spell_book', 3);
    applySpellbook('irons_spellbooks:rotten_spell_book', 3);

    // 4 SLOTS
    applySpellbook('irons_spellbooks:gold_spell_book', 4);

    // 5 SLOTS
    applySpellbook('irons_spellbooks:diamond_spell_book', 5);

    // 6 SLOTS
    applySpellbook('wind_spellbooks:wind_spell_book', 6);
    applySpellbook('ess_requiem:spellblade_spellbook', 6);

    // 7 SLOTS
    applySpellbook('irons_spellbooks:villager_spell_book', 7);
    applySpellbook('irons_spellbooks:evoker_spell_book', 7, [
        {locked: true, index: 0, id: "irons_spellbooks:fang_strike", level: 6},
        {locked: true, index: 1, id: "irons_spellbooks:fang_ward", level: 4},
        {locked: true, index: 2, id: "irons_spellbooks:summon_vex", level: 4}
    ]);

    // 8 SLOTS
    applySpellbook('irons_spellbooks:blaze_spell_book', 8);
    applySpellbook('irons_spellbooks:druidic_spell_book', 8);

    // 9 SLOTS
    applySpellbook('irons_spellbooks:ice_spell_book', 9);
    applySpellbook('irons_spellbooks:cursed_doll_spell_book', 9);

    // 10 SLOTS
    applySpellbook('firesenderexpansion:endchiridion', 10);
    applySpellbook('irons_spellbooks:necronomicon_spell_book', 10, [
        {locked: true, index: 0, id: "irons_spellbooks:blood_slash", level: 5},
        {locked: true, index: 1, id: "irons_spellbooks:blood_step", level: 5},
        {locked: true, index: 2, id: "irons_spellbooks:ray_of_siphoning", level: 5},
        {locked: true, index: 3, id: "irons_spellbooks:blaze_storm", level: 5}
    ]);

    // 11 SLOTS
    applySpellbook('irons_spellbooks:dragonskin_spell_book', 11);
    applySpellbook('enigmatic_arcana:antonomos', 11);

    // 12 SLOTS
    applySpellbook('irons_spellbooks:netherite_spell_book', 12);
    applySpellbook('darkermagic:volume_of_the_deep', 12);

    // 13 SLOTS
    applySpellbook('allthewizardgear:allthemodium_spell_book', 13);
    applySpellbook('cataclysm_spellbooks:abyss_spell_book', 13);
    applySpellbook('cataclysm_spellbooks:ignis_spell_book', 13);
    applySpellbook('cataclysm_spellbooks:codex_of_malice_spell_book', 13);
    applySpellbook('cataclysm_spellbooks:desert_spell_book', 13, [
        {locked: true, index: 0, id: "cataclysm_spellbooks:monolith_crash", level: 5},
        {locked: true, index: 1, id: "cataclysm_spellbooks:desert_winds", level: 3},
        {locked: true, index: 2, id: "cataclysm_spellbooks:sandstorm", level: 3},
        {locked: true, index: 3, id: "cataclysm_spellbooks:thoths_witness", level: 1},
        {locked: true, index: 4, id: "cataclysm_spellbooks:pharaohs_wrath", level: 3}
    ]);

    // 14 SLOTS
    applySpellbook('allthewizardgear:vibranium_spell_book', 14);

    // 15 SLOTS
    applySpellbook('allthewizardgear:unobtainium_spell_book', 15);

});
