ItemEvents.modification(event => {
    // Gates of Avarice sword damage scaling
    
    // +1 scaling
    event.modify('gatesofavarice:mana_steel_sword', item => { item.attackDamage = 10; });
    event.modify('gatesofavarice:elixrite_sword', item => { item.attackDamage = 11; });
    event.modify('gatesofavarice:astrite_sword', item => { item.attackDamage = 12; });
    event.modify('gatesofavarice:lunarium_sword', item => { item.attackDamage = 13; });
    event.modify('gatesofavarice:ignite_sword', item => { item.attackDamage = 14; });
    
    // +2 scaling starting from Iridium
    event.modify('gatesofavarice:iridium_sword', item => { item.attackDamage = 16; });
    event.modify('gatesofavarice:mythril_sword', item => { item.attackDamage = 18; });
    event.modify('gatesofavarice:arcanium_sword', item => { item.attackDamage = 20; });
    event.modify('gatesofavarice:prismatic_steel_sword', item => { item.attackDamage = 22; });
});
