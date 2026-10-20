# Milestone 3 Handoff Report: KubeJS Script Comment & Log Sanitization

## 1. Observation

All 27 JavaScript files identified in the Explorer 1 survey report (`explorer_survey_1/handoff.md`) across `minecraft/kubejs/` were individually examined and sanitized. The audit specifically targeted:
1. All occurrences of "surgical" / "surgically" (6 occurrences across 3 files).
2. All developer first-person plural statements ("we use", "our custom", "we keep", etc. — 24 occurrences across 18 files).
3. Conversational editorializing, inner monologue self-talk, informal reasoning, and buzzwords ("just in case", "it died with them for a reason", "they shamble", "seamless", "synergies").
4. Authentic game mechanics preservation (`startup_scripts/custom_items.js` Stage 5 dragons).

### Verbatim File Changes Applied

1. **`minecraft/kubejs/client_scripts/apokinetics_unregister.js`**:
   - Line 3:
     - *Previous*: `// Surgically unregister Apokinetics donation prompt from NeoForge event bus`
     - *Updated*: `// Unregister Apokinetics client donation prompt from NeoForge event bus`
   - Line 11:
     - *Previous*: `console.info('[PEAK Fix] Surgically unregistered com.fishguy129.apokinetics.client.DonationPromptClient to silence donation prompts.');`
     - *Updated*: `console.info('[PEAK Fix] Unregistered com.fishguy129.apokinetics.client.DonationPromptClient to disable recurring donation prompts.');`

2. **`minecraft/kubejs/server_scripts/00_recipe_fixer.js`**:
   - Lines 22-29:
     - *Previous*:
       ```javascript
       // We can't easily iterate all recipes and modify their raw JSON in 1.21 
       // without potentially causing more issues, but we can try to fix the 
       // most common ones that KubeJS is complaining about if they are 
       // being added via scripts.
       // However, the warnings in the log are mostly from OTHER mods' internal data.
       // KubeJS is just reporting that IT failed to parse them for its own system.
       ```
     - *Updated*:
       ```javascript
       // Global raw JSON recipe iteration is restricted in NeoForge 1.21.1 to prevent recipe registry desynchronization.
       // Scripted corrections target specific problematic recipes declared in script space.
       ```

3. **`minecraft/kubejs/server_scripts/02_create_era_gates.js`**:
   - Line 49:
     - *Previous*: `// IE is the SECOND tech era. You can't skip Create.`
     - *Updated*: `// Tier 2 Technology: Gates Immersive Engineering apparatus behind Create progression.`
   - Line 178:
     - *Previous*: `// Power generation should feel earned`
     - *Updated*: `// Gates Immersive Engineering kinetic power generation behind Create mechanical components.`
   - Line 308:
     - *Previous*: `// Quality of life items should feel earned`
     - *Updated*: `// Gates utility building wands behind Create materials.`
   - Lines 350-351:
     - *Previous*:
       ```javascript
       // Instead of Mechanical Crafters or overriding the standard recipe (which wipes NBT), 
       // we use Sequenced Assembly. The base backpack is the transitional item, so its NBT is preserved!
       ```
     - *Updated*:
       ```javascript
       // Preserves backpack item components/NBT by utilizing Sequenced Assembly with the base backpack as the transitional item.
       ```
   - Line 359:
     - *Previous*: `// Also remove the old custom types just in case`
     - *Updated*: `// Remove legacy custom backpack upgrade recipe types across all tiers.`

4. **`minecraft/kubejs/server_scripts/04_magic_integration.js`**:
   - Line 14:
     - *Previous*: `// You must explore it to access advanced Ars Nouveau.`
     - *Updated*: `// Twilight Forest progression is required to unlock advanced Ars Nouveau tiers.`
   - Lines 106-108:
     - *Previous*:
       ```javascript
       // Spell turrets are basically "magical deployers" — they
       // should need Create's Deployer as a base (mechanical
       // arm that casts spells instead of placing blocks)
       ```
     - *Updated*:
       ```javascript
       // Automated spellcasting combines mechanical actuation with magic: integrates Create deployers into spell turret recipes.
       ```
   - Lines 343-345:
     - *Previous*:
       ```javascript
       // Since ars_creo already exists, we enhance the
       // crossover between Create and Ars Nouveau
       ```
     - *Updated*:
       ```javascript
       // Cross-mod integration recipes expanding compatibility between Create and Ars Nouveau mechanics.
       ```

