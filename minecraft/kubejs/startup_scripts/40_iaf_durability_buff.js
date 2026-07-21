ItemEvents.modification(event => {
    // Buff Dragon Scale armor and Dragonbone tools (~1.3x of base values)
    // We use explicit values because reading maxDamage dynamically returns undefined/NaN during startup.

    event.modify(/iceandfire:armor_.*(helmet)/, item => { item.maxDamage = 529; });
    event.modify(/iceandfire:armor_.*(chestplate)/, item => { item.maxDamage = 770; });
    event.modify(/iceandfire:armor_.*(leggings)/, item => { item.maxDamage = 722; });
    event.modify(/iceandfire:armor_.*(boots)/, item => { item.maxDamage = 625; });

    event.modify(/iceandfire:dragonbone_(sword|pickaxe|axe|shovel|hoe|bow)/, item => { item.maxDamage = 2159; });
});
