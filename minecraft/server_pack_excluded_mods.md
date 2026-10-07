# Server Pack Excluded Mods Audit

This document lists all mod JAR files present in `minecraft/mods/` that must **NOT** be included in a dedicated server pack. It includes active `.jar` files, disabled `.jar.disabled` files, and development artifacts.

---

## Executive Summary

- **Total Mod Files Audited in `minecraft/mods/`:** 447
- **Total Files Excluded from Server Pack:** 79
  - **Active Client-Only & Dev Mods:** 65
  - **Disabled Client-Only Mods (`.jar.disabled`):** 12
  - **Duplicate / Backup Artifacts (`.jar.backup`, `.jar.modified`):** 2
- **Total Server / Common Mods Retained:** 368

---

## Excluded Mods List by Category

### 1. Client Rendering Engines, Performance & Culling (8 Mods)

These mods replace or alter client-side graphics rendering, immediate mode rendering, or occlusion culling. Dedicated servers have no GPU rendering pipeline and will either ignore them or crash if loaded.

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `BadOptimizations-2.4.1-1.21.1.jar` | BadOptimizations (`badoptimizations`) | Active | Optimizes client entity rendering, HUD rendering, and particle tick rates. Declared `environment = client`. |
| `denseflower-1.0.0.jar` | Dense Flowers (`denseflowers`) | Active | Modifies flower chunk meshing and Sodium section meshing. Client-side meshing only. |
| `dynamic-fps-3.7.7+minecraft-1.21.0-neoforge.jar` | Dynamic FPS (`dynamic_fps`) | Active | Throttles client frame rates when the Minecraft window is unfocused or minimized. Manifest `side = CLIENT`. |
| `entityculling-neoforge-1.10.5-mc1.21.1.jar` | EntityCulling (`entityculling`) | Active | Raytraces entity and block entity visibility to skip client rendering behind solid geometry. |
| `ImmediatelyFast-NeoForge-1.6.11+1.21.1.jar` | ImmediatelyFast (`immediatelyfast`) | Active | Optimizes immediate mode OpenGL buffer allocation on the client. Manifest `side = CLIENT`. |
| `moreculling-neoforge-1.21.1-1.0.7.jar` | More Culling (`moreculling`) | Active | Overhauls block state, leaf, and cloud culling pipelines. Pure client rendering optimization. |
| `rhenium-1.0.0+neo.jar` | Rhenium (`rhenium`) | Active | NeoForge rendering pipeline implementation for the Sodium ecosystem. Pure client rendering. |
| `sodium-neoforge-0.6.13+mc1.21.1.jar` | Sodium (`sodium`) | Active | Modern OpenGL rendering engine replacing vanilla chunk renderers. Manifest `side = CLIENT`. |

---

### 2. Shaders, Upscaling & Video Settings Menus (6 Mods)

Shaders and upscaling technologies hook into client framebuffers and shaders.

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `iris-neoforge-1.8.12+mc1.21.1.jar.disabled` | Iris (`iris`) | Disabled | Modern shaderpack loader supporting OptiFine shaderpacks. Manifest `side = CLIENT`. |
| `reeses-sodium-options-neoforge-2.2.3+mc1.21.1.jar.disabled` | Reese's Sodium Options (`reeses_sodium_options`) | Disabled | Overhauls the Sodium video settings GUI with scrolling tabs. Client GUI only. |
| `shine-2.0.1+1.21.1-neoforge.jar` | Shine (`shine`) | Active | Screen-space bloom and glow post-processing shader. Manifest `side = CLIENT`. |
| `sodiumoptionsapi-neoforge-1.0.10-1.21.1.jar.disabled` | Sodium Options API (`sodiumoptionsapi`) | Disabled | Event API allowing other mods to inject options pages into Sodium's video settings menu. |
| `sodiumoptionsmodcompat-neoforge-1.0.0-1.21.1.jar.disabled` | Sodium Options Mod Compat (`sodiumoptionsmodcompat`) | Disabled | Video settings menu integration for Sodium. Client GUI only. |
| `super_resolution-neoforge-1.21..1.21.1-0.8.3-alpha.4+opengl.jar.disabled` | Super Resolution (`super_resolution`) | Disabled | DLSS, FSR, and XeSS temporal upscaling for client rendering. |

---

### 3. Client Visuals, Textures, Particles & Animations (23 Mods)

