// ==========================================
// YAGM RESTORE KEY & GHOST PEARL RECIPES
// Multi-path synthesis for Yet Another Grave Mod key progression.
// Supported paths: Crafting Table, Create, Ars Nouveau, Malum.
// ==========================================

ServerEvents.recipes(event => {
    // -------------------------------------------------------------
    // GHOST PEARL (yagm:ghost_pearl) SYNTHESIS
    // -------------------------------------------------------------

    // Ars Nouveau: Enchanting Apparatus
    event.recipes.ars_nouveau.enchanting_apparatus(
        [
            'minecraft:ghast_tear',
            'minecraft:soul_sand',
            'ars_nouveau:source_gem'
        ],
        'minecraft:ender_pearl',
        'yagm:ghost_pearl'
    ).sourceCost(1000).id('kubejs:ars_nouveau/enchanting_apparatus/ghost_pearl');

    // Ars Nouveau: Imbuement Chamber
    event.recipes.ars_nouveau.imbuement(
        'minecraft:ender_pearl',
        'yagm:ghost_pearl',
        1000,
        [
            'minecraft:ghast_tear',
            'minecraft:soul_sand'
        ]
    ).id('kubejs:ars_nouveau/imbuement/ghost_pearl');

    // Malum: Spirit Infusion
    event.custom({
        type: 'malum:spirit_infusion',
        input: { count: 1, item: 'minecraft:ender_pearl' },
        extraInputs: [
            { count: 1, item: 'minecraft:ghast_tear' },
            { count: 1, item: 'minecraft:soul_sand' }
        ],
        spirits: [
            { count: 2, type: 'malum:sacred' },
            { count: 2, type: 'malum:arcane' }
        ],
        result: { count: 1, id: 'yagm:ghost_pearl' }
    }).id('kubejs:malum/spirit_infusion/ghost_pearl');

    // Create: Heated Mixing
    event.recipes.create.mixing('yagm:ghost_pearl', [
        'minecraft:ender_pearl',
        'minecraft:ghast_tear',
        'minecraft:soul_sand'
    ]).heated().id('kubejs:create/mixing/ghost_pearl');

    // -------------------------------------------------------------
    // RESTORE KEY (yagm:restore_key) SYNTHESIS
    // -------------------------------------------------------------

    // Remove default recipe requiring standard obsidian
    event.remove({ id: 'yagm:restore_key' });

    // Crafting Table: Shaped Crafting (Crying Obsidian matches key texture)
    event.shaped('yagm:restore_key', [
        ' E ',
        ' T ',
        ' C '
    ], {
        E: 'minecraft:ender_pearl',
        T: 'yagm:ghost_pearl',
        C: 'minecraft:crying_obsidian'
    }).id('kubejs:crafting/restore_key');

    // Create: Mechanical Crafting
    event.recipes.create.mechanical_crafting('yagm:restore_key', [
        'E',
        'T',
        'C'
    ], {
        E: 'minecraft:ender_pearl',
        T: 'yagm:ghost_pearl',
        C: 'minecraft:crying_obsidian'
    }).id('kubejs:create/mechanical_crafting/restore_key');

    // Ars Nouveau: Enchanting Apparatus
    event.recipes.ars_nouveau.enchanting_apparatus(
        [
            'minecraft:crying_obsidian',
            'minecraft:ender_pearl',
            'ars_nouveau:source_gem'
        ],
        'yagm:ghost_pearl',
        'yagm:restore_key'
    ).sourceCost(1000).id('kubejs:ars_nouveau/enchanting_apparatus/restore_key');

    // Malum: Spirit Infusion
    event.custom({
        type: 'malum:spirit_infusion',
        input: { count: 1, item: 'yagm:ghost_pearl' },
        extraInputs: [
            { count: 1, item: 'minecraft:crying_obsidian' },
            { count: 1, item: 'minecraft:ender_pearl' }
        ],
        spirits: [
            { count: 2, type: 'malum:arcane' },
            { count: 2, type: 'malum:sacred' }
        ],
        result: { count: 1, id: 'yagm:restore_key' }
    }).id('kubejs:malum/spirit_infusion/restore_key');
});
