# PEAK Modpack — Comprehensive Deep AI Reference & Buzzword Audit Report

## 1. Executive Summary

A comprehensive, multi-layered audit was conducted across the entire **PEAK** modpack workspace (`minecraft/kubejs/`, `minecraft/config/`, `minecraft/datapacks/`, root documentation, distribution scripts in `scrapped_tools/`, and Desktop export staging `ServerPackStaging`).

### Key Verified Findings:
1. **Critical "Surgical" / "Surgically" Marker**: Exactly **8 occurrences across 5 unique files** in the active repository (plus **3 mirrored occurrences** in the Desktop `ServerPackStaging` export). Found across KubeJS script headers, in-game console logs, FTB Quest subtitles, and release descriptions.
2. **Explicit AI Assistants/Names**: **ZERO** active occurrences of `"ChatGPT"`, `"Antigravity"`, `"Claude"`, `"Gemini"`, `"Copilot"`, `"OpenAI"`, or `"LLM"` in custom game scripts, quest prose, or configs.
3. **Rule 1 Metadata Attribution Violations (Omitted in Prior Investigation)**: Identified **9 JSON model files** containing `"credit": "Made with Blockbench"` and **24 JSON model files** containing `"credit": "zanderest"` in `minecraft/kubejs/assets/` which violate Rule 1 of `GEMINI.md` regarding metadata attribution.
4. **AI Brainstorming, Inner Thoughts & Conversational Editorializing in Comments**: Cataloged **24 script files** with self-dialogue, implementation debates (*"We can't easily iterate all recipes..."*), conversational commentary (*"basically 'magical deployers'"*, *"You can't skip Create"*, *"Quality of life items should feel earned"*, *"just in case"*), and first-person plural statements (*"we use"*, *"our custom"*, *"we add"*).
5. **Stereotypical AI Buzzwords**: Cataloged occurrences of words favored by LLMs, including **"surgical"**, **"seamless"**, **"cornerstone"**, **"unleash"**, **"meticulously"**, **"synergy"**, **"harness"**, **"embark"**, and **"mastery"**.
6. **Prior Investigation Error Corrections**: Corrected a false-positive in the prior investigation that mistakenly flagged the *Apokinetics* mod's `DonationPromptClient` class as an AI prompt artifact.

In strict compliance with instructions, **zero game files or scripts were modified or deleted**. All findings are cataloged below with exact file paths, line numbers, snippets, and neutral technical replacements for review.

---

## 2. Occurrences of "Surgical" / "Surgically" (Critical Priority)

| File Path | Line | Snippet | Type / Context |
| :--- | :--- | :--- | :--- |
| `minecraft/kubejs/client_scripts/apokinetics_unregister.js` | 3 | `// Surgically unregister Apokinetics donation prompt from NeoForge event bus` | Script header comment |
| `minecraft/kubejs/client_scripts/apokinetics_unregister.js` | 11 | `console.info('[PEAK Fix] Surgically unregistered com.fishguy129.apokinetics.client.DonationPromptClient to silence donation prompts.');` | In-game client console log |
| `minecraft/kubejs/startup_scripts/apokinetics_unregister.js` | 3 | `// Surgically unregister Apokinetics donation prompt from NeoForge event bus` | Script header comment |
| `minecraft/kubejs/startup_scripts/apokinetics_unregister.js` | 11 | `console.info('[PEAK Fix] Surgically unregistered com.fishguy129.apokinetics.client.DonationPromptClient to silence donation prompts.');` | In-game startup console log |
| `minecraft/kubejs/startup_scripts/fix_malum_watchdog.js` | 5 | `// This script surgically unregisters Malum's RuntimeEvents class` | Script header comment |
| `minecraft/kubejs/startup_scripts/fix_malum_watchdog.js` | 13 | `console.info('[PEAK Fix] Surgically unregistered com.sammy.malum.events.RuntimeEvents to prevent watchdog hangs.');` | In-game startup console log |
| `minecraft/config/ftbquests/quests/lang/en_us.snbt` | 1810 | `quest.4103000000000020.quest_subtitle: "Filter, extract, and sort with surgical precision."` | Player-visible quest subtitle (Create Logistics) |
| `scrapped_tools/curseforge_peak_lite_description.md` | 16 | `Every single heavy visual engine has been surgically stripped while leaving **100% of the gameplay...**` | Modpack release description |