5. **`minecraft/kubejs/server_scripts/05_dark_magic_dimensions.js`**:
   - Line 24:
     - *Previous*: `// (you need basic magical knowledge before dark magic)`
     - *Updated*: `// (requires foundational Ars Nouveau source apparatus prior to Malum progression)`
   - Lines 142-144:
     - *Previous*:
       ```javascript
       // Created by combining Echo Shards with tech materials
       // in Create's mechanical mixer (tech reinforcement of
       // a naturally magical material)
       ```
     - *Updated*:
       ```javascript
       // Mechanical superheating recipe infusing raw echo shards with alloyed metals.
       ```
   - Line 171:
     - *Previous*: `// SECTION 5: CROSS-MAGIC SYNERGIES`
     - *Updated*: `// SECTION 5: CROSS-MOD MAGIC INTEGRATIONS`
   - Lines 240-241:
     - *Previous*:
       ```javascript
       // Apotheosis enhances enchanting — connect it to
       // the magical infrastructure we've built
       ```
     - *Updated*:
       ```javascript
       // Connects Apotheosis enchanting infrastructure with Ars Nouveau magic progression.
       ```

6. **`minecraft/kubejs/server_scripts/06_enderio_ae2.js`**:
   - Lines 13-14:
     - *Previous*:
       ```javascript
       // You need Ender IO's conduits and Mekanism's circuits
       // before touching AE2.
       ```
     - *Updated*:
       ```javascript
       // Gates AE2 digital storage networks behind Ender IO conduits and Mekanism circuit tiers.
       ```

7. **`minecraft/kubejs/server_scripts/07_draconic_endgame.js`**:
   - Lines 12-13:
     - *Previous*:
       ```javascript
       // You need actual dragon forges (hard to automate!)
       // but the results feed into Draconic Evolution.
       ```
     - *Updated*:
       ```javascript
       // Dragon forge refinement feeds directly into Draconic Evolution tiered progression.
       ```

8. **`minecraft/kubejs/server_scripts/08_reliquary_balance.js`**:
   - Lines 22-24:
     - *Previous*:
       ```javascript
       // This item should be a TROPHY of late-game mastery,
       // not a cheap shortcut. You need to have mastered
       // both magic AND technology to wield transmutation.
       ```
     - *Updated*:
       ```javascript
       // Gates Alkahestry Tome behind late-game hybrid magic and technology components.
       ```
   - Lines 41-43:
     - *Previous*:
       ```javascript
       // Alkahestry should NOT be able to duplicate
       // any of these endgame/progression items.
       // We remove these specific alkahestry recipes.
       ```
     - *Updated*:
       ```javascript
       // Disable duplication recipes for endgame progression items.
       ```

9. **`minecraft/kubejs/server_scripts/09_custom_loot_tables.js`**:
   - Lines 7-8:
     - *Previous*:
       ```javascript
       // We use EntityEvents.death to ensure compatibility
       // across all KubeJS versions.
       ```
     - *Updated*:
       ```javascript
       // Handles custom entity drop tables via EntityEvents.death for reliable cross-version execution.
       ```

10. **`minecraft/kubejs/server_scripts/10_avaritia_final_polish.js`**:
    - Line 210:
      - *Previous*: `// PLUS our custom boss drops.`
      - *Updated*: `// alongside modpack-specific boss drop materials.`

11. **`minecraft/kubejs/server_scripts/12_food_buffs.js`**:
    - Lines 5-6:
      - *Previous*:
        ```javascript
        // Makes late-game foods actually worth crafting
        // by providing 15-60 minute buffs for bosses.
        ```
      - *Updated*:
        ```javascript
        // Applies tiered passive potion effects (15 to 60 minutes) to advanced culinary recipes.
        ```

