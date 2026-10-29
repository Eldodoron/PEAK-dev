// ==========================================
// PEAK EXPERT MODE — SCRIPT 31
// REMOVE OP ALLOY BLENDING & CRAFTING HAMMERS
// ==========================================
// Enforces kinetic and thermal machinery for alloy creation (Create heated mixer,
// TFMG metallurgy, IE arc furnace) and prevents crafting-table ore doubling,
// instant plate hammering, and rod hammering.
// ==========================================

ServerEvents.recipes(event => {

    // 1. Remove All Instant Alloy Blending Recipes (Crafting Table Dust Mixing)
    const atoAlloyMats = [
        'brass', 'bronze', 'constantan', 'electrum', 'enderium',
        'invar', 'lumium', 'signalum', 'steel'
    ];
    atoAlloyMats.forEach(mat => {
        event.remove({ id: `alltheores:crafting/${mat}/alloy_blending_from_dust` });
    });

    // Immersive Engineering shapeless dust mixing
    event.remove({ id: 'immersiveengineering:crafting/constantan_mix' });
    event.remove({ id: 'immersiveengineering:crafting/electrum_mix' });

    // 2. Disable AllTheOres Ore Hammers Crafting
    const atoHammers = [
        'alltheores:copper_ore_hammer',
        'alltheores:iron_ore_hammer',
        'alltheores:bronze_ore_hammer',
        'alltheores:invar_ore_hammer',
        'alltheores:platinum_ore_hammer'
    ];
    atoHammers.forEach(hammer => {
        event.remove({ output: hammer });
    });

    // 3. Remove All Recipes Using ATO Ore Hammers (Ore Crushing, Doubling, Ingots to Dust, Plates, Rods)
    const atoMaterials = [
        'aluminum', 'brass', 'bronze', 'cinnabar', 'constantan', 'copper',
        'diamond', 'electrum', 'enderium', 'fluorite', 'gold', 'invar',
        'iridium', 'iron', 'lead', 'lumium', 'netherite', 'nickel',
        'osmium', 'peridot', 'platinum', 'ruby', 'salt', 'sapphire',
        'signalum', 'silver', 'steel', 'sulfur', 'tin', 'uranium', 'zinc'
    ];
    const atoCrushTypes = [
        'dust_from_ore', 'dust_from_raw', 'dust_from_ingot',
        'dust_from_gem', 'gem_from_ore', 'scrap_from_debris'
    ];

    atoMaterials.forEach(mat => {
        atoCrushTypes.forEach(type => {
            event.remove({ id: `alltheores:crafting/hammer/${mat}/${type}` });
        });
        event.remove({ id: `alltheores:crafting/${mat}/plate` });
        event.remove({ id: `alltheores:crafting/${mat}/rod` });
    });

    // AllTheModium Raw Ore Doubling via Hammers
    [
        'allthemodium:allthemodium_dust_from_ore_crushing',
        'allthemodium:ancient_chiseled_stone_bricks_from_crushing',
        'allthemodium:ancient_cracked_stone_bricks_from_crushing',
        'allthemodium:unobtainium_dust_from_ore_crushing',
        'allthemodium:vibranium_dust_from_ore_crushing'
    ].forEach(id => event.remove({ id: id }));

    // Tag and regex fallbacks
    event.remove({ input: '#alltheores:ore_hammers' });
    event.remove({ id: /alltheores:crafting\/hammer\/.*/ });
    event.remove({ id: /alltheores:crafting\/.*\/plate/ });
    event.remove({ id: /alltheores:crafting\/.*\/rod/ });
    event.remove({ id: /allthemodium:.*_dust_from_ore_crushing/ });
    event.remove({ id: /allthemodium:ancient_.*_from_crushing/ });

    // 4. Rebalance Immersive Engineering Hammer Recipes
    event.remove({ type: 'immersiveengineering:hammer_crushing' });
    [
        'aluminum', 'copper', 'gold', 'iron', 'lead', 'nickel', 'silver', 'uranium',
        'constantan', 'electrum', 'steel'
    ].forEach(mat => {
        event.remove({ id: `immersiveengineering:crafting/hammercrushing_${mat}` });
        event.remove({ id: `immersiveengineering:crafting/plate_${mat}_hammering` });
    });
    event.remove({ id: /immersiveengineering:crafting\/.*hammercrushing.*/ });
    event.remove({ id: /immersiveengineering:crafting\/plate_.*_hammering/ });

    // 5. Rebalance Create Diesel Generators Hammer
    event.remove({ type: 'createdieselgenerators:hammering' });
    event.remove({ id: /createdieselgenerators:hammering\/.*/ });
    event.remove({ id: /createdieselgenerators:recipe\/compat\/.*\/.*_sheet/ });
    event.remove({ output: 'createdieselgenerators:hammer' });

});