### Mirrored Occurrences in Desktop Server Pack Staging:
- `ServerPackStaging/kubejs/startup_scripts/fix_malum_watchdog.js`: Lines 5 & 13
- `ServerPackStaging/config/ftbquests/quests/lang/en_us.snbt`: Line 1810

---

## 3. GEMINI.md Rule 1 Metadata Attribution Findings

`GEMINI.md` Rule 1 strictly prohibits comments, headers, or metadata attributing code or assets (e.g. `"credit": "Made with Blockbench / Fixed by Antigravity"`). The prior investigation skipped `.json` model files in `minecraft/kubejs/assets/`. The following files contain attribution metadata:

### 3.1 "Made with Blockbench" (9 files)
- `minecraft/kubejs/assets/minecraft/models/block/sunflower_top.json:3`
- `minecraft/kubejs/assets/minecraft/models/block/sunflower_bottom.json:2`
- `minecraft/kubejs/assets/minecraft/models/block/flowerbed_1.json:2`
- `minecraft/kubejs/assets/minecraft/models/block/flowerbed_2.json:2`
- `minecraft/kubejs/assets/minecraft/models/block/flowerbed_3.json:2`
- `minecraft/kubejs/assets/minecraft/models/block/flowerbed_4.json:2`
- `minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_with_seeds.json:3`
- `minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_no_seeds.json:3`
- `minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_bottom.json:2`

### 3.2 Third-Party Author Credits in Custom Overrides (24 files)
- `minecraft/kubejs/assets/cubicleaves/models/block/template_*.json:2` (24 files contain `"credit": "zanderest"`)
- `minecraft/kubejs/assets/kubejs/models/block/green_screen.json:2` (`"credit": "PEAK"`)

---

## 4. AI Brainstorming, Inner Thoughts & Conversational Editorializing in Comments

A total of **24 script files** contain comments where AI agents recorded inner design deliberations, implementation arguments, conversational filler, or first-person pronouns:

1. **`minecraft/kubejs/server_scripts/00_recipe_fixer.js:22-28`**:
   ```javascript
   // We can't easily iterate all recipes and modify their raw JSON in 1.21 
   // without potentially causing more issues, but we can try to fix the 
   // most common ones that KubeJS is complaining about if they are 
   // being added via scripts.
   // However, the warnings in the log are mostly from OTHER mods' internal data.
   // KubeJS is just reporting that IT failed to parse them for its own system.
   ```
2. **`minecraft/kubejs/server_scripts/02_create_era_gates.js`**:
   - Line 49: `// IE is the SECOND tech era. You can't skip Create.`
   - Line 178: `// Power generation should feel earned`
   - Line 217: `// These are late-Create era. They should require`
   - Line 308: `// Quality of life items should feel earned`
   - Lines 350–351: `// Instead of Mechanical Crafters or overriding the standard recipe (which wipes NBT), we use Sequenced Assembly. The base backpack is the transitional item, so its NBT is preserved!`
3. **`minecraft/kubejs/server_scripts/04_magic_integration.js`**:
   - Lines 5–15: `// Magic runs PARALLEL to technology, but they intersect... You must explore it to access advanced Ars Nouveau.`
   - Line 52: `// --- SCRIBES TABLE (Where you design spells) ---`
   - Lines 106–108: `// Spell turrets are basically "magical deployers" — they should need Create's Deployer as a base (mechanical arm that casts spells instead of placing blocks)`
   - Line 167: `// Apotheosis Gem = mastery over the Apotheosis system`
   - Lines 343–344: `// Since ars_creo already exists, we enhance the crossover between Create and Ars Nouveau`
