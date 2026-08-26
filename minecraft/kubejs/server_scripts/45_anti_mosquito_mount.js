NativeEvents.onEvent('net.neoforged.neoforge.event.entity.EntityMountEvent', event => {
    if (event.isMounting()) {
        try {
            let mounter = event.getEntityMounting();
            let mounted = event.getEntityBeingMounted();
            
            if (mounter && mounted && mounter.getType() == 'alexsmobs:crimson_mosquito') {
                if (mounted.isPlayer()) {
                    event.setCanceled(true);
                    
                    try {
                        let lvl = mounted.level;
                        if (typeof lvl === 'function') {
                            lvl = mounted.level();
                        } else if (mounted.getLevel) {
                            lvl = mounted.getLevel();
                        }
                        if (lvl && lvl.damageSources) {
                            mounted.attack(lvl.damageSources().mobAttack(mounter), 2.0);
                        } else {
                            mounted.attack(2.0);
                        }
                    } catch (e) {}
                    
                    try {
                        let mx = mounter.getX() - mounted.getX();
                        let mz = mounter.getZ() - mounted.getZ();
                        let dist = Math.sqrt(mx * mx + mz * mz);
                        
                        let dx = 0, dy = 0.4, dz = -0.8;
                        if (dist > 0.1) {
                            dx = (mx / dist) * 0.8;
                            dz = (mz / dist) * 0.8;
                        }
                        
                        let Vec3 = Java.loadClass('net.minecraft.world.phys.Vec3');
                        mounter.setDeltaMovement(new Vec3(dx, dy, dz));
                    } catch (e) {}
                }
            }
        } catch (err) {}
    }
});
