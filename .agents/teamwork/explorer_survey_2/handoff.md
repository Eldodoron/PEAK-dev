# Comprehensive Survey Report: Custom Block Model JSON Files (R2)

## 1. Observation

### Scope and Inventory Overview
A recursive scan of `minecraft/kubejs/assets/` identified **94 JSON files** in total across active namespaces. The breakdown by asset type is:
- **Block Models (`models/block/`)**: 37 files
  - `adorablehamsterpets/models/block/`: 3 files
  - `cubicleaves/models/block/`: 26 files (1 `empty.json`, 25 `template_*.json`)
  - `kubejs/models/block/`: 2 files (`green_screen.json`, `void_teleport_pad.json`)
  - `minecraft/models/block/`: 6 files (`flowerbed_1.json` to `flowerbed_4.json`, `sunflower_bottom.json`, `sunflower_top.json`)
- **Item Models (`models/item/`)**: 49 files (`cataclysm`: 24, `cataclysm_tools`: 4, `ignissoulfires`: 11, `kubejs`: 10)
- **Blockstates (`blockstates/`)**: 4 files (`kubejs`: 2, `minecraft`: 2)
- **Localization (`lang/`)**: 2 files (`acsol/lang/en_us.json`, `kubejs/lang/en_us.json`)
- **Entity Geometry & Animation**: 2 files (`kubejs/geo/entity/vampillager.geo.json`, `kubejs/animations/entity/vampillager.animation.json`)

All 94 files were tested for UTF-8 encoding and Byte Order Marks (BOM); **0 files contain BOM**, and all start cleanly with `{` (`0x7B`). Line endings for all target block models are Windows standard CRLF (`\r\n`).

---

### The 9 Custom Block Model JSON Files with `"credit": "Made with Blockbench"`

Grep search command:
`grep_search` across `minecraft/kubejs/assets` with query `"Made with Blockbench"` matched **exactly 9 files**.

Below are the exact file paths, line numbers, and verbatim context for each of the 9 files:

#### 1. `minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_bottom.json`
- **Total lines**: 506
- **Target line**: Line 2
- **Verbatim context (Lines 1–5)**:
  ```json
  {
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```
- **Proposed replacement (Line 2 removed)**:
  ```json
  {
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```

#### 2. `minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_no_seeds.json`
- **Total lines**: 865
- **Target line**: Line 3
- **Verbatim context (Lines 1–6)**:
  ```json
  {
    "format_version": "1.9.0",
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```
- **Proposed replacement (Line 3 removed)**:
  ```json
  {
    "format_version": "1.9.0",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```

#### 3. `minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_with_seeds.json`
- **Total lines**: 865
- **Target line**: Line 3
- **Verbatim context (Lines 1–6)**:
  ```json
  {
    "format_version": "1.9.0",
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```
- **Proposed replacement (Line 3 removed)**:
  ```json
  {
    "format_version": "1.9.0",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```

#### 4. `minecraft/kubejs/assets/minecraft/models/block/flowerbed_1.json`
- **Total lines**: 307
- **Target line**: Line 2
- **Verbatim context (Lines 1–5)**:
  ```json
  {
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```
- **Proposed replacement (Line 2 removed)**:
  ```json
  {
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```

#### 5. `minecraft/kubejs/assets/minecraft/models/block/flowerbed_2.json`
- **Total lines**: 131
- **Target line**: Line 2
- **Verbatim context (Lines 1–5)**:
  ```json
  {
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```
- **Proposed replacement (Line 2 removed)**:
  ```json
  {
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```

#### 6. `minecraft/kubejs/assets/minecraft/models/block/flowerbed_3.json`
- **Total lines**: 219
- **Target line**: Line 2
- **Verbatim context (Lines 1–5)**:
  ```json
  {
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```
- **Proposed replacement (Line 2 removed)**:
  ```json
  {
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```

#### 7. `minecraft/kubejs/assets/minecraft/models/block/flowerbed_4.json`
- **Total lines**: 219
- **Target line**: Line 2
- **Verbatim context (Lines 1–5)**:
  ```json
  {
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```
- **Proposed replacement (Line 2 removed)**:
  ```json
  {
    "ambientocclusion": false,
    "textures": {
      "particle": "minecraft:block/pink_petals",
  ```

