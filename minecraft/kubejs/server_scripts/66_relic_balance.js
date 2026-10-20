// ==========================================
// Relic Balance: Cloak of Concealment
// ==========================================

let $IRelicItem = null;
let $EntityUtils = null;

try {
    $IRelicItem = Java.loadClass('it.hurts.sskirillss.relics.items.relics.base.IRelicItem');
    $EntityUtils = Java.loadClass('it.hurts.sskirillss.relics.utils.EntityUtils');
} catch (e) {
    // Relics classes not present
}

function updateCloakStack(stack) {
    if (!stack || stack.isEmpty() || !$IRelicItem) return;
    if (stack.id !== 'reliquified_ars_nouveau:cloak_of_concealment') return;
    try {
        let item = stack.getItem();
        if (item instanceof $IRelicItem) {
            let current = item.getStatInitialValue(stack, 'absorption', 'absorbing');
            // If the item has the old low value (< 600.0), migrate it to balanced 800.0
            if (current > 0 && current < 600.0) {
                item.setStatInitialValue(stack, 'absorption', 'absorbing', 800.0);
            }
        }
    } catch (err) {
        // Silently ignore component differences
    }
}

PlayerEvents.tick(event => {
    let player = event.player;
    if (player.level.isClientSide() || player.age % 40 !== 0) return;

    // Check main inventory
    for (let stack of player.inventory.allItems) {
        if (stack && stack.id === 'reliquified_ars_nouveau:cloak_of_concealment') {
            updateCloakStack(stack);
        }
    }

    // Check equipped curio
    if ($EntityUtils && $IRelicItem) {
        try {
            let cloakItem = Item.of('reliquified_ars_nouveau:cloak_of_concealment').getItem();
            if (cloakItem) {
                let equipped = $EntityUtils.findEquippedCurio(player, cloakItem);
                if (equipped && !equipped.isEmpty()) {
                    updateCloakStack(equipped);
                }
            }
        } catch (e) {
            // Curio lookup fallback
        }
    }
});
