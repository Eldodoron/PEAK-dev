// priority: 0
// Script for creating Sequenced Assembly recipes for advanced spellbooks that used the normal crafting table

ServerEvents.recipes(event => {
    
    // Remove the normal shaped crafting recipes for these books, 
    // forcing them to use the Sequenced Assembly lines below.
    const booksToPort = [
        'irons_spellbooks:druidic_spell_book',
        'irons_spellbooks:cursed_doll_spell_book',
        'irons_spellbooks:netherite_spell_book'
    ];
    
    booksToPort.forEach(book => {
        event.remove({ type: 'minecraft:crafting_shaped', output: book });
    });

    // Alias for Sequenced Assembly
    const seq = event.recipes.create.sequenced_assembly;
    const deploy = event.recipes.createDeploying;
    const press = event.recipes.createPressing;

    // 1. Druidic Spellbook
    seq(
        [Item.of('irons_spellbooks:druidic_spell_book')],
        'irons_spellbooks:rotten_spell_book',
        [
            deploy('irons_spellbooks:rotten_spell_book', ['irons_spellbooks:rotten_spell_book', 'minecraft:spore_blossom']),
            deploy('irons_spellbooks:rotten_spell_book', ['irons_spellbooks:rotten_spell_book', 'minecraft:amethyst_cluster']),
            deploy('irons_spellbooks:rotten_spell_book', ['irons_spellbooks:rotten_spell_book', 'irons_spellbooks:magic_cloth']),
            press('irons_spellbooks:rotten_spell_book', 'irons_spellbooks:rotten_spell_book')
        ]
    ).transitionalItem('irons_spellbooks:rotten_spell_book').loops(3).id('kubejs:assembly/druidic_spell_book');

    // 2. Cursed Doll Spellbook
    seq(
        [Item.of('irons_spellbooks:cursed_doll_spell_book')],
        'irons_spellbooks:ruined_book',
        [
            deploy('irons_spellbooks:ruined_book', ['irons_spellbooks:ruined_book', 'irons_spellbooks:bloody_vellum']),
            deploy('irons_spellbooks:ruined_book', ['irons_spellbooks:ruined_book', 'irons_spellbooks:arcane_ingot']),
            press('irons_spellbooks:ruined_book', 'irons_spellbooks:ruined_book')
        ]
    ).transitionalItem('irons_spellbooks:ruined_book').loops(4).id('kubejs:assembly/cursed_doll_spell_book');

    // 3. Netherite Spellbook
    seq(
        [Item.of('irons_spellbooks:netherite_spell_book')],
        'irons_spellbooks:ruined_book',
        [
            deploy('irons_spellbooks:ruined_book', ['irons_spellbooks:ruined_book', 'irons_spellbooks:magic_cloth']),
            deploy('irons_spellbooks:ruined_book', ['irons_spellbooks:ruined_book', 'irons_spellbooks:blood_vial']),
            deploy('irons_spellbooks:ruined_book', ['irons_spellbooks:ruined_book', 'minecraft:netherite_ingot']),
            deploy('irons_spellbooks:ruined_book', ['irons_spellbooks:ruined_book', 'irons_spellbooks:lightning_bottle']),
            press('irons_spellbooks:ruined_book', 'irons_spellbooks:ruined_book')
        ]
    ).transitionalItem('irons_spellbooks:ruined_book').loops(4).id('kubejs:assembly/netherite_spell_book');

});
