# PEAK Modpack: KubeJS & Custom Script Registry

This file documents the development guidelines, coding standards, and existing custom scripts utilized in the **PEAK** modpack (NeoForge 1.21.1, Mojang Official Mappings).

---

## 📜 KubeJS 6/21+ Scripting Standards

To maintain absolute code stability under Minecraft 1.21.1 (NeoForge) and Mojmap, all script changes must adhere to the following rules:

### 1. Modern Event Architecture
Do **not** use deprecated legacy `onEvent('name', event => {})` blocks. Always use modern direct class event handlers:
- **Server Scripts (`server_scripts/`):** `ServerEvents.recipes(event => {})`, `ServerEvents.tags('item', event => {})`, `ItemEvents.crafted(event => {})`
- **Startup Scripts (`startup_scripts/`):** `StartupEvents.registry('item', event => {})`

### 2. High-Performance Guard Clauses
High-frequency events like `ItemEvents.crafted` fire for every single item crafted in the game (torches, sticks, blocks, etc.). To prevent catastrophic MSPT lag:
- **Rule:** Exit immediately using `return` at the very beginning of the script if the target item ID does not match your specific custom item.
```javascript
ItemEvents.crafted(event => {
    if (event.item.id !== 'kubejs:boss_duplicator') return; // Guard clause!
    // Heavy execution follows
});
```

### 3. Data Components API (Minecraft 1.21.1 Component Revolution)
Minecraft 1.21 replaced the traditional item NBT dictionary with structured Data Components. Calling `.withNBT()` or direct `nbt` edits will fail.
- **Rule:** Modify items using `.withComponents(...)` and official namespaced keys.
```javascript
event.shaped(
    Item.of('minecraft:diamond_sword').withComponents({
        'minecraft:custom_name': '"§bEldritch Blade§r"',
        'minecraft:lore': ['"§7Forged in PEAK.§r"'],
        'minecraft:enchantments': { levels: { 'minecraft:sharpness': 6 } },
        'minecraft:unbreakable': {} // Empty JSON object sets tag to true
    }),
    [' D ', ' D ', ' S '], { D: 'minecraft:diamond', S: 'minecraft:stick' }
);
```

### 4. Safe Biome Checks (The Holder `Either` wrapper)
Under NeoForge 1.21.1, level biome queries return a Holder structure wrapped in an `Either` instance. Reading `.unwrap().key()` directly causes silent crashes or logs full of exception spam in certain biomes (like dripstone caves).
- **Rule:** Use a safe double-wrapped check to extract the location string safely:
```javascript
function getBiomeId(level, blockPos) {
    let biomeHolder = level.getBiome(blockPos);
    let biomeKey = null;
    if (biomeHolder.unwrapKey().isPresent()) {
        biomeKey = biomeHolder.unwrapKey().get().location();
    } else if (biomeHolder.unwrap().left().isPresent()) {
        biomeKey = biomeHolder.unwrap().left().get().location();
    }
    return biomeKey ? biomeKey.toString() : "minecraft:plains";
}
```

---

## 📂 Registered Custom Scripts

The modpack currently contains the following custom scripts designed to optimize performance and prevent crashes:

### 1. `minecraft/local/kubejs/server_scripts/18_boss_duplicator.js`
- **Purpose:** Optimizes the `ItemEvents.crafted` listener for the custom Boss Duplicator item.
- **Tweak:** Added high-performance guard clauses to prevent looping through players' inventories on standard crafts.

### 2. `minecraft/local/kubejs/server_scripts/19_mob_gear.js`
- **Purpose:** Manages custom mob equipment spawns across specific biomes.
- **Tweak:** Fixed the biome extraction parser using the safe Holder `Either` unwrap mechanism, removing dripstone cave biome crashes.

### 3. `minecraft/local/kubejs/startup_scripts/fix_malum_watchdog.js`
- **Purpose:** Prevents severe main server thread deadlocks triggered by Malum's Weeping Well ticking searches.
- **Tweak:** Dynamically desubscribes Malum's Weeping Well `RuntimeEvents` from the NeoForge `EVENT_BUS` upon startup. Bypasses síncrono `getChunk` queries, preventing Watchdog server termination.
