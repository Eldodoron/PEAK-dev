# PEAK Modpack: Performance & Optimization Registry

This document registers the active performance configurations and JVM optimizations implemented in the **PEAK** modpack (NeoForge 1.21.1, 360+ mods). These settings are crucial for maintaining steady 20 TPS server ticks and 60+ FPS client rendering.

---

## 💻 JVM & Garbage Collector (G1GC) Tuning

Due to off-heap memory mapping utilized by mods like **Distant Horizons** (LOD chunk rendering), assigning excessive memory actually decreases performance by magnifying Garbage Collection sweeps. 

### Recommended JVM Allocations:
- **Base Memory Allocation:** **6.3 GB to 7.0 GB** maximum (`-Xmx6450m` to `-Xmx7168m`).
- **Standard Allocation (`instance.cfg`):** `MaxMemAlloc=6816` (6.8 GB).
- *Warning:* For systems with 16 GB of physical RAM, allocating more than 7 GB forces Minecraft into swap file paging, which results in devastating multi-second game freezes.

### ⚠️ Critical Prism Launcher Overwrite Behavior:
Prism Launcher **overwrites the `instance.cfg` file on every single startup**. Any edits to JVM arguments or memory allocation within the code are discarded. 
To apply these changes, you **must apply them manually in the Prism Launcher UI**:
1. Open **Prism Launcher**.
2. Right-click the **PEAK-dev** instance and select **Edit**.
3. Navigate to **Settings** -> **Java** (check "Java Settings" to override globally).
4. Set **Maximum memory allocation** to `6816 MB` (or similar between `6450` and `7168`).
5. Copy and paste the optimized G1GC parameters in **JVM Arguments**.

### Optimized G1GC Parameters:
```text
-XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=10 -XX:G1MixedGCCountTarget=8 -XX:InitiatingHeapOccupancyPercent=25 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1
```
*   **`-XX:InitiatingHeapOccupancyPercent=25`**: Kicks off garbage sweeping early in the background to prevent Old Gen heaps from clogging.
*   **`-XX:G1HeapWastePercent=10`**: Tolerates minor fragmentation, saving significant ticking pauses.
*   **`-XX:G1MixedGCCountTarget=8`**: Splits heavy Old Gen reclamation pauses into 8 lightweight increments to eliminate micro-stutters.

---

## 🛠️ Active Config Optimizations

### 1. ModernFix Optimization (`config/modernfix-mixins.properties`)
- **`mixin.perf.dynamic_languages=false`** (or removed): **CRITICAL.** If enabled (`true`), NeoForge 1.21.1 will crash instantly on boot.
- **`mixin.bugfix.skip_redundant_saves=true`**: Eliminates unnecessary chunk disk saves during gameplay, reducing auto-save stutters on SSDs.
- **`mixin.feature.integrated_server_watchdog=false`**: Disables the aggressive watchdog that terminates the internal server when terrain generation takes longer than 40 seconds during high-distance teleports.

### 2. C2ME Multi-threaded Chunk Loading (`config/c2me.toml`)
Prevents gateway/portal deadlocks during dimension shifts (circular `TIMED_WAITING` locks).
- **`useLegacyScheduling = false`**: Bypasses cascading síncrono queries.
- **`syncPlayerTickets = false`**: Decouples player coordinates from the main server thread, shifting chunk queues to worker hilos.
- **`globalExecutorParallelism = 4`**: Assigns 4 dedicated CPU cores to active chunk loading and generation.

### 3. ServerCore Dynamic Ticking (`config/servercore/`)
- **`fast-biome-lookups: true`**: Accelerates spawner location calculations.
- **`cancel-duplicate-fluid-ticks: true`**: Cancels redundant fluid double-ticks.
- **`lobotomize-villagers: enabled: true`**: Lobotomizes trapped villagers (e.g. 1x1 trading cells) to skip heavy pathfinding queries, keeping trades intact.
- **`spawn-interval`**: Increased to `400` (20 seconds) for ambient, passive, and water creatures.

### 4. Valkyrien Skies Physics (`config/sable-common.toml`)
- **`sub_level_tracking_range = 64.0`**: Prevents physics containers from passively searching for airships 128 blocks away (saves up to 20% CPU ticking cost).
- **`sub_level_splitting_heatmap_steps = 20`**.

### 5. Ice and Fire Dragons (`config/iceandfire/iaf-common.json`)
- **`targetSearchLength = 64`**: Restricts the massive dragon AI targeting radar to 4 chunks, completely removing chunk-load stutters.

### 6. Nether Exploration Loop (`saves/World 2/datapacks/peak_optimizations/`)
- Intercepts datapack loops executing high-frequency queries.
- **`boss_rifts_extended_compat:tick.mcfunction`**: Purged 5 recursive `@e` entity selector checks; rescheduled key ticks from **12 ticks (0.6s) to 60 ticks (3s)**.
- **`nova_structures:tick`**: Rescheduled structural ticking from **5 ticks (0.25s) to 40 ticks (2.0s)**.
- *Result:* Reduced Nether datapack ticking load from **53.4% CPU** to **under 2% CPU**.

