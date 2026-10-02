// ==========================================
// PEAK EXPERT MODE — SCRIPT 27
// VAMPILLAGER: NOCTURNAL ILLAGER VAMPIRE AI & WORLDGEN
// ==========================================

const VAMPIRE_STRUCTURES = [
    'minecraft:mansion',
    'idas:haunted_manor',
    'nova_structures:illager_manor',
    'idas:pillager_fortress',
    'idas:castle',
    'create_structures_arise:darkcastle',
    'illagerinvasion:labyrinth',
    'illagerinvasion:illager_fort',
    'dungeons_arise:illager_fort'
];

// Active Vampillager instance registry
const activeVampillagers = new Map();

// Helper: Safely resolve biome location string
function getBiomeString(entity) {
    try {
        let biomeHolder = entity.level.getBiome(entity.blockPosition());
        if (biomeHolder.unwrapKey && biomeHolder.unwrapKey().isPresent()) {
            return biomeHolder.unwrapKey().get().location().toString();
        } else if (biomeHolder.unwrap && biomeHolder.unwrap().left().isPresent()) {
            return biomeHolder.unwrap().left().get().location().toString();
        }
    } catch (e) {}
    return 'minecraft:plains';
}

// Helper: Check if entity is inside a recognized illager mansion/stronghold structure
function checkStructurePresence(entity, server) {
    for (let struct of VAMPIRE_STRUCTURES) {
        server.runCommandSilent(`execute at ${entity.uuid} if structure ${struct} run tag ${entity.uuid} add in_vampire_struct`);
        if (entity.tags.contains('in_vampire_struct')) {
            entity.tags.remove('in_vampire_struct');
            return true;
        }
    }
    return false;
}

// Helper: Check if line between two coordinates is occluded by opaque/solid terrain blocks
function hasBlockObstruction(level, x1, y1, z1, x2, y2, z2) {
    let dx = x2 - x1;
    let dy = y2 - y1;
    let dz = z2 - z1;
    let dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
    if (dist < 1.0) return false;

    let steps = Math.min(18, Math.floor(dist * 1.5));
    for (let i = 1; i < steps; i++) {
        let t = i / steps;
        let bx = Math.floor(x1 + dx * t);
        let by = Math.floor(y1 + dy * t);
        let bz = Math.floor(z1 + dz * t);
        let block = level.getBlock(bx, by, bz);
        if (block && !block.air && !block.liquid) {
            let state = block.blockState;
            if (state && (state.canOcclude() || state.isSolid())) {
                return true;
            }
        }
    }
    return false;
}

// Helper: Check if candidate coordinate is a safe standable block
function isStandable(level, x, y, z) {
    let bx = Math.floor(x);
    let by = Math.floor(y);
    let bz = Math.floor(z);
    let feet = level.getBlock(bx, by, bz);
    let head = level.getBlock(bx, by + 1, bz);
    let ground = level.getBlock(bx, by - 1, bz);

    let feetClear = !feet || feet.air || !feet.blockState.canOcclude();
    let headClear = !head || head.air || !head.blockState.canOcclude();
    let groundSolid = ground && !ground.air && !ground.liquid;
    return feetClear && headClear && groundSolid;
}

// Helper: Find nearest standable block protected from direct sunlight (shade/canopy/roof)
function findNearestShade(level, centerPos, radius) {
    let BlockPosClass = Java.loadClass('net.minecraft.core.BlockPos');
    let cx = centerPos.getX();
    let cy = centerPos.getY();
    let cz = centerPos.getZ();

    for (let r = 2; r <= radius; r += 2) {
        for (let ox = -r; ox <= r; ox += 2) {
            for (let oz = -r; oz <= r; oz += 2) {
                // Check perimeter of expanding concentric shells for optimal efficiency
                if (Math.abs(ox) !== r && Math.abs(oz) !== r) continue;

                for (let oy = -3; oy <= 3; oy++) {
                    let testPos = new BlockPosClass(cx + ox, cy + oy, cz + oz);
                    if (!level.canSeeSky(testPos) && isStandable(level, cx + ox, cy + oy, cz + oz)) {
                        return testPos;
                    }
                }
            }
        }
    }
    return null;
}

