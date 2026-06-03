// ==========================================
// PEAK ZENITH SABER Ã¢â‚¬â€ RECIPE AND EVENTS SCRIPT
// Minecraft 1.21.1 NeoForge Mojmap
// ==========================================

ServerEvents.recipes(event => {
    // Registers a shaped crafting recipe outputting a highly customized Diamond Sword
    event.shaped(
        Item.of('minecraft:diamond_sword', {
            // Custom Display Name (must be a JSON component string in 1.21+)
            'minecraft:custom_name': '"Â§bPEAK Zenith SaberÂ§r"',
            
            // Lore (Array of JSON component strings in 1.21+)
            'minecraft:lore': [
                '"Â§7Forged inside PEAK dev instance.Â§r"',
                '"Â§8Active stabilizing core.Â§r"'
            ],
            
            // Enchantments (levels object map in 1.21+)
            'minecraft:enchantments': {
                levels: {
                    'minecraft:sharpness': 7,
                    'minecraft:unbreaking': 4
                }
            },
            
            // Unbreakable flag (empty JSON object means true in 1.21+)
            'minecraft:unbreakable': {}
        }),
        [
            'D',
            'D',
            'N'
        ], {
            D: 'minecraft:diamond',
            N: 'minecraft:nether_star'
        }
    );

    console.log('[PEAK Dev] Zenith Saber recipe successfully registered!');
});

ItemEvents.crafted(event => {
    // 1. Mandatory high-performance early-exit guard clause
    // This runs for EVERY crafted item, so we exit instantly if not a diamond sword.
    if (event.item.id !== 'minecraft:diamond_sword') return;

    // 2. Safely extract the item's display name string to check for the custom name
    let itemName = event.item.name.getString();
    
    // 3. Verify if it is our custom Zenith Saber
    if (itemName && itemName.includes('Zenith Saber')) {
        let player = event.player;
        if (player) {
            // Send the calibration message
            player.tell('Ã‚Â§b[PEAK]Ã‚Â§r Zenith Saber successfully calibrated and ready!');
            
            // Trigger the toast challenge complete sound effect
            player.playSound('minecraft:ui.toast.challenge_complete', 1.0, 1.0);
        }
    }
});

