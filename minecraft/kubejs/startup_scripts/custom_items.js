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
});
