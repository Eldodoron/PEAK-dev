// ==========================================
// PEAK EXPERT MODE Ã¢â‚¬â€ SCRIPT 04
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
    // SECTION 1: ARS NOUVEAU Ã¢â‚¬â€ MAGIC ERA 1
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
    // Pure magic starter workstation
    event.remove({ output: 'ars_nouveau:scribes_table' });
    event.shaped('ars_nouveau:scribes_table', [
        'SSS',
        'I I',
        'W W'
    ], {
        S: 'minecraft:smooth_stone_slab',
        I: '#c:ingots/gold',
        W: '#minecraft:planks'
    });

    // --- ENCHANTING APPARATUS (Ars Nouveau enchanting workstation) ---
    event.remove({ output: 'ars_nouveau:enchanting_apparatus' });
    event.shaped('ars_nouveau:enchanting_apparatus', [
        'DGD',
        'GAG',
        'DBD'
    ], {
        D: '#c:gems/diamond',
        G: '#c:ingots/gold',
        A: 'ars_nouveau:arcane_core',
        B: 'ars_nouveau:source_gem'
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
    // Spell turrets are basically "magical deployers" Ã¢â‚¬â€ they
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
        A: 'create_sa:heap_of_experience'
    });

    // Apprentice Spell Book: CEI + Irons Spellbooks + Ars Nouveau
    event.remove({ output: 'ars_nouveau:apprentice_spell_book' });
    event.shaped('ars_nouveau:apprentice_spell_book', [
        'TET',
        'GBG',
        'RSR'
    ], {
        T: 'ars_nouveau:blank_thread',
        E: 'create_enchantment_industry:super_experience_nugget',
        G: '#c:ingots/gold',
        B: 'ars_nouveau:novice_spell_book',
        R: '#kubejs:irons_runes',
        S: 'ars_nouveau:source_gem'
    });

    // Archmage Spell Book: Pure late-game magic, no tech required
    // Wilden Tribute = defeated the Wilden Chimera (Ars Nouveau boss)
    // Magic Beans = deep Twilight Forest progression
    // Mystic Essence = Gates of Avarice lore material
    // Apotheosis Gem = mastery over the Apotheosis system
    event.remove({ output: 'ars_nouveau:archmage_spell_book' });
    event.shaped('ars_nouveau:archmage_spell_book', [
        'WSW',
        'GBG',
        'TMT'
    ], {
        W: 'ars_nouveau:wilden_tribute',
        S: 'ars_nouveau:source_gem_block',
        G: 'gatesofavarice:mystic_essence',
        B: 'ars_nouveau:apprentice_spell_book',
        T: 'twilightforest:magic_beans',
        M: 'apotheosis:gem'
    });

    // ==========================================
    // SECTION 2: TWILIGHT FOREST ORE PROCESSING
    // Create's crushing gives bonus Twilight metals
    // ==========================================



    // ==========================================
    // SECTION 3: IRON'S SPELLBOOKS Ã¢â‚¬â€ MAGIC ERA 2
    // Requires Ars Nouveau foundation.
    // Combat magic that needs both magical knowledge
    // and craftsmanship.
    // ==========================================

    // --- INSCRIPTION TABLE ---
    event.remove({ output: 'irons_spellbooks:inscription_table' });
    event.shaped('irons_spellbooks:inscription_table', [
        'ISW',
        ' D '
    ], {
        I: Ingredient.of(['irons_spellbooks:common_ink', 'irons_spellbooks:uncommon_ink', 'irons_spellbooks:rare_ink', 'irons_spellbooks:epic_ink', 'irons_spellbooks:legendary_ink']),
        S: Ingredient.of(['#curios:spellbook', 'ars_nouveau:novice_spell_book', 'ars_nouveau:apprentice_spell_book', 'ars_nouveau:archmage_spell_book']),
        W: 'minecraft:writable_book',
        D: Ingredient.of([
            'refurbished_furniture:dark_oak_desk',
            'refurbished_furniture:dark_oak_table',
            'refurbished_furniture:spruce_desk',
            'refurbished_furniture:spruce_table'
        ])
    });

    // --- SCROLL FORGE ---
    event.remove({ output: 'irons_spellbooks:scroll_forge' });
    event.shaped('irons_spellbooks:scroll_forge', [
        'SSS',
        ' A ',
        'OOO'
    ], {
        S: Ingredient.of(['minecraft:polished_deepslate', 'minecraft:polished_deepslate_slab']),
        A: 'ars_nouveau:arcane_core',
        O: 'minecraft:crying_obsidian'
    });

    // --- ALCHEMIST CAULDRON ---
    event.remove({ output: 'irons_spellbooks:alchemist_cauldron' });
    event.shaped('irons_spellbooks:alchemist_cauldron', [
        ' E ',
        ' C ',
        'SSS'
    ], {
        E: Ingredient.of([
            'irons_spellbooks:arcane_essence', 'irons_spellbooks:cinder_essence',
            'ars_nouveau:abjuration_essence', 'ars_nouveau:air_essence', 'ars_nouveau:conjuration_essence',
            'ars_nouveau:earth_essence', 'ars_nouveau:fire_essence', 'ars_nouveau:manipulation_essence',
            'ars_nouveau:water_essence', 'gatesofavarice:arcane_essence', 'gatesofavarice:dark_essence',
            'gatesofavarice:mystic_essence'
        ]),
        C: 'minecraft:cauldron',
        S: 'minecraft:stick'
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

    // Uncommon Ink: Early-mid magic ink using amethyst
    event.remove({ output: 'irons_spellbooks:uncommon_ink' });
    event.shapeless('irons_spellbooks:uncommon_ink', [
        'irons_spellbooks:common_ink',
        'minecraft:amethyst_shard',
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
        CreateItem.of('irons_spellbooks:arcane_essence', 0.3)
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

    // Create Mixing: Raw Source materials Ã¢â€ â€™ Pure Source Gems
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
        CreateItem.of('ars_nouveau:source_gem', 0.15)
    ], 'minecraft:amethyst_block');

    // ==========================================
    // SECTION 5: ARS CREO ENHANCED INTEGRATION
    // Since ars_creo already exists, we enhance the
    // crossover between Create and Ars Nouveau
    // ==========================================


    // --- SPELL BOOKS GATES (Avaritia Integration) ---

    // Move Ice Spellbook to Sculk Crafting Table (Tier 1)
    event.remove({ output: 'irons_spellbooks:ice_spell_book' });
    event.custom({
        type: 'avaritia:shaped_table',
        pattern: [
            "FWF",
            "IBI",
            "FWF"
        ],
        key: {
            F: Ingredient.of(['twilightforest:arctic_fur', 'twilightforest:alpha_yeti_fur']).toJson(),
            W: { item: 'ars_nouveau:water_essence' },
            I: { item: 'minecraft:blue_ice' },
            B: Ingredient.of(['ars_nouveau:apprentice_spell_book', 'irons_spellbooks:diamond_spell_book']).toJson()
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
            D: { item: 'iceandfire:dragonbone' },
            A: { item: 'irons_spellbooks:arcane_ingot' },
            P: { item: 'kubejs:primordial_dragon_blood' },
            B: { item: 'ars_nouveau:apprentice_spell_book' }
        },
        result: { id: 'irons_spellbooks:dragonskin_spell_book', count: 1 },
        tier: 2
    });

    console.log('[PEAK Expert Mode] Script 04: Magic Integration (Ars Nouveau + Iron Spellbooks) loaded!');
});



