# PEAK Modpack: Categorized Mod Registry

This file contains the categorized list of all **380+ mods** in the PEAK NeoForge 1.21.1 modpack development workspace. Mods are classified by technical function and gameplay category.

---

## 🚀 Optimization & Performance Mods (20 mods)

These mods are the structural backbone of PEAK's client FPS and server TPS stability.

| File / Mod Jar | Category / Purpose | Key Optimization Details |
| :--- | :--- | :--- |
| `c2me-neoforge-mc1.21.1-0.3.0+alpha.0.91.jar` | Chunk Generation Speed | Multi-threaded world generation and chunk loading engine. Prevented gateway deadlocks in configs. |
| `lithium-neoforge-0.15.3+mc1.21.1.jar` | General Game Engine | General optimization for physics, chunk loading, mob AI ticking, and entity collision checks. |
| `sodium-neoforge-0.6.13+mc1.21.1.jar` | Rendering Engine | Rewritten modern client-side rendering pipeline (massive FPS boost). |
| `entityculling-neoforge-1.10.2-mc1.21.1.jar` | Render Thread Culling | Skips rendering blocks/entities hidden from camera sight. |
| `moreculling-neoforge-1.21.1-1.0.7.jar` | Render Culling Additions | Aggressive culling for rain, item frames, and hidden face elements. *Downgraded from 1.0.8 to prevent respawn crashes.* |
| `ferritecore-7.0.3-neoforge.jar` | Memory / RAM reduction | Replaces Minecraft's heavy blockstate and model memory representation (saves ~1-2GB RAM). |
| `immediatelyfast-NeoForge-1.6.10+1.21.1.jar` | Rendering Speedup | Speeds up text rendering, HUDs, and immediate GUI draws. |
| `krypton_fnp-neoforge-1.21.1-0.2.28.1-1.21.1.jar` | Network Optimization | Optimizes packet sizes and transport layers to prevent packet-overflow disconnects. |
| `modernfix-neoforge-5.27.8+mc1.21.1.jar` | Engine Patches & Bugfixes | Plugs dozens of core memory leaks, bypasses redundant saves. *Hard-locked: Dynamic Languages mixin disabled.* |
| `servercore-neoforge-1.5.5+1.21.1.jar` | Server TPS Optimization | Dynamically optimizes entity ticking and simulation distances based on load. Enables villager lobotomization. |
| `rhenium-1.0.0+neo.jar` | Structure Template Optim. | Limits structure template cache sizes to prevent runaway worldgen memory leaks. |
| `chunky-NeoForge-1.4.23.jar` | Chunk Pre-generation | Allows pre-loading map chunks while the server is idle, eliminating dynamic worldgen lag. |
| `clumps-neoforge-1.21.1-19.0.0.1.jar` | Experience Orb Lag | Clumps XP orbs together into singular floating objects to prevent CPU render stutters. |
| `fastsuite-1.21.1-6.0.7.jar` | Recipe Lookup Optim. | Speeds up item craft and smelting ingredient searches to eliminate grid ticks. |
| `ixeris-4.3.0+1.21.1-neoforge.jar` | Mouse Input Thread | Offloads mouse movements and high-Hz poll rates from the render thread to prevent micro-stutters. |
| `letmedespawn-1.21.x-neoforge-1.5.0.jar` | Entity Despawner | Forces standard despawning rules on items/entities stuck in passive state. |
| `asynclogger-1.1.1+1.21.1-neoforge.jar` | Asynchronous Disk Logging | Offloads console logging to separate hilos, keeping disk IO off the game thread. |
| `fastboot-1.21.x-v1.3neo.jar` | Startup Speedup | Accelerates modpack launch loading stages. |
| `jeiworldgen-neoforge-1.1.0.jar` | JEI Optimization | Optimizes recipe list caches during world initialization. |
| `nowheel-1.0.3+1.21.1neoforge.jar` | Create Culling Helper | Preserved explicitly to maintain custom culling for *Create* contraptions. |

---

## 🛠️ Scripting & Development Tools (9 mods)

These mods provide script compilation, runtime environments, and diagnostic systems.

*   `kubejs-neoforge-2101.7.2-build.363.jar` — Direct JavaScript scripting engine for recipes, tags, events, and asset injections.
*   `kubejs-create-neoforge-2101.3.1-build.18.jar` — KubeJS integration for Create recipes and contraptions.
*   `kubejs-mekanism-neoforge-2101.1.7-build.18.jar` — KubeJS integration for Mekanism chemical and factory recipes.
*   `kubejs_curios_neoforge_1.21.1-1.0.4.jar` — KubeJS integration for accessory and trinket events.
*   `kubejs_enderio-neoforge-1.21.1-0.12.0.jar` — KubeJS integration for EnderIO recipes.
*   `kubejsarsnouveau-1.3.2.jar` — KubeJS integration for Ars Nouveau spellcrafting.
*   `kubejsde-1.21.1-1.1.0.jar` — KubeJS Draconic Evolution expansion.
*   `lootjs-neoforge-1.21.1-3.7.0.jar` — JavaScript-based loot table editing framework.
*   `morejs-neoforge-1.21.1-0.16.0.jar` — JavaScript additions for merchant trades and custom structures.
*   `rhino-2101.2.7-build.81.jar` — Modern JS compilation engine utilized by KubeJS.
*   `spark-1.10.124-neoforge.jar` — Elite CPU profiler and memory tracking tool for debugging TPS and lag.
*   `crashassistant-neoforge-1.20.6-1.21.4-1.11.9.jar` — Diagnostic screen presenting helpful advice during game crashes.

