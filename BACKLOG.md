# PEAK Modpack - Development Backlog

## Core Design Philosophy: "Freedom Without Looseness" (Expert-Kitchen Sink)
- **Modpack Identity:** PEAK is an **Expert-Kitchen Sink** hybrid modpack.
- **Guiding Pillar:** Freedom without aimless looseness. Players must clearly feel a path ahead and understand their progression milestones, while retaining the freedom, agency, and creative flexibility to approach objectives through multiple viable disciplines (Tech, Magic, Exploration, Alchemy, Automation).
- **Quest & Progression Design Rule:** Quests provide a structured spine and milestones (guiding the player forward), but must never bottleneck the entire experience into a single hyper-linear choke point. Parallel pathways and creative problem solving must always be supported.

## Pending Investigations & Bug Fixes

### 1. Sable Physics Structures & Iron's Spells Teleportation Deadlock / Hang
- **Issue:** Using Iron's Spells 'n Spellbooks teleportation spells (Teleport, Portal, Recall, Blood Step, Frost Step, etc.) causes a server thread freeze / deadlock in two scenarios:
  1. Teleporting **away from or while mounted / attached** to a Sable physics structure via a steering handle (`sable`, `sabledestructive`, `sable_player_ragdoll`).
  2. Teleporting **directly onto or into** an active Sable physics structure / sub-level.
- **Context & Symptoms:**
  - The server thread deadlocks during entity coordinate and sublevel transform synchronization between Minecraft's world space and Sable's physics sublevel container.
  - No crash stacktrace is generated because the server thread hangs waiting on physics mutex locks / sublevel chunk references.
- **Action Items for Future Investigation:**
  - Investigate event listeners for player teleportation (`EntityTeleportEvent`, `PlayerTeleportEvent`).
  - Implement a safety check / dismount handler: force-release steering handles and validate destination coordinates (e.g. transform physics-space coordinates to world-space if targeting a ship).
  - Review `sable-common.toml` / `sabledestructive` configs for teleportation and detached sublevel safeguards.

---

### 2. Magic & QoL Tech/Dimension Gate Purge
- **Target Items:**
  - `ars_nouveau:scribes_table`
  - `ars_nouveau:enchanting_apparatus`
  - `irons_spellbooks:uncommon_ink`
  - `malum:spirit_crucible`
  - `wands:diamond_wand`
- **Objective:** Strip arbitrary `twilightforest:ironwood_ingot` and `create:precision_mechanism` requirements from pure magic workstations and basic QoL building tools to prevent arbitrary dimension/tech locking on magic progression.

---

### 3. Traveler's Compass Integration & Create Rail Grinding
- **Objective:** Complete balanced recipe integrations for Traveler's Compass and automated rail grinding mechanics in Create.

---

### 4. Space Exploration Architecture (Northstar Redux)
- **Selected Mods:** `Northstar-0.6.6+1.21.1.jar` and `mek_x_star-1.21.1-1.2.0.jar`.
- **Progression Sequence:** Earth ➔ Mars ➔ Venus.
- **Boss / Ender Eye Rule:** No Ender Eye is gated behind space travel since Northstar does not feature dedicated boss entities (Eyes are strictly reserved for boss kills). Space travel gates late-game industrial metals and catalysts instead.
- **Mars (First Space Milestone):** Focuses on kinetic rocket construction, fuel pipelines (TFMG Kerosene/LOX vs Mekanism H2/O2), raiding abandoned Martian Bases (`martian_base`), and smelting **Martian Steel** (`martian_steel_ingot`).
- **Venus (Deferred Content):** High-hazard world (acid rain, heat, pressure). Deep exclusive content, custom mob drops, and subterranean structures deferred for a later dedicated development cycle.

---

### 5. Atmospherics Sky Hijack & Northstar Orbit Skybox Incompatibility
- **Issue:** Atmospherics (`atmospherics-2.6.5-mc-1.21.1.jar`) overrides the Minecraft sky rendering pipeline, preventing Northstar (`Northstar-0.6.6+1.21.1.jar`) from rendering orbit skyboxes, solar system planets, moons, and multi-layered starfields.
- **Root Cause Analysis:**
  - Atmospherics' mixin `com.beash.atmospherics.mixin.WorldRendererSkyMixin` injects at `HEAD` of `LevelRenderer.renderSky()`.
  - When `level.effects().skyType() == DimensionSpecialEffects.SkyType.NORMAL` (which Northstar's `SpaceEffects` uses for orbit and planet dimensions), Atmospherics unconditionally invokes `CallbackInfo.cancel()`.
  - This cancels `LevelRenderer.renderSky()` before Northstar's injection `northstar$onRenderSky` (`SpaceEffects.renderPlanetsAndStars`) is ever reached.
  - In-game config toggles (via the B menu) only toggle whether Atmospherics draws its own sub-elements (stars, haze); they do not bypass the unconditional `ci.cancel()`.
- **Future Resolution Paths:**
  - Explore upstream mod compatibility updates or official dimension exclusion settings in future Atmospherics releases.
  - Implement a dedicated bridge/compat mixin to gate `WorldRendererSkyMixin` when inside Northstar space/orbit dimensions (`effects instanceof SpaceEffects`).
  - Or evaluate alternative atmosphere/fog mods that do not cancel `renderSky`.


