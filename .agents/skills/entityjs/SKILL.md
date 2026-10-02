---
name: entityjs
description: Bytecode-verified guide and reference for EntityJS 1.5.0 on Minecraft 1.21.1 NeoForge. Covers entity registration, GeckoLib model/texture/layer binding, AI goal selectors, target goals, and lifecycle combat hooks.
---

# EntityJS 1.5.0 Reference Guide (Minecraft 1.21.1 NeoForge)

EntityJS allows creating custom entities via KubeJS without bytecode hacks or overriding vanilla entity behaviors.

---

## 1. Startup Entity Registration

Register entities in `startup_scripts/` under `StartupEvents.registry('entity_type', event => { ... })`.

```javascript
StartupEvents.registry('entity_type', event => {
    event.create('kubejs:vampillager', 'entityjs:mob')
        .sized(0.5, 1.45) // Width and height in blocks
        // Attributes
        .modifyAttribute('minecraft:generic.max_health', 30.0)
        .modifyAttribute('minecraft:generic.movement_speed', 0.35)
        .modifyAttribute('minecraft:generic.attack_damage', 5.0)
        .modifyAttribute('minecraft:generic.follow_range', 32.0)
        // GeckoLib Model & Textures
        .modelResource(e => 'kubejs:geo/entity/vindicator.geo.json')
        .textureResource(e => 'kubejs:textures/entity/vampillager.png')
        // Emissive Eye Layer
        .newGlowingGeoLayer(layer => {
            layer.textureResource(e => 'kubejs:textures/entity/vampillager_glow.png')
        })
        // Sound Hooks (Bytecode-verified exact method names)
        .setAmbientSound('minecraft:entity.vindicator.ambient')
        .setDeathSound('minecraft:entity.vindicator.death')
        .setHurtSound(ctx => 'minecraft:entity.vindicator.hurt')
        // Combat & Lifecycle Hooks
        .aiStep(entity => {
            // Sunlight combustion check
            if (!entity.level.isClientSide() && entity.level.isDay()) {
                let brightness = entity.getLightLevelDependentMagicValue()
                if (brightness > 0.5 && entity.level.canSeeSky(entity.blockPosition())) {
                    if (entity.getHeadArmorItem().isEmpty()) {
                        entity.igniteForSeconds(8)
                    }
                }
            }
        })
        .onHurtTarget(ctx => {
            // ctx.entity = attacker (self), ctx.targetEntity = victim
            let self = ctx.entity
            let target = ctx.targetEntity
            if (target && !self.level.isClientSide()) {
                // Example: Bite heal
                self.heal(2.0)
            }
        })
        .onHurt(ctx => {
            // Triggered when entity takes damage
        })
        .onDeath(ctx => {
            // Triggered on mob death
        })
        .dropCustomDeathLoot(ctx => {
            // Add custom drop items directly
        })
})
```

---

## 2. Server AI Goal Selectors & Target Goals

EntityJS separates action goals and target selectors into two distinct server events:

### A. Action Goals: `EntityJSEvents.addGoalSelectors`
```javascript
EntityJSEvents.addGoalSelectors('kubejs:vampillager', event => {
    let Player = Java.loadClass('net.minecraft.world.entity.player.Player')

    // Priority 0: Float in water
    event.floatSwim(0)

    // Priority 1: Avoid direct sun exposure
    event.restrictSun(1)
    event.fleeSun(1, 1.25)

    // Priority 2: Pounce / Leap at target
    event.leapAtTarget(2, 0.45)

    // Priority 3: Melee attack
    event.meleeAttack(3, 1.25, false)

    // Priority 4: Stroll and look around
    event.waterAvoidingRandomStroll(4, 0.9, 0.001)
    event.lookAtEntity(5, Player, 8.0, 0.02, false)
    event.randomLookAround(6)
})
```

### B. Target Selectors: `EntityJSEvents.addGoals`
```javascript
EntityJSEvents.addGoals('kubejs:vampillager', event => {
    let Player = Java.loadClass('net.minecraft.world.entity.player.Player')
    let Villager = Java.loadClass('net.minecraft.world.entity.npc.Villager')
    let IronGolem = Java.loadClass('net.minecraft.world.entity.animal.IronGolem')

    // Retaliate against attackers (hurtByTarget: priority, toIgnoreDamage, alertSameType, toIgnoreAlert)
    event.hurtByTarget(1, [], true, [])

    // Aggro on Players and Villagers (priority, class, checkInterval, mustSee, mustReach, predicate)
    event.nearestAttackableTarget(2, Player, 10, true, false, null)
    event.nearestAttackableTarget(3, Villager, 10, true, false, null)
    event.nearestAttackableTarget(4, IronGolem, 20, false, false, null)
})
```


---

## 3. Important Invariants & Pitfalls

