# PEAK Modpack: Performance Standards & Profiling Guidelines

This document details the exact performance rules, GC configurations, and optimization history for **PEAK** (1.21.1 NeoForge, 360+ mods). These metrics must guide all profiling reviews, config edits, and server audits.

---

## 1. JVM & Garbage Collector (G1GC) Tuning

PEAK runs much better with leaner memory allocations to avoid GC sweep overheads. Depending on the desired view distance, allocate between **6.3GB and ~7.0GB** of RAM. A base allocation of **6.3GB** (`MaxMemAlloc=6450`) is plenty for a 6-chunk render distance paired with a 32 LOD Distant Horizons rendering (LOD meshes reside off-heap).

### Crucial GC Rules (Preventing 1.1s Old Gen Pauses)
To prevent garbage collector freezes (stutters lasting >1 second), the following `instance.cfg` parameters must be preserved:
*   `MaxMemAlloc=6450` to `7168` (Tailored to active render needs).
*   `-XX:InitiatingHeapOccupancyPercent=25` (Triggers Old Gen collection early enough to prevent concurrent cycles from falling behind).
*   `-XX:G1HeapWastePercent=10` (Allows minor fragmentation to prevent G1 from locking the main thread seeking absolute optimization).
*   `-XX:G1MixedGCCountTarget=8` (Spreads Old Gen recycles across 8 smaller passes, smoothing CPU distribution).

---

## 2. WorldGen & Entity Optimizations

Every tick count counts. The following critical mod bounds have been established through exhaustive Spark profiling:

### Valkyrien Skies Physics (Sable)
*   **Problem:** Sable passively scanned for ships 128 blocks away, consuming up to 28% of the Server Thread.
*   **Standard (`sable-common.toml`):**
    *   `sub_level_tracking_range = 64.0` (Do not increase to 128).
    *   `sub_level_splitting_heatmap_steps = 20`.

### Ice and Fire (Dragons AI)
*   **Problem:** Dragon targeting AI was scanning a massive 128-block radius, spiking CPU by 14% on chunk loads.
*   **Standard (`iaf-common.json`):**
    *   `targetSearchLength = 64` (Limits AI scan radius to 4 chunks).

### ServerCore Ticking & Mob Caps
*   **Activation Range:** Must remain `enabled: true`. This prevents far-off mobs from executing tick logic.
*   **Monster Cap:** Hard-capped at `50` in the Nether to prevent Blaze/Strider overpopulation (which once peaked at 116 Blazes and 106 Striders in a single active Nether area).
*   **Spawn Interval:** Increased to `400` (20 seconds) for passive mobs (`AMBIENT`, `WATER_CREATURE`, etc.).

### Mimic Optimization (Artifacts)
*   **Standard (`lootr_liason-common.toml`):**
    *   `mimic_roll_timing = "first_interact"` (Never roll mimics on chunk loading; only calculate on right-click to prevent micro-stutters during exploration).

---

## 3. Crash Mitigation & Stability Rules

### Integrated Server Watchdog (ModernFix)
*   **Rule:** `mixin.feature.integrated_server_watchdog=false` in `modernfix-mixins.properties`.
*   **Why:** Generating high-speed terrain or executing teleports (>20,000 blocks) under a heavy 360-modpack can legitimately take up to 40 seconds. We bypass the watchdog to prevent the JVM from killing a perfectly healthy server during intense flight tests.

### C2ME Async Scheduling & Gateway Deadlocks
*   **Rule:** Prevent Gateway loading deadlocks by keeping these `c2me.toml` properties active:
    1.  `useLegacyScheduling = false` (Stops nested cascading chunk requests).
    2.  `syncPlayerTickets = false` (Moves player tickets off the Main Server thread).
    3.  `delayFullChunkEvents = false`.
*   **Executors:** Set `globalExecutorParallelism = 4` to assign 4 dedicated CPU cores to chunk gen.

### Network Packets (Krypton)
*   **Rule:** Habilitar `permitOversizedPackets: true` in `krypton_fnp.yaml` to prevent immediate connection drops when loading giant NBT metadata (e.g. Sophisticated Backpacks or heavy magic mods).