// Helper: Check if line between two positions crosses direct daylight (open to the sky)
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
        let sx = Math.floor(x1 + dx * t);
        let sy = Math.floor(y1 + dy * t);
        let sz = Math.floor(z1 + dz * t);
        let samplePos = new BlockPosClass(sx, sy, sz);
        if (level.canSeeSky(samplePos)) {
            return true;
        }
    }
    return false;
}

// Helper: Cast Blood Magic projectile with proper owner and forward trajectory
function castBloodMagic(level, entity, targetX, targetY, targetZ) {
    let BloodSlash = Java.loadClass('io.redspace.ironsspellbooks.entity.spells.blood_slash.BloodSlashProjectile');
    let BloodNeedle = Java.loadClass('io.redspace.ironsspellbooks.entity.spells.blood_needle.BloodNeedle');
    let Vec3d = Java.loadClass('net.minecraft.world.phys.Vec3');

    let eyeY = entity.y + entity.eyeHeight;
    let pdx = targetX - entity.x;
    let pdy = targetY - eyeY;
    let pdz = targetZ - entity.z;
    let aimDist = Math.sqrt(pdx * pdx + pdy * pdy + pdz * pdz) || 1;

    let speed = 1.25;
    let motionVec = new Vec3d((pdx / aimDist) * speed, (pdy / aimDist) * speed, (pdz / aimDist) * speed);

    try {
        let isSlash = Math.random() < 0.5;
        let proj = isSlash ? new BloodSlash(level, entity) : new BloodNeedle(level, entity);
        proj.setPos(entity.x, eyeY, entity.z);
        proj.setDamage(7.0);
        proj.shoot(motionVec);
        level.addFreshEntity(proj);

        let server = entity.server || (level && level.server);
        if (server) {
            server.runCommandSilent(`playsound irons_spellbooks:cast.generic.blood hostile @a ${entity.x} ${entity.y} ${entity.z} 1.0 1.2`);
        }
    } catch (e) {
        console.error('[PEAK Vampillager] Projectile instantiation error, using fallback: ' + e);
        let server = entity.server || (level && level.server);
        if (server) {
            let spellType = Math.random() < 0.5 ? 'irons_spellbooks:blood_slash' : 'irons_spellbooks:blood_needle';
            let vx = ((pdx / aimDist) * 1.15).toFixed(3);
            let vy = ((pdy / aimDist) * 1.15).toFixed(3);
            let vz = ((pdz / aimDist) * 1.15).toFixed(3);
            server.runCommandSilent(`execute at ${entity.uuid} anchored eyes facing ${targetX} ${targetY} ${targetZ} run summon ${spellType} ^ ^ ^1.5 {Damage:7.0f,Motion:[${vx},${vy},${vz}]}`);
        }
    }
}

// ---- SECTION 1: ENTITYJS GOALS & TARGETS ----

EntityJSEvents.addGoalSelectors('kubejs:vampillager', event => {
    // Priority 0: Float in water
    event.floatSwim(0);

    // Priority 1: Melee attack
    event.meleeAttack(1, 1.15, false);

    // Priority 2: Stroll and look around (reduced frequency so mob remains focused on stalking and fleeing)
    event.waterAvoidingRandomStroll(2, 0.7, 0.02);
    event.randomLookAround(3);
});