Visual enhancements that manipulate particles, models, animations, beam renderers, and skyboxes on the client.

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `atmospherics-2.6.5-mc-1.21.1.jar` | Atmospherics (`atmospherics`) | Active | In-game visual editor for sky, fog, air haze, and clouds. Manifest `side = CLIENT`. |
| `bigwater-1.2.0-neoforge+mc1.21.1.jar.disabled` | Big Water (`bigwater`) | Disabled | Scales water texture UV mapping and modifies Sodium fluid rendering. Client visual only. |
| `cinematic_respawn-1.21.1-neoforge-1.2.0.jar` | Cinematic Respawn (`cinematic_respawn`) | Active | Interpolates camera pan and screen fade on player death and respawn. Manifest `side = CLIENT`. |
| `cirrus-neoforge-1.21.1-1.2.1.jar.disabled` | Cirrus (`cirrus`) | Disabled | Volumetric cloud generation and sky rendering engine. Manifest `side = CLIENT`. |
| `cloudlayers-1.21.1-1.1.jar` | Cloud Layers (`cloudlayers`) | Active | Multi-tier altitude cloud rendering in the skybox. Client visual only. |
| `cosycritters-0.3.2+1.21.1-neoforge.jar` | Cosy Critters (`cosycritters`) | Active | Spawns ambient moths, birds, and insects as client-side particles. Manifest `side = CLIENT`. |
| `emf_compat_better_combat_1.21.1_1.1.0.jar` | EMF Compat Better Combat (`emf_compat_better_combat`) | Active | Synchronizes Custom Entity Models with Better Combat attack motions. Manifest `side = CLIENT`. |
| `emf_compat_core-1.1.2.jar` | EMF Compat Core (`emf_compat_core`) | Active | Core compatibility layer for Entity Model Features. Manifest `side = CLIENT`. |
| `entity_model_features-3.2.4-1.21-neoforge.jar` | Entity Model Features (`entity_model_features`) | Active | OptiFine custom entity model format (.jem) parser and renderer. Manifest `side = CLIENT`. |
| `entity_texture_features_1.21-neoforge-7.1.jar` | Entity Texture Features (`entity_texture_features`) | Active | OptiFine emissive, random, and blinking entity textures. Manifest `side = CLIENT`. |
| `explosiveenhancement-neoforge-1.21.1-1.1.2.jar` | Explosive Enhancement (`explosiveenhancement`) | Active | Custom 2D animated explosion smoke and fireball particle sprites. Client-side only. |
| `fwa+1.21.1-neoforge-1.2.31.jar` | Fancy World Animations (`fwa`) | Active | Adds client-side opening animations to chests, shulker boxes, and bells. Pure client visual. |
| `lambdynamiclights-4.8.8+1.21.1.jar` | LambDynamicLights (`lambdynlights`) | Active | Real-time dynamic light levels calculated on client mesh for held/dropped light sources. |
| `Loot Beams Refork-neoforge-1.21.1-3.4.7.jar` | Loot Beams Refork (`lootbeams`) | Active | Renders 3D light beams above dropped items. Zero server logic; entrypoint is a no-op; all events hook `Dist.CLIENT`. |
| `Nirvana Lib-neoforge-1.21.1-2.2.0.jar` | Nirvana Lib (`nirvana_lib`) | Active | Dedicated client rendering helper library for Loot Beams Refork. Contains only client render type accessors. |
| `notenoughanimations-neoforge-1.12.3-mc1.21.1.jar` | Not Enough Animations (`notenoughanimations`) | Active | Third-person body animations for eating, drinking, boat rowing, and map holding. |
| `particle_core-0.3.3+1.21+neoforge.jar` | Particle Core (`particle_core`) | Active | Low-level client rendering framework for custom particle systems. Manifest `side = CLIENT`. |
| `particular-1.21.1-NeoForge-1.5.5.jar` | Particular (`particular`) | Active | Ambient biome particle effects (leaf flakes, dust, water drips). Client visual only. |
| `Perception-NEOFORGE-0.2.1+1.21.1.jar` | Perception (`perception`) | Active | Post-processing screen effects including vignette, speed lines, and motion blur. |
| `punchy-2.6.2-neoforge-1.21.1.jar` | Punchy (`punchy`) | Active | Weapon recoil screen impulse and punch impact animations. Manifest `side = CLIENT`. |
| `simplefog-neoforge-1.21.1-2.0.5.jar.disabled` | Simple Fog Control (`simplefog`) | Disabled | Fog density and start/end distance configuration menu. Manifest `side = CLIENT`. |
| `smoothchunk-1.21-4.1.jar.disabled` | Smooth Chunk (`smoothchunk`) | Disabled | Client-side opacity fade-in animation for newly meshed chunks. Pure client visual. |
| `visuality-forge-3.0.0.jar` | Visuality: Reforged (`visuality`) | Active | Client visual particles for entity actions (sparkles, splash, slime dripping). |

