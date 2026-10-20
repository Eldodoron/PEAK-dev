// ==========================================
// PEAK EXPERT MODE — SCRIPT 64
// ANVIL COST CAP & MANAGEMENT
// ==========================================
// Optional fixed anvil cost limit for Apotheic Enchanting.
// When enabled, limits anvil operations to a configurable cap (default 64 levels)
// and prevents the prior work penalty (minecraft:repair_cost) from growing
// past (cap - 1), preventing integer overflow and excessive XP requirements.
// Configurable strictly via /peak anvil cost fixed <true|false>.
// ==========================================

(() => {

const $AnvilMenu = Java.loadClass('net.minecraft.world.inventory.AnvilMenu');
const $DataComponents = Java.loadClass('net.minecraft.core.component.DataComponents');
const $Integer = Java.loadClass('java.lang.Integer');
const $AnvilUpdateEvent = Java.loadClass('net.neoforged.neoforge.event.AnvilUpdateEvent');
const $AnvilRepairEvent = Java.loadClass('net.neoforged.neoforge.event.entity.player.AnvilRepairEvent');
const $PlayerContainerOpenEvent = Java.loadClass('net.neoforged.neoforge.event.entity.player.PlayerContainerEvent$Open');

const DEFAULT_COST_LIMIT = 64;

let fixedCostEnabled = false;
let anvilCostLimit = DEFAULT_COST_LIMIT;
let settingsInitialized = false;
let inBroadcastSync = false;

function syncSettings(server) {
    if (!server) return;
    try {
        fixedCostEnabled = Boolean(server.persistentData.getBoolean('peak_anvil_cost_fixed'));
        let storedLimit = server.persistentData.getInt('peak_anvil_cost_limit');
        anvilCostLimit = (storedLimit > 0) ? storedLimit : DEFAULT_COST_LIMIT;
    } catch (e) {}
}

function ensureSettings(server) {
    if (!settingsInitialized && server) {
        syncSettings(server);
        settingsInitialized = true;
    }
}

function isFixedCostEnabled(server) {
    if (server) ensureSettings(server);
    return fixedCostEnabled;
}

function getAnvilCostLimit(server) {
    if (server) ensureSettings(server);
    return anvilCostLimit;
}

function getItemRepairCost(stack) {
    if (!stack || stack.isEmpty()) return 0;
    try {
        if (stack.has && stack.has($DataComponents.REPAIR_COST)) {
            let val = stack.get ? stack.get($DataComponents.REPAIR_COST) : stack.kjs$get($DataComponents.REPAIR_COST);
            if (val != null) return Number(val);
        }
    } catch (e) {}
    try {
        let comps = stack.getComponents ? stack.getComponents() : null;
        if (comps && comps.has($DataComponents.REPAIR_COST)) {
            let val = comps.get($DataComponents.REPAIR_COST);
            if (val != null) return Number(val);
        }
    } catch (e) {}
    return 0;
}

function setItemRepairCost(stack, cost) {
    if (!stack || stack.isEmpty()) return;
    try {
        if (typeof stack.setRepairCost === 'function') {
            stack.setRepairCost(cost);
            return;
        }
    } catch (e) {}
    try {
        if (typeof stack.kjs$setRepairCost === 'function') {
            stack.kjs$setRepairCost(cost);
            return;
        }
    } catch (e) {}
    try {
        if (typeof stack.kjs$override === 'function') {
            stack.kjs$override($DataComponents.REPAIR_COST, $Integer.valueOf(cost));
            return;
        }
    } catch (e) {}
    try {
        stack.set($DataComponents.REPAIR_COST, $Integer.valueOf(cost));
    } catch (e) {}
}

function clampRepairCost(stack, maxRepairCost) {
    if (!stack || stack.isEmpty()) return false;
    if (getItemRepairCost(stack) > maxRepairCost) {
        setItemRepairCost(stack, maxRepairCost);
        return true;
    }
    return false;
}

function isAnvilMenu(menu) {
    if (!menu) return false;
    try {
        if (menu instanceof $AnvilMenu) return true;
        let name = menu.getClass().getSimpleName();
        return name.includes('Anvil');
    } catch (e) {
        return false;
    }
}

function enforceAnvilMenu(menu, limit) {
    if (!menu) return false;
    let maxRepair = Math.max(0, limit - 1);
    let changed = false;

    // Handle standard AnvilMenu
    if (isAnvilMenu(menu)) {
        // 1. Clamp input slots (0 and 1)
        try {
            if (typeof menu.getSlot === 'function') {
                let inputClamped = false;
                for (let i = 0; i <= 1; i++) {
                    let slot = menu.getSlot(i);
                    if (slot && slot.hasItem()) {
                        if (clampRepairCost(slot.getItem(), maxRepair)) {
                            inputClamped = true;
                        }
                    }
                }
                if (inputClamped && typeof menu.createResult === 'function') {
                    menu.createResult();
                    changed = true;
                }
            }
        } catch (e) {}

        // 2. Clamp result slot (2)
        try {
            if (typeof menu.getSlot === 'function') {
                let slot2 = menu.getSlot(2);
                if (slot2 && slot2.hasItem()) {
                    if (clampRepairCost(slot2.getItem(), maxRepair)) {
                        changed = true;
                    }
                }
            }
        } catch (e) {}

        // 3. Clamp live cost DataSlot
        try {
            let currentCost = (typeof menu.getCost === 'function') ? menu.getCost() : 0;
            if (currentCost > limit) {
                if (!inBroadcastSync) {
                    inBroadcastSync = true;
                    try {
                        if (typeof menu.setMaximumCost === 'function') {
                            menu.setMaximumCost(limit + 1);
                            if (typeof menu.broadcastChanges === 'function') menu.broadcastChanges();
                            menu.setMaximumCost(limit);
                            if (typeof menu.broadcastChanges === 'function') menu.broadcastChanges();
                        } else if (typeof menu.setData === 'function') {
                            menu.setData(0, limit + 1);
                            if (typeof menu.broadcastChanges === 'function') menu.broadcastChanges();
                            menu.setData(0, limit);
                            if (typeof menu.broadcastChanges === 'function') menu.broadcastChanges();
                        }
                    } finally {
                        inBroadcastSync = false;
                    }
                }
                changed = true;
            }
        } catch (e) {}

        return changed;
    }

    // Handle Sophisticated Backpacks Anvil Upgrade container if open
    try {
        if (typeof menu.getOpenContainer === 'function') {
            let opt = menu.getOpenContainer();
            if (opt && opt.isPresent && opt.isPresent()) {
                let openContainer = opt.get();
                if (openContainer && typeof openContainer.getSlots === 'function') {
                    let slots = openContainer.getSlots();
                    if (slots && slots.size() >= 3) {
                        for (let i = 0; i < 3; i++) {
                            let s = slots.get(i);
                            if (s && s.hasItem()) {
                                clampRepairCost(s.getItem(), maxRepair);
                            }
                        }
                        if (typeof openContainer.getCost === 'function' && openContainer.getCost() > limit) {
                            if (typeof openContainer.setCost === 'function') {
                                openContainer.setCost(limit);
                            }
                            return true;
                        }
                    }
                }
            }
        }
    } catch (e) {}

    return false;
}

// 1. Intercept AnvilUpdateEvent (custom mod recipes, tomes, and input clamping)
NativeEvents.onEvent($AnvilUpdateEvent, event => {
    let player = event.getPlayer ? event.getPlayer() : event.player;
    let server = player ? player.getServer() : null;
    if (!isFixedCostEnabled(server)) return;

    let limit = getAnvilCostLimit(server);
    let maxRepair = Math.max(0, limit - 1);

    // Clamp input items before createResult() reads prior work penalties
    let leftClamped = clampRepairCost(event.getLeft(), maxRepair);
    let rightClamped = clampRepairCost(event.getRight(), maxRepair);

    let out = event.getOutput();
    if (out && !out.isEmpty()) {
        clampRepairCost(out, maxRepair);
        if (event.getCost() > limit) {
            event.setCost(limit);
        }
    } else if (event.getCost() > limit) {
        event.setCost(limit);
    }

    // If an anvil menu is already open and inputs were clamped, re-enforce
    if (player && player.containerMenu && (leftClamped || rightClamped)) {
        enforceAnvilMenu(player.containerMenu, limit);
    }
});

// 2. Intercept AnvilRepairEvent when taking the output item
NativeEvents.onEvent($AnvilRepairEvent, event => {
    let player = event.getEntity ? event.getEntity() : event.player;
    let server = player ? player.getServer() : null;
    if (!isFixedCostEnabled(server)) return;

    let limit = getAnvilCostLimit(server);
    let maxRepair = Math.max(0, limit - 1);

    let out = event.getOutput();
    if (out && !out.isEmpty()) {
        clampRepairCost(out, maxRepair);
    }

    if (player) {
        if (player.containerMenu && typeof player.containerMenu.getCarried === 'function') {
            clampRepairCost(player.containerMenu.getCarried(), maxRepair);
        }
        let inv = player.getInventory ? player.getInventory() : player.inventory;
        if (inv && typeof inv.getContainerSize === 'function') {
            let size = inv.getContainerSize();
            for (let i = 0; i < size; i++) {
                clampRepairCost(inv.getItem(i), maxRepair);
            }
        }
    }
});

// 3. Attach when opening container
NativeEvents.onEvent($PlayerContainerOpenEvent, event => {
    let player = event.getEntity ? event.getEntity() : event.player;
    let server = player ? player.getServer() : null;
    if (!isFixedCostEnabled(server)) return;

    let menu = event.getContainer ? event.getContainer() : event.container;
    if (menu) {
        enforceAnvilMenu(menu, getAnvilCostLimit(server));
    }
});

// 4. Enforce on player tick
PlayerEvents.tick(event => {
    let player = event.player;
    if (!player) return;
    let server = player.getServer();
    if (!isFixedCostEnabled(server)) return;

    let menu = player.containerMenu;
    if (menu) {
        enforceAnvilMenu(menu, getAnvilCostLimit(server));
    }
});

// 5. Sync settings on server load
ServerEvents.loaded(event => {
    syncSettings(event.server);
});

// ==========================================
// COMMAND REGISTRATION (/peak anvil cost ...)
// ==========================================

ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event;

    function reply(ctx, text, broadcast) {
        let src = ctx.source;
        if (src.player) {
            src.player.tell(text);
            return;
        }
        try {
            src.sendSuccess(() => text, Boolean(broadcast));
        } catch (e) {
            try {
                src.sendSuccess(text, Boolean(broadcast));
            } catch (e2) {}
        }
    }

    function replyFailure(ctx, text) {
        let src = ctx.source;
        if (src.player) {
            src.player.tell(text);
            return;
        }
        try {
            src.sendFailure(text);
        } catch (e) {
            try {
                src.sendFailure(() => text);
            } catch (e2) {}
        }
    }

    function setFixedCost(ctx, enabled) {
        let server = ctx.source.server;
        let isEnabled = (String(enabled).toLowerCase() === 'true');
        server.persistentData.putBoolean('peak_anvil_cost_fixed', isEnabled ? true : false);
        syncSettings(server);

        let limit = getAnvilCostLimit(server);
        let msg = isEnabled
            ? Text.green(`[PEAK] Fixed Anvil Cost is now ENABLED (capped at ${limit} levels).`)
            : Text.yellow('[PEAK] Fixed Anvil Cost is now DISABLED (uncapped Apotheic Enchanting behavior).');

        reply(ctx, msg, true);
        return 1;
    }

    function setCostLimit(ctx, levels) {
        let lvl = Math.floor(Number(levels));
        if (isNaN(lvl) || lvl < 1 || lvl > 1000) {
            let err = Text.red('[PEAK] Anvil cost limit must be between 1 and 1000 levels.');
            replyFailure(ctx, err);
            return 0;
        }
        let server = ctx.source.server;
        server.persistentData.putInt('peak_anvil_cost_limit', lvl);
        syncSettings(server);

        let msg = Text.green(`[PEAK] Anvil cost limit set to ${lvl} levels.`);
        reply(ctx, msg, true);
        return 1;
    }

    function showFixedStatus(ctx) {
        let server = ctx.source.server;
        let enabled = isFixedCostEnabled(server);
        let limit = getAnvilCostLimit(server);
        let statusText = enabled
            ? Text.green('true').append(Text.gray(` (capped at ${limit} levels)`))
            : Text.red('false').append(Text.gray(' (uncapped Apotheic Enchanting)'));
        let msg = Text.gold('Fixed anvil cost is currently: ').append(statusText);

        reply(ctx, msg, false);
        return 1;
    }

    function showLimitStatus(ctx) {
        let server = ctx.source.server;
        let limit = getAnvilCostLimit(server);
        let msg = Text.gold('Current anvil cost limit: ').append(Text.aqua(`${limit} levels`));

        reply(ctx, msg, false);
        return 1;
    }

    function showAnvilStatus(ctx) {
        let server = ctx.source.server;
        let enabled = isFixedCostEnabled(server);
        let limit = getAnvilCostLimit(server);

        let statusLine = enabled
            ? Text.green('ENABLED').append(Text.gray(` (capped at ${limit} levels)`))
            : Text.red('DISABLED').append(Text.gray(' (default Apothic uncapped)'));

        let header = Text.gold('=== PEAK Anvil Cost Configuration ===\n')
            .append(Text.yellow('Fixed Cost: ')).append(statusLine).append(Text.white('\n'))
            .append(Text.yellow('Max Level Cost: ')).append(Text.aqua(`${limit} levels\n`))
            .append(Text.yellow('Max Prior Work Penalty: ')).append(Text.aqua(`${Math.max(0, limit - 1)}\n`))
            .append(Text.gray('Usage:\n'))
            .append(Text.gray(' - /peak anvil cost fixed <true|false>\n'))
            .append(Text.gray(' - /peak anvil cost limit <levels>'));

        reply(ctx, header, false);
        return 1;
    }

    // Register strictly structured /peak anvil cost command tree
    event.register(
        Commands.literal('peak')
            .requires(src => src.hasPermission(2))
            .then(Commands.literal('anvil')
                .executes(ctx => showAnvilStatus(ctx))
                .then(Commands.literal('cost')
                    .executes(ctx => showAnvilStatus(ctx))
                    .then(Commands.literal('fixed')
                        .executes(ctx => showFixedStatus(ctx))
                        .then(Commands.argument('enabled', Arguments.BOOLEAN.create(event))
                            .executes(ctx => setFixedCost(ctx, Arguments.BOOLEAN.getResult(ctx, 'enabled')))))
                    .then(Commands.literal('limit')
                        .executes(ctx => showLimitStatus(ctx))
                        .then(Commands.argument('levels', Arguments.INTEGER.create(event))
                            .executes(ctx => setCostLimit(ctx, Arguments.INTEGER.getResult(ctx, 'levels')))))))
    );
});

console.log('[PEAK Expert Mode] Script 64: Anvil Cost Cap & Management loaded!');

})();
