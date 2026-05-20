# PEAK Modpack: 1.21.1 NeoForge KubeJS Standards & Mappings

This document serves as the absolute "source of truth" for writing KubeJS scripts in Minecraft 1.21.1 (NeoForge) under **Mojmap** (Mojang Official Mappings).

---

## 1. Modern Event Architecture (No `onEvent`)

In KubeJS 6/21+ (Minecraft 1.21.1), the old `onEvent('event_name', event => {})` structure is fully deprecated. You must use the direct event class listeners.

### Server Scripts (`kubejs/server_scripts/`)
```javascript
// Recipe modifications
ServerEvents.recipes(event => {
    // Recipe logic here
});

// Tag additions
ServerEvents.tags('item', event => {
    // Tag logic here
});

// High-frequency item events
ItemEvents.crafted(event => {
    // Early exit guard clauses are MANDATORY here
});
```

### Startup Scripts (`kubejs/startup_scripts/`)
```javascript
// Registering blocks or items
StartupEvents.registry('item', event => {
    // Item registration
});

StartupEvents.registry('block', event => {
    // Block registration
});
```

---

## 2. The 1.21.1 Data Components Revolution

Minecraft 1.21 replaced traditional item NBT tags (e.g. `Damage`, `display.Name`, `Enchantments`) with **Data Components**. 

> [!WARNING]
> Calls to `.withNBT()` or modifying the `nbt` property of an Item Stack are obsolete and will cause scripting errors or silent failures. You must use the Component APIs.

### Modern Component Syntax in KubeJS
When generating customized items, use `.withComponents(...)` with the official namespaced component keys:

```javascript
// Registering a recipe that outputs a highly custom sword
event.shaped(
    Item.of('minecraft:diamond_sword').withComponents({
        // Custom Display Name (must be a JSON component string)
        'minecraft:custom_name': '"§bEldritch Blade§r"',
        
        // Lore (Array of JSON component strings)
        'minecraft:lore': [
            '"§7Forged in the deepest dungeons of PEAK.§r"',
            '"§8A high-frequency vibration cuts anything.§r"'
        ],
        
        // Enchantments (levels object map)
        'minecraft:enchantments': {
            levels: {
                'minecraft:sharpness': 6,
                'minecraft:unbreaking': 3
            }
        },
        
        // Unbreakable flag (empty JSON object means true)
        'minecraft:unbreakable': {},
        
        // Custom model data
        'minecraft:custom_model_data': 1205
    }),
    [
        ' D ',
        ' D ',
        ' S '
    ], {
        D: 'minecraft:diamond',
        S: 'minecraft:stick'
    }
);
```

---

## 3. High-Performance Guard Clauses

Listeners like `ItemEvents.crafted` or `EntityEvents.spawned` fire continuously for every single event on the server. To avoid MSPT spikes:
1. **Always check the target ID first.**
2. **Exit immediately (return)** if the event does not involve the specific custom modpack item.

### Correct Pattern (High Performance)
```javascript
ItemEvents.crafted(event => {
    // Guard clause! If it's not our boss duplicator or custom item, EXIT IMMEDIATELY.
    if (event.item.id !== 'kubejs:boss_duplicator') return;

    // Heavy CPU/inventory logic ONLY runs for this specific item
    let player = event.player;
    player.tell("You have crafted the Boss Duplicator!");
});
```

### Incorrect Pattern (Causes Severe Ticking Lag)
```javascript
ItemEvents.crafted(event => {
    // BAD: Scans inventory / runs heavy logic for EVERY SINGLE item crafted (torches, slabs, etc.)
    let player = event.player;
    let hasMaterial = player.inventory.find('kubejs:boss_core'); 
    if (event.item.id === 'kubejs:boss_duplicator') {
        // ...
    }
});
```

---

## 4. NeoForge Biome Parsing (The `Either` Wrapper)

In NeoForge 1.21.1, biome data returned by the level uses a Holder architecture wrapped in an `Either` structure. Trying to read `.unwrap().key()` directly will crash when spawning in certain biomes (like dripstone caves).

### Safe Biome Extraction in KubeJS
Always use this robust parsing logic to extract the `ResourceLocation` key:

```javascript
function getBiomeId(level, blockPos) {
    let biomeHolder = level.getBiome(blockPos);
    let biomeKey = null;
    
    // Check Holder.Reference unwrap key
    if (biomeHolder.unwrapKey().isPresent()) {
        biomeKey = biomeHolder.unwrapKey().get().location();
    } 
    // Check Holder.Direct unwrap left
    else if (biomeHolder.unwrap().left().isPresent()) {
        biomeKey = biomeHolder.unwrap().left().get().location();
    }
    
    return biomeKey ? biomeKey.toString() : "minecraft:plains";
}
```
