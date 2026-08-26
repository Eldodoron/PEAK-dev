# PEAK Modpack - Recipe Design Philosophy & Critical Audit

## 1. Guiding Principles for Custom Recipes

1. **Visual Accuracy (What You See Is What You Craft):**
   - 3D models and textures define the recipe. If a block is made of dark oak planks, open manuscripts, and inkwells (like the Inscription Table), its recipe MUST reflect wooden desks, books, ink, and quills.
   - Do NOT inject arbitrary metals or stone slabs into wooden furniture models.

2. **Thematic Consistency (Magic vs. Industry):**
   - **Magic Workstations (Ars Nouveau, Iron's Spells, Malum):** Must be crafted using magical woods, botanical essences, source gems, gold, crystals, and mystical components.
   - **Industrial Machinery (PneumaticCraft, Immersive Engineering, AE2):** Belongs to the mechanical progression. Clockwork gears, `create:precision_mechanism`, steel, and electron tubes belong here.
   - **NEVER** put clockwork gears (`create:precision_mechanism`) or heavy mechanical casings into ethereal spirit cauldrons or spell enchanting altars.

3. **Organic Progression (No Senseless Dimension Gating):**
   - Basic Tier 1 magic tools (like writing your first spell in Ars Nouveau) must NEVER require dimension-gated materials like Twilight Forest Ironwood. Early magic belongs in the Overworld.

---

## 2. Detailed Audit of Illogical / "Ridiculous" Recipes

| Target Item / Recipe | Current Illogical Ingredients | Why It Is Illogical | Proposed Thematic Replacement |
| :--- | :--- | :--- | :--- |
| **`ars_nouveau:scribes_table`** | `twilightforest:ironwood_ingot`, `minecraft:smooth_stone_slab` | Requiring Twilight Forest Ironwood to craft the starter glyph discovery table gates all early spell creation behind dimension hopping. Model is pure Archwood & gold. | Archwood planks / noble wood (`#minecraft:planks`), Gold ingot (`#c:ingots/gold`), and Book/Feather. |
| **`ars_nouveau:enchanting_apparatus`** | `create:precision_mechanism`, `create:brass_casing`, `twilightforest:ironwood_ingot` | Clockwork mechanisms and brass motors inside a pure floating mana crystal pedestal destroy the mystical fantasy aesthetic. | Gold ingots, `ars_nouveau:source_gem_block`, `ars_nouveau:arcane_core`, Amethyst Shard, and Polished Deepslate/Arcane Stone. |
| **`irons_spellbooks:uncommon_ink`** | `twilightforest:ironwood_ingot` | Dissolving a forged metal-wood ingot into liquid writing ink is absurd physically and lore-wise. | Botanical / Alchemical reagents: Glowstone dust, Magebloom fiber, Lapis Lazuli, or Ghast Tears. |
| **`malum:spirit_crucible`** | `create:precision_mechanism` | A gothic soul-refining cauldron for spirits of the dead has no reason to contain clockwork escapements and mechanical gears. | `malum:refined_soulstone`, `malum:hallowed_gold_ingot`, Spectral quartz, and Dark bone materials. |
| **`wands:diamond_wand`** | `create:precision_mechanism` | Artificial tech gating on a simple Quality of Life (QoL) builder's tool. | Diamond, Gold/Copper reinforcement, and wooden handle. |

---

## 3. Valid & Justified Precision Mechanism Recipes

These recipes are **thematically coherent** and should remain:

- **`pneumaticcraft:assembly_platform` / `drill` / `laser`:** Precision robotic CNC tooling.
- **`pneumaticcraft:advanced_air_compressor` / `thermopneumatic_processing_plant`:** High-precision industrial pneumatic machinery.
- **`ae2:inscriber`:** Microchip and silicon processor press with micron tolerances.
- **`immersiveengineering:metal_press` & `tfmg:radial_engine`:** Transition from Create kinetic energy into heavy industrial mechanics.
