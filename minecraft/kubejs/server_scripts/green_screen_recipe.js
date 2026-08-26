ServerEvents.recipes(event => {
    // Green Screen Crafting Recipes
    event.shaped('8x kubejs:green_screen', [
        'GGG',
        'GLG',
        'GGG'
    ], {
        G: '#c:dyes/lime',
        L: '#c:lights'
    });

    event.shapeless('4x kubejs:green_screen', [
        'minecraft:lime_wool',
        'minecraft:lime_wool',
        'minecraft:lime_wool',
        'minecraft:lime_wool',
        'minecraft:glowstone'
    ]);

    event.shapeless('4x kubejs:green_screen', [
        'minecraft:lime_concrete',
        'minecraft:lime_concrete',
        'minecraft:lime_concrete',
        'minecraft:lime_concrete',
        'minecraft:glowstone'
    ]);
});
