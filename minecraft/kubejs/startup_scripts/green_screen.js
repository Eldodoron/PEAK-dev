StartupEvents.registry('block', event => {
    event.create('green_screen')
        .displayName('Green Screen')
        .soundType('wool')
        .hardness(0.5)
        .resistance(0.5)
        .lightLevel(1.0)
        .tagBlock('minecraft:mineable/axe')
        .tagBlock('minecraft:mineable/pickaxe')
        .tagBlock('minecraft:mineable/hoe');
});