#### 8. `minecraft/kubejs/assets/minecraft/models/block/sunflower_bottom.json`
- **Total lines**: 506
- **Target line**: Line 2
- **Verbatim context (Lines 1–5)**:
  ```json
  {
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```
- **Proposed replacement (Line 2 removed)**:
  ```json
  {
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```

#### 9. `minecraft/kubejs/assets/minecraft/models/block/sunflower_top.json`
- **Total lines**: 865
- **Target line**: Line 3
- **Verbatim context (Lines 1–6)**:
  ```json
  {
    "format_version": "1.21.11",
    "credit": "Made with Blockbench",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```
- **Proposed replacement (Line 3 removed)**:
  ```json
  {
    "format_version": "1.21.11",
    "ambientocclusion": false,
    "textures": {
      "0": "minecraft:block/sunflower_leaves_3d",
  ```

---

### Community and Pack Credits (MUST BE PRESERVED)

A search for `"credit"` across `minecraft/kubejs/assets/` returned 35 matches. Aside from the 9 files listed above, the remaining 26 files are:

1. **Open-Source Community Credits (`"credit": "zanderest"`) — 25 files**:
   Located in `minecraft/kubejs/assets/cubicleaves/models/block/`:
   - `template_block.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_all.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_all_notint.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_all_overlaid.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_all_overlaid_inversed.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_column.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_column_notint.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_column_overlaid_sides.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_column_overlaid_sides_halftint.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_column_overlaid_sides_horizontal.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_notint.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_overlaid.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_overlaid_inversed.json` (Line 2: `  "credit": "zanderest",`)
   - `template_block_uvdown_notint.json` (Line 2: `  "credit": "zanderest",`)
   - `template_conifer_canopy.json` (Line 2: `  "credit": "zanderest",`)
   - `template_conifer_canopy_notint.json` (Line 2: `  "credit": "zanderest",`)
   - `template_conifer_canopy_overlaid.json` (Line 2: `  "credit": "zanderest",`)
   - `template_cross_ao.json` (Line 2: `  "credit": "zanderest",`)
   - `template_generic_canopy.json` (Line 2: `  "credit": "zanderest",`)
   - `template_generic_canopy_column.json` (Line 2: `  "credit": "zanderest",`)
   - `template_generic_canopy_notint.json` (Line 2: `  "credit": "zanderest",`)
   - `template_generic_canopy_overlaid.json` (Line 2: `  "credit": "zanderest",`)
   - `template_generic_canopy_overlaid_inversed.json` (Line 2: `  "credit": "zanderest",`)
   - `template_willow_canopy.json` (Line 2: `  "credit": "zanderest",`)
   - `template_willow_canopy_notint.json` (Line 2: `  "credit": "zanderest",`)
   *Requirement Status*: Per R2 and Acceptance Criteria, all 25 community credits must remain strictly intact.

2. **In-House Pack Credit (`"credit": "PEAK"`) — 1 file**:
   - `minecraft/kubejs/assets/kubejs/models/block/green_screen.json` (Line 2: `  "credit": "PEAK",`)
   *Requirement Status*: In-house pack credit for green screen block; does not contain Blockbench attribution. Must remain intact.

3. **Block Models with NO Credit Tags — 2 files**:
   - `minecraft/kubejs/assets/cubicleaves/models/block/empty.json` (`{"elements": []}`)
   - `minecraft/kubejs/assets/kubejs/models/block/void_teleport_pad.json` (No credit tag)

---

## 2. Logic Chain

1. **Step 1 (Exhaustive Asset Inventory)**:
   Recursive listing of `minecraft/kubejs/assets/` confirmed a total of 94 JSON files across 10 namespaces. 37 are block models, 49 are item models, 4 are blockstates, 2 are lang files, and 2 are entity animations/geometries.
2. **Step 2 (Attribution Attribution Filtering)**:
   A ripgrep search for `Made with Blockbench` and `Blockbench` across the entire directory tree identified exactly 9 files. No other files in `minecraft/kubejs/assets/` contain Blockbench or AI-generator signatures.
