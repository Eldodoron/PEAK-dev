# Python Utilities Inventory & Archival Plan

## 1. Observation

A full recursive search was performed across the `minecraft/` directory tree and workspace root to locate all standalone Python utility scripts (`.py`).

### Verification Commands & Results
- **Command 1**: `Get-ChildItem -Path "minecraft" -Recurse -Filter "*.py" | Select-Object FullName, Length`
  - **Result**: Exactly 24 `.py` files identified across 3 directory locations. Total size: 39,207 bytes.
- **Command 2**: `Test-Path "scrapped_tools"`
  - **Result**: `False`. The `scrapped_tools/` directory does not currently exist at the workspace root (`c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/`).
- **Command 3**: `Get-ChildItem -Path "minecraft" -Recurse -Force | Where-Object { $_.Name -like "*pycache*" -or $_.Extension -eq ".pyc" }`
  - **Result**: Zero `.pyc` files or `__pycache__` directories exist inside `minecraft/`.

---

### Complete Inventory of Python Utility Scripts in `minecraft/`

| # | Current Relative Path | Size (Bytes) | Lines | Primary Purpose / Core Functionality |
|---|-----------------------|-------------:|------:|--------------------------------------|
| 1 | `minecraft/check_client_toml.py` | 1,638 | 53 | Reads mod JARs in `minecraft/mods/` using `zipfile` & `tomllib` to inspect `displayTest` for client-only flags (`IGNORE_SERVER_VERSION`). |
| 2 | `minecraft/check_mods.py` | 2,697 | 74 | Heuristic keyword scan (`oculus`, `rubidium`, `hud`, `gui`, etc.) and TOML metadata inspector for identifying client-only mods. |
| 3 | `minecraft/check_shine.py` | 390 | 10 | Targeted inspector that prints TOML/JSON mod metadata from `shine-2.0.1+1.21.1-neoforge.jar`. |
| 4 | `minecraft/check_specific.py` | 1,376 | 42 | Targeted `displayTest` property checker for 9 specific mod jars (e.g., `bigwater`, `CrashAssistant`, `sounds`, `particular`). |
| 5 | `minecraft/deep_check.py` | 2,703 | 67 | Deep description & mod name keyword scanner for client-side mod classification; outputs matches to `suspect_mods.txt`. |
| 6 | `minecraft/find_recipes.py` | 2,035 | 56 | Scans `minecraft/mods/*.jar` data directories for JSON recipe definitions producing spell books (`irons_spellbooks`, `cataclysm_spellbooks`, etc.). |
| 7 | `minecraft/fix_fluids.py` | 956 | 23 | String replacer fixing fluid tag strings in `00_recipe_error_suppressor.js` and `20_fixed_datapacks.js` to use `createdieselgenerators` & `createmetalwork`. |
| 8 | `minecraft/fix_json.py` | 683 | 18 | Regex replacer for `20_fixed_datapacks.js` converting `"base": {"id": ...}` to `"item": ...` and cleaning fluid tag syntax. |
| 9 | `minecraft/fix_suppressor.py` | 474 | 13 | Strips broken `{'id': '` prefixes from recipe strings in `00_recipe_error_suppressor.js`. |
| 10 | `minecraft/fix_syntax.py` | 469 | 15 | Repairs nested string syntax errors (e.g. `'{'id': 'create:andesite_alloy'}'`) in `00_recipe_error_suppressor.js`. |
| 11 | `minecraft/fix_syntax_errors.py` | 2,131 | 52 | Multi-file syntax fixer commenting out broken lines in `13b_...js`, `expert_mode_recipes.js`, and adjusting fluid tags in `20_...js`. |
| 12 | `minecraft/generate_dummy_recipes.py` | 1,964 | 56 | Parses `minecraft/errors2.txt` for broken recipes/loot tables and writes dummy replacement JSONs into `minecraft/kubejs/data/`. |
| 13 | `minecraft/generate_high_priority_data.py` | 3,259 | 75 | Generates KubeJS script `01_high_priority_data_override.js` from `errors.txt`/`errors2.txt` using `ServerEvents.highPriorityData`. |
| 14 | `minecraft/generate_physical_datapack.py` | 3,120 | 89 | Generates a complete physical global datapack at `global_packs/required_data/recipe_error_fixer` with `pack.mcmeta` and dummy JSONs for broken recipes. |
| 15 | `minecraft/get_missing_items.py` | 1,088 | 30 | Scans `minecraft/logs/latest.log` for registry key errors and missing items/fluids reported by KubeJS. |
| 16 | `minecraft/replace_missing_items.py` | 1,143 | 34 | Replaces deprecated 1.20 item IDs with valid 1.21.1 IDs across all `kubejs/server_scripts/*.js` (e.g. `compressor` -> `air_compressor`). |
| 17 | `minecraft/rewrite_20_fixed_datapacks.py` | 5,426 | 143 | Transforms `event.custom({...})` Create recipes in `20_fixed_datapacks.js` into native KubeJS Create recipe builder syntax (`event.recipes.create...`). |
| 18 | `minecraft/kubejs/server_scripts/clean_suppressor.py` | 1,411 | 39 | Scans `kubejs/data/` JSON files and removes already-fixed recipe IDs from `00_recipe_error_suppressor.js`. |
| 19 | `minecraft/kubejs/server_scripts/convert_chance.py` | 1,503 | 36 | Regex converter for `Item.of(...).withChance(X)` -> `CreateItem.of(...)` and fluid tag normalization across server scripts. |
| 20 | `minecraft/kubejs/server_scripts/convert_to_js.py` | 1,500 | 36 | Converts JSON recipe files in `kubejs/data/` into `event.custom()` calls inside `20_fixed_datapacks.js`. |
| 21 | `minecraft/kubejs/server_scripts/fix_datapacks.py` | 3,206 | 83 | Extracts broken recipes from mod JARs listed in `00_recipe_error_suppressor.js`, fixes fluid tags/transitional items, and saves to `kubejs/data/`. |
| 22 | `minecraft/kubejs/server_scripts/fix_fluid.py` | 435 | 12 | Performs string substitutions (`"fluid":` -> `"id":`, `"fluidTag":` -> `"tag":`) in `20_fixed_datapacks.js`. |
| 23 | `minecraft/kubejs/server_scripts/fix_transitional.py` | 426 | 13 | Replaces `"transitionalItem":` with `"transitional_item":` across JS files in its directory. |
| 24 | `minecraft/scratch/mod_extraction/convert_recipes.py` | 4,158 | 103 | Converts extracted Create mod recipes from `minecraft/scratch/mod_extraction/data/` to KubeJS recipe builder syntax in `00_recipe_error_suppressor.js`. |