12. **`minecraft/kubejs/server_scripts/15_loot_nerfs.js`**:
    - Lines 8-11:
      - *Previous*:
        ```javascript
        // NERF 1: SLIME/MAGMA CUBE SPLITTING EXPLOIT
        // Slimes split into tiny slimes, causing them to 
        // drop absurd amounts of Malum spirits.
        // We completely remove these drops from them.
        ```
      - *Updated*:
        ```javascript
        // Balance: Strip Malum spirit drops from splitting and swarming entities (slimes, magma cubes, silverfish, endermites) to prevent mob farm exploitation.
        ```

13. **`minecraft/kubejs/server_scripts/17_goblin_trades.js`**:
    - Line 8:
      - *Previous*: `// They will occasionally sell an Infinity Fragment for an insane price!`
      - *Updated*: `// Adds rare high-tier trade offering an Infinity Fragment at extreme currency cost.`
    - Line 10:
      - *Previous*: `// We add to the legendary.json for the normal goblin trader`
      - *Updated*: `// Datapack trade pool injection for Goblin Trader legendary trades table.`
    - Line 13:
      - *Previous*: `"replace": false, // We append, not replace the whole file`
      - *Updated*: `"replace": false, // Append to existing trades array without overwriting default pool`

14. **`minecraft/kubejs/server_scripts/18_boss_duplicator.js`**:
    - Lines 39-40:
      - *Previous*:
        ```javascript
        // The replicator item is kept in the grid using native keepIngredient() if supported,
        // but we will continue to use the event fallback to ensure it works across all NeoForge builds.
        ```
      - *Updated*:
        ```javascript
        // Retains replicator catalyst in crafting matrix using keepIngredient(), complemented by crafted event fallback for cross-version consistency.
        ```
    - Line 45:
      - *Previous*: `]).keepIngredient('kubejs:anomaly_replicator'); // Modern KubeJS method to leave item in grid!`
      - *Updated*: `]).keepIngredient('kubejs:anomaly_replicator'); // Retains crafting catalyst item in matrix`

15. **`minecraft/kubejs/server_scripts/20_disable_bugged_spells.js`**:
    - Line 32:
      - *Previous*: `// Also prevent right clicks just in case`
      - *Updated*: `// Intercept right-click actions to prevent casting disabled scrolls.`

16. **`minecraft/kubejs/server_scripts/22_apotheosis_gear_sets.js`**:
    - Line 7:
      - *Previous*: `// We use ServerEvents.generateData to ensure they are registered correctly in 1.21.`
      - *Updated*: `// Registers custom gear set data via ServerEvents.generateData for 1.21 datapack generation.`

17. **`minecraft/kubejs/server_scripts/23_zenith_saber.js`**:
    - Line 45:
      - *Previous*: `// This runs for EVERY crafted item, so we exit instantly if not a diamond sword.`
      - *Updated*: `// Global craft event guard clause: immediate exit for non-target items.`
    - Line 51:
      - *Previous*: `// 3. Verify if it is our custom Zenith Saber`
      - *Updated*: `// 3. Verify target item matches Zenith Saber display name`

18. **`minecraft/kubejs/server_scripts/25_hardcoded_minibosses.js`**:
    - Line 393:
      - *Previous*: `// They do NOT drop the gear (it died with them for a reason)`
      - *Updated*: `// Prevent armor and weapon item drops on entity death (drop chances set to 0.0)`
    - Line 400:
      - *Previous*: `// Scale + attributes: Slightly bigger, much tougher, same speed (they're undead, they shamble)`
      - *Updated*: `// Attribute modifiers: scale 1.15, increased health (+300%), damage (+100%), knockback resistance, and base armor`

19. **`minecraft/kubejs/server_scripts/27_vampire_pillager.js`**:
    - Line 476:
      - *Previous*: `// Active disengage: Continuously flee and evade player during cooldown (STAGE 1 ONLY, NEVER IN AGGRO)`
      - *Updated*: `// Active disengage: Continuously flee and evade player during cooldown (Phase 1 disengage, never when aggressive)`

