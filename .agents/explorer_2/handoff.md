# Comprehensive Audit Report: AI Generation Indicators in Non-KubeJS Assets & Configs

**Investigator**: Explorer 2 (`teamwork_preview_explorer`)  
**Scope**: `minecraft/config/`, `minecraft/defaultconfigs/`, `minecraft/patchouli_books/`, `minecraft/datapacks/`, `minecraft/scratch/`, root Python scripts, markdown documentation, and quest data.  
**Date**: 2026-08-16  

---

## 1. Observation

A deep, multi-pass search across all non-KubeJS files and directories in `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\` yielded exact matches, explicit signatures, and structural indicators of Artificial Intelligence generation across multiple categories.

### A. Explicit AI Generation Signatures & Antigravity Attribution

| # | File Path | Line(s) | Verbatim Quoted Content / Indicator | Confidence |
|---|---|---|---|---|
| 1 | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\check_client_toml.py` | 8 | `# List from user prompt` | **Definite** |
| 2 | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\generate_high_priority_data.py` | 47 | `out.write("// Archivo generado automáticamente para sobrescribir JSONs rotos de los mods.\n")` | **Definite** |
| 3 | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\scratch\mod_extraction\convert_recipes.py` | 97 | `out.write("// Archivo generado automáticamente para corregir las recetas rotas de Create en 1.21.1\n")` | **Definite** |
| 4 | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs\assets\minecraft\models\block\flowerbed_1.json` | 2 | `"credit": "Made with Blockbench / Fixed by Antigravity",` | **Definite** |
| 5 | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs\assets\minecraft\models\block\flowerbed_2.json` | 2 | `"credit": "Made with Blockbench / Fixed by Antigravity",` | **Definite** |
| 6 | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs\assets\minecraft\models\block\flowerbed_3.json` | 2 | `"credit": "Made with Blockbench / Fixed by Antigravity",` | **Definite** |
| 7 | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs\assets\minecraft\models\block\flowerbed_4.json` | 2 | `"credit": "Made with Blockbench / Fixed by Antigravity",` | **Definite** |

---

### B. AI-Authored Maintenance & Diagnostic Scripts in `minecraft/` Root

The root directory contains 18 Python scripts written to diagnose, extract, regex-repair, and generate Minecraft/KubeJS configurations and datapacks.

1. **`c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\check_client_toml.py`** (Lines 1–53):
   - **Line 8**: `# List from user prompt`
   - **Function**: Takes a hardcoded mod list from a user prompt, opens jar archives, and inspects `neoforge.mods.toml` and `mods.toml` for `displayTest = "IGNORE_SERVER_VERSION"`.
   - **Confidence**: **Definite**

2. **`c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\generate_physical_datapack.py`** (Lines 1–89):
   - **Lines 26–31**:
     ```json
     "pack": {
       "pack_format": 48,
       "description": "Fixes broken mod recipes and loot tables by overriding them with valid dummies"
     }
     ```
   - **Function**: Reads `errors.txt` and `errors2.txt` to generate a fallback datapack at `minecraft/global_packs/required_data/recipe_error_fixer` overriding crashing recipes with barrier items and empty loot tables.
   - **Confidence**: **High**

3. **`c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\generate_high_priority_data.py`** (Lines 1–75):
   - **Line 47**: `out.write("// Archivo generado automáticamente para sobrescribir JSONs rotos de los mods.\n")`
   - **Function**: Scans game log errors via regex and outputs KubeJS high priority data event handlers.
   - **Confidence**: **Definite / High**

4. **`c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\generate_dummy_recipes.py`** (Lines 1–56):
   - **Function**: Regex-extracts RecipeManager parsing errors and writes dummy JSON recipes directly into `kubejs/data/`.
   - **Confidence**: **High**

5. **`c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\deep_check.py`** (Lines 1–67) & **`suspect_mods.txt`**:
   - **Lines 8–12**: Heuristic keyword scanner (`client`, `visual`, `hud`, `gui`, `menu`, `tooltip`, `render`, `animation`, `sound`, `particle`, `shader`, `bloom`, etc.).
   - **Function**: Scans mod jar metadata descriptions in bulk and outputs structured findings to `suspect_mods.txt`.
   - **Confidence**: **High**

6. **`c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\ore_report.md`** (Lines 1–144):
   - **Lines 1–7**:
     ```markdown
     # Reporte de Generación Original de Minerales Modeados
     Esta tabla muestra los valores **originales** (antes de aplicar nuestro Datapack) de los minerales que analizamos. Úsala para identificar cuáles minerales son tan raros que no deberíamos tocarlos.
     ```
   - **Function**: Markdown table documenting original ore distribution (Count & Rarity) across 15+ mods in Spanish, generated by an AI assistant during balancing.
   - **Confidence**: **High**