---

## 2. Logic Chain

1. **Discovery & Verification**: Recursive enumeration of all files matching `*.py` in `minecraft/` confirmed exactly 24 files across three distinct levels:
   - Root `minecraft/` (17 files)
   - `minecraft/kubejs/server_scripts/` (6 files)
   - `minecraft/scratch/mod_extraction/` (1 file)
2. **Analysis of Script Roles**:
   - The scripts represent four main operational categories:
     1. **Mod Inspection / TOML Analysis**: (5 scripts: `check_client_toml.py`, `check_mods.py`, `check_shine.py`, `check_specific.py`, `deep_check.py`)
     2. **KubeJS & Datapack Recipe Repair / Code Transformation**: (13 scripts: `fix_fluids.py`, `fix_json.py`, `fix_suppressor.py`, `fix_syntax.py`, `fix_syntax_errors.py`, `replace_missing_items.py`, `rewrite_20_fixed_datapacks.py`, `clean_suppressor.py`, `convert_chance.py`, `convert_to_js.py`, `fix_datapacks.py`, `fix_fluid.py`, `fix_transitional.py`, `convert_recipes.py`)
     3. **Recipe & Datapack Dummy Generation**: (3 scripts: `generate_dummy_recipes.py`, `generate_high_priority_data.py`, `generate_physical_datapack.py`)
     4. **Mod Log & Registry Analysis**: (2 scripts: `get_missing_items.py`, `find_recipes.py`)
3. **Absence of `scrapped_tools/` Directory**:
   - `Test-Path "scrapped_tools"` returned `False`.
   - Creation of the base folder `c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/scrapped_tools/` will be required before file migration.
4. **Preservation of Subfolder Hierarchy**:
   - Moving scripts directly to a flat `scrapped_tools/` folder would lose their historical execution context (e.g. scripts located directly inside `kubejs/server_scripts/` relied on relative paths to nearby `.js` files or `kubejs/data`).
   - Maintaining relative subfolder structure (stripping `minecraft/`) ensures zero namespace collision and preserves provenance:
     - `minecraft/*.py` → `scrapped_tools/*.py`
     - `minecraft/kubejs/server_scripts/*.py` → `scrapped_tools/kubejs/server_scripts/*.py`
     - `minecraft/scratch/mod_extraction/*.py` → `scrapped_tools/scratch/mod_extraction/*.py`