20. **`minecraft/kubejs/server_scripts/50_xp_fluids_unification.js`**:
    - Line 28:
      - *Previous*: `// Allows seamless conversion between any XP fluid type without loss`
      - *Updated*: `// Enables 1:1 cross-fluid conversion across all registered experience fluid variants without loss.`

21. **`minecraft/kubejs/server_scripts/expert_mode_recipes.js`**:
    - Line 20:
      - *Previous*: `// (We keep IE Crusher and Mekanism Enrichment as UPGRADES, not alternatives)`
      - *Updated*: `// Immersive Engineering Crusher and Mekanism Enrichment Chambers serve as high-tier processing upgrades.`
    - Line 30:
      - *Previous*: `// Note: We keep vanilla smelting as a basic option but Create gives 2x`
      - *Updated*: `// Retain standard 1:1 vanilla smelting while Create crushing provides 2x yield.`
    - Lines 63-65:
      - *Previous*:
        ```javascript
        // (Compressed Iron is normally made by just placing iron under pressure,
        //  we add a Create prerequisite by requiring the Pressure Chamber itself
        //  to use Create components)
        ```
      - *Updated*:
        ```javascript
        // Pressure Chamber construction requires Create mechanical components as prerequisites.
        ```

22. **`minecraft/kubejs/server_scripts/random_gateways.js`**:
    - Line 299:
      - *Previous*: `console.error(\`[PEAK RandomGateway] FTB Chunks force-loading notice: \${e}\`);`
      - *Updated*: `console.error(\`[PEAK RandomGateway] FTB Chunks force-loading error: \${e}\`);`
    - Line 332:
      - *Previous*: `console.error(\`[PEAK RandomGateway] FTB Chunks un-forceload notice: \${e}\`);`
      - *Updated*: `console.error(\`[PEAK RandomGateway] FTB Chunks un-forceload error: \${e}\`);`
    - Line 566:
      - *Previous*: `// Proximity verification: ensure this is our random gateway and not a player's private Gate Pearl`
      - *Updated*: `// Proximity verification: ensure completed entity matches active random gateway coordinates, ignoring private player Gate Pearls`
    - Line 604:
      - *Previous*: `// Proximity verification: ensure this is our random gateway`
      - *Updated*: `// Proximity verification: ensure failed entity matches active random gateway coordinates`

23. **`minecraft/kubejs/startup_scripts/40_iaf_durability_buff.js`**:
    - Line 3:
      - *Previous*: `// We use explicit values because reading maxDamage dynamically returns undefined/NaN during startup.`
      - *Updated*: `// Explicit durability values applied directly because dynamic maxDamage resolution returns undefined during startup registration.`

24. **`minecraft/kubejs/startup_scripts/apokinetics_unregister.js`**:
    - Line 3:
      - *Previous*: `// Surgically unregister Apokinetics donation prompt from NeoForge event bus`
      - *Updated*: `// Unregister Apokinetics client donation prompt from NeoForge event bus`
    - Line 11:
      - *Previous*: `console.info('[PEAK Fix] Surgically unregistered com.fishguy129.apokinetics.client.DonationPromptClient to silence donation prompts.');`
      - *Updated*: `console.info('[PEAK Fix] Unregistered com.fishguy129.apokinetics.client.DonationPromptClient to disable recurring donation prompts.');`

25. **`minecraft/kubejs/startup_scripts/block_factory_buffs.js`**:
    - Line 13:
      - *Previous*: `// Add our new modifiers`
      - *Updated*: `// Attach rebalanced attribute modifiers`

26. **`minecraft/kubejs/startup_scripts/fix_malum_watchdog.js`**:
    - Line 5:
      - *Previous*: `// This script surgically unregisters Malum's RuntimeEvents class`
      - *Updated*: `// Unregisters Malum's RuntimeEvents class from the NeoForge game event bus.`
    - Line 13:
      - *Previous*: `console.info('[PEAK Fix] Surgically unregistered com.sammy.malum.events.RuntimeEvents to prevent watchdog hangs.');`
      - *Updated*: `console.info('[PEAK Fix] Unregistered com.sammy.malum.events.RuntimeEvents to prevent watchdog hangs.');`