4. **`minecraft/kubejs/server_scripts/05_dark_magic_dimensions.js`**:
   - Lines 23–25: `// The spiritual workbench. Needs Ars Nouveau Source (you need basic magical knowledge before dark magic)`
   - Line 144: `// a naturally magical material)`
   - Line 171: `// SECTION 5: CROSS-MAGIC SYNERGIES`
   - Lines 191–193: `// If you can't farm Withers, you can CREATE a Nether Star... (This is expensive but provides an alternative path)`
   - Lines 240–245: `// Apotheosis enhances enchanting — connect it to the magical infrastructure we've built... (A library of enchantments should have magical knowledge)`
5. **`minecraft/kubejs/server_scripts/06_enderio_ae2.js:6-14`**:
   `// Ender IO is where technology and magic MERGE... AE2 sits ABOVE Ender IO... You need Ender IO's conduits and Mekanism's circuits before touching AE2.`
6. **`minecraft/kubejs/server_scripts/07_draconic_endgame.js`**:
   - Lines 11–13: `// Ice and Fire's Dragonsteel is the physical endgame. You need actual dragon forges (hard to automate!)`
   - Line 26: `// They feed into Draconic Evolution's mid-tiers.`
7. **`minecraft/kubejs/server_scripts/08_reliquary_balance.js`**:
   - Lines 22–24: `// This item should be a TROPHY of late-game mastery, not a cheap shortcut. You need to have mastered both magic AND technology...`
   - Lines 43–45: `// Alkahestry should NOT be able to duplicate any of these endgame/progression items. We remove these specific alkahestry recipes.`
8. **`minecraft/kubejs/server_scripts/09_custom_loot_tables.js:7-8`**:
   `// We use EntityEvents.death to ensure compatibility across all KubeJS versions.`
9. **`minecraft/kubejs/server_scripts/10_avaritia_final_polish.js`**:
   - Line 21: `// They also work in Mechanical Crafters!`
   - Line 176: `// The ultimate mastery of gastronomy.`
   - Line 190: `// Infinite food mastery`
   - Line 210: `// PLUS our custom boss drops.`
   - Line 239: `// Mastery of all foods`
10. **`minecraft/kubejs/server_scripts/12_food_buffs.js:5`**:
    `// Makes late-game foods actually worth crafting`
11. **`minecraft/kubejs/server_scripts/15_loot_nerfs.js:9-11`**:
    `// Slimes split into tiny slimes, causing them to drop absurd amounts of Malum spirits. We completely remove these drops from them.`
12. **`minecraft/kubejs/server_scripts/16_recipes_and_balance.js:10`**:
    `event.remove({ type: 'create:mixing', output: '#c:ingots/hallowed_gold' }); // 1.21 uses #c instead of #forge sometimes`
13. **`minecraft/kubejs/server_scripts/17_goblin_trades.js`**:
    - Line 8: `// They will occasionally sell an Infinity Fragment for an insane price!`
    - Line 10: `// We add to the legendary.json for the normal goblin trader`
    - Line 13: `"replace": false, // We append, not replace the whole file`
14. **`minecraft/kubejs/server_scripts/18_boss_duplicator.js`**:
    - Line 40: `// but we will continue to use the event fallback to ensure it works across all NeoForge builds.`
    - Line 45: `// Modern KubeJS method to leave item in grid!`
15. **`minecraft/kubejs/server_scripts/20_disable_bugged_spells.js:32`**:
    `// Also prevent right clicks just in case`
16. **`minecraft/kubejs/server_scripts/22_apotheosis_gear_sets.js:7`**:
    `// We use ServerEvents.generateData to ensure they are registered correctly in 1.21.`