---

## ⚙️ Core Libraries & APIs (34 mods)

Essential API foundations required by major content mods.

*   `architectury-13.0.8-neoforge.jar` — Cross-platform API layer.
*   `balm-neoforge-1.21.1-21.0.56.jar` — Waystones API layer.
*   `bookshelf-neoforge-1.21.1-21.1.81.jar` — General library wrapper.
*   `brandonscore-1.21.1-3.2.1.309.jar` — Core library for Draconic Evolution.
*   `citadel-1.21.1-2.7.6.jar` — Animation library for Alex's Caves and Alex's Mobs. *(Duplicate 2.7.0 deleted).*
*   `cloth-config-15.0.140-neoforge.jar` — Universal config screen GUI engine.
*   `codechickenlib-1.21.1-4.6.1.526.jar` — 3D rendering and model compilation library.
*   `curios-neoforge-9.5.1+1.21.1.jar` — Accessory slots API system. *(Duplicate 9.1.4 deleted).*
*   `geckolib-neoforge-1.21.1-4.8.4.jar` — 3D animation engine for custom entity meshes.
*   `insanelib-2.4.15.0.jar` — Core API helper.
*   `kotlinforforge-5.11.0-all.jar` — Kotlin language loader for NeoForge.
*   `lodestone-1.21.1-1.8.2.jar` — Advanced client rendering and particle effects library for Malum/Apotheosis.
*   `moonlight-neoforge-1.21.1-3.0.5.jar` — Utility API for dynamic block mappings and maps.
*   `puzzleslib-v21.1.39-1.21.1-NeoForge.jar` — API helper for Easy Anvils.
*   `smartbrainlib-neoforge-1.21.1-1.16.11.jar` — Optimization framework for mob Pathfinding AI.
*   `terrablender-neoforge-1.21.1-4.1.0.8.jar` — Universal custom biome registration engine.
*   `yungsapi-1.21.1-NeoForge-5.1.6.jar` — Structural API backing all YUNG's Better Dungeons/Structures mods.
*   `zeta-1.1-40.jar` — Core API library backing Quark.

---

## 🎨 UI & Quality of Life (QoL) Mods (25 mods)

Enhances client interfaces, HUDs, inventory management, and immersive details.

*   `jei-1.21.1-neoforge-19.27.0.336.jar` — Just Enough Items (recipe viewing).
*   `jade-1.21.1-NeoForge-15.10.5.jar` — HUD tooltips showing block details and entities in real time.
*   `controlling-neoforge-1.21.1-19.0.5.jar` — Dynamic keybinding search utility.
*   `mousetweaks-neoforge-mc1.21-2.26.1.jar` — Fluid item inventory sorting and drag-clicks.
*   `healthbars-v21.1.0-1.21.1-NeoForge.jar` — Floating health indicators. *(Crosshair raycast disabled to prevent Render Thread stutters).*
*   `overflowingbars-v21.1.1-1.21.1-NeoForge.jar` — Clean stack overlays for massive health values.
*   `loot beams refork-neoforge-1.21.1-3.4.5.jar` — ColorfulRPG-style light pillars for dropped items.
*   `antique atlas-1.21.1-8.0.1-NeoForge.jar` — RPG-themed schematic maps.
*   `solcarrot-1.21.1-1.16.6.jar` — Spice of Life (rewards for eating diverse foods).
*   `notenoughanimations-neoforge-1.12.2-mc1.21.1.jar` — Dynamic animations for climbing, eating, and map-reading.
*   `particlerain-4.0.0-beta.10+1.21.1-neoforge.jar` — Replaces vanilla rain blocks with highly optimized 3D particle threads.
*   `aaa-particles-neoforge-1.21-1.4.15.jar` — RPG spell effect rendering engine.

---

## ⚙️ Tech, Automation & Industry (12 mods)

Advanced assembly lines, flying physics ships, power grids, and fluid mechanics.

