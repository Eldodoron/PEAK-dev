// ==========================================
// PEAK SERVER SCRIPT - APOTHEOSIS AUTO-TIERS
// Automatically upgrades the player's Apotheosis World Tier
// when they unlock the corresponding progression advancements,
// and awards them a themed gift of Apotheosis and Create items!
// Event-driven: Zero background looping, zero tick performance overhead.
// ==========================================

// Define the custom rewards for each world tier progression
const TIER_REWARDS = {
    haven: [
        { item: 'minecraft:bread', count: 8 },
        { item: 'minecraft:coal', count: 16 }
    ],
    frontier: [
        { item: 'apotheosis:gem_dust', count: 4 },
        { item: 'create:brass_ingot', count: 4 }
    ],
    ascent: [
        { item: 'apotheosis:sigil_of_enhancement', count: 2 },
        { item: 'create:precision_mechanism', count: 2 }
    ],
    summit: [
        { item: 'apotheosis:sigil_of_socketing', count: 1 },
        { item: 'create:sturdy_sheet', count: 2 }
    ],
    pinnacle: [
        { item: 'apotheosis:sigil_of_supremacy', count: 1 },
        { item: 'kubejs:infinity_fragment', count: 1 }
    ]
};

PlayerEvents.advancement(event => {
    let advancementId = event.advancement.id.toString();
    
    // Check if it's an Apotheosis progression advancement
    if (advancementId.startsWith('apotheosis:progression/')) {
        let tier = advancementId.split('/')[1]; // e.g. 'haven', 'frontier', 'ascent', 'summit', 'pinnacle'
        
        // Skip the root advancement
        if (tier === 'root') return;
        
        let player = event.player;
        let server = event.server;
        
        // Format the tier name for output (e.g. 'frontier' -> 'FRONTIER')
        let tierDisplayName = tier.toUpperCase();
        
        // Run the command to set the player's world tier
        server.runCommandSilent(`apotheosis set_world_tier ${player.username} ${tier}`);
        
        // Premium, immersive chat notification
        player.tell(Text.darkGray('\u00A7m' + '\u2500'.repeat(40)));
        player.tell(Text.gold('\u2605 APOTHIC PROGRESSION \u2605'));
        player.tell(Text.white('Your World Tier has advanced to: ').append(Text.aqua(tierDisplayName)));
        player.tell(Text.darkGray('\u00A7m' + '\u2500'.repeat(40)));
        
        // Award the progression gifts
        let rewards = TIER_REWARDS[tier];
        if (rewards) {
            player.tell(Text.gold('\u2605 Tier Advancement Gifts \u2605'));
            rewards.forEach(reward => {
                player.give(Item.of(reward.item, reward.count));
                
                // Use descriptionId to let the client translate the item name properly
                let itemComponent = Text.translate(Item.of(reward.item).descriptionId);
                player.tell(Text.gray(` - Received: `).append(Text.yellow(`${reward.count}x `)).append(itemComponent));
            });
            player.tell(Text.darkGray('\u00A7m' + '\u2500'.repeat(40)));
        }
    }
});

// Auto-initialize player on login so they never need to open the Ctrl+T tutorial menu
PlayerEvents.loggedIn(event => {
    let player = event.player;
    let server = event.server;
    
    // Check if player has already initialized Haven
    if (!player.persistentData.contains('apoth_tier_initialized')) {
        player.persistentData.putBoolean('apoth_tier_initialized', true);
        
        // Grant root and haven advancements automatically
        server.runCommandSilent(`advancement grant ${player.username} only apotheosis:progression/root`);
        server.runCommandSilent(`advancement grant ${player.username} only apotheosis:progression/haven`);
        
        // Ensure Haven tier is active
        server.runCommandSilent(`apotheosis set_world_tier ${player.username} haven`);
    }
});