17. **`minecraft/kubejs/server_scripts/23_zenith_saber.js`**:
    - Line 45: `// This runs for EVERY crafted item, so we exit instantly if not a diamond sword.`
    - Line 51: `// 3. Verify if it is our custom Zenith Saber`
18. **`minecraft/kubejs/server_scripts/25_hardcoded_minibosses.js`**:
    - Line 393: `// They do NOT drop the gear (it died with them for a reason)`
    - Line 400: `// Scale + attributes: Slightly bigger, much tougher, same speed (they're undead, they shamble)`
19. **`minecraft/kubejs/server_scripts/expert_mode_recipes.js`**:
    - Line 20: `// (We keep IE Crusher and Mekanism Enrichment as UPGRADES, not alternatives)`
    - Line 30: `// Note: We keep vanilla smelting as a basic option but Create gives 2x`
    - Line 38: `// Every mod's FIRST crafting step needs this`
    - Lines 63–65: `// (Compressed Iron is normally made by just placing iron under pressure, we add a Create prerequisite by requiring the Pressure Chamber itself to use Create components)`
    - Line 166: `// but TFMG gets you there first via Create infrastructure`
20. **`minecraft/kubejs/server_scripts/random_gateways.js:566, 604`**:
    `// Proximity verification: ensure this is our random gateway and not a player's private Gate Pearl`
21. **`minecraft/kubejs/startup_scripts/40_iaf_durability_buff.js:3`**:
    `// We use explicit values because reading maxDamage dynamically returns undefined/NaN during startup.`
22. **`minecraft/kubejs/startup_scripts/block_factory_buffs.js:13`**:
    `// Add our new modifiers`
23. **`minecraft/kubejs/startup_scripts/custom_items.js:154`**:
    `// The ultimate mastery of gastronomy.`
24. **`minecraft/kubejs/startup_scripts/vampillager_entity.js:92`**:
    `// Check backward landing position: ensure we don't leap backwards into direct sunlight!`

---

## 5. Stereotypical AI Buzzwords in In-Game Lore & Configs

### 5.1 FTB Quests Localization (`minecraft/config/ftbquests/quests/lang/en_us.snbt`)
| Line | Buzzword | In-Game Text Snippet | Note / Context |
| :--- | :--- | :--- | :--- |
| 556 | `unleashed` | `"&9The ocean's fury unleashed upon the surface."` | Boss / dimension flavor text |
| 863 | `mastery` | `"&5The Cosmos recognizes your supreme mastery.&r"` | Endgame astral milestone |
| 1022 | `delves` | `"&7Exceptional base durability for sustained dungeon delves."` | Relic durability tooltip |
| 1511 | `unleashing` | `quest.3105000000000032.quest_desc: ["&aThe radioactive leviathan unleashing devastating atomic breath rays.&r"]` | Alex's Caves Luxtructosaurus description |
| 1650 | `cornerstone` | `quest.4101000000000010.quest_subtitle: "The cornerstone of all kinetic mechanics."` | Create Shaft quest subtitle |
| 1674 | `harness` | `"&eWindmill Bearings harness the breeze to generate massive kinetic power.&r"` | Create Windmill quest text |
| 1716 | `Mastery` | `quest.4101000000000110.quest_subtitle: "Mastery of rotational motion."` | Create speed controller quest |
| 1794 | `mastery` | `"&6Precision Mechanisms represent true engineering mastery.&r"` | Create precision mechanism quest |
| 1810 | `surgical` | `quest.4103000000000020.quest_subtitle: "Filter, extract, and sort with surgical precision."` | Create smart logistics subtitle |
| 1853 | `Unleashing` | `quest.4103000000000090.quest_subtitle: "Unleashing the power of pressurized steam."` | Create Steam Engine quest subtitle |
| 1873 | `Mastery` | `quest.4103000000000120.quest_subtitle: "Mastery of factory logistics and transit."` | Create train logistics quest |
| 1878 | `cornerstone` | `"Steel is the cornerstone of industrial casings, diesel combustion, and aerospace rocketry."` | TFMG steel quest text |
| 1943 | `mastery` | `"With steel foundries, diesel power, physics airships, and Martian bases under your command, your industrial mastery over PEAK is absolute."` | Create chapter milestone description |
| 1955 | `mastery` | `quest.47ACECB62DA96AD6.quest_subtitle: "Combat mastery and weapons"` | Simply Swords chapter subtitle |
| 2128 | `delve` | `quest.5100000000000048.quest_desc: ["&e* Classic lunchbox sandwich ready for any mining delve."` | Farmer's Delight food flavor text |
| 2389 | `robust` | `quest.5101000000000031.quest_desc: ["&c* Distinct robust flavor that craves rosemary and garlic."` | Culinary flavor text |
| 2506 | `Meticulously`| `quest.5101000000000067.quest_desc: ["&c* Meticulously arranged baked summer vegetable layers."` | Culinary flavor text |
| 2907 | `meticulously`| `quest.5102000000000066.quest_desc: ["&e* Toxins meticulously removed. Spicy and thrilling."` | Nether food flavor text |
| 2949 | `delves` | `quest.5102000000000080.quest_desc: ["&6* Slow-cooked until tender. The staple food of underworld delves."` | Underworld food flavor text |
| 3986 | `Synergy` | `quest.7000000000000140.title: "&eCurios Synergy - Trinket Optimization&r"` | Curios quest title |
| 3989 | `embark` | `"You are now equipped to master the kinetic factories of Create, conquer the 12 Boss Eyes, and embark on the voyage to Mars and Venus."` | Chapter summary text |
| 3993 | `Mastery` | `quest.7000000000000150.title: "&6The PEAK Pioneer - Summit Mastery&r"` | Final summit quest title |
| 4125 | `Embark` | `task.5400000000004001.title: "Embark on the Safari"` | Safari task title |