---

### 4. Client Camera, View & Input Controls (10 Mods)

Mods adjusting client perspective, mouse input capture, or raw input threading.

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `aero_cam_sync-1.3.1.jar` | Aero Cam Sync (`aero_cam_sync`) | Active | Synchronizes client camera yaw with rotating Create Aeronautics contraptions. |
| `BetterThirdPerson-neoforge-1.9.0.jar` | Better Third Person (`betterthirdperson`) | Active | Decouples camera rotation from player facing direction in third person. Client-side only. |
| `CameraOverhaul-v2.1.1-neoforge+mc[1.21-1.21.1].jar.disabled` | Camera Overhaul (`cameraoverhaul`) | Disabled | Adds first-person camera roll, tilting, and momentum physics. Client-side only. |
| `freecam-neoforge-1.3.0+mc1.21.jar` | Freecam (`freecam`) | Active | Client-side detached spectator camera for screenshots and observation. Manifest `side = CLIENT`. |
| `Ixeris-4.4.1+1.21.1-neoforge.jar` | Ixeris (`ixeris_dummy`) | Active | Dedicated client-side background input polling thread bypassing GLFW queue latency. |
| `minecraft-cursor-neoforge-3.11.3+1.21.1.jar` | Minecraft Cursor (`minecraft_cursor`) | Active | Replaces the operating system mouse cursor with pixel-styled Minecraft pointers. Manifest `side = CLIENT`. |
| `MouseTweaks-neoforge-mc1.21-2.26.1.jar` | Mouse Tweaks (`mousetweaks`) | Active | Adds RMB dragging and scroll wheel inventory item sorting in client container screens. |
| `nowheel-1.0.6+1.21.1neoforge.jar` | Nowheel (`nowheel`) | Active | Disables cycling hotbar slots using the mouse scroll wheel. Manifest `side = CLIENT`. |
| `smooth_steps-neoforge-1.1.0.jar` | Smooth Steps (`smooth_steps`) | Active | Interpolates client camera vertical offset when stepping onto slabs/stairs. Client camera only. |
| `smooththirdpersoncamera-26.05.28-mc1.21.1.jar.disabled` | Smooth Third Person Camera (`smooththirdpersoncamera`) | Disabled | Dampens and smooths third-person camera rotation tracking. Manifest `side = CLIENT`. |

---

### 5. Client HUD, Tooltips & GUI Enhancements (18 Mods)

