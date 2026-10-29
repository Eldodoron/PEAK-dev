// ==========================================
// PEAK MODPACK — SCRIPT 65
// SABLE / AERONAUTICS PHYSICS RATE & SOLVER ENFORCEMENT
// ==========================================
// Sable defaults to 2 substeps per tick (40 steps/s) and 18 solver iterations.
// It does not persist in-game options menu adjustments across reloads.
// This script enforces 1 substep/tick (20 steps/s minimum) and 8 solver iterations
// for optimal performance, persists custom rates in server persistent data,
// and exposes management via:
// /peak physics steps [1-10]
// ==========================================

(() => {

let $SubLevelContainer = null;
try {
    $SubLevelContainer = Java.loadClass('dev.ryanhcode.sable.api.sublevel.SubLevelContainer');
} catch (e) {
    // Sable not present in current environment
}

const DEFAULT_SUBSTEPS = 1; // 1 substep/tick = 20 physics steps/second (minimum)
const TARGET_SOLVER_ITERATIONS = 8; // Optimized from default 18 to reduce CPU/memory thrashing

function getTargetSubsteps(server) {
    if (!server) return DEFAULT_SUBSTEPS;
    let p = server.persistentData;
    if (p && p.contains('peak_physics_substeps')) {
        let val = p.getInt('peak_physics_substeps');
        if (val >= 1 && val <= 10) return val;
    }
    return DEFAULT_SUBSTEPS;
}

function applyPhysicsSettingsToLevel(level, substeps) {
    if (!level || level.isClientSide() || !$SubLevelContainer) return;
    try {
        let container = $SubLevelContainer.getContainer(level);
        if (!container) return;
        let system = container.physicsSystem();
        if (!system) return;
        let config = system.getConfig();
        if (config) {
            let updated = false;
            if (config.substepsPerTick !== substeps) {
                config.substepsPerTick = substeps;
                updated = true;
            }
            if (config.solverIterations !== TARGET_SOLVER_ITERATIONS) {
                config.solverIterations = TARGET_SOLVER_ITERATIONS;
                updated = true;
            }
            if (updated) {
                system.onConfigUpdated();
            }
        }
    } catch (e) {
        // Safe fallback if internal structure changes
    }
}

function applyPhysicsSettings(server, substeps) {
    if (!server) return;
    try {
        server.getAllLevels().forEach(level => {
            applyPhysicsSettingsToLevel(level, substeps);
        });
    } catch (e) {
        // Safe fallback
    }
    // Command fallbacks ensure internal server state synchronization
    server.runCommandSilent(`sable debug substeps ${substeps}`);
    server.runCommandSilent(`sable debug solver_iterations ${TARGET_SOLVER_ITERATIONS}`);
}

ServerEvents.loaded(event => {
    let server = event.server;
    let target = getTargetSubsteps(server);
    applyPhysicsSettings(server, target);
});

NativeEvents.onEvent('net.neoforged.neoforge.event.level.LevelEvent$Load', event => {
    let level = event.getLevel();
    if (!level || level.isClientSide()) return;
    try {
        let server = level.getServer();
        if (!server) return;
        let target = getTargetSubsteps(server);
        applyPhysicsSettingsToLevel(level, target);
    } catch (e) {
        // Level load safety
    }
});

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

    function queryStatus(ctx) {
        let server = ctx.source.server;
        let substeps = getTargetSubsteps(server);
        let stepsPerSec = substeps * 20;
        reply(ctx, Component.literal('§e[PEAK Physics] §r')
            .append(Component.literal('§7Current rate: §r'))
            .append(Component.literal(`§a${substeps} substep${substeps > 1 ? 's' : ''}/tick (${stepsPerSec} steps/s)§r`))
            .append(Component.literal('§7 | Solver Iterations: §r'))
            .append(Component.literal(`§a${TARGET_SOLVER_ITERATIONS}§r`)), false);
        return 1;
    }

    function setRate(ctx, substeps) {
        let server = ctx.source.server;
        if (substeps < 1 || substeps > 10) {
            replyFailure(ctx, Component.literal('§c[PEAK Physics] Substeps must be between 1 and 10 (20 to 200 steps/s).§r'));
            return 0;
        }
        server.persistentData.putInt('peak_physics_substeps', substeps);
        applyPhysicsSettings(server, substeps);
        let stepsPerSec = substeps * 20;
        reply(ctx, Component.literal(`§a[PEAK Physics] Set physics rate to ${substeps} substep${substeps > 1 ? 's' : ''}/tick (${stepsPerSec} steps/s).§r`), true);
        return 1;
    }

    event.register(
        Commands.literal('peak')
            .requires(src => src.hasPermission(2))
            .then(Commands.literal('physics')
                .executes(ctx => queryStatus(ctx))
                .then(Commands.literal('steps')
                    .executes(ctx => queryStatus(ctx))
                    .then(Commands.argument('substeps', Arguments.INTEGER.create(event))
                        .executes(ctx => setRate(ctx, Arguments.INTEGER.getResult(ctx, 'substeps'))))
                )
            )
    );
});

console.log('[PEAK] Script 65: Sable / Aeronautics Physics Rate Enforcement loaded.');

})();
