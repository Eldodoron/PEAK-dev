# PEAK Lite - Excluded Visual & Render-Thread Components

This document outlines all mods, resource packs, and shader files that are stripped in **PEAK Lite** to maximize FPS on budget laptops, integrated graphics (iGPUs), and older CPUs.

---

## 1. Compatibility Guarantee

- **100% Cross-Play Compatible:** A player running PEAK Lite can connect to the exact same dedicated server or peer-to-peer Essential multiplayer session as a player running PEAK Standard ("Fat").
- **Zero Content Removal:** Every block, item, recipe, KubeJS script, FTB quest, mob drop, dimension, and tech/magic machine is identical.
- **Client Render Thread Only:** Exclusions strictly target visual shaders, post-processing filters, entity animation tick hooks, particle emitters, and high-vertex 3D models.

---

## 2. Excluded Client Visual Mods (15 Mods)

These mods run continuously on the client render and particle threads, consuming GPU fill-rate and CPU frame time:

| Mod File | Name | Primary Render Overhead |
|---|---|---|
| `shine-2.0.1+1.21.1-neoforge.jar` | Shine | Full-screen post-processing bloom and emissive light bleed passes. |
| `lambdynamiclights-4.8.8+1.21.1.jar` | LambDynamicLights | Continuously recalculates chunk section vertex meshes when holding/dropping torches. |
| `particular-1.21.1-NeoForge-1.5.5.jar` | Particular | Heavy ambient biome environmental particle loops (pollen, dust, falling leaves). |
| `visuality-forge-3.0.0.jar` | Visuality | Extra entity hit-sparkles, splash water ripples, and soul dripping particles. |
| `explosiveenhancement-neoforge-1.1.2.jar` | Explosive Enhancement | Spawns high-density 2D physics explosion particle puffs. |
| `particle_core-0.3.3+1.21+neoforge.jar` | Particle Core | Low-level particle rendering framework. |
| `cosycritters-0.3.2+1.21.1-neoforge.jar` | Cosy Critters | Client-side ambient insect and bird particle calculations. |
| `notenoughanimations-1.12.3-mc1.21.1.jar` | Not Enough Animations | Polls and interpolates third-person player animations (eating, drinking, rowing). |
| `fwa+1.21.1-neoforge-1.2.31.jar` | Fancy World Animations | Dynamic opening/closing animations for chests, shulker boxes, and bells. |
| `punchy-2.6.2-neoforge-1.21.1.jar` | Punchy | Screen shake impulse and weapon attack recoil physics. |
| `Perception-NEOFORGE-0.2.1+1.21.1.jar` | Perception | Post-processing vignette, speed lines, and camera motion blur. |
| `Loot Beams Refork-3.4.7.jar` | Loot Beams Refork | 3D vertical light beam rendering and depth testing for all ground items. |
| `Nirvana Lib-2.2.0.jar` | Nirvana Lib | Dedicated render-type buffer accessor library for Loot Beams. |
| `cloudlayers-1.21.1-1.1.jar` | Cloud Layers | Multi-altitude cloud mesh generation in the skybox. |
| `denseflower-1.0.0.jar` | Dense Flowers | Triples vertex count and polygon density of flower patches. |

---

## 3. Excluded Cosmetic & Non-Essential Client Mods (2 Mods)

These mods add cosmetic visual flair or client animations that are non-essential for gameplay:

| Mod File | Name | Reason for Exclusion |
|---|---|---|
| `atmospherics-2.6.5-mc-1.21.1.jar` | Atmospherics | In-game visual editor for sky, fog, clouds, and celestial bodies. |
| `smoothswapping-0.9.3.2-1.21.1-neoforge.jar` | Smooth Swapping | Client item swap and slot transition animations. |

---

## 4. Excluded Development & Diagnostic Mods (4 Mods)

Development and inspection tools used solely for modpack creation, structure inspection, or profiling:

| Mod File | Name | Reason for Exclusion |
|---|---|---|
| `CraftTweaker-neoforge-1.21.1-21.0.38.jar` | CraftTweaker | Scripting / registry dump utility (`/ct dump`). Modpack scripting is driven by KubeJS. |
| `Panoptic-1.08a-NeoForge-1.21.1.jar` | Panoptic | Structure worldgen inspection and seed map analysis. |
| `spark-1.10.124-neoforge.jar` | Spark | Performance profiler for development diagnostics and servers. |
| `wits-1.3.0+1.21-neoforge.jar` | WITS (What Is That Structure) | Structure identification overlay for debugging. |

---

## 5. Excluded Heavy Resource Packs & Shaders (8 Items)

These resource packs alter mob geometry, add 3D block complexity, or engage OpenGL shader stages:

| Resource Pack / Asset | Location | Reason for Exclusion |
|---|---|---|
| `FreshAnimations_v1.10.4.zip` | `config/paxi/resourcepacks/` | Complex multi-bone procedural mob animations; significant CPU draw call overhead. |
| `FreshCompats_v1.6.zip` | `config/paxi/resourcepacks/` | Mod compatibility layer for Fresh Animations. |
| `FA_Player-v1.0.zip` | `config/paxi/resourcepacks/` | Complex player model animation rig. |
| `Whimscape_x_FreshAnimations...zip`| `config/paxi/resourcepacks/` | Texture bridge for Fresh Animations. |
| `Cubic Leaves 2.3...zip` | `config/paxi/resourcepacks/` | 3D leaf models that multiply quad counts in forests and jungles. |
| `HyperPunchy-v2.5+.zip` | `config/paxi/resourcepacks/` | Animation data for Punchy screen recoil. |
| `Modded Swords x Punchy!...zip` | `config/paxi/resourcepacks/` | Punchy weapon model definitions. |
| `BSL_v10.1.3.zip` | `shaderpacks/` | Shaderpack cleared by default; boots directly into clean, lightweight Sodium rasterization. |

---

## 4. Retained Optimization Engines (Active in Both Packs)

PEAK Lite retains all performance-enhancing mods to ensure maximum possible frame rates:
- **`sodium`**: Core OpenGL 3.3 chunk render pipeline.
- **`entityculling`**: Skips rendering entities behind solid walls.
- **`moreculling`**: Culls hidden block faces and leaves.
- **`badoptimizations`**: Bypasses vanilla CPU entity/scoreboard bottlenecks.
- **`ImmediatelyFast`**: Optimizes GUI and font buffer allocations.
- **`modernfix`**: Dynamic memory caching and memory leak prevention.
- **`dynamic-fps`**: Reduces background CPU/GPU usage when tabbed out.