EntityJSEvents.addGoals('kubejs:vampillager', event => {
    let mob = event.getEntity();
    let Player = Java.loadClass('net.minecraft.world.entity.player.Player');
    let Villager = Java.loadClass('net.minecraft.world.entity.npc.Villager');
    let IronGolem = Java.loadClass('net.minecraft.world.entity.animal.IronGolem');

    let canTargetEntity = target => {
        if (!target || !target.isAlive()) return false;
        if (target.isPlayer() && (target.isCreative() || target.isSpectator())) return false;

        let server = mob.server || (mob.level && mob.level.server);
        let isAggro = mob.persistentData.getBoolean('isAggro');
        let fleeUntil = mob.persistentData.getInt('fleeUntil');
        if (!isAggro && server && server.tickCount < fleeUntil) return false;

        let level = target.level;
        let isDay = level.isDay() && !level.isRaining();
        if (!isDay) return true;

        let head = mob.getHeadArmorItem();
        let vulnerable = !head || head.isEmpty();
        if (!vulnerable) return true;

        // If mob is burning/in direct sunlight: NEVER target anyone! Shelter is priority #1!
        if (level.canSeeSky(mob.blockPosition())) return false;

        // If candidate target is out in direct sunlight: NEVER target them!
        if (level.canSeeSky(target.blockPosition())) return false;

        // If there is an open sunlight gap between mob and target: NEVER acquire melee target!
        if (hasSunlitGapBetween(level, mob.x, mob.y, mob.z, target.x, target.y, target.z)) return false;

        return true;
    };

    // Retaliate against attackers (hurtByTarget: priority, toIgnoreDamage, alertSameType, toIgnoreAlert)
    event.hurtByTarget(1, [], true, []);

    // Aggro on Players, Villagers, and Iron Golems with daylight safety filter (mustSee: false so it tracks players from behind cover)
    event.nearestAttackableTarget(2, Player, 10, false, false, canTargetEntity);
    event.nearestAttackableTarget(3, Villager, 10, false, false, canTargetEntity);
    event.nearestAttackableTarget(4, IronGolem, 20, false, false, canTargetEntity);
});


// ---- SECTION 2: NATURAL WORLD SPAWNING ----

// Hook 1: Replace 15% of mansion / fortress vindicators with Vampillagers
EntityEvents.spawned('minecraft:vindicator', event => {
    const { entity, server } = event;
    if (!entity || !entity.living) return;

    let reason = event.spawnReason ? String(event.spawnReason) : '';
    if (reason !== 'NATURAL' && reason !== 'STRUCTURE') return;

    if (checkStructurePresence(entity, server)) {
        if (Math.random() <= 0.15) {
            event.cancel();
            server.runCommandSilent(`execute at ${entity.uuid} run summon kubejs:vampillager ~ ~ ~`);
        }
    }
});

// Hook 2: Replace 1% of nocturnal Dark Forest zombie spawns with Vampillagers
EntityEvents.spawned('minecraft:zombie', event => {
    const { entity, server } = event;
    if (!entity || !entity.living) return;

    let reason = event.spawnReason ? String(event.spawnReason) : '';
    if (reason !== 'NATURAL') return;

    let biome = getBiomeString(entity);
    if (biome === 'minecraft:dark_forest' && entity.level.isNight()) {
        if (Math.random() <= 0.01) {
            event.cancel();
            server.runCommandSilent(`execute at ${entity.uuid} run summon kubejs:vampillager ~ ~ ~`);
        }
    }
});

// Track Vampillagers on spawn
EntityEvents.spawned('kubejs:vampillager', event => {
    const { entity } = event;
    if (entity && entity.living) {
        activeVampillagers.set(entity.uuid.toString(), entity);
    }
});

// Helper: Trigger Aggressive Mode with enrage visuals and sound
function triggerAggro(entity, tickCount, pData, attacker) {
    let wasAggro = pData.getBoolean('isAggro');
    pData.putBoolean('isAggro', true);
    pData.putInt('aggroUntil', tickCount + 300); // 15 seconds
    pData.putInt('fleeUntil', 0); // Cancel disengage retreat immediately
    pData.putBoolean('hasCover', false);

    let server = entity.server || (entity.level && entity.level.server);
    if (!wasAggro && server) {
        server.runCommandSilent(`playsound minecraft:entity.evoker.prepare_attack hostile @a ${entity.x} ${entity.y} ${entity.z} 1.0 1.1`);
        server.runCommandSilent(`particle minecraft:angry_villager ${entity.x} ${entity.y + 1.8} ${entity.z} 0.2 0.2 0.2 0.05 4`);
        server.runCommandSilent(`particle minecraft:crimson_spore ${entity.x} ${entity.y + 1.2} ${entity.z} 0.3 0.3 0.3 0.1 12`);
    }

    if (attacker && attacker.isLiving()) {
        let level = entity.level;
        let isDay = level.isDay() && !level.isRaining();
        let head = entity.getHeadArmorItem();
        let vulnerable = isDay && (!head || head.isEmpty());
        let attackerInSun = vulnerable && level.canSeeSky(attacker.blockPosition());
        let selfInSun = vulnerable && level.canSeeSky(entity.blockPosition());

        if (!attackerInSun && !selfInSun) {
            entity.setTarget(attacker);
        }
    }
}

