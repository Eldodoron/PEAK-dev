// ==========================================
// PEAK EXPERT MODE — SCRIPT 12
// EPIC FOOD BUFFS & CULINARY OVERHAUL
// ==========================================
// Makes late-game foods actually worth crafting
// by providing 15-60 minute buffs for bosses.
// ==========================================

ItemEvents.foodEaten(event => {
    const player = event.player;
    if (!player) return;

    const item = event.item.id;

    // --- TIER 3: STRONG PLATED MEALS (15 MINUTES) ---
    // Good meals that require multiple cooked ingredients
    const tier3Foods = [
        'farmersdelight:steak_and_potatoes',
        'farmersdelight:roasted_mutton_chops',
        'farmersdelight:grilled_salmon',
        'farmersdelight:bacon_and_eggs',
        'veggiesdelight:steak_and_broccoli',
        'veggiesdelight:garlic_baked_cod',
        'aquaculturedelight:fish_and_chips',
        'aquaculturedelight:large_fish_with_vegetables',
        'mynethersdelight:blue_tenderloin_steak',
        'mynethersdelight:breakfast_sampler',
        'endersdelight:shulker_bowl',
        'twilightdelight:ghast_brain_salad'
    ];

    if (tier3Foods.includes(item)) {
        // Strength I, Resistance I, Regen (15 mins)
        player.potionEffects.add('minecraft:strength', 18000, 0);
        player.potionEffects.add('minecraft:resistance', 18000, 0);
        player.potionEffects.add('minecraft:regeneration', 3600, 0); // 3 min regen
        player.tell('§a✦ A hearty meal! You feel reinvigorated. ✦');
    }

    // --- TIER 4: DIMENSIONAL FEASTS (30 MINUTES) ---
    // Powerful buffs for mastering other dimensions
    const tier4Foods = [
        'twilightdelight:meef_wellington_block',
        'mynethersdelight:roast_hoglin',
        'mynethersdelight:raw_stuffed_hoglin',
        'oceansdelight:stuffed_squid',
        'oceansdelight:stuffed_cod',
        'aquaculturedelight:fish_roll_medley',
        'lendersdelight:honey_glazed_horn',
        'arsdelight:wilden_salad',
        'mynethersdelight:sizzling_pudding',
        'mynethersdelight:rock_soup'
    ];

    if (tier4Foods.includes(item)) {
        // Strength II, Resistance I, Fire Resistance, Absorption II (30 mins)
        player.potionEffects.add('minecraft:strength', 36000, 1);
        player.potionEffects.add('minecraft:resistance', 36000, 0);
        player.potionEffects.add('minecraft:fire_resistance', 36000, 0);
        player.potionEffects.add('minecraft:absorption', 36000, 1);
        player.tell('§6✦ The dimensional feast empowers your very soul! ✦');
    }

    // --- TIER 5: MASTER FEASTS (60 MINUTES) ---
    // The absolute best foods — Overworld Feast Blocks
    const tier5Foods = [
        'farmersdelight:roast_chicken_block',
        'farmersdelight:honey_glazed_ham_block',
        'farmersdelight:shepherds_pie_block',
        'farmersdelight:stuffed_pumpkin_block',
        'farmersdelight:rice_roll_medley_block'
    ];

    if (tier5Foods.includes(item)) {
        // Strength III, Resistance II, Absorption IV, Regeneration II (60 mins)
        player.potionEffects.add('minecraft:strength', 72000, 2);
        player.potionEffects.add('minecraft:resistance', 72000, 1);
        player.potionEffects.add('minecraft:absorption', 72000, 3);
        player.potionEffects.add('minecraft:regeneration', 7200, 1); // Regen is 6 mins
        player.tell('§d✦ A culinary masterpiece! You feel unstoppable! ✦');
    }

    // --- MAGICAL PIES (Ars Delight) — SPECIAL BUFFS ---
    const magicPies = [
        'arsdelight:bastion_pie',
        'arsdelight:bombegrante_pie',
        'arsdelight:frostaya_pie',
        'arsdelight:mendosteen_pie'
    ];

    if (magicPies.includes(item)) {
        // Night Vision, Speed II, Luck (45 mins) — magical exploration
        player.potionEffects.add('minecraft:night_vision', 54000, 0);
        player.potionEffects.add('minecraft:speed', 54000, 1);
        player.potionEffects.add('minecraft:luck', 54000, 0);
        player.potionEffects.add('minecraft:strength', 54000, 0);
        player.tell('§b✦ Arcane flavors heighten your senses! ✦');
    }
});

console.log('[PEAK Expert Mode] Script 12: Epic Food Buffs loaded!');
console.log('  → Tier 3: Plated Meals (15 min buffs)');
console.log('  → Tier 4: Dimensional Feasts (30 min buffs)');
console.log('  → Tier 5: Master Feasts (60 min buffs)');
console.log('  → Magic: Ars Pies (45 min exploration buffs)');