*   `create-1.21.1-6.0.10.jar` — Mechanical automation, cogwheels, belts, and moving structures.
*   `create-aeronautics-bundled-1.21.1-1.2.1.jar` — Real physics-based aircraft, airships, and flying machines.
*   `sable-neoforge-1.21.1-1.2.2.jar` — Valkyrien Skies physics engine backbone. *(Tuning: 64 tracking range).*
*   `appliedenergistics2-19.2.17.jar` — Digital matter storage networks, autocrafting, and sub-routing.
*   `mekanism-1.21.1-10.7.19.85.jar` — Advanced high-tech energy grids, chemical processing, and item purification.
*   `immersiveengineering-1.21.1-12.4.2-194.jar` — Retro-futuristic heavy machinery, power cables, and multi-block structures.
*   `pneumaticcraft-repressurized-8.2.19+mc1.21.1.jar` — Pressure-driven automation, assembly arms, drones, and suits.
*   `enderio-8.2.8-beta.jar` — Highly compact alloy smelters, fluid tubes, and teleportation conduits.
*   `tfmg-1.2.0.jar` — The Factory Must Grow: Heavy petrochemical refining and industrial automation expansion.

---

## 🔮 Magic & Spellcraft (10 mods)

*   `ars_nouveau-1.21.1-5.11.3.jar` — Spellcrafting, dynamic custom spells, magical automation, and glyphs.
*   `irons_spellbooks-1.21.1-3.15.6.jar` — RPG magic, customizable spellbooks, dungeons, and unique spell lines.
*   `malum-1.21.1-1.8.2.jar` — Spirit magic, alter offerings, scythes, and dark alchemy. *(Optimized Malum event bus to prevent Watchdog freezes).*
*   `reliquary-1.21.1-2.0.70.1464.jar` — Magical relics, alchemy flasks, mob drops, and utility charms.

---

## 🗡️ RPG Mechanics, Monsters & Mobs (18 mods)

*   `alexsmobs-1.22.17.jar` — Dozens of custom animals, creatures, and unique drops.
*   `vampirism-1.21-1.10.10.jar` — Vampiric skill trees, faction levels, blood systems, and biome conversions.
*   `guardvillagers-2.4.7-1.21.1.jar` — Spawnable guards protecting villages. *(Ticking capped in hotspots).*
*   `iceandfirece-2.0-beta.16-1.21.1-neoforge.jar` — Dragons, gorgons, and massive mythical mobs. *(Tuning: dragon target search set to 64).*
*   `bettercombat-neoforge-2.3.2+1.21.1.jar` — Dynamic attack swings, combos, and custom hitboxes.
*   `apotheosis-1.21.1-8.5.2.jar` — Heavy RPG stats, gem socketing, custom weapon traits, and boss spawns.
*   `l_ender's cataclysm 1.21.1-3.27.jar` — Epic, highly detailed endgame dungeons and catastrophic bosses. *(Tuning: Block griefing disabled, ender guardian break-span set to 0).*

---

## 🌍 WorldGen, Dungeons & Dimensions (15 mods)

*   `twilightforest-1.21.1-4.8.3345-universal.jar` — Enchanted twilight dimension filled with hollow hills and classic bosses.
*   `the_undergarden-1.21.1-0.9.6.jar` — Dark, subterranean dimension under the bedrock.
*   `deeperdarker-neoforge-1.21.1-1.4.jar` — Expands the Deep Dark biome into an entirely new ancient-portal dimension.
*   `dungeons-and-taverns-v4.4.4 [NeoForge].jar` — Immense custom structures spanning taverns, keeps, and ruins. *(Optimized ticking rate of structures).*
*   `dungeonsarise-1.21.1-2.1.68-release.jar` — Gigantic exploration dungeons and sky structures.
*   `yungsbetterdungeons-1.21.1-NeoForge-5.1.4.jar` — complete redesign of vanilla dungeons (and desert/jungle temples, mineshafts, fortresses).
*   `tectonic-3.0.22-neoforge-21.1.jar` — Re-engineered world generation featuring mountain ranges, deep canyons, and rivers.

---

## 🚫 Purged / Disabled Mods (7 mods)

These mods were identified as highly unstable or catastrophic to performance and have been safely disabled.

| Mod / Jar File | Status | Reason for Removal |
| :--- | :--- | :--- |
| `superbosses-2.0.0-1.21.1.jar` | 🚫 Renamed `.disabled` | Infinite loop spamming console, spawning thousands of entities, leading to instant OOM. |
| `epic-bosses-0.2.0-1.21.1.jar.disabled` | 🚫 Renamed `.disabled` | MCreator loop applying passive potion effects to all loaded entities every tick. Consumed 13.35% CPU constantly. |
| `heavier_weapons-1.21.1-NeoForge-1.1.0.jar.disabled` | 🚫 Renamed `.disabled` | General compatibility failures on NeoForge 1.21.1. |
| `unusualend-2.2.1.jar.disabled` | 🚫 Renamed `.disabled` | Dim transition deadlock conflicts under C2ME. |
| `betterend-21.0.24.jar.disabled` | 🚫 Renamed `.disabled` | Dependency classloader conflicts under NeoForge. |
| `bclib-21.0.20.jar.disabled` | 🚫 Renamed `.disabled` | Obsolete duplicate of fabric-centered APIs causing startup crash. |
| `legendary_arsenal-2.4-neoforge-1.21.1.jar.disabled` | 🚫 Renamed `.disabled` | Severe weapon registration crashes under Apotheosis. |