// ---- SECTION 3: COMBAT COORDINATOR (RANGED MAGIC & SHADOW DASH) ----

ServerEvents.tick(event => {
    let server = event.server;
    let tickCount = server.tickCount;

    // Periodic census: Discover any loaded Vampillagers near active players every 3 seconds (60 ticks)
    if (tickCount % 60 === 0) {
        server.players.forEach(player => {
            let level = player.level;
            let box = player.boundingBox.inflate(48.0);
            let nearby = level.getEntities(null, box);
            for (let i = 0; i < nearby.length; i++) {
                let e = nearby[i];
                if (e.type === 'kubejs:vampillager' && e.isAlive()) {
                    activeVampillagers.set(e.uuid.toString(), e);
                }
            }
        });
    }

    // Run combat coordinator every 5 ticks (0.25 seconds)
    if (tickCount % 5 !== 0) return;
    if (activeVampillagers.size === 0) return;

    activeVampillagers.forEach((entity, uuidStr) => {
        if (!entity || !entity.isAlive() || entity.isRemoved()) {
            activeVampillagers.delete(uuidStr);
            return;
        }

        let pData = entity.persistentData;
        let isAggro = pData.getBoolean('isAggro');
        let aggroUntil = pData.getInt('aggroUntil');

        // Check if aggravated state expired
        if (isAggro && tickCount > aggroUntil) {
            pData.putBoolean('isAggro', false);
            isAggro = false;
        }

        // Engine-level fail-safe: Detect damage via health reduction, hurtTime, or vanilla lastHurtByMobTimestamp
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

        // When aggressive, ensure fleeing and cover seeking are strictly suppressed
        if (isAggro) {
            pData.putInt('fleeUntil', 0);
            pData.putBoolean('hasCover', false);
        }

        let level = entity.level;
        let isDay = level.isDay() && !level.isRaining();
        let headItem = entity.getHeadArmorItem();
        let vulnerableToSun = isDay && (!headItem || headItem.isEmpty());
        let currentPos = entity.blockPosition();
        let inDirectSun = vulnerableToSun && level.canSeeSky(currentPos);

        // ==========================================
        // PROTOCOL: SUN AVOIDANCE (THE SUN IS ITS BIGGEST ENEMY)
        // ==========================================
        if (vulnerableToSun) {
            // Check if entity has any active target, and if either is exposed to sunlight or separated by a sunlit gap
            if (entity.target && entity.target.isAlive()) {
                let targetInSun = level.canSeeSky(entity.target.blockPosition());
                let sunGap = hasSunlitGapBetween(level, entity.x, entity.y, entity.z, entity.target.x, entity.target.y, entity.target.z);
                if (inDirectSun || targetInSun || sunGap) {
                    // NEVER chase or bite a target into the sun!
                    entity.setTarget(null);
                    entity.navigation.stop();
                }
            }

            // Priority 1: Burning in direct sunlight -> Sprint to nearest shade immediately!
            if (inDirectSun) {
                // Ensure target is null so meleeAttack goal cannot drag the mob towards a player
                entity.setTarget(null);

                let shadePos = findNearestShade(level, currentPos, 24);
                if (shadePos) {
                    entity.navigation.moveTo(shadePos.getX() + 0.5, shadePos.getY(), shadePos.getZ() + 0.5, 1.40);
                    return; // Survival comes first: reach shelter!
                } else {
                    // No shade within 24 blocks: sprint away from players/threats to find any shelter
                    let nearestPlayer = level.getNearestPlayer(entity, 32.0);
                    let fdx = nearestPlayer ? (entity.x - nearestPlayer.x) : Math.sin(tickCount) * 16.0;
                    let fdz = nearestPlayer ? (entity.z - nearestPlayer.z) : Math.cos(tickCount) * 16.0;
                    let fdist = Math.sqrt(fdx * fdx + fdz * fdz) || 1;
                    entity.navigation.moveTo(entity.x + (fdx / fdist) * 16.0, entity.y, entity.z + (fdz / fdist) * 16.0, 1.40);
                    return;
                }
            }

            // Priority 2: Safely in shade, but target is in sun OR there is an open sunlit gap between them!
            let targetCandidate = entity.target || level.getNearestPlayer(entity, 32.0);
            if (targetCandidate && targetCandidate.isAlive() && (!targetCandidate.isPlayer() || (!targetCandidate.isCreative() && !targetCandidate.isSpectator()))) {
                let candPos = targetCandidate.blockPosition();
                let candInSun = level.canSeeSky(candPos);
                let sunGap = hasSunlitGapBetween(level, entity.x, entity.y, entity.z, targetCandidate.x, targetCandidate.y, targetCandidate.z);

                // If candidate is in direct sun OR path crosses a sun gap, and vampire is in shade: NEVER step into the sun!
                if ((candInSun || sunGap) && !inDirectSun) {
                    entity.setTarget(null);
                    entity.navigation.stop();

                    let pdx = targetCandidate.x - entity.x;
                    let pdy = (targetCandidate.y + targetCandidate.eyeHeight / 2) - (entity.y + entity.eyeHeight);
                    let pdz = targetCandidate.z - entity.z;
                    let pDist = Math.sqrt(pdx * pdx + pdz * pdz);

                    // Cast blood magic across the sunlight gap only when in aggressive mode
                    if (isAggro && pDist >= 3.5 && pDist <= 28.0) {
                        entity.lookControl.setLookAt(targetCandidate.x, targetCandidate.y + targetCandidate.eyeHeight / 2, targetCandidate.z, 30.0, 30.0);
                        let castingTick = pData.getInt('castingSpellTick');
                        let spellCooldown = pData.getInt('spellCooldown');

                        if (castingTick > 0) {
                            server.runCommandSilent(`particle minecraft:crimson_spore ${entity.x} ${entity.y + 1.1} ${entity.z} 0.25 0.25 0.25 0.05 8`);
                            server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 1.1} ${entity.z} 0.15 0.15 0.15 0.02 5`);

                            if (tickCount >= castingTick) {
                                pData.putInt('castingSpellTick', 0);
                                pData.putInt('spellCooldown', tickCount + 55); // 2.75s cooldown
                                castBloodMagic(level, entity, targetCandidate.x, targetCandidate.y + targetCandidate.eyeHeight / 2, targetCandidate.z);
                            }
                        } else if (tickCount >= spellCooldown) {
                            pData.putInt('castingSpellTick', tickCount + 12);
                            entity.triggerAnimation('cast', 'cast');
                            server.runCommandSilent(`playsound irons_spellbooks:cast.generic.blood hostile @a ${entity.x} ${entity.y} ${entity.z} 0.9 0.8`);
                            server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 1.2} ${entity.z} 0.15 0.15 0.15 0.05 6`);
                            server.runCommandSilent(`particle minecraft:crimson_spore ${entity.x} ${entity.y + 1.2} ${entity.z} 0.2 0.2 0.2 0.05 8`);
                        }
                    } else if (tickCount % 40 === 0) {
                        server.runCommandSilent(`playsound minecraft:entity.evoker.ambient hostile @a ${entity.x} ${entity.y} ${entity.z} 0.8 1.0`);
                    }
                    return; // Refuse to leave shade!
                }
            }
        }

        // ==========================================
        // PROTOCOL: DISENGAGE & CONCEALMENT (STALKING HIDE)
        // ==========================================
        let fleeUntil = pData.getInt('fleeUntil');

        // Check if 10-second disengage just expired
        if (fleeUntil > 0 && tickCount >= fleeUntil) {
            pData.putInt('fleeUntil', 0);
            pData.putBoolean('hasCover', false);
            server.runCommandSilent(`playsound minecraft:entity.evoker.ambient hostile @a ${entity.x} ${entity.y} ${entity.z} 0.8 1.3`);
            server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 0.5} ${entity.z} 0.15 0.15 0.15 0.02 6`);
        }

        // Active disengage: Continuously flee and evade player during cooldown (STAGE 1 ONLY, NEVER IN AGGRO)
        if (!isAggro && fleeUntil > 0 && tickCount < fleeUntil) {
            let nearestPlayer = level.getNearestPlayer(entity, 32.0);
            if (nearestPlayer && nearestPlayer.isAlive() && !nearestPlayer.isCreative() && !nearestPlayer.isSpectator()) {
                let pEyeY = nearestPlayer.y + nearestPlayer.eyeHeight;
                let fdx = entity.x - nearestPlayer.x;
                let fdz = entity.z - nearestPlayer.z;
                let pDist = Math.sqrt(fdx * fdx + fdz * fdz) || 1;
                let baseAngle = Math.atan2(fdz, fdx);

                let hasCover = pData.getBoolean('hasCover');
                let coverX = pData.getDouble('coverX');
                let coverY = pData.getDouble('coverY');
                let coverZ = pData.getDouble('coverZ');
                let coverSetTick = pData.getInt('coverSetTick');

                let distToCover = Math.sqrt(Math.pow(entity.x - coverX, 2) + Math.pow(entity.z - coverZ, 2));

                // Check if current position is visible to player
                let playerCanSeeMob = !hasBlockObstruction(level, nearestPlayer.x, pEyeY, nearestPlayer.z, entity.x, entity.y + entity.eyeHeight, entity.z);

                // Continuous evasion trigger:
                // Keep running if not in cover, or player is close (< 12 blocks), or player has line of sight, or destination reached while player still nearby
                let needsNewDestination = !hasCover ||
                    (pDist < 12.0) ||
                    (playerCanSeeMob && pDist < 18.0) ||
                    (distToCover <= 2.0 && pDist < 14.0) ||
                    (tickCount - coverSetTick > 60 && distToCover > 3.0);

                if (needsNewDestination) {
                    let angleOffsets = [0, 0.4, -0.4, 0.8, -0.8, 1.2, -1.2, 1.6, -1.6];
                    let bestCover = null;
                    let fallbackDest = null;
                    let BlockPosClass = Java.loadClass('net.minecraft.core.BlockPos');

                    // Calculate flee distance: dynamically scale away from player
                    let fleeDist = Math.max(12.0, Math.min(20.0, pDist + 8.0));

                    for (let i = 0; i < angleOffsets.length; i++) {
                        let ang = baseAngle + angleOffsets[i];
                        let cx = nearestPlayer.x + Math.cos(ang) * fleeDist;
                        let cz = nearestPlayer.z + Math.sin(ang) * fleeDist;
                        let cy = entity.y;

                        let testPos = new BlockPosClass(Math.floor(cx), Math.floor(cy), Math.floor(cz));
                        let sunBlocked = !vulnerableToSun || !level.canSeeSky(testPos);
                        if (!sunBlocked) continue; // NEVER flee into a sunlit spot!

                        if (!fallbackDest && isStandable(level, cx, cy, cz)) {
                            fallbackDest = { x: cx, y: cy, z: cz };
                        }

                        // Test if sightline between player eyes and this spot is blocked by terrain
                        if (hasBlockObstruction(level, nearestPlayer.x, pEyeY, nearestPlayer.z, cx, cy + 1.0, cz)) {
                            if (isStandable(level, cx, cy, cz)) {
                                bestCover = { x: cx, y: cy, z: cz };
                                break;
                            }
                        }
                    }

                    let shadeFallback = vulnerableToSun ? findNearestShade(level, currentPos, 20) : null;
                    let targetDest = bestCover || fallbackDest || (shadeFallback ? { x: shadeFallback.getX() + 0.5, y: shadeFallback.getY(), z: shadeFallback.getZ() + 0.5 } : null) || {
                        x: entity.x + (fdx / pDist) * 12.0,
                        y: entity.y,
                        z: entity.z + (fdz / pDist) * 12.0
                    };

                    coverX = targetDest.x;
                    coverY = targetDest.y;
                    coverZ = targetDest.z;
                    pData.putDouble('coverX', coverX);
                    pData.putDouble('coverY', coverY);
                    pData.putDouble('coverZ', coverZ);
                    pData.putInt('coverSetTick', tickCount);
                    pData.putBoolean('hasCover', true);
                    distToCover = Math.sqrt(Math.pow(entity.x - coverX, 2) + Math.pow(entity.z - coverZ, 2));
                }

                // Lurk only when fully covered, hidden from sight, and at a safe distance (> 14 blocks)
                if (distToCover <= 1.5 && !playerCanSeeMob && pDist >= 14.0) {
                    entity.setTarget(null);
                    entity.navigation.stop();

                    if (tickCount % 20 === 0) {
                        server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 0.3} ${entity.z} 0.1 0.1 0.1 0.01 3`);
                    }
                    return;
                } else {
                    // Actively sprint away from player towards cover/flee position
                    entity.setTarget(null);
                    entity.navigation.moveTo(coverX, coverY, coverZ, 1.35);

                    // Swiftness burst for fluid, slippery evasion
                    entity.potionEffects.add('minecraft:speed', 20, 1, false, false);

                    // Shadow smoke trail while sprinting
                    if (tickCount % 8 === 0) {
                        server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 0.5} ${entity.z} 0.15 0.15 0.15 0.02 5`);
                    }
                    return;
                }
            }

            entity.setTarget(null);
            return;
        }

        // ==========================================
        // HUNT RESUMPTION & TARGET MANAGEMENT
        // ==========================================
        let target = entity.target;
        if (!target || !target.isAlive() || (target.isPlayer() && (target.isCreative() || target.isSpectator()))) {
            let candidate = level.getNearestPlayer(entity, 32.0);
            if (candidate && candidate.isAlive() && !candidate.isCreative() && !candidate.isSpectator()) {
                let candInSun = vulnerableToSun && level.canSeeSky(candidate.blockPosition());
                let sunGap = vulnerableToSun && hasSunlitGapBetween(level, entity.x, entity.y, entity.z, candidate.x, candidate.y, candidate.z);
                if (!candInSun && !sunGap && (!vulnerableToSun || !inDirectSun)) {
                    entity.setTarget(candidate);
                    entity.navigation.moveTo(candidate.x, candidate.y, candidate.z, 1.25);
                    target = candidate;
                }
            }
        }

        if (!target || !target.isAlive()) return;

        let dx = target.x - entity.x;
        let dy = (target.y + target.eyeHeight / 2) - (entity.y + entity.eyeHeight);
        let dz = target.z - entity.z;
        let distSq = dx * dx + dz * dz;
        let dist = Math.sqrt(distSq);

        // ==========================================
        // STATE 1: EXTENDED COMBAT (AGGRO STANCE)
        // ==========================================
        if (isAggro) {
            // Close Range (< 4.5 blocks): Strict Melee combat. Cancel any casting.
            if (dist <= 4.5) {
                if (pData.getInt('castingSpellTick') > 0) {
                    pData.putInt('castingSpellTick', 0);
                }
                return;
            }

            // Long Range (4.5 to 28.0 blocks): Telegraphed Blood Magic
            if (dist > 4.5 && dist <= 28.0) {
                entity.lookControl.setLookAt(target.x, target.y + target.eyeHeight / 2, target.z, 30.0, 30.0);
                let castingTick = pData.getInt('castingSpellTick');
                let spellCooldown = pData.getInt('spellCooldown');

                if (castingTick > 0) {
                    server.runCommandSilent(`particle minecraft:crimson_spore ${entity.x} ${entity.y + 1.1} ${entity.z} 0.25 0.25 0.25 0.05 8`);
                    server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 1.1} ${entity.z} 0.15 0.15 0.15 0.02 5`);

                    if (tickCount >= castingTick) {
                        pData.putInt('castingSpellTick', 0);
                        pData.putInt('spellCooldown', tickCount + 70); // 3.5s cooldown
                        castBloodMagic(level, entity, target.x, target.y + target.eyeHeight / 2, target.z);
                    }
                } else if (tickCount >= spellCooldown) {
                    pData.putInt('castingSpellTick', tickCount + 12);
                    entity.triggerAnimation('cast', 'cast');
                    server.runCommandSilent(`playsound irons_spellbooks:cast.generic.blood hostile @a ${entity.x} ${entity.y} ${entity.z} 0.9 0.8`);
                    server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 1.2} ${entity.z} 0.15 0.15 0.15 0.05 10`);
                    server.runCommandSilent(`particle minecraft:crimson_spore ${entity.x} ${entity.y + 1.2} ${entity.z} 0.3 0.3 0.3 0.1 15`);
                }
            }

            // Beyond spell range (> 28.0 blocks): Sprint to close distance
            if (dist > 28.0) {
                entity.navigation.moveTo(target.x, target.y, target.z, 1.25);
            }
        }
        // ==========================================
        // STATE 2: PREDATORY HUNTING (NORMAL STANCE)
        // ==========================================
        else {
            // Gap-Closing Shadow Leap (5.5 to 16 blocks away): Airborne gap close
            if (dist >= 5.5 && dist <= 16.0) {
                let targetInSun = vulnerableToSun && level.canSeeSky(target.blockPosition());
                let sunGap = vulnerableToSun && hasSunlitGapBetween(level, entity.x, entity.y, entity.z, target.x, target.y, target.z);
                if (targetInSun || sunGap) {
                    return;
                }

                let dashCooldown = pData.getInt('dashCooldown');
                if (tickCount >= dashCooldown) {
                    pData.putInt('dashCooldown', tickCount + 80); // 4.0s cooldown

                    let Vec3d = Java.loadClass('net.minecraft.world.phys.Vec3');
                    let leapHorizontalSpeed = Math.min(2.4, Math.max(1.3, (dist - 1.0) * 0.165));
                    let vx = (dx / dist) * leapHorizontalSpeed;
                    let vz = (dz / dist) * leapHorizontalSpeed;

                    // Low aerodynamic jump arc (Vy = 0.35) gives enough hang-time to eliminate ground friction
                    entity.setDeltaMovement(new Vec3d(vx, 0.35, vz));
                    entity.hurtMarked = true;

                    // Brief burst of speed and pathfinding command directly to target coordinates
                    entity.potionEffects.add('minecraft:speed', 25, 2, false, false);
                    entity.navigation.moveTo(target.x, target.y, target.z, 1.30);

                    // Jet-black ink smoke + crimson spore burst + blood step audio + bat takeoff
                    server.runCommandSilent(`playsound irons_spellbooks:cast.blood_step hostile @a ${entity.x} ${entity.y} ${entity.z} 1.0 1.0`);
                    server.runCommandSilent(`playsound minecraft:entity.bat.takeoff hostile @a ${entity.x} ${entity.y} ${entity.z} 1.0 0.8`);
                    server.runCommandSilent(`particle minecraft:squid_ink ${entity.x} ${entity.y + 0.5} ${entity.z} 0.25 0.25 0.25 0.04 12`);
                    server.runCommandSilent(`particle minecraft:crimson_spore ${entity.x} ${entity.y + 0.5} ${entity.z} 0.2 0.2 0.2 0.04 8`);
                }
            }
        }
    });
});

// ---- SECTION 4: DAMAGE HOOK (AGGRESSIVE MODE ENRAGE) ----

EntityEvents.afterHurt(event => {
    let entity = event.entity;
    if (entity && entity.isAlive() && entity.type === 'kubejs:vampillager') {
        let server = event.server || (entity.level && entity.level.server);
        let tickCount = server ? server.tickCount : 0;
        let source = event.source;
        let attacker = source ? (source.actual || source.entity || source.player) : null;
        triggerAggro(entity, tickCount, entity.persistentData, attacker);
    }

    let source = event.source;
    let attacker = source ? (source.actual || source.entity || source.player) : null;
    if (attacker && attacker.type === 'kubejs:vampillager') {
        let aData = attacker.persistentData;
        if (aData.getBoolean('isAggro')) {
            // Once in aggressive mode, hitting targets never triggers disengage retreat
            aData.putInt('fleeUntil', 0);
            aData.putBoolean('hasCover', false);
        }
    }
});
