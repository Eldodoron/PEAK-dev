// ==========================================
// VAMPILLAGER ENTITY REGISTRATION
// ==========================================

StartupEvents.registry('entity_type', event => {
    event.create('kubejs:vampillager', 'entityjs:mob')
        .sized(0.6, 1.95)
        .eggItem(egg => {
            egg.backgroundColor(0x1a0505)
            egg.highlightColor(0x8a0000)
        })
        .modelResource(entity => 'kubejs:geo/entity/vampillager.geo.json')
        .textureResource(entity => 'kubejs:textures/entity/vampillager.png')
        .animationResource(entity => 'kubejs:animations/entity/vampillager.animation.json')
        .newGlowingGeoLayer(layer => {
            layer.textureResource(entity => 'kubejs:textures/entity/vampillager_glow.png')
        })
        .setAmbientSound('minecraft:entity.evoker.ambient')
        .setDeathSound('minecraft:entity.evoker.death')
        .setHurtSound(ctx => 'minecraft:entity.evoker.hurt')
        .addAnimationController('main', 4, event => {
            if (event.isMoving()) {
                event.thenLoop('walk')
            } else {
                event.thenLoop('idle')
            }
            return true
        })
        .addTriggerableAnimationController('attack', 2, 'attack', 'attack', 'play_once')
        .addTriggerableAnimationController('cast', 2, 'cast', 'cast', 'play_once')
        .aiStep(entity => {
            if (!entity.level.clientSide) {
                // Trigger attack animation on swing initiation
                if (entity.swinging && entity.swingTime === 1) {
                    entity.triggerAnimation('attack', 'attack')
                }

                if (entity.level.isDay()) {
                    let pos = entity.blockPosition()
                    if (entity.level.canSeeSky(pos) && !entity.isInWaterOrRain()) {
                        let head = entity.getHeadArmorItem()
                        if (!head || head.isEmpty()) {
                            if (entity.tickCount % 20 === 0) {
                                entity.igniteForSeconds(8)
                            }
                        }
                    }
                }
            }
        })
        .onHurtTarget(ctx => {
            let self = ctx.entity
            let target = ctx.targetEntity
            if (!target || self.level.clientSide) return

            // Ensure attack animation is triggered upon connecting a strike
            self.triggerAnimation('attack', 'attack')

            // Bite audio and blood effects
            let server = self.server || (self.level && self.level.server)
            if (server) {
                server.runCommandSilent(`playsound minecraft:entity.player.hurt_drown hostile @a ${target.x} ${target.y} ${target.z} 1.0 1.6`)
                server.runCommandSilent(`particle minecraft:crimson_spore ${target.x} ${target.y + 1} ${target.z} 0.2 0.2 0.2 0.05 8`)
                server.runCommandSilent(`particle minecraft:squid_ink ${target.x} ${target.y + 1} ${target.z} 0.15 0.15 0.15 0.02 4`)
            }

            let isAggro = self.persistentData.getBoolean('isAggro')

            // Siphon vitality only during normal predatory feeding (disabled in aggressive mode)
            if (!isAggro) {
                self.heal(6.0)
            }

            // Inflict bleeding and mild slowness
            if (target.isLiving()) {
                target.potionEffects.add('apothic_attributes:bleeding', 100, 1)
                target.potionEffects.add('minecraft:slowness', 40, 0)
            }

            // Hit-and-run disengage: If not provoked in extended combat, leap backwards and flee
            if (!isAggro && server) {
                let Vec3d = Java.loadClass('net.minecraft.world.phys.Vec3')
                let dx = self.x - target.x
                let dz = self.z - target.z
                let dist = Math.sqrt(dx * dx + dz * dz) || 1

                let level = self.level
                let isDay = level.isDay() && !level.isRaining()
                let head = self.getHeadArmorItem()
                let vulnerable = isDay && (!head || head.isEmpty())

                // Check backward landing position: ensure we don't leap backwards into direct sunlight!
                let backX = self.x + (dx / dist) * 2.5
                let backZ = self.z + (dz / dist) * 2.5
                let BlockPosClass = Java.loadClass('net.minecraft.core.BlockPos')
                let backPos = new BlockPosClass(Math.floor(backX), Math.floor(self.y), Math.floor(backZ))
                let landsInSun = vulnerable && level.canSeeSky(backPos)

                if (!landsInSun) {
                    self.setDeltaMovement(new Vec3d((dx / dist) * 0.9, 0.3, (dz / dist) * 0.9))
                }
                self.persistentData.putInt('fleeUntil', server.tickCount + 200)
                self.persistentData.putBoolean('hasCover', false)

                // Mocking Illager celebrate laugh and shadowy illusioner whoosh
                server.runCommandSilent(`playsound minecraft:entity.evoker.celebrate hostile @a ${self.x} ${self.y} ${self.z} 1.0 1.25`)
                server.runCommandSilent(`playsound minecraft:entity.illusioner.mirror_move hostile @a ${self.x} ${self.y} ${self.z} 0.8 1.1`)
            }
        })
        .onHurt(ctx => {
            let self = ctx.entity
            let server = self.server || (self.level && self.level.server)
            let tick = server ? server.tickCount : 0

            let wasAggro = self.persistentData.getBoolean('isAggro')

            // Enter aggravated state when damaged: cancels fleeing and locks into combat
            self.persistentData.putBoolean('isAggro', true)
            self.persistentData.putInt('aggroUntil', tick + 300)
            self.persistentData.putInt('fleeUntil', 0)
            self.persistentData.putBoolean('hasCover', false)

            if (!wasAggro && server) {
                server.runCommandSilent(`playsound minecraft:entity.evoker.prepare_attack hostile @a ${self.x} ${self.y} ${self.z} 1.0 1.1`)
                server.runCommandSilent(`particle minecraft:angry_villager ${self.x} ${self.y + 1.8} ${self.z} 0.2 0.2 0.2 0.05 4`)
                server.runCommandSilent(`particle minecraft:crimson_spore ${self.x} ${self.y + 1.2} ${self.z} 0.3 0.3 0.3 0.1 12`)
            }

            let source = ctx.damageSource
            let attacker = null
            if (source) {
                attacker = source.actual || source.entity || source.player
            }

            if (attacker && attacker.isLiving()) {
                let level = self.level
                let isDay = level.isDay() && !level.isRaining()
                let head = self.getHeadArmorItem()
                let vulnerable = isDay && (!head || head.isEmpty())
                let attackerInSun = vulnerable && level.canSeeSky(attacker.blockPosition())
                let selfInSun = vulnerable && level.canSeeSky(self.blockPosition())

                // A vampire NEVER chases into the sun!
                if (!attackerInSun && !selfInSun) {
                    self.setTarget(attacker)
                }
            }
        })
        .onDeath(ctx => {
            let self = ctx.entity
            let server = self.server || (self.level && self.level.server)
            if (!server) return

            // Dissipate into fleeing bats with audio and shadow burst
            for (let i = 0; i < 3; i++) {
                server.runCommandSilent(`execute at ${self.uuid} run summon bat ~ ~0.5 ~`)
            }
            server.runCommandSilent(`playsound minecraft:entity.bat.death hostile @a ${self.x} ${self.y} ${self.z} 1.0 1.0`)
            server.runCommandSilent(`playsound minecraft:entity.bat.takeoff hostile @a ${self.x} ${self.y} ${self.z} 1.0 0.8`)
            server.runCommandSilent(`particle minecraft:squid_ink ${self.x} ${self.y + 0.8} ${self.z} 0.25 0.25 0.25 0.05 10`)
            server.runCommandSilent(`particle minecraft:crimson_spore ${self.x} ${self.y + 0.8} ${self.z} 0.25 0.25 0.25 0.05 12`)
        })
        .dropCustomDeathLoot(ctx => {
            ctx.entity.block.popItem(Item.of('kubejs:vampire_fang'))
            if (Math.random() < 0.5) {
                ctx.entity.block.popItem(Item.of('irons_spellbooks:blood_vial'))
            }
        })
})

EntityJSEvents.attributes(event => {
    event.modify('kubejs:vampillager', helper => {
        helper.add('minecraft:generic.max_health', 36.0)
        helper.add('minecraft:generic.movement_speed', 0.28)
        helper.add('minecraft:generic.attack_damage', 6.0)
        helper.add('minecraft:generic.follow_range', 32.0)
        helper.add('minecraft:generic.scale', 0.75)
    })
})