3. **Step 3 (Syntactic Positioning Analysis)**:
   Analysis of the top lines of each of the 9 files revealed two grammatical arrangements in JSON:
   - **Pattern A (6 files)**: `"credit": "Made with Blockbench",` is the first property inside the root object `{` on line 2, followed by `"ambientocclusion": false,` on line 3.
     Removing line 2 leaves the opening `{` followed by `"ambientocclusion"`, which is valid JSON syntax with no dangling or missing commas.
   - **Pattern B (3 files)**: `"credit": "Made with Blockbench",` is the second property on line 3, preceded by `"format_version": "...",` (which already ends with a comma) on line 2, and followed by `"ambientocclusion": false,` on line 4.
     Removing line 3 leaves `"format_version": "...",` directly followed by `"ambientocclusion": false,`, which is also valid JSON syntax.
4. **Step 4 (In-Memory Syntax Parsing Simulation)**:
   An in-memory simulation script parsed all 9 files after removing the single `"credit": "Made with Blockbench",` line using .NET `ConvertFrom-Json`. All 9 files parsed cleanly with zero syntax errors and retained all underlying geometry, UV mapping, texture variables, and groups intact.
5. **Step 5 (Third-Party License Protection)**:
   Cross-referencing the remaining 26 `"credit"` hits confirmed 25 belong to `zanderest` (cubic leaves templates) and 1 belongs to `PEAK` (`green_screen.json`). Preserving these satisfies requirement R2 and protects open-source license integrity.

---

## 3. Caveats

1. **Dynamic Runtime Cache**:
   A search across the broader `minecraft/` instance found Blockbench tags in `minecraft/dynamic-resource-pack-cache/supplementaries-generated_pack/assets/supplementaries/models/block/way_signs/...`. These are auto-generated dynamically at game startup by the Supplementaries mod into an ephemeral cache. They do NOT reside in the modpack codebase (`minecraft/kubejs/assets/`), are generated by compiled Java mod code at runtime, and should not be modified.
2. **Read-Only Scope**:
   This survey is 100% read-only. No source files in `minecraft/kubejs/assets/` have been modified during this investigation.

---

## 4. Conclusion

- Exactly **9 custom block model JSON files** require sanitization to remove `"credit": "Made with Blockbench"`.
- Exactly **25 open-source community model files** (`cubicleaves`) with `"credit": "zanderest"` are identified and verified to be preserved.
- Exactly **1 pack model file** (`kubejs/models/block/green_screen.json`) with `"credit": "PEAK"` is verified to be preserved.
- In every case, deleting the single `"credit": "Made with Blockbench",` line (line 2 for Pattern A, line 3 for Pattern B) produces valid, clean JSON with zero structural alterations.
- An editing agent can execute these 9 targeted replacements with absolute precision and zero risk of JSON corruption.

---

## 5. Verification Method

To independently verify the observations and results:

1. **Verify the 9 Blockbench files**:
   ```powershell
   Get-ChildItem -Path "minecraft/kubejs/assets" -Filter "*.json" -Recurse | Select-String -Pattern '"credit":\s*"Made with Blockbench"'
   ```
   *Expected Result*: Exactly 9 matches.

2. **Verify community credit preservation (25 files)**:
   ```powershell
   (Get-ChildItem -Path "minecraft/kubejs/assets/cubicleaves/models/block" -Filter "*.json" | Select-String -Pattern '"credit":\s*"zanderest"').Count
   ```
   *Expected Result*: 25.

3. **Verify JSON parsing validity on all 9 target models before/after**:
   ```powershell
   $targets = @(
     "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_bottom.json",
     "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_no_seeds.json",
     "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_with_seeds.json",
     "minecraft/kubejs/assets/minecraft/models/block/flowerbed_1.json",
     "minecraft/kubejs/assets/minecraft/models/block/flowerbed_2.json",
     "minecraft/kubejs/assets/minecraft/models/block/flowerbed_3.json",
     "minecraft/kubejs/assets/minecraft/models/block/flowerbed_4.json",
     "minecraft/kubejs/assets/minecraft/models/block/sunflower_bottom.json",
     "minecraft/kubejs/assets/minecraft/models/block/sunflower_top.json"
   )
   foreach ($f in $targets) {
     Get-Content $f -Raw | ConvertFrom-Json | Out-Null
     Write-Host "VALID: $f"
   }
   ```
   *Expected Result*: All 9 files return `VALID`.
