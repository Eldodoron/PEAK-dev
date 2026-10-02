StartupEvents.registry('block', event => {
    event.create('void_teleport_pad')
        .displayName('Void Teleport Pad')
        .soundType('metal')
        .hardness(50.0)
        .resistance(1200.0)
        .lightLevel(0.75)
        .box(0, 0, 0, 16, 3, 16)
        .notSolid()
        .tagBlock('minecraft:mineable/pickaxe')
        .tagBlock('minecraft:needs_diamond_tool')
        .item(item => {
            item.rarity('epic');
            item.glow(true);
            item.tooltip('§7Sneak + Right-Click to teleport to The Beyond.');
            item.tooltip('§8Use in The Beyond to return to your original position.');
        });
});