### 5.2 Server Scripts & Config Buzzwords
- `minecraft/kubejs/server_scripts/50_xp_fluids_unification.js:28`: `// Allows seamless conversion between any XP fluid type without loss`
- `minecraft/kubejs/server_scripts/05_dark_magic_dimensions.js:171`: `// SECTION 5: CROSS-MAGIC SYNERGIES`
- `minecraft/config/ars_n_spells-server.toml:421`: `["Source Jar Synergy"]` *(Mod-native config header)*

---

## 6. Public Descriptions & Distribution Copy

- **`scrapped_tools/curseforge_peak_lite_description.md`**:
  - Line 16: `Every single heavy visual engine has been surgically stripped while leaving **100% of the gameplay...**`
  - Line 45: `At its heart, **PEAK** is a Create-centered industrial sandbox stacked with rich magic, deep dungeons, and space exploration.`
  - Line 47: `We avoided hand-holding quest rails and rigid checklists. Whether you want to master rotational engineering...`
- **`scrapped_tools/curseforge_peak_dev_description_update.md`**:
  - Line 16: `For PEAK, I spent back-breaking hours doing deep optimization...`
  - Line 26: `At its heart, PEAK is a Create-centered pack...`
  - Line 28: `dive straight into kinetics...`
  - Line 60: `I have put manyyy hours into balancing recipes...`

---

## 7. Clarifications & Disproved False Positives

1. **Apokinetics "Donation Prompt"**: The prior investigation flagged lines containing `"donation prompt"` as prompt meta remnants (`PROMPT_USER`). This was a false positive. `DonationPromptClient` is an actual class in the *Apokinetics* mod that displays a donation solicitation GUI on client tick. Silencing this class is an in-game technical fix.
2. **"Antigravity" Spell Effect**: Found in `minecraft/ct_dumps/effect.txt:156` as `<mobeffect:irons_spellbooks:antigravity>`. This is a native spell effect from *Iron's Spells 'n Spellbooks*, not an AI attribution.
3. **"Minecraft Cursor" Mod**: Found in `minecraft/server_pack_excluded_mods.md:97` and `minecraft/config/minecraft-cursor.json`. This is the third-party client mod *Minecraft Cursor*, not an IDE reference.
4. **Player-Facing Achievement First-Person Pronouns**: Lines in `en_us.snbt:4081-4139` (e.g. `"I have forged all 25 weapon archetypes!"`, `"I AM THE ARSENAL EMPEROR OF PEAK!"`) are intentional player milestone checkmark titles and do not represent developer self-talk.

