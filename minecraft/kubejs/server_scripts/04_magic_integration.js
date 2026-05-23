// ==========================================
// PEAK EXPERT MODE â€” SCRIPT 04
// MAGIC INTEGRATION: ARS NOUVEAU + IRON'S SPELLBOOKS
// ==========================================
// Magic runs PARALLEL to technology, but they intersect
// at key points. The rule: magic ingredients in magical
// items, tech ingredients in tech items, BOTH in items
// that bridge the two worlds (like Ender IO's Soularium).
//
// CREATE remains central: even magic infrastructure
// benefits from mechanical precision.
//
// TWILIGHT FOREST is the gateway dimension for magic.
// You must explore it to access advanced Ars Nouveau.
// ==========================================

ServerEvents.recipes(event => {

    // ==========================================
    // SECTION 1: ARS NOUVEAU â€” MAGIC ERA 1
    // The first magical system. Create enhances it.
    // Twilight Forest materials unlock advanced tiers.
    // ==========================================

    // --- ARCANE CORE (The heart of Ars Nouveau) ---
    // Requires Create Brass: mechanical precision channels
    // magical energy more efficiently. This makes SENSE:
    // brass is a conductor, and arcane cores conduct Source.
    event.remove({ output: 'ars_nouveau:arcane_core' });
    event.shaped('ars_nouveau:arcane_core', [
        'GBG',
        'BSB',
        'GBG'
    ], {
        G: '#c:ingots/gold',
        B: 'create:brass_ingot',
        S: 'ars_nouveau:source_gem'
    });

    // --- SOURCE JAR (Stores liquid Source) ---
    // Glass + Brass fittings for a proper magical container
    event.remove({ output: 'ars_nouveau:source_jar' });
    event.shaped('ars_nouveau:source_jar', [
        'B B',
        'G G',
        'GBG'
    ], {
        B: 'create:brass_ingot',
        G: '#c:glass_blocks'
    });

    // --- SCRIBES TABLE (Where you design spells) ---
    // Needs Twilight Forest Ironwood: a naturally magical wood
    // perfect for a magical workstation (wood + iron + magic)
    event.remove({ output: 'ars_nouveau:scribes_table' });
    event.shaped('ars_nouveau:scribes_table', [
        'SSS',
        'I I',
        'W W'
    ], {
        S: 'minecraft:smooth_stone_slab',
        I: 'twilightforest:ironwood_ingot',
        W: '#minecraft:planks'
    });

    // --- ENCHANTING APPARATUS (Advanced magical crafting) ---
    // This is the Ars Nouveau "machine" â€” it deserves to need
    // Create Precision Mechanisms (mechanical precision for
    // precise enchantment channeling) + Twilight materials
    event.remove({ output: 'ars_nouveau:enchanting_apparatus' });
    event.shaped('ars_nouveau:enchanting_apparatus', [
        'IPI',
        'GAG',
        'IBI'
    ], {
        I: 'twilightforest:ironwood_ingot',
        P: 'create:precision_mechanism',
        G: '#c:ingots/gold',
        A: 'ars_nouveau:arcane_core',
        B: 'create:brass_casing'
    });

    // --- IMBUEMENT CHAMBER (Source infusion) ---
    // Requires Twilight Forest Steeleaf: a magical metal-plant
    // hybrid perfect for channeling Source into items
    event.remove({ output: 'ars_nouveau:imbuement_chamber' });
    event.shaped('ars_nouveau:imbuement_chamber', [
        'SAS',
        'L L',
        'SAS'
    ], {
        S: 'twilightforest:steeleaf_ingot',
        A: 'ars_nouveau:arcane_core',
        L: 'ars_nouveau:source_gem'
    });

    // --- RELAY (Source energy transfer) ---
    // Brass + Source = magical energy conductor
    event.remove({ output: 'ars_nouveau:relay' });
    event.shaped('ars_nouveau:relay', [
        ' S ',
        'BAB',
        ' S '
    ], {
        S: 'ars_nouveau:source_gem',
        B: 'create:brass_ingot',
        A: 'ars_nouveau:arcane_core'
    });

    // --- SPELL TURRETS (Automated magic = tech + magic) ---
    // Spell turrets are basically "magical deployers" â€” they
    // should need Create's Deployer as a base (mechanical
    // arm that casts spells instead of placing blocks)
    event.remove({ output: 'ars_nouveau:basic_spell_turret' });
    event.shaped('ars_nouveau:basic_spell_turret', [
        ' S ',
        'DAD',
        ' G '
    ], {
        S: 'ars_nouveau:source_gem',
        D: 'create:deployer',
        A: 'ars_nouveau:arcane_core',
        G: '#c:ingots/gold'
    });

    // --- ARCANE PEDESTAL ---
    // Brass base for magical display and ritual use
    event.remove({ output: 'ars_nouveau:arcane_pedestal' });
    event.shaped('ars_nouveau:arcane_pedestal', [
        'SBS',
        ' B ',
        'SBS'
    ], {
        S: 'minecraft:stone',
        B: 'create:brass_ingot'
    });

    // --- SPELL BOOKS (Progression through tiers) ---

    // Novice Spell Book: Accessible with basic magic + Create
    event.remove({ output: 'ars_nouveau:novice_spell_book' });
    event.shaped('ars_nouveau:novice_spell_book', [
        ' S ',
        'GBG',
        ' A '
    ], {
        S: 'ars_nouveau:source_gem',
        G: '#c:ingots/gold',
        B: 'minecraft:book',
        A: 'create:andesite_alloy'
    });

    // Apprentice Spell Book: Needs Twilight Forest progression
    // Naga Scale = you've defeated the Naga boss = earned power
    event.remove({ output: 'ars_nouveau:apprentice_spell_book' });
    event.shaped('ars_nouveau:apprentice_spell_book', [
        'NSN',
        'IBN',
        'GIG'
    ], {
        N: 'twilightforest:naga_scale',
        S: 'ars_nouveau:source_gem',
        I: 'twilightforest:ironwood_ingot',
        B: 'ars_nouveau:novice_spell_book',
        G: '#c:ingots/gold'
    });

    // Archmage Spell Book: Late-game magic, requires advanced tech
    // Knightmetal = deep Twilight progression (Goblin Knights)
    // Precision Mechanism = technological mastery enhances magic
    event.remove({ output: 'ars_nouveau:archmage_spell_book' });
    event.shaped('ars_nouveau:archmage_spell_book', [
        'KSK',
        'PBP',
        'KSK'
    ], {
        K: 'twilightforest:knightmetal_ingot',
        S: 'ars_nouveau:source_gem_block',
        P: 'create:precision_mechanism',
        B: 'ars_nouveau:apprentice_spell_book'
    });

    // ==========================================
    // SECTION 2: TWILIGHT FOREST ORE PROCESSING
    // Create's crushing gives bonus Twilight metals
    // ==========================================

    // Ironwood processing via Create
    event.recipes.create.crushing([
        'twilightforest:raw_ironwood',
        Item.of('twilightforest:raw_ironwood').withChance(0.4)
    ], 'twilightforest:ironwood_ore');

    // ==========================================
    // SECTION 3: IRON'S SPELLBOOKS â€” MAGIC ERA 2
    // Requires Ars Nouveau foundation.
    // Combat magic that needs both magical knowledge
    // and craftsmanship.
    // ==========================================

    // --- INSCRIPTION TABLE (Where you inscribe spells) ---
    // Requires Source Gems: you need Ars Nouveau knowledge
    // to write combat spells. Also needs Brass for precision.
    event.remove({ output: 'irons_spellbooks:inscription_table' });
    event.shaped('irons_spellbooks:inscription_table', [
        'SSS',
        'BAB',
        'W W'
    ], {
        S: 'minecraft:smooth_stone_slab',
        B: 'create:brass_ingot',
        A: 'ars_nouveau:source_gem',
        W: 'twilightforest:ironwood_ingot'
    });

    // --- SCROLL FORGE (Creates spell scrolls) ---
    // An advanced magical machine that combines Ars Nouveau's
    // enchanting knowledge with Iron's Spellbooks combat system
    event.remove({ output: 'irons_spellbooks:scroll_forge' });
    event.shaped('irons_spellbooks:scroll_forge', [
        'ISI',
        'PAP',
        'IGI'
    ], {
        I: 'twilightforest:ironwood_ingot',
        S: 'ars_nouveau:source_gem',
        P: 'create:precision_mechanism',
        A: 'ars_nouveau:arcane_core',
        G: '#c:ingots/gold'
    });

    // --- ALCHEMIST CAULDRON (Potion crafting for spells) ---
    // Needs Ars Nouveau Source + Create mechanical components
    event.remove({ output: 'irons_spellbooks:alchemist_cauldron' });
    event.shaped('irons_spellbooks:alchemist_cauldron', [
        'I I',
        'ISI',
        'BCB'
    ], {
        I: '#c:ingots/iron',
        S: 'ars_nouveau:source_gem',
        B: 'create:brass_ingot',
        C: 'minecraft:cauldron'
    });

    // --- INK SYSTEM (Tiered spell power) ---
    // Inks determine spell rarity. Higher tier inks need
    // progressively rarer materials from exploration.

    // Common Ink: Basic magical materials
    event.remove({ output: 'irons_spellbooks:common_ink' });
    event.shaped('irons_spellbooks:common_ink', [
        ' F ',
        'GBG',
        ' D '
    ], {
        F: 'minecraft:feather',
        G: 'minecraft:glow_ink_sac',
        B: 'minecraft:glass_bottle',
        D: 'ars_nouveau:magebloom_fiber'
    });

    // Uncommon Ink: Requires Twilight Forest materials
    event.remove({ output: 'irons_spellbooks:uncommon_ink' });
    event.shapeless('irons_spellbooks:uncommon_ink', [
        'irons_spellbooks:common_ink',
        'twilightforest:ironwood_ingot',
        'ars_nouveau:source_gem',
        'minecraft:lapis_lazuli'
    ]);

    // Rare Ink: Requires Wilden boss drops + Steeleaf
    event.remove({ output: 'irons_spellbooks:rare_ink' });
    event.shapeless('irons_spellbooks:rare_ink', [
        'irons_spellbooks:uncommon_ink',
        'ars_nouveau:wilden_horn',
        'twilightforest:steeleaf_ingot',
        'minecraft:blaze_powder'
    ]);

    // Epic Ink: Requires Knightmetal + Fiery Ingot (deep TF)
    event.remove({ output: 'irons_spellbooks:epic_ink' });
    event.shapeless('irons_spellbooks:epic_ink', [
        'irons_spellbooks:rare_ink',
        'twilightforest:knightmetal_ingot',
        'twilightforest:fiery_ingot',
        'ars_nouveau:wilden_wing'
    ]);

    // Legendary Ink: Requires endgame magical materials
    // Carminite from TF + Wilden Spike (rarest Wilden drop)
    event.remove({ output: 'irons_spellbooks:legendary_ink' });
    event.shapeless('irons_spellbooks:legendary_ink', [
        'irons_spellbooks:epic_ink',
        'twilightforest:carminite',
        'ars_nouveau:wilden_spike',
        'minecraft:nether_star'
    ]);

    // --- ARCANE ESSENCE processing via Create ---
    // Arcane Essence can be crushed in Create for bonus output
    event.recipes.create.crushing([
        '2x irons_spellbooks:arcane_essence',
        Item.of('irons_spellbooks:arcane_essence').withChance(0.3)
    ], 'ars_nouveau:source_gem');

    // --- ARCANE INGOT (Iron's Spellbooks core material) ---
    // Made by mixing iron with Source in Create's Mixer
    // (Mechanical infusion of magic into metal = makes sense)
    event.recipes.create.mixing(
        'irons_spellbooks:arcane_ingot',
        [
            '#c:ingots/gold',
            'irons_spellbooks:arcane_essence',
            'irons_spellbooks:arcane_essence',
            'ars_nouveau:source_gem'
        ]
    ).heated();

    // ==========================================
    // SECTION 4: SOURCE GEM PROCESSING VIA CREATE
    // Create's machinery can process and purify Source
    // ==========================================

    // Create Mixing: Raw Source materials â†’ Pure Source Gems
    // (Mechanical purification of wild magical energy)
    event.recipes.create.mixing(
        '2x ars_nouveau:source_gem',
        [
            'ars_nouveau:sourceberry_bush',
            'ars_nouveau:sourceberry_bush',
            'ars_nouveau:sourceberry_bush',
            'minecraft:amethyst_shard'
        ]
    ).heated();

    // Create Crushing: Amethyst can yield Source fragments
    // (Amethyst has innate magical resonance in lore)
    event.recipes.create.crushing([
        'minecraft:amethyst_shard',
        Item.of('ars_nouveau:source_gem').withChance(0.15)
    ], 'minecraft:amethyst_block');

    // ==========================================
    // SECTION 5: ARS CREO ENHANCED INTEGRATION
    // Since ars_creo already exists, we enhance the
    // crossover between Create and Ars Nouveau
    // ==========================================

    // Source-powered Create machines:
    // Mixing Source Gems with Create metals yields enhanced alloys
    event.recipes.create.mixing(
        'create:brass_ingot',
        [
            '#c:ingots/copper',
            'create:zinc_ingot',
            Item.of('ars_nouveau:source_gem').withChance(0.1)
        ]
    ).heated();

    // --- SPELL BOOKS GATES (Avaritia Integration) ---

    // Move Ice Spellbook to Sculk Crafting Table (Tier 1)
    event.remove({ output: 'irons_spellbooks:ice_spell_book' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "SIS",
            "IBI",
            "SIS"
        ],
        key: {
            S: { item: 'twilightforest:naga_scale' },
            I: { item: 'minecraft:packed_ice' },
            B: { item: 'irons_spellbooks:apprentice_spell_book' }
        },
        result: { id: 'irons_spellbooks:ice_spell_book', count: 1 },
        tier: 1
    });

    // Move Dragonskin Spellbook to End Crafting Table (Tier 2)
    event.remove({ output: 'irons_spellbooks:dragonskin_spell_book' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "DDDDD",
            "DAPAD",
            "DPBPD",
            "DAPAD",
            "DDDDD"
        ],
        key: {
            D: { item: 'minecraft:barrier' },
            A: { item: 'irons_spellbooks:arcane_ingot' },
            P: { item: 'kubejs:primordial_dragon_blood' },
            B: { item: 'irons_spellbooks:apprentice_spell_book' }
        },
        result: { id: 'irons_spellbooks:dragonskin_spell_book', count: 1 },
        tier: 2
    });

    console.log('[PEAK Expert Mode] Script 04: Magic Integration (Ars Nouveau + Iron Spellbooks) loaded!');
});



