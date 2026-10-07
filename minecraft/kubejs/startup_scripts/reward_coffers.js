// Quest reward coffer items for FTB Quests reward tables

StartupEvents.registry('item', event => {
    event.create('coffer_common')
        .displayName('Novice Coffer')
        .rarity('common')
        .texture('kubejs:item/coffer_common');

    event.create('coffer_uncommon')
        .displayName('Pioneer Coffer')
        .rarity('uncommon')
        .texture('kubejs:item/coffer_uncommon');

    event.create('coffer_rare')
        .displayName('Slayer Coffer')
        .rarity('rare')
        .texture('kubejs:item/coffer_rare');

    event.create('coffer_epic')
        .displayName('Ancient Coffer')
        .rarity('epic')
        .texture('kubejs:item/coffer_epic');

    event.create('coffer_mythic')
        .displayName('Apex Coffer')
        .rarity('epic')
        .glow(true)
        .texture('kubejs:item/coffer_mythic');
});