---

## 8. Clean Technical Replacement Guide

| Target File & Line | Current AI-Flavored Phrasing | Clean Technical Replacement |
| :--- | :--- | :--- |
| `apokinetics_unregister.js:3` | `// Surgically unregister Apokinetics donation prompt...` | `// Unregister Apokinetics DonationPromptClient from NeoForge event bus` |
| `apokinetics_unregister.js:11` | `console.info('[PEAK Fix] Surgically unregistered...');` | `console.info('[PEAK Fix] Unregistered DonationPromptClient to silence popups.');` |
| `fix_malum_watchdog.js:5` | `// This script surgically unregisters Malum's...` | `// Unregisters Malum RuntimeEvents class from NeoForge event bus` |
| `fix_malum_watchdog.js:13` | `console.info('[PEAK Fix] Surgically unregistered com.sammy.malum...');` | `console.info('[PEAK Fix] Unregistered com.sammy.malum.events.RuntimeEvents.');` |
| `en_us.snbt:1810` | `"Filter, extract, and sort with surgical precision."` | `"High-precision item filtering, extraction, and sorting."` |
| `curseforge_peak_lite_description.md:16` | `...surgically stripped while leaving 100% of the gameplay...` | `...stripped of heavy visual overhead while leaving 100% of gameplay...` |
| `50_xp_fluids_unification.js:28` | `// Allows seamless conversion between any XP fluid...` | `// 1:1 conversion recipes between registered XP fluids` |
| `00_recipe_fixer.js:22-25` | `// We can't easily iterate all recipes and modify their raw JSON...` | `// Note: Runtime recipe adjustments restricted to script-registered IDs.` |
| `02_create_era_gates.js:49` | `// IE is the SECOND tech era. You can't skip Create.` | `// Immersive Engineering recipe prerequisites require Create components.` |
| `04_magic_integration.js:106` | `// Spell turrets are basically "magical deployers"...` | `// Basic Spell Turret recipe requires Create Deployer.` |
| `15_loot_nerfs.js:11` | `// We completely remove these drops from them.` | `// Exclude Malum spirit drops from split slime entities.` |
| `20_disable_bugged_spells.js:32` | `// Also prevent right clicks just in case` | `// Cancel right-click interaction event.` |
| `23_zenith_saber.js:45` | `// This runs for EVERY crafted item, so we exit instantly...` | `// Early exit guard for non-sword items.` |
| `23_zenith_saber.js:51` | `// 3. Verify if it is our custom Zenith Saber` | `// 3. Verify Zenith Saber custom item name.` |
| `vampillager_entity.js:92` | `// Check backward landing position: ensure we don't leap backwards into direct sunlight!` | `// Guard backward trajectory against sunlight exposure.` |
| `en_us.snbt:1650` | `"The cornerstone of all kinetic mechanics."` | `"The foundation of all kinetic mechanics."` |
| `en_us.snbt:1853` | `"Unleashing the power of pressurized steam."` | `"Pressurized steam engine operation."` |
| `en_us.snbt:2506` | `"&c* Meticulously arranged baked summer vegetable layers."` | `"&c* Baked summer vegetable layers seasoned with herbs."` |
| `en_us.snbt:3986` | `"&eCurios Synergy - Trinket Optimization&r"` | `"&eCurios Loadout - Trinket Optimization&r"` |
| `en_us.snbt:3989` | `"...and embark on the voyage to Mars and Venus."` | `"...and journey to Mars and Venus."` |