In-game overlays, HUD indicators, tooltip styling, and keybind menus.

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `apothiccombat-1.2.1.jar` | Apothic Combat (`apothiccombat`) | Active | Pure client mixin into Better Combat's `WeaponAttributeTooltip` class to deduplicate tooltip reach lines. No server mechanics. |
| `catalogue-neoforge-1.21.1-1.11.2.jar` | Catalogue (`catalogue`) | Active | Replaces the in-game Mod List menu with a rich mod browser UI. Pure client GUI. |
| `clean_tooltips-1.1-neoforge-1.21.1.jar.disabled` | Clean Tooltips (`clean_tooltips`) | Disabled | Formats and hides redundant mod namespace tags on item tooltips. Pure client GUI. |
| `configured-neoforge-1.21.1-2.6.3.jar` | Configured (`configured`) | Active | Provides an in-game GUI configuration menu for editing mod configs. Dedicated servers have no GUI. |
| `Controlling-neoforge-1.21.1-19.0.5.jar` | Controlling (`controlling`) | Active | Adds a search bar and conflict filter to the Controls / Key Binds menu. Manifest `side = CLIENT`. |
| `enchdesc-neoforge-1.21.1-21.1.10.jar` | Enchantment Descriptions (`enchdesc`) | Active | Appends explanatory text descriptions to enchanted book tooltips. Pure client GUI. |
| `HealthBars-v21.1.0-1.21.1-NeoForge.jar` | Health Bars (`healthbars`) | Active | Displays stylized mob health bars above entity heads and on screen. Pure client rendering. |
| `healthbars-dd-compat-0.3.0+1.21.1.jar` | Health Bars - Deeper and Darker Compat (`healthbars_dd_compat`) | Active | Compatibility bridge for Health Bars on Deeper and Darker entities. Pure client rendering. |
| `ImmersiveUI-NEOFORGE-0.3.3+1.21.1.jar` | Immersive UI (`immersive_ui`) | Active | Overhauls health, food, armor, and mount HUD displays. Manifest `side = CLIENT`. |
| `LocatorBar-neoforge-1.2.2+1.21.1.jar` | Locator Bar (`locatorbar`) | Active | Skyrim-style compass navigation bar rendered across the top edge of the HUD. |
| `miningspeedtooltips-neoforge-1.0.0-1.21.1.jar` | Mining Speed Tooltips (`miningspeedtooltips`) | Active | Displays dynamic harvest speed stats on item hover boxes. Pure client GUI. |
| `NBTac-NEOFORGE-1.21.1-1.3.10.jar` | NBT Autocomplete (`nbt_ac`) | Active | Adds command line autocomplete suggestions for NBT tags in client chat. Client mixins only. |
| `Not Enough Recipe Book-NEOFORGE-0.4.3+1.21.jar` | Not Enough Recipe Book (`nerb`) | Active | Unlocks recipe book dimensions and UI tweaks in inventory crafting screens. |
| `OverflowingBars-v21.1.1-1.21.1-NeoForge.jar` | Overflowing Bars (`overflowingbars`) | Active | Stacks health and armor bars into tiered colored overlays when exceeding 20 points. |
| `Searchables-neoforge-1.21.1-1.0.2.jar` | Searchables (`searchables`) | Active | Helper search widget library used exclusively by Controlling and client menus. |
| `smoothswapping-0.9.3.2-1.21.1-neoforge.jar` | Smooth Swapping (`smoothswapping`) | Active | Visual slide animation when swapping items between hotbar slots. Pure client GUI. |
| `ToastControl-1.21.1-9.0.1.jar` | Toast Control (`toastcontrol`) | Active | Configurable popup blocker for advancement, tutorial, and recipe toast alerts. |
| `tooltipoverhaul-neoforge-1.21.1-1.5.1.jar` | Tooltip Overhaul (`tooltipoverhaul`) | Active | Customizable high-resolution tooltip frames and text rendering. Pure client GUI. |

---

### 6. Client JEI Addons (Purely Client-Side) (4 Mods)

JEI addons that only register display categories in the client JEI screen and have zero server network packets.

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `collapsible_groups-neoforge-1.21.1-1.4.2.jar` | Collapsible Recipe Groups (`collapsible_groups`) | Active | Folds redundant recipe variants into collapsible groups inside the client JEI window. |
| `jeed-1.21-2.3.3.jar` | Just Enough Effect Descriptions (`jeed`) | Active | Adds a JEI recipe category documenting status effects and potions. Pure client JEI plugin. |
| `JustEnoughBeacons-NeoForge-1.21-1.3.0.jar` | Just Enough Beacons (`just_enough_beacons`) | Active | Displays beacon pyramid block arrangements and valid payment items in JEI. Manifest `side = CLIENT`. |
| `JustEnoughProfessions-neoforge-1.21.1-4.0.5.jar` | Just Enough Professions (`justenoughprofessions`) | Active | Displays villager profession outfits and required workstation blocks in JEI. |

---

### 7. Client Audio & Sound Packs (2 Mods)

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `sounds-2.4.22+lts+1.21.1-neoforge.jar` | Sounds (`sounds`) | Active | Dynamic acoustic sound physics, reverb, room occlusion, and footsteps. Manifest `side = CLIENT`. |
| `towntalk-1.2.0.jar` | TownTalk (`towntalk`) | Active | 52.3 MB client sound pack registering `.ogg` spoken voice files for MineColonies citizens. Contains only client audio assets. |

---

### 8. Client Social & Crash Management (2 Mods)

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `CrashAssistant-neoforge-1.20.6-1.21.4-1.11.9.jar` | Crash Assistant (`crash_assistant`) | Active | Displays an interactive GUI upon game crash for log analysis and one-click uploading. Unneeded on headless servers. |
| `Essential_1-5-0-1_neoforge_1-21-1.jar` | Essential (`essential`) | Active | Social wardrobe, cosmetics, friend messaging, and singleplayer world sharing. Incompatible/unwanted on dedicated servers. |

