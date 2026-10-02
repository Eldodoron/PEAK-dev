// ==========================================
// PEAK EXPERT MODE — VAMPIRE ITEMS
// ==========================================

StartupEvents.registry('item', event => {
    event.create('vampire_fang')
        .displayName('Vampire Fang')
        .tooltip('§7A razor-sharp canine tooth harvested from a Dark Forest stalker.')
        .tooltip('§8Pulses with dark, sanguinary vitality.')
        .rarity('uncommon')
        .maxStackSize(64);
});