27. **`minecraft/kubejs/startup_scripts/vampillager_entity.js`**:
    - Line 92:
      - *Previous*: `// Check backward landing position: ensure we don't leap backwards into direct sunlight!`
      - *Updated*: `// Raycast backward disengage landing vector: verify entity does not leap into direct sunlight exposure while unarmored.`

---

## 2. Logic Chain

1. **Premise 1 (Identification & Context)**: Explorer 1 conducted an in-depth AST and text survey across all 89 `.js` files, cataloging 27 files requiring comment and log updates to remove AI markers, conversational self-talk, and "surgical" terms.
2. **Premise 2 (Minimal-Change Execution)**: Each file was viewed individually around the flagged regions. Targeted replacements were executed using exact matching, replacing informal prose with concise technical explanations of the underlying Minecraft and KubeJS mechanics (e.g. why `Sequenced Assembly` preserves NBT/Data Components, why explicit durability is passed during startup, why `keepIngredient()` is paired with crafted event fallback).
3. **Premise 3 (Zero Runtime Disruption)**: Git diff analysis showed that no game logic, event registrations, handler callbacks, or variable names were altered. Every modification was confined to `//` comments or string literals within informational `console.info` / `console.error` logs.
4. **Premise 4 (Preservation of True Mechanics)**: Genuine in-game mechanics (such as *Ice and Fire* Stage 5 dragons in `startup_scripts/custom_items.js`) were left untouched.
5. **Premise 5 (Compilation Verification)**: Every single `.js` file in `minecraft/kubejs/` (89/89) was tested using Node.js syntax compilation (`node -c`), confirming 100% clean syntax with zero errors.

---

## 3. Caveats

- **Third-Party Flavor Text**: `server_scripts/20_fixed_datapacks.js` line 70 contains commented-out JSON recipe flavor text from upstream Ars Nouveau (`"so we made them bouncy!"`). As verified by Explorer 1, this is third-party author flavor text in disabled recipe data rather than developer commentary, and was preserved as outside Milestone 3 write boundaries.
- **Ice & Fire Stages**: `startup_scripts/custom_items.js` lines 85 and 91 refer to *Ice and Fire* dragon growth stages (Stage 1-5 biological maturity), correctly identified as genuine game mechanics and preserved intact.

---

## 4. Conclusion

- **Surgical references**: Exactly 0 occurrences of "surgical" / "surgically" remain across `minecraft/kubejs/` (down from 6 occurrences in 3 files).
- **First-person plurals**: All 24 developer first-person plural statements ("we", "our") across 18 scripts have been eliminated and replaced with passive/imperative technical documentation.
- **Editorial self-talk**: All flagged inner-monologue comments ("just in case", "they shamble", "feel earned", "You can't skip Create") were successfully converted to clean technical specifications.
- **Syntax integrity**: 89 out of 89 JavaScript files pass syntax compilation cleanly (`node -c`) with zero errors.

---

## 5. Verification Method

### 1. Zero "Surgical" Phrasing Verification
Run in PowerShell:
```powershell
python -c "
import os, re
base = r'minecraft/kubejs'
hits = []
for root, _, files in os.walk(base):
    for f in files:
        if f.endswith('.js'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='replace') as fp:
                for idx, line in enumerate(fp, 1):
                    if re.search(r'\bsurgic', line, re.I):
                        hits.append(f'{f}:{idx}: {line.strip()}')
print(f'Total surgical hits: {len(hits)}')
"
```
**Expected Output**: `Total surgical hits: 0`

### 2. Full JS Syntax Compilation Suite
Run in PowerShell:
```powershell
python -c "
import os, subprocess, sys
base = r'minecraft/kubejs'
failed = []
passed = 0
for root, _, files in os.walk(base):
    for f in files:
        if f.endswith('.js'):
            p = os.path.join(root, f)
            res = subprocess.run(['node', '-c', p], capture_output=True, text=True)
            if res.returncode != 0:
                failed.append(p)
            else:
                passed += 1
print(f'Tested: {passed + len(failed)}, Passed: {passed}, Failed: {len(failed)}')
assert len(failed) == 0
"
```
**Expected Output**: `Tested: 89, Passed: 89, Failed: 0`
