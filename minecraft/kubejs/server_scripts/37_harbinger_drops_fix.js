NativeEvents.onEvent('net.neoforged.neoforge.event.entity.living.LivingDropsEvent', event => {
    if (event.getEntity().getType() == 'cataclysm:harbinger') {
        let drops = event.getDrops();
        // Make all drops from the Harbinger invulnerable so its death explosion doesn't destroy them
        drops.forEach(drop => {
            drop.setInvulnerable(true);
        });
    }
});
