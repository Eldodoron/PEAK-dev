NativeEvents.onEvent('net.neoforged.neoforge.event.entity.living.LivingDropsEvent', event => {
    let type = event.getEntity().getType();
    if (type === 'cataclysm:the_harbinger' || type === 'cataclysm:harbinger') {
        let drops = event.getDrops();
        // Make all drops from the Harbinger invulnerable so its death explosion doesn't destroy them
        drops.forEach(drop => {
            drop.setInvulnerable(true);
        });
    }
});