1. **Strict Lifecycle Separation:** `startup_scripts/` is ONLY for static registrations (entity types, dimensions, attributes, GeckoLib assets, basic sounds). Dynamic combat state machines, phase changes, abilities, and fleeing AI MUST live in `server_scripts/` so they can be reloaded live via `/kubejs reload server_scripts`.
2. **DamageSource Bean Properties:** In KubeJS 1.21 NeoForge / Rhino, NEVER call `source.getEntity()`. Use `source.actual || source.entity || source.player`. Calling non-existent getters throws unhandled TypeErrors that abort event handlers.
3. **Untargeted Hurt Events:** `EntityEvents.afterHurt` and `EntityEvents.beforeHurt` do NOT accept entity type arguments. Always use untargeted `EntityEvents.afterHurt(event => { if (event.entity?.type !== 'modid:name') return; ... })`.
4. **Helmet Slot Check:** Always use `entity.getHeadArmorItem().isEmpty()`. Never use string-based slot lookups like `getEquipment('head')`.
5. **Method Names:** Use `setAmbientSound`, `setDeathSound`, and `setHurtSound(ctx => ...)`. Do not use `ambientSound`.
6. **Geo Model Location:** Models live in `kubejs/assets/<namespace>/geo/` and textures in `kubejs/assets/<namespace>/textures/`.
7. **No Ad-Hoc Paxi Zips:** Keep all custom entity resources inside `minecraft/kubejs/assets/`.
8. **Animation Predicate Return Value:** In `addAnimationController`, `IAnimationPredicateJS.test(event)` expects a primitive `boolean`. Never write `return event.thenLoop(...)` (which returns `PlayState.CONTINUE`). Instead, call `event.thenLoop(...)` as a statement and explicitly `return true`.

---

## 4. Multi-Layer Engine Fail-Safes for Enrage / Phase Shifts

Never rely solely on `EntityEvents.afterHurt` to switch entity phases. Modded damage, shield blocks, and projectile mechanics can bypass single event listeners. Implement a 4-layer engine check in the 5-tick `ServerEvents.tick` loop:

```javascript
// ServerEvents.tick loop (every 5 ticks)
let currentHp = entity.health;
let lastHp = pData.getDouble('lastHealth');
if (lastHp > 0 && currentHp < lastHp - 0.01) {
    triggerAggro(entity, tickCount, pData, entity.lastHurtByMob);
    isAggro = true;
}
pData.putDouble('lastHealth', currentHp);

let hurtTimestamp = entity.lastHurtByMobTimestamp;
let lastObsHurt = pData.getInt('lastObsHurt');
if (hurtTimestamp > 0 && hurtTimestamp !== lastObsHurt) {
    pData.putInt('lastObsHurt', hurtTimestamp);
    triggerAggro(entity, tickCount, pData, entity.lastHurtByMob);
    isAggro = true;
}

if (entity.hurtTime > 0 && !isAggro) {
    triggerAggro(entity, tickCount, pData, entity.lastHurtByMob);
    isAggro = true;
}
```

---

## 5. Dynamic Pursuit Evasion & Continuous Fleeing Pattern

Hit-and-run mobs must never stop at a fixed coordinate if the player is in active pursuit. Dynamically check player distance and line of sight:

```javascript
// Active disengage: Continuously flee and evade during cooldown
if (!isAggro && fleeUntil > 0 && tickCount < fleeUntil) {
    let nearestPlayer = level.getNearestPlayer(entity, 32.0);
    if (nearestPlayer && nearestPlayer.isAlive()) {
        let pEyeY = nearestPlayer.y + nearestPlayer.eyeHeight;
        let fdx = entity.x - nearestPlayer.x;
        let fdz = entity.z - nearestPlayer.z;
        let pDist = Math.sqrt(fdx * fdx + fdz * fdz) || 1;

        let playerCanSeeMob = !hasBlockObstruction(level, nearestPlayer.x, pEyeY, nearestPlayer.z, entity.x, entity.y + entity.eyeHeight, entity.z);

        // Keep running if exposed, player is close, or destination reached while player still nearby
        let needsNewDestination = !hasCover || (pDist < 12.0) || (playerCanSeeMob && pDist < 18.0) || (distToCover <= 2.0 && pDist < 14.0);

        if (needsNewDestination) {
            // Calculate new evasion point away from player behind solid blocks
            // ...
        }

        // Lurk ONLY when fully covered, hidden from sight, and at a safe distance (> 14 blocks)
        if (distToCover <= 1.5 && !playerCanSeeMob && pDist >= 14.0) {
            entity.setTarget(null);
            entity.navigation.stop();
            return;
        } else {
            entity.setTarget(null);
            entity.navigation.moveTo(coverX, coverY, coverZ, 1.35);
            entity.potionEffects.add('minecraft:speed', 20, 1, false, false);
            return;
        }
    }
}
```

---

## 6. Sunlight Gap Raycasting Pattern

Prevent sun-sensitive mobs from making suicidal charges across daylight clearings:

```javascript
function hasSunlitGapBetween(level, x1, y1, z1, x2, y2, z2) {
    let dx = x2 - x1;
    let dy = y2 - y1;
    let dz = z2 - z1;
    let dist = Math.sqrt(dx * dx + dz * dz);
    if (dist < 1.5) return false;

    let BlockPosClass = Java.loadClass('net.minecraft.core.BlockPos');
    let steps = Math.min(24, Math.max(3, Math.floor(dist * 1.2)));
    for (let i = 1; i < steps; i++) {
        let t = i / steps;
        let samplePos = new BlockPosClass(Math.floor(x1 + dx * t), Math.floor(y1 + dy * t), Math.floor(z1 + dz * t));
        if (level.canSeeSky(samplePos)) {
            return true;
        }
    }
    return false;
}
```


