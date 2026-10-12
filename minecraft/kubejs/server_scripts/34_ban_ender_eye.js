ServerEvents.recipes(event => {
    // Ban Ender Eye crafting so players must kill bosses for them
    event.remove({ output: 'minecraft:ender_eye' });
});

LootJS.modifiers(event => {
    // Remove Ender Eye from all chest loots (structures, dungeons, etc.)
    event.addTableModifier(LootType.CHEST)
        .removeLoot('minecraft:ender_eye');
});

// Helper to reliably extract item ID across Vanilla, KubeJS, and MoreJS item stacks
function getEnderEyeId(stack) {
    if (!stack) return '';
    try {
        if (stack.id) return stack.id.toString();
        if (stack.getId) return stack.getId().toString();
        if (stack.getItem) {
            let item = stack.getItem();
            if (item && item.builtInRegistryHolder) {
                return item.builtInRegistryHolder().key().location().toString();
            }
        }
    } catch (e) {}
    return '';
}

function isEnderEyeListing(listing) {
    if (!listing) return false;
    try {
        if (listing.forSale && getEnderEyeId(listing.forSale) === 'minecraft:ender_eye') {
            return true;
        }
    } catch (e) {}
    try {
        let offer = listing.getOffer(null, null);
        if (offer) {
            let res = offer.result || offer.output;
            if (getEnderEyeId(res) === 'minecraft:ender_eye') {
                return true;
            }
        }
    } catch (e) {}
    return false;
}

function purgeEnderEyeTrades(event) {
    try {
        if (event.genericTrades) event.genericTrades.removeIf(isEnderEyeListing);
        if (event.getGenericTrades) event.getGenericTrades().removeIf(isEnderEyeListing);
    } catch (e) {}
    try {
        if (event.rareTrades) event.rareTrades.removeIf(isEnderEyeListing);
        if (event.getRareTrades) event.getRareTrades().removeIf(isEnderEyeListing);
    } catch (e) {}
}

// Intercept NeoForge WandererTradesEvent on normal and lowest priority
try {
    let WandererTradesEvent = Java.loadClass('net.neoforged.neoforge.event.village.WandererTradesEvent');
    NativeEvents.onEvent(WandererTradesEvent, event => {
        purgeEnderEyeTrades(event);
    });

    let EventPriority = Java.loadClass('net.neoforged.bus.api.EventPriority');
    if (EventPriority && EventPriority.LOWEST) {
        NativeEvents.onEvent(EventPriority.LOWEST, WandererTradesEvent, event => {
            purgeEnderEyeTrades(event);
        });
    }
} catch (e) {}

// Prevent offer generation if an Ender Eye trade is somehow instantiated
MoreJS.updateOffer(event => {
    try {
        let offer = event.offer;
        if (offer) {
            let res = offer.result || offer.output;
            if (getEnderEyeId(res) === 'minecraft:ender_eye') {
                event.cancel();
                if (offer.setDisabled) offer.setDisabled(true);
            }
        }
    } catch (e) {}
});

// Purge Ender Eye offers when a player opens any merchant trading GUI
MoreJS.playerStartTrading(event => {
    try {
        let merchant = event.merchant;
        if (merchant && merchant.offers) {
            merchant.offers.removeIf(offer => {
                if (!offer) return false;
                let res = offer.result || offer.output;
                return getEnderEyeId(res) === 'minecraft:ender_eye';
            });
        }
        if (event.forEachOffers) {
            event.forEachOffers((offer, index) => {
                if (!offer) return;
                let res = offer.result || offer.output;
                if (getEnderEyeId(res) === 'minecraft:ender_eye') {
                    if (offer.setDisabled) offer.setDisabled(true);
                }
            });
        }
    } catch (e) {}
});

// Scrub Ender Eye offers on newly spawned Wandering Traders
EntityEvents.spawned('minecraft:wandering_trader', event => {
    try {
        let trader = event.entity;
        if (trader && trader.offers) {
            trader.offers.removeIf(offer => {
                if (!offer) return false;
                let res = offer.result || offer.output;
                return getEnderEyeId(res) === 'minecraft:ender_eye';
            });
        }
    } catch (e) {}
});
