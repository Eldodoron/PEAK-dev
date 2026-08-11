// ==========================================
// PEAK EXPERT MODE — SCRIPT 26
// MOB MAX HEALTH FIX
// ==========================================
// Some mods (like Dynamic Difficulty) scale the max_health attribute on spawn
// but fail to heal the entity to match the new max health.
// This script heals specific targeted mobs to full a tick after they spawn to fix this,
// avoiding the performance overhead of running this check on every single mob spawn.

const MOBS_TO_HEAL = [
    'block_factorys_bosses:infernal_dragon'
    // Add any other bosses or mobs here that suffer from the health bug
];

EntityEvents.spawned(event => {
    const { entity, server } = event;
    
    if (!entity || !entity.isLiving()) return;

    // Only apply to the specific mobs defined above
    if (MOBS_TO_HEAL.includes(entity.type)) {
        server.scheduleInTicks(2, callback => {
            if (entity && entity.isAlive() && entity.health < entity.maxHealth) {
                entity.setHealth(entity.maxHealth);
            }
        });
    }
});