---

## 3. Caveats

- **External / Root Scripts**: Note that there are additional Python scripts at the workspace root (`analyze_spark.py`, `analyze_spark_tree.py`, `patch_lithostitched.py`, `read_mcmeta.py`, and `scratch/*.py`). These are already outside `minecraft/` and do not violate the `minecraft/` directory sanitation requirement, though the implementer may choose whether to unify all tools into `scrapped_tools/`.
- **Hardcoded Paths Inside Scripts**: Several scripts contain hardcoded Windows absolute paths (e.g. `C:\Users\wamb9\...` or `C:\Users\chris\...`). Archiving these scripts into `scrapped_tools/` will preserve them for reference without impacting Minecraft runtime, as they are standalone development tools.
- **Non-Python Scratch Data**: `minecraft/scratch/mod_extraction/` contains a large directory `data/` of extracted recipe JSONs and `mod_list.txt`. Only `.py` scripts were surveyed for this task; if `minecraft/scratch/` as a whole is to be cleaned, that should be handled in subsequent cleanup milestones.

---

## 4. Conclusion & Recommended Target Mapping

All 24 Python utility scripts located inside `minecraft/` have been surveyed, cataloged, and mapped.

### Exact Target Mapping to `scrapped_tools/`

```
c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/scrapped_tools/
├── check_client_toml.py               <- minecraft/check_client_toml.py
├── check_mods.py                      <- minecraft/check_mods.py
├── check_shine.py                     <- minecraft/check_shine.py
├── check_specific.py                  <- minecraft/check_specific.py
├── deep_check.py                      <- minecraft/deep_check.py
├── find_recipes.py                    <- minecraft/find_recipes.py
├── fix_fluids.py                      <- minecraft/fix_fluids.py
├── fix_json.py                        <- minecraft/fix_json.py
├── fix_suppressor.py                  <- minecraft/fix_suppressor.py
├── fix_syntax.py                      <- minecraft/fix_syntax.py
├── fix_syntax_errors.py               <- minecraft/fix_syntax_errors.py
├── generate_dummy_recipes.py          <- minecraft/generate_dummy_recipes.py
├── generate_high_priority_data.py     <- minecraft/generate_high_priority_data.py
├── generate_physical_datapack.py      <- minecraft/generate_physical_datapack.py
├── get_missing_items.py               <- minecraft/get_missing_items.py
├── replace_missing_items.py           <- minecraft/replace_missing_items.py
├── rewrite_20_fixed_datapacks.py      <- minecraft/rewrite_20_fixed_datapacks.py
├── kubejs/
│   └── server_scripts/
│       ├── clean_suppressor.py        <- minecraft/kubejs/server_scripts/clean_suppressor.py
│       ├── convert_chance.py          <- minecraft/kubejs/server_scripts/convert_chance.py
│       ├── convert_to_js.py           <- minecraft/kubejs/server_scripts/convert_to_js.py
│       ├── fix_datapacks.py           <- minecraft/kubejs/server_scripts/fix_datapacks.py
│       ├── fix_fluid.py               <- minecraft/kubejs/server_scripts/fix_fluid.py
│       └── fix_transitional.py        <- minecraft/kubejs/server_scripts/fix_transitional.py
└── scratch/
    └── mod_extraction/
        └── convert_recipes.py         <- minecraft/scratch/mod_extraction/convert_recipes.py
```

---

## 5. Verification Method

To independently verify this inventory and validate the migration when executed:

1. **Verify Current Inventory Count**:
   ```powershell
   (Get-ChildItem -Path "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft" -Recurse -Filter "*.py").Count
   # Expected output: 24
   ```

2. **Post-Migration Verification (for Implementer)**:
   ```powershell
   # Invalidation check: No .py files remaining in minecraft/
   (Get-ChildItem -Path "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft" -Recurse -Filter "*.py").Count
   # Must return: 0

   # Verification of relocated files in scrapped_tools/
   (Get-ChildItem -Path "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/scrapped_tools" -Recurse -Filter "*.py").Count
   # Must return: 24
   ```
