# PEAK Modpack Changelog
**Date:** May 27, 2026
**Target Platform:** Minecraft 1.21.1 (NeoForge)
**Engine:** KubeJS (Rhino Integration) / Mojang Mappings (Mojmap)

---

## 🚀 Key Highlights & Major Additions

### 👑 1. Automatic Apotheosis World Tier Progression
*   **Manual Bypass Disabled:** Fully locked manual tier selection in `apotheosis.cfg`. Players must now earn their progression naturally to view and unlock advanced loot statistics.
*   **Event-Driven Progression Script (`apotheosis_auto_tiers.js`):** Built a zero-overhead, highly performant server event script listening to advancement unlocks.
*   **Automatic Upgrades:** Reaching progression milestones instantly runs silent console commands to advance the player's Apotheosis World Tier:
    *   `Haven` ➔ `Frontier` ➔ `Ascent` ➔ `Summit` ➔ `Pinnacle`
*   **Premium Visual Feedback:** Displays styled, dark-gold framed border banners in the player's chat highlighting their achievement in a premium interface.
*   **Themed Gift Distribution:** Awards balanced custom progression loot directly to the player's inventory upon tier completion:
    *   **Frontier:** 4x Gem Dust, 4x Brass Ingot
    *   **Ascent:** 2x Sigil of Enhancement, 2x Precision Mechanism
    *   **Summit:** 1x Sigil of Socketing, 2x Sturdy Sheet
    *   **Pinnacle:** 1x Sigil of Supremacy, 1x Infinity Fragment

### ⛏️ 2. Comprehensive World Ore Unification
*   **Duplicate Spawns Removed:** Disabled duplicate placed features for Tin, Lead, Zinc, Uranium, Osmium, Nickel, Silver, Aluminum, and Fluorite across all Overworld biomes.
*   **Physical Biome Modifier Integration:** Engineered a custom biome modifier registry JSON at `kubejs/data/kubejs/neoforge/biome_modifier/remove_duplicate_ores_overworld.json` to handle feature exclusions natively at the startup engine level. This bypasses late-loading KubeJS worldgen phase limits in 1.21.1.
*   **Mod Compatibility Preserved:** Safely whitelisted Alex's Caves Uranium inside specialized radioactive biomes, and restricted duplicate Mekanism worldgen options in `world.toml`.

### ⚔️ 3. Boss Weaponry & Gear Integration (Knight Quest, Simply Swords & Simply More)
*   **Weapon Expansion:** Expanded Apotheosis boss gear configurations (`19_mob_gear.js`) with **79 unique high-end weapons** to give boss spawns incredible visual and combat variety:
    *   **Simply Swords (43 weapons):** Fully registered all special weapons, including unique broadswords, rapiers, cutlasses, glaives, chakrams, and katanas.
    *   **Simply More (36 weapons):** Integrated additional configuration weapons to expand the pool.
    *   **Knight Quest:** Integrated the entire suite of Knight Quest weapons (Cleavers, Halberds, Greatswords) and custom thematic armor sets (Doom, Gale, Phoenix, etc.) directly into the boss equipment tables.

---

## 🛠️ Performance & Bug Fixes

### 🐛 1. KubeJS Rhino Engine Redeclaration Fixes
*   **The Problem:** The Rhino JS engine threw critical script exceptions due to duplicate `const` declarations when firing entity spawn listeners repeatedly.
*   **The Fix:** Migrated local scope constants inside active listeners to flexible block-scoped `let` variables and moved static global tables outside of event closures, preventing execution halts.

### 🧪 2. Armor of the Ages & Knight Quest ID Migrations
*   **Asset Restructuring:** Addressed broken references in scripts caused by internal item ID changes in the 1.21.1 port of these mods:
    *   *Armor of the Ages:* Mapped legacy armor sets to new formats (e.g., `anubis_helmet` ➔ `anubis_armor_head`, `ra_chestplate` ➔ `ra_armor_chest`, etc.).
    *   *Knight Quest:* Corrected discontinued legacy IDs (e.g., `crimson_sword` ➔ `cleaver`, `water_axe` ➔ `halberd` / `greatsword`).

### 📦 3. Recipe Cleanups & Balances
*   **Malum Integration:** Deleted the duplicate Create mechanical mixing recipe for **Hallowed Gold** to restore progression integrity through Malum's Spirit Altar / Infusion rituals.
*   **Paraglider Balance:**
    *   Completely cleared **Spirit Orbs** from standard dungeon loot chests.
    *   Introduced an active **8% drop rate** for Spirit Orbs when breaking vanilla and modded Mob Spawners, incentivizing active dungeon exploration.
