// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 05
// DARK MAGIC + DIMENSIONS
// Malum (Spirits/Souls) + Vampirism (Blood)
// Deeper Darker + Undergarden enhanced roles
// ==========================================
// Malum is the bridge between magic and Ender IO.
// Its spirit system feeds directly into Ender IO's
// soul-based technology (Soularium, Soul Machines).
//
// Vampirism represents the pinnacle of dark magic,
// with Pure Blood being a key endgame material for
// Draconic Evolution's higher tiers.
//
// Deeper Darker provides endgame materials that gate
// access to Draconic Evolution's Wyvern tier.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: MALUM â€” DARK MAGIC (MAGIC ERA 3)
    // Spirits, souls, and the bridge to Ender IO
    // ==========================================

    // --- SPIRIT ALTAR (Malum's core crafting station) ---
    // The spiritual workbench. Needs Ars Nouveau Source
    // (you need basic magical knowledge before dark magic)
    // and Create Brass (precision channeling of spirits)
    event.remove({ output: 'malum:spirit_altar' });
    event.shaped('malum:spirit_altar', [
        'GSG',
        'BAB',
        'SSS'
    ], {
        G: '#c:ingots/gold',
        S: 'malum:soulstone_ingot',
        B: 'create:brass_ingot',
        A: 'ars_nouveau:source_gem'
    });

    // --- SPIRIT CRUCIBLE (Advanced spirit processing) ---
    // Requires Enchanting Apparatus knowledge + dark materials
    // The crucible refines raw spirits into usable essences
    event.remove({ output: 'malum:spirit_crucible' });
    event.shaped('malum:spirit_crucible', [
        'SHS',
        'HAH',
        'SPS'
    ], {
        S: 'malum:soul_stained_steel_ingot',
        H: 'malum:hallowed_gold_ingot',
        A: 'ars_nouveau:arcane_core',
        P: 'create:precision_mechanism'
    });

    // --- SOUL STAINED STEEL (Malum's dark metal) ---
    // Created by mixing steel with soul essence in Create's Mixer
    // (Mechanical infusion of souls into steel = dark engineering)
    event.remove({ output: 'malum:soul_stained_steel_ingot' });
    event.recipes.create.mixing(
        'malum:soul_stained_steel_ingot',
        [
            '#c:ingots/steel',
            'malum:soulstone_ingot',
            'minecraft:soul_sand'
        ]
    ).heated();



    // --- HEX ASH (Critical dark magic reagent) ---
    // Used later in Draconic Evolution Wyvern tier recipes
    // Made by Create crushing soul materials
    event.recipes.create.crushing([
        'malum:hex_ash',
        CreateItem.of('malum:hex_ash', 0.5)
    ], 'malum:soulstone_ingot');

    // --- SPIRIT FABRIC ---
    // Needs magebloom fiber from Ars Nouveau (magical textile base)
    // This connects the two magic systems organically
    event.remove({ output: 'malum:spirit_fabric' });
    event.shaped('malum:spirit_fabric', [
        'FHF',
        'HSH',
        'FHF'
    ], {
        F: 'ars_nouveau:magebloom_fiber',
        H: 'malum:hex_ash',
        S: 'malum:processed_soulstone'
    });

    // ==========================================
    // SECTION 2: MALUM â†’ ENDER IO BRIDGE
    // Malum's spirits are literally souls.
    // Ender IO's Soularium is literally soul-metal.
    // This is the most natural cross-mod connection.
    // ==========================================

    // SOULARIUM INGOT (Ender IO's soul metal)
    // Normally: Gold + Soul Sand in Alloy Smelter
    // Expert Mode: Requires Malum spirit processing first!
    // Soul Stained Steel (Malum's processed souls) + Gold
    // in the Alloy Smelter or Create Mixer
    event.remove({ output: 'enderio:soularium_ingot' });
    event.recipes.create.mixing(
        'enderio:soularium_ingot',
        [
            '#c:ingots/gold',
            'malum:soul_stained_steel_ingot',
            'malum:hex_ash'
        ]
    ).superheated();

    // PULSATING CRYSTAL (Ender IO â€” magical ender tech)
    // Requires Source Gems from Ars Nouveau
    // (Pulsating energy = magical resonance = Source)
    event.remove({ output: 'enderio:pulsating_crystal' });
    event.recipes.create.mixing(
        'enderio:pulsating_crystal',
        [
            'minecraft:ender_pearl',
            'ars_nouveau:source_gem',
            '#c:gems/diamond'
        ]
    ).heated();

    // VIBRANT CRYSTAL (Ender IO â€” advanced magical tech)
    // Requires both tech (Precision Mechanism) and magic (Source)
    event.remove({ output: 'enderio:vibrant_crystal' });
    event.recipes.create.mixing(
        'enderio:vibrant_crystal',
        [
            'enderio:pulsating_crystal',
            'minecraft:glowstone_dust',
            'ars_nouveau:source_gem',
            'malum:hallowed_gold_ingot'
        ]
    ).superheated();

    // ==========================================
    // SECTION 3: VAMPIRISM â€” BLOOD MAGIC (MAGIC ERA 4)
    // The darkest magic. Late-game magical progression.
    // Blood = life force = power for Draconic Evolution.
    // ==========================================

    // --- VAMPIRE FANG processing ---
    // Vampire Fangs can be processed in Create for essence
    event.recipes.create.crushing([
        'minecraft:bone_meal',
        CreateItem.of('minecraft:bone_meal', 0.5),
        CreateItem.of('minecraft:redstone', 0.25)
    ], 'vampirism:vampire_fang');

    // --- BLOOD PROCESSING (Tech meets dark magic) ---
    // Mekanism's Chemical systems can process blood
    // (Blood is a fluid â†’ Mekanism handles fluids â†’ logical)
    // This is mostly a narrative connection for Prompt 4

    // --- HUNTER CROSSBOW ENHANCED ---
    // Vampire Hunters need tech to fight supernatural threats
    // Hunter weapons benefit from Create engineering
    event.remove({ output: 'vampirism:crossbow_arrow_normal' });
    event.shaped('8x vampirism:crossbow_arrow_normal', [
        ' I ',
        ' S ',
        ' F '
    ], {
        I: '#c:ingots/iron',
        S: 'create:shaft',
        F: 'minecraft:feather'
    });

    // --- GARLIC PROCESSING via Create ---
    // Garlic can be crushed in Create for concentrated garlic
    // (Used in anti-vampire technology)
    event.recipes.create.milling([
        'vampirism:item_garlic',
        CreateItem.of('vampirism:item_garlic', 0.5)
    ], 'vampirism:item_garlic');

    // ==========================================
    // SECTION 4: DEEPER DARKER â€” ENDGAME DIMENSION
    // Materials here gate Draconic Evolution Wyvern Tier
    // ==========================================

    // Deeper Darker ores processed via Create for bonus
    event.recipes.create.crushing([
        'minecraft:echo_shard',
        CreateItem.of('minecraft:echo_shard', 0.35),
        CreateItem.of('minecraft:sculk', 0.5)
    ], 'minecraft:sculk_catalyst');

    // --- WARDEN CARAPACE ---
    // The Warden's shell is one of the hardest materials.
    // Used as a component in Draconic Evolution Wyvern cores.
    // (Defined in Prompt 4's Draconic recipes)

    // --- REINFORCED ECHO SHARD ---
    // Created by combining Echo Shards with tech materials
    // in Create's mechanical mixer (tech reinforcement of
    // a naturally magical material)
    event.remove({ output: 'deeperdarker:reinforced_echo_shard' });
    event.recipes.create.mixing(
        'deeperdarker:reinforced_echo_shard',
        [
            'minecraft:echo_shard',
            'minecraft:echo_shard',
            '#c:ingots/steel',
            'malum:soul_stained_steel_ingot'
        ]
    ).superheated();

    // --- SOUL CRYSTAL (Deeper Darker's magical crystal) ---
    // Requires both dark magic (Malum) and Ars Nouveau Source
    // to crystallize raw soul energy from the deep dark
    event.remove({ output: 'deeperdarker:soul_crystal' });
    event.recipes.create.mixing(
        'deeperdarker:soul_crystal',
        [
            'minecraft:echo_shard',
            'malum:processed_soulstone',
            'ars_nouveau:source_gem',
            'minecraft:amethyst_shard'
        ]
    ).superheated();

    // ==========================================
    // SECTION 5: CROSS-MAGIC SYNERGIES
    // Items that bridge multiple magic systems
    // ==========================================

    // --- ENCHANTED GOLDEN APPLE ---
    // Remove cheap crafting, make it a magic + tech feat
    event.remove({ output: 'minecraft:enchanted_golden_apple' });
    event.recipes.create.mixing(
        'minecraft:enchanted_golden_apple',
        [
            'minecraft:golden_apple',
            'ars_nouveau:source_gem_block',
            'malum:hallowed_gold_ingot',
            'malum:hallowed_gold_ingot',
            'malum:hallowed_gold_ingot',
            'malum:hallowed_gold_ingot'
        ]
    ).superheated();

    // --- NETHER STAR ALTERNATIVE ---
    // If you can't farm Withers, you can CREATE a Nether Star
    // using the pinnacle of both tech and magic
    // (This is expensive but provides an alternative path)
    event.recipes.create.mixing(
        'minecraft:nether_star',
        [
            'malum:soul_stained_steel_ingot',
            'malum:soul_stained_steel_ingot',
            'malum:hallowed_gold_ingot',
            'malum:hallowed_gold_ingot',
            'ars_nouveau:source_gem_block',
            'minecraft:wither_skeleton_skull',
            'minecraft:wither_skeleton_skull',
            'minecraft:wither_skeleton_skull'
        ]
    ).superheated();

    // --- TOTEM OF UNDYING ---
    // Require both magic systems for this powerful item
    event.remove({ output: 'minecraft:totem_of_undying' });
    event.recipes.create.mixing(
        'minecraft:totem_of_undying',
        [
            'malum:hallowed_gold_ingot',
            'malum:hallowed_gold_ingot',
            'malum:hallowed_gold_ingot',
            '#c:gems/emerald',
            'ars_nouveau:source_gem',
            'twilightforest:fiery_ingot'
        ]
    ).superheated();

    // ==========================================
    // SECTION 6: MAGICAL ARMOR PROGRESSION
    // Magical armors need materials from multiple systems
    // ==========================================

    // Wizard Armor (All The Wizard Gear) should need
    // both Ars Nouveau and Iron's Spellbooks materials
    // (This mod provides gear for spellcasters)

    // Fantasy Armor should require Twilight Forest materials
    // (Fantasy themes match the fairy-tale dimension)

    // Immersive Armors magical tiers need Source Gems
    // (Magical enhancement of physical protection)

    // ==========================================
    // SECTION 7: APOTHEOSIS ENCHANTING INTEGRATION
    // Apotheosis enhances enchanting â€” connect it to
    // the magical infrastructure we've built
    // ==========================================

    // Apotheosis Enchantment Library needs Ars Nouveau Source
    // (A library of enchantments should have magical knowledge)
    event.remove({ output: 'apothic_enchanting:library' });
    event.shaped('apothic_enchanting:library', [
        'SBS',
        'BAB',
        'SBS'
    ], {
        S: 'ars_nouveau:source_gem',
        B: 'minecraft:book',
        A: 'create:brass_casing'
    });

    // Apotheosis Ender Shelf needs Source + Ender Pearl
    event.remove({ output: 'apothic_enchanting:endshelf' });
    event.shaped('apothic_enchanting:endshelf', [
        'SES',
        'EBE',
        'SES'
    ], {
        S: 'ars_nouveau:source_gem',
        E: 'minecraft:ender_pearl',
        B: 'minecraft:bookshelf'
    });

    console.log('[PEAK Expert Mode] Script 05: Dark Magic + Dimensions loaded!');
});


