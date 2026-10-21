// Tomes used as the core ingredient of the specialised enchanting bookshelves.
// Textures live in kubejs/assets/kubejs/textures/item/<id>.png.
// Recipes are defined in server_scripts/66_bookshelf_overhaul.js.

StartupEvents.registry('item', event => {
    event.create('stonebook')
        .displayName('Stonebook')
        .tooltip('§7Binds the Stoneshelf.');

    event.create('melonbook')
        .displayName('Melonbook')
        .tooltip('§7Binds the Melonshelf.');

    event.create('beebook')
        .displayName('Beebook')
        .tooltip('§7Binds the Beeshelf.');

    event.create('hellbook')
        .displayName('Hellbook')
        .tooltip('§7Binds the Hellshelf.');

    event.create('seabook')
        .displayName('Seabook')
        .tooltip('§7Binds the Seashelf.');

    event.create('deepbook')
        .displayName('Deepbook')
        .tooltip('§7Binds the Dormant Deepshelf.')
        .tooltip('§7Can be infused into a Sculkbook.');

    event.create('sculkbook')
        .displayName('Sculkbook')
        .tooltip('§7An infused Deepbook.')
        .tooltip('§7Binds Echoing and Soul-Touched Sculkshelves.');

    event.create('endbook')
        .displayName('Endbook')
        .tooltip('§7Binds the End Shelf.');

    // Enchanted Precision Mechanism: Kinetic clockwork infused at max enchanting power.
    event.create('enchanted_precision_mechanism')
        .displayName('Enchanted Precision Mechanism')
        .tooltip('§7Infused at an Enchanting Table with 90 Eterna, 90 Quanta, and 90 Arcana.')
        .rarity('epic')
        .glow(true);
});

// Enchanted Brass Cube: Placeable block and base of the Brass Bookshelf, bound with all eight tomes.
StartupEvents.registry('block', event => {
    event.create('enchanted_brass_cube')
        .displayName('Enchanted Brass Cube')
        .soundType('metal')
        .hardness(5.0)
        .resistance(12.0)
        .tagBlock('minecraft:mineable/pickaxe')
        .tagBlock('minecraft:needs_iron_tool')
        .item(item => {
            item.rarity('epic');
            item.glow(true);
            item.component('quark:rune_color', 'rainbow');
            item.tooltip('§7Imbued with the knowledge of eight arcane tomes.');
        });
});