7. **Other Single-Purpose Diagnostic Scripts in `minecraft/`**:
   - `check_mods.py`: Heuristic client mod identifier.
   - `check_shine.py`: Jar manifest inspector for `shine-2.0.1`.
   - `check_specific.py`: Targeted `displayTest` inspector for 9 specific jars.
   - `find_recipes.py`: Recipe searcher for 21 spellbook items.
   - `fix_fluids.py`: String substitution for fluid tags (`Fluid.of('#c:crude_oil'`).
   - `fix_json.py`: Regex substitution for item and fluid keys.
   - `fix_suppressor.py` & `fix_syntax.py` & `fix_syntax_errors.py`: Syntax error patchers for KubeJS scripts.
   - `get_missing_items.py`: Regex parser for missing item IDs from `latest.log`.
   - `replace_missing_items.py`: Batch dictionary replacer for renamed 1.21.1 items.
   - `rewrite_20_fixed_datapacks.py`: AST-style line rewriter for Create recipe builders.
   - `scratch/mod_extraction/convert_recipes.py`: Automated recipe extractor from raw data.
   - **Confidence**: **High**

---

### C. Quest Content & Dialogue Analysis (`config/ftbquests/`)

- **File**: `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\config\ftbquests\quests\lang\en_us.snbt` (3,310 lines)
- **Observations**:
  1. **Consistent Tone and Formatting**: Every single quest follows an identical structural pattern:
     - 1-line punchy subtitle (`quest.XXXX.quest_subtitle`)
     - Color-formatted bullet points (`&e• ...&r`, `&c• ...&r`, `&6• ...&r`)
     - Flavor text closing with humorous/thematic guidance (`&7...&r`, `&6Doctor's Advice:&r`, `&6Pitmaster's Tip:&r`)
  2. **Exhaustive Systematic Coverage**:
     - 25 Weapon Archetypes fully cataloged with exact combat characteristics (lines 170–341).
     - 49 Simply Swords Mythic Relics categorized by elemental traits (lines 343–695).
     - 36 Simply More Exotic Relics (lines 697–935).
     - 7 Simply Bows with smithing rune descriptions (lines 949–1081).
     - Cross-Mod Dimensional Metals for Cataclysm, Ice and Fire, Twilight Forest, Undergarden, and Deeper Darker (lines 1083–1225).
     - 530-meal Culinary Compendium across 5 thematic wings (Homestead, Dimensional, Arcane, Fisheries, Prehistoric Safari) with Spice of Life heart milestone formulas (lines 1280–3310).
  3. **AI Generation Hallmarks**:
     - The uniform voice, complete completeness without gaps, formatted subtitles ("Shift + Right Click = free Waystone. You're a genius.", "Variety is the spice of violence.", "Eat varied foods, permanently expand your health bar, and conquer the 530-meal compendium!"), and programmatic symmetry are classic hallmarks of LLM-generated game quest content.
  - **Confidence**: **High (AI-Generated / AI-Assisted)**

---

### D. Verified Clean / Mod-Authored Standard Files

1. **`minecraft/config/` (General Mod Configs)**:
   - Evaluated `.toml`, `.json`, `.json5`, `.cfg`, and `.yml` files across 130+ mod folders (e.g. `Mekanism`, `alexscaves`, `apotheosis`, `ars_nouveau`, `crash_assistant`, `draconicevolution`, `lootr`, `quark`, `servercore`, `twilightforest`).
   - All comments and boilerplate originate from upstream mod developers (e.g. `DraconicEvolution.cfg` comments mentioning "generated by a previous version of DE", `CrashAssistant` internal documentation). No AI hallucinated configs or prompt residue found in standard mod configs.
2. **`minecraft/defaultconfigs/`**:
   - `minecraft/defaultconfigs/biolith/general.json`: Standard 7-line Biolith worldgen scale configuration.
3. **Empty Directories**:
   - `minecraft/patchouli_books/`: Empty (no custom Patchouli books present).
   - `minecraft/datapacks/`: Empty (custom datapacks are managed via KubeJS or `global_packs/required_data/`).
   - `minecraft/scripts/`: Empty (CraftTweaker is not utilized; KubeJS handles all scripting).
   - `minecraft/resourcepacks/`: Empty.

---

## 2. Logic Chain

