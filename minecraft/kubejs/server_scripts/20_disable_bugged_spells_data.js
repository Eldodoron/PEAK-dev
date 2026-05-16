ServerEvents.generateData('peak', 'disabled_spells', event => {
    // Disable bugged spells from Traveloptics by overriding their datapack configuration
    // This tells Iron's Spellbooks to treat these spells as completely disabled in the world.
    
    const spellsToDisable = [
        'traveloptics:fire_dash',
        'traveloptics:water_dash',
        'traveloptics:air_dash',
        'traveloptics:earth_dash'
    ];

    spellsToDisable.forEach(spellId => {
        // Path matches Iron's Spellbooks spell configuration path in datapacks
        let path = `irons_spellbooks:spells/${spellId.split(':')[1]}.json`;
        event.json(path, {
            "enabled": false
        });
    });

    console.log('[PEAK Expert Mode] Script 20: Bugged Spells disabled via DataGen!');
});
