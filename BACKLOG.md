# PEAK Modpack - Development Backlog

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
