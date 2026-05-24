// ==========================================
// PEAK EXPERT MODE — CUSTOM ITEMS
// These are special crafting components that drop
// from specific bosses and are used in endgame recipes.
// ==========================================
// IMPORTANT: This is a STARTUP script, NOT a server script.
// It runs ONCE when the game starts to register new items.
// ==========================================

StartupEvents.registry('item', event => {

    // ==========================================
    // BOSS DROP ITEMS — Each boss drops a unique
    // crafting component that feeds into the tech tree
    // ==========================================

    // --- FROSTMAW (Mowzie's Mobs) ---
    // A core of pure frozen energy from the beast's heart
    // Used in: PneumaticCraft refrigeration, cryogenic recipes
    event.create('frozen_heart_core')
        .displayName('§b❄ Frozen Heart Core')
        .tooltip('§7Drops from: §fFrostmaw §8(Mowzie\'s Mobs)')
        .rarity('rare')
        .maxStackSize(16)
        .glow(true);

    // --- CATACLYSM: ANCIENT REMNANT / HARBINGER ---
    // A fragment of primordial power from before time
    // Used in: Draconic Evolution Wyvern upgrades
    event.create('primordial_core')
        .displayName('§5⚡ Primordial Core')
        .tooltip('§7Drops from: §fAncient Remnant §8(Cataclysm)')
        .rarity('epic')
        .maxStackSize(8)
        .glow(true);

    // --- CATACLYSM: ENDER GUARDIAN ---
    // A crystal that resonates with the void between dimensions
    // Used in: AE2 ME Controllers, dimensional tech
    event.create('void_resonator')
        .displayName('§d🌌 Void Resonator')
        .tooltip('§7Drops from: §fEnder Guardian, Void Worm, Ender Dragon')
        .rarity('epic')
        .maxStackSize(8)
        .glow(true);

    // Endgame Custom Core (Boss Drop Duplicator)
    event.create('anomaly_replicator')
        .displayName('§dAnomaly Replicator')
        .tooltip('§7A miraculous device forged from the Infinity Catalyst.')
        .tooltip('§7Can replicate matter when combined with high-energy resources.')
        .glow(true)
        .rarity('epic');

    // --- CATACLYSM: IGNIS ---
    // Used in: Re-Avaritia Infinity Catalyst
    event.create('heart_of_the_inferno')
        .displayName('§c🔥 Heart of the Inferno')
        .tooltip('§7Drops from: §fIgnis §8(Cataclysm)')
        .rarity('epic')
        .maxStackSize(4)
        .glow(true);

    // --- CATACLYSM: LEVIATHAN ---
    // A catalyst forged in the deepest ocean trenches
    // Used in: Ender IO Soul Machines, advanced fluid tech
    event.create('abyssal_catalyst')
        .displayName('§3🌊 Abyssal Catalyst')
        .tooltip('§7Drops from: §fThe Leviathan §8(Cataclysm)')
        .rarity('epic')
        .maxStackSize(8)
        .glow(true);

    // --- CATACLYSM: NETHERITE MONSTROSITY ---
    // A core of concentrated Nether energy
    // Used in: Mekanism reactors, nuclear tech
    event.create('netheric_core')
        .displayName('§4⬛ Netheric Core')
        .tooltip('§7Drops from: §fNetherite Monstrosity §8(Cataclysm)')
        .rarity('epic')
        .maxStackSize(8)
        .glow(true);

    // --- WARDEN (Deeper Darker enhanced) ---
    // A crystallized heart of sculk resonance
    // Used in: Draconic Evolution Wyvern cores
    event.create('sculk_heart')
        .displayName('§8💎 Sculk Heart')
        .tooltip('§7Drops from: §fThe Warden')
        .rarity('epic')
        .maxStackSize(4)
        .glow(true);

    // --- STAGE 5 DRAGON (Ice and Fire) ---
    // Ancient primordial dragon blood, far more potent
    // than regular dragon blood
    // Used in: Draconic Evolution Draconic tier
    event.create('primordial_dragon_blood')
        .displayName('§4🩸 Primordial Dragon Blood')
        .tooltip('§7Drops from: §fStage 5 Dragons §8(Ice and Fire)')
        .rarity('epic')
        .maxStackSize(4)
        .glow(true);

    // --- LICH (Twilight Forest) ---
    // The Lich's preserved phylactery containing
    // centuries of accumulated dark knowledge
    // Used in: Iron's Spellbooks legendary crafting
    event.create('lich_phylactery')
        .displayName('§e💀 Lich Phylactery')
        .tooltip('§7Drops from: §fTwilight Lich §8(Twilight Forest)')
        .rarity('rare')
        .maxStackSize(8)
        .glow(true);

    // --- INFINITY CATALYST FRAGMENT ---
    // Dropped by the absolute hardest bosses in tiny amounts
    // Collect enough to forge the Infinity Catalyst
    event.create('infinity_fragment')
        .displayName('§6♾ Infinity Fragment')
        .tooltip('§7Drops from: §fVarious Major Bosses')
        .rarity('epic')
        .maxStackSize(64)
        .glow(true);

    // --- CHAOS ESSENCE ---
    // The distilled essence of entropy itself
    // Created by processing Chaos Shards in Create
    event.create('chaos_essence')
        .displayName('§c✦ Chaos Essence')
        .tooltip('§7Process Chaos Shards in Create Crushing Wheels')
        .rarity('epic')
        .maxStackSize(16)
        .glow(true);

    // --- INCOMPLETE ENDER EYE ---
    // Used in the Sequenced Assembly for the Ender Eye
    event.create('incomplete_ender_eye')
        .displayName('Incomplete Ender Eye')
        .texture('minecraft:item/ender_pearl');

    // --- WITHER SOUL ---
    // Dropped by the Wither
    event.create('wither_soul')
        .displayName('§8💀 Wither Soul')
        .tooltip('§7Drops from: §fThe Wither')
        .rarity('epic')
        .maxStackSize(8)
        .glow(true);

    // --- DRACONIC SCALE ---
    // Dropped by the Ender Dragon
    event.create('draconic_scale')
        .displayName('§5🐉 Draconic Scale')
        .tooltip('§7Drops from: §fThe Ender Dragon')
        .rarity('epic')
        .maxStackSize(16)
        .glow(true);

    // --- CULINARY SINGULARITY ---
    // The ultimate mastery of gastronomy.
    event.create('culinary_singularity')
        .displayName('§dCulinary Singularity')
        .tooltip('§7The distilled essence of all worldy flavors')
        .rarity('epic')
        .maxStackSize(16)
        .glow(true);

    // --- SOPHISTICATED BACKPACKS INCOMPLETE TRANSITIONAL ITEMS ---
    event.create('incomplete_upgrade_base')
        .displayName('Incomplete Upgrade Base')
        .texture('minecraft:item/leather');



    event.create('incomplete_magnet_upgrade')
        .displayName('Incomplete Magnet Upgrade')
        .texture('sophisticatedbackpacks:item/upgrade_base');

    event.create('incomplete_advanced_magnet_upgrade')
        .displayName('Incomplete Advanced Magnet Upgrade')
        .texture('sophisticatedbackpacks:item/magnet_upgrade');

    event.create('incomplete_filter_upgrade')
        .displayName('Incomplete Filter Upgrade')
        .texture('sophisticatedbackpacks:item/upgrade_base');

    event.create('incomplete_advanced_filter_upgrade')
        .displayName('Incomplete Advanced Filter Upgrade')
        .texture('sophisticatedbackpacks:item/filter_upgrade');

    event.create('incomplete_pickup_upgrade').displayName('Incomplete Pickup Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_pickup_upgrade').displayName('Incomplete Advanced Pickup Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_restock_upgrade').displayName('Incomplete Restock Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_restock_upgrade').displayName('Incomplete Advanced Restock Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_deposit_upgrade').displayName('Incomplete Deposit Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_deposit_upgrade').displayName('Incomplete Advanced Deposit Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_refill_upgrade').displayName('Incomplete Refill Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_refill_upgrade').displayName('Incomplete Advanced Refill Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_pump_upgrade').displayName('Incomplete Pump Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_pump_upgrade').displayName('Incomplete Advanced Pump Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_smelting_upgrade').displayName('Incomplete Smelting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_auto_smelting_upgrade').displayName('Incomplete Auto Smelting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_blasting_upgrade').displayName('Incomplete Blasting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_auto_blasting_upgrade').displayName('Incomplete Auto Blasting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_smoking_upgrade').displayName('Incomplete Smoking Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_auto_smoking_upgrade').displayName('Incomplete Auto Smoking Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_compacting_upgrade').displayName('Incomplete Compacting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_compacting_upgrade').displayName('Incomplete Advanced Compacting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_void_upgrade').displayName('Incomplete Void Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_void_upgrade').displayName('Incomplete Advanced Void Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_feeding_upgrade').displayName('Incomplete Feeding Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_feeding_upgrade').displayName('Incomplete Advanced Feeding Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_xp_pump_upgrade').displayName('Incomplete Xp Pump Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_alchemy_upgrade').displayName('Incomplete Alchemy Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_alchemy_upgrade').displayName('Incomplete Advanced Alchemy Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_starter_tier').displayName('Incomplete Stack Upgrade Starter Tier').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_tier_1').displayName('Incomplete Stack Upgrade Tier 1').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_tier_2').displayName('Incomplete Stack Upgrade Tier 2').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_tier_3').displayName('Incomplete Stack Upgrade Tier 3').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_tier_4').displayName('Incomplete Stack Upgrade Tier 4').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_omega_tier').displayName('Incomplete Stack Upgrade Omega Tier').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_jukebox_upgrade').displayName('Incomplete Jukebox Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_jukebox_upgrade').displayName('Incomplete Advanced Jukebox Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_tool_swapper_upgrade').displayName('Incomplete Tool Swapper Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_advanced_tool_swapper_upgrade').displayName('Incomplete Advanced Tool Swapper Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_crafting_upgrade').displayName('Incomplete Crafting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stonecutter_upgrade').displayName('Incomplete Stonecutter Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_anvil_upgrade').displayName('Incomplete Anvil Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_smithing_upgrade').displayName('Incomplete Smithing Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_tank_upgrade').displayName('Incomplete Tank Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_battery_upgrade').displayName('Incomplete Battery Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_inception_upgrade').displayName('Incomplete Inception Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_everlasting_upgrade').displayName('Incomplete Everlasting Upgrade').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_tier_5').displayName('Incomplete Stack Upgrade Tier 5').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_tier_6').displayName('Incomplete Stack Upgrade Tier 6').texture('sophisticatedbackpacks:item/upgrade_base');
    event.create('incomplete_stack_upgrade_tier_7').displayName('Incomplete Stack Upgrade Tier 7').texture('sophisticatedbackpacks:item/upgrade_base');
    // --- BACKPACKS ---
    event.create('incomplete_copper_backpack').texture('sophisticatedbackpacks:item/copper_backpack').displayName('Incomplete Copper Backpack');
    event.create('incomplete_iron_backpack').texture('sophisticatedbackpacks:item/iron_backpack').displayName('Incomplete Iron Backpack');
    event.create('incomplete_gold_backpack').texture('sophisticatedbackpacks:item/gold_backpack').displayName('Incomplete Gold Backpack');
    event.create('incomplete_diamond_backpack').texture('sophisticatedbackpacks:item/diamond_backpack').displayName('Incomplete Diamond Backpack');
    event.create('incomplete_netherite_backpack').texture('sophisticatedbackpacks:item/netherite_backpack').displayName('Incomplete Netherite Backpack');
});