### 7. Nether Entity Spawn Weights (`config/alexsmobs-common.toml`)
To resolve client-side FPS lag caused by high Nether entity densities, the spawn rates for the heaviest Alex's Mobs have been tuned down:
- **`warpedToadSpawnWeight`**: Reduced from **`30` to `12`**
- **`straddlerSpawnWeight`**: Reduced from **`70` to `25`**
- **`laviathanSpawnWeight`**: Reduced from **`15` to `6`**

### 8. Targeted Nether Particle Throttling (`config/particle_core_config.toml`)
Rather than reducing the global Minecraft particle quality setting, the **Particle Core** mod was configured to selectively throttle the exact heavy particle effects that flood the Nether:
- **`minecraft:flame`**, **`minecraft:smoke`**, **`minecraft:large_smoke`**: Capped to **10% spawn rate** (mitigates Blaze particle storms).
- **`minecraft:ash`**, **`minecraft:white_ash`**: Capped to **5% spawn rate** (optimizes Basalt Deltas rendering).
- **`minecraft:crimson_spore`**, **`minecraft:warped_spore`**: Capped to **10% spawn rate** (optimizes Nether forests rendering).

### 9. Lootr Container Ticking (`config/lootr-common.toml`)
To eliminate the heavy ticking overhead of Lootr chest block entities, active background ticking has been disabled:
- **`perform_decay_while_ticking`**: Set to `false`
- **`perform_refresh_while_ticking`**: Set to `false`
- **`start_refresh_while_ticking`**: Set to `false`
*Result:* This completely removes Lootr container ticks from the level tick cycle. Container decay and refresh checks are now processed exclusively when players interact with them (e.g. opening the container). This has zero effect on gameplay but saves ~16% of server CPU ticking time.

### 10. Mowzie's Mobs Spawn Tunings (`config/mowziesmobs-common.toml`)
To prevent jungles and loaded Overworld chunks from being congested with complex entities, the spawn rates for heavy Mowzie's Mobs have been tuned down:
- **Foliaath (`spawn_rate`)**: Reduced from **`70` to `15`**
- **Naga (`spawn_rate`)**: Reduced from **`20` to `6`**

### 11. Vampirism Native Spawn Limiting (`config/servercore/config.yml`)
To prevent runaway pathfinding calculations from heavy vampire entity densities in loaded chunks, we leverage ServerCore's custom spawn categories to restrict spawning frequency and cap maximum counts natively:
- **`VAMPIRISM_HUNTER`**: `mobcap` reduced from `15` to `8`, `spawn-interval` increased from `1` (every tick) to `15` ticks.
- **`VAMPIRISM_VAMPIRE`**: `mobcap` reduced from `30` to `12`, `spawn-interval` increased from `1` (every tick) to `15` ticks.
*Result:* Drastically reduces the server CPU overhead spent checking for vampire spawns (15x check-rate improvement) and keeps entity density tightly controlled natively.

### 12. Ice and Fire Pixie Optimization (Multi-layered)
Profile `8A6WsMMiBM` revealed **51 `iceandfire:pixie`** entities loaded simultaneously — causing flying AI overhead and dense particle emission every tick. Two complementary changes were applied:

**a) Spawn Rate Control (`kubejs/server_scripts/24_pixie_spawn_limiter.js`)**
- A KubeJS `EntityEvents.spawned` handler cancels **45% of brand new pixie spawns** on the server.
- **Robustness Fix:** The script uses `entity.persistentData` to check if a pixie has already been processed. This prevents the script from accidentally canceling/deleting existing saved pixies when chunks load or reload from disk, making it 100% safe.
- Target: Keep peak density around ~28 pixies in loaded chunks.

**b) Particle Throttling via Particle Core (`config/particle_core_config.toml`)**
- Instead of using the native mod config which affects rendering scale, the particle emissions were optimized directly through **Particle Core**.
- Added `"iceandfire:pixie_dust" = 0.3` which restricts pixie flying particles to only **30% spawn rate**.
- Result: 70% reduction in client-side pixie particle rendering load, while keeping the native pixie size/model at its default value of `5` (as requested).

*Combined result:* Safe server-side spawn limits keep pixie populations controlled, and Particle Core throttles their particle emission, improving both server TPS and client-side FPS without changing visual models.

### 13. Multi-threaded Pathfinding for Alex's Mobs & Caves
To prevent pathfinding calculations for large, complex entities from choking the main server thread, we leveraged multi-threaded pathfinding:
- **Alex's Caves (`config/alexscaves-general.toml`)**: Increased `pathfinding_threads` from `5` to `8`.
- **Alex's Mobs (`config/alexsmobs-common.toml`)**: Increased `pathfindingThreads` from `5` to `8`.
*Result:* Mobs can calculate paths using up to 8 parallel CPU cores, significantly lowering the impact of entity AI on TPS during chunk exploration.