1. **Observation**: `check_client_toml.py:8` contains the verbatim text `# List from user prompt` above a hardcoded string block of jar filenames.
   - **Reasoning**: This exact phrasing occurs exclusively when an LLM assistant converts a user prompt listing items into a Python data structure.
   - **Inference**: The file was directly generated by an AI assistant in response to a developer inquiry.

2. **Observation**: Four block model JSONs (`flowerbed_1.json` through `flowerbed_4.json`) contain `"credit": "Made with Blockbench / Fixed by Antigravity"`.
   - **Reasoning**: "Antigravity" is the AI agent/IDE system used during workspace management.
   - **Inference**: The 3D model JSONs were repaired and committed by the AI assistant.

3. **Observation**: Both `generate_high_priority_data.py:47` and `convert_recipes.py:97` contain programmatic file output statements writing `"// Archivo generado automáticamente para..."`.
   - **Reasoning**: These generator scripts were constructed by a Spanish-speaking AI assistant to programmatically output repair scripts that suppress NeoForge 1.21.1 recipe registration crashes.
   - **Inference**: The pipeline of error fixing (`errors.txt` $\rightarrow$ Python parser $\rightarrow$ KubeJS output) was created and executed by AI.

4. **Observation**: `ore_report.md` contains a Spanish markdown introduction (`"Esta tabla muestra los valores originales (antes de aplicar nuestro Datapack)..."`) alongside a complete data extraction table.
   - **Reasoning**: The collaborative first-person plural framing ("nuestro Datapack", "que analizamos") and structured markdown formatting match AI agent workflow documentation.

5. **Observation**: `ftbquests/quests/lang/en_us.snbt` contains 3,310 lines with 100% complete descriptions for hundreds of items and relics across multiple mods with uniform formatting and style.
   - **Reasoning**: Manual writing of 3,300+ lines of quests typically exhibits variation in style, typos, and incomplete sections; the uniform cadence, thematic naming, and systematic structure strongly indicate extensive AI-assisted batch drafting.

---

## 3. Caveats

1. **KubeJS Directory**: Investigated primarily by Explorer 1; references to KubeJS files here (`flowerbed_*.json`, script generators) are included solely for complete context where non-KubeJS tools interacted with or created them.
2. **Mod Jars**: Compiled `.jar` files in `minecraft/mods/` were inspected for internal toml/json metadata during Python script execution, but binary `.class` decompilation was not performed as it falls outside user-generated content.
3. **Third-Party Mod References**: Phrases such as "generated by" in `DraconicEvolution.cfg` or "AI goal" in `adorablehamsterpets/main.toml` and `guardvillagers-common.toml` are genuine game engine mob AI / mod config defaults and are NOT generative AI markers.

---

## 4. Conclusion

- **Explicit AI Markers Found**: 7 exact instances, including direct user-prompt references (`check_client_toml.py`), AI attribution metadata (`Fixed by Antigravity` in 4 flowerbed model files), and automated Spanish code generator headers (`generate_high_priority_data.py`, `convert_recipes.py`).
- **AI-Created Tooling & Documentation**: 18 diagnostic/repair Python scripts in `minecraft/` root and `scratch/`, along with `ore_report.md` and `suspect_mods.txt`.
- **AI-Assisted Quest Content**: `config/ftbquests/quests/lang/en_us.snbt` shows overwhelming structural evidence of AI-generated batch lore and descriptions for the combat and culinary quest lines.
- **Mod Configs & Other Directories**: Standard mod configs in `config/` and `defaultconfigs/` are authentic mod defaults. `patchouli_books/`, `datapacks/`, and `scripts/` are empty.

---

## 5. Verification Method

To independently verify these findings, inspect the specified files on disk:

1. **Verify Prompt Reference in `check_client_toml.py`**:
   - Inspect line 8 of `minecraft/check_client_toml.py`.
2. **Verify Antigravity Credit in Block Models**:
   - Inspect line 2 of `minecraft/kubejs/assets/minecraft/models/block/flowerbed_1.json`.
3. **Verify Generator Script Headers**:
   - Inspect line 47 of `minecraft/generate_high_priority_data.py`.
   - Inspect line 97 of `minecraft/scratch/mod_extraction/convert_recipes.py`.
4. **Verify Ore Report Documentation**:
   - Inspect lines 1–7 of `minecraft/ore_report.md`.
5. **Verify Quest Lore Structure**:
   - Inspect lines 1–150 and lines 1280–1350 of `minecraft/config/ftbquests/quests/lang/en_us.snbt`.
