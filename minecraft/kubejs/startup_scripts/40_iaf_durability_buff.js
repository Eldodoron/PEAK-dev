ItemEvents.modification(event => {
    // Buff Dragon Scale armor and Dragonbone tools by 1.3x as requested
    event.modify(/iceandfire:armor_.*(helmet|chestplate|leggings|boots)/, item => {
        // Exclude the normal metal armors (copper/silver) added by Ice and Fire
        if (!item.id.includes('metal')) {
            item.maxDamage = Math.round(item.maxDamage * 1.3);
        }
    });

    event.modify(/iceandfire:dragonbone_.*/, item => {
        item.maxDamage = Math.round(item.maxDamage * 1.3);
    });
});