---

### 9. Development & Diagnostic Tools (5 Files)

Tools used for modpack development, registry dumps, structure inspection, and leftover backup binaries.

| Filename | Mod Name (ID) | Status | Exclusion Rationale |
| :--- | :--- | :--- | :--- |
| `CraftTweaker-neoforge-1.21.1-21.0.38.jar` | CraftTweaker (`crafttweaker`) | Active | Scripting and registry dump tool (`/ct dump`). Modpack scripting is entirely handled by KubeJS. |
| `Panoptic-1.08a-NeoForge-1.21.1.jar` | Panoptic (`panoptic`) | Active | Developer tool for structure generation auditing and seed mapping. Unnecessary in production. |
| `wits-1.3.0+1.21-neoforge.jar` | WITS (`wits`) | Active | Developer utility for checking structure boundaries (`/wits`). Unnecessary in production. |
| `txnilib-neoforge-1.0.24-1.21.1.jar.backup` | TxniLib (Backup Copy) | Backup | Redundant copy of `txnilib-neoforge-1.0.24-1.21.1.jar`. Must never be deployed. |
| `txnilib-neoforge-1.0.24-1.21.1.jar.modified` | TxniLib (Modified Copy) | Modified | Redundant altered binary of TxniLib. Must never be deployed. |

---

## Critical Edge-Case Mods That MUST REMAIN on the Server

The following mods may appear to be client-side, visual, or performance-related, but **MUST NOT** be excluded from the dedicated server pack:

1. **Config Libraries:**
   - `cloth_config`: Depended on by `bettercombat`, `libertyvillagers`, `BuildingWands`, and `BOMD`.
   - `yet_another_config_lib_v3`: Depended on by `friendsandfoes`, `structurify`, `takesapillage`, `variantsandventures`, and `armoroftheages`.
   - `octolib`: Depended on by `relics` and all `reliquified_*` content addons.
   - `fzzy_config`: Depended on by `simplyswords` and `simplymore`.
   - `jupiter`: Required dependency of `iceandfire`.
   - `guideme`: Required dependency of `appliedenergistics2`.

2. **Network & Gameplay Synchronization:**
   - **Trade Cycling (`trade-cycling-neoforge-1.21.1-1.0.18.jar`):** Must stay on server. Contains `CycleTradesPacket` and server-side trade regeneration hooks on `MerchantMenu` and `Villager`.
   - **JEI (`jei-1.21.1-neoforge-19.43.0.393.jar`):** Must stay on server. Handles server recipe transfer packet packets (`RecipeTransferPacket`).
   - **Jade (`Jade-1.21.1-NeoForge-15.10.5.jar`):** Must stay on server. Synchronizes tile entity inventory, progress, and NBT data to clients.
   - **JEIWorldGen (`jeiworldgen-neoforge-1.21.1-1.4.1.jar`):** Must stay on server. Transmits server-side structure and chest loot tables via `LootInfoPayload`.
   - **Healight (`healight-neoforge-1.21.1-1.0.1.jar`):** Must stay on server. Registers `DATA_HEAL_TIME` on `LivingEntity` via `SynchedEntityData`; removing it from the server causes entity data ID mismatches.
   - **Heavier Weapons (`heavier_weapons-1.21.1-NeoForge-1.1.0.jar`):** Must stay on server. Emits server-to-client `HitstopPacket` across the network.
   - **EvoLoginTimeout (`EvoLoginTimeout-NeoForge-1.21.1-1.0.9.jar`):** Must stay on server. Prevents server handshake timeouts during heavy modpack client connections.
   - **NetherPortalFix (`netherportalfix-neoforge-1.21.1-21.1.1.jar`):** Must stay on server. Tracks portal coordinates on the server level.

3. **Server Performance & Diagnostic Optimizations:**
   - `modernfix`, `ferritecore`, `lithium`, `krypton_fnp`, `noisiumed`, `servercore`, `spark`, `letmedespawn`, `packetfixer`, `logprot`, `memguard`, `leaky`, `saturn` (if re-enabled).

4. **Special Note on Distant Horizons:**
   - `DistantHorizons-3.3.2-1.21.1-fabric-neoforge.jar` has an active server entrypoint and can run on dedicated servers to pre-generate and stream LOD data to clients. It is optional on the server, but not purely client-only.
