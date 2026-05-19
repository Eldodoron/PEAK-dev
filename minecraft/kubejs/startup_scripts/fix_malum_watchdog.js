// ==========================================
// PEAK EXPERT MODE — STARTUP SCRIPT
// EMERGENCY FIX: MALUM WATCHDOG HANGS
// ==========================================
// This script surgically unregisters Malum's RuntimeEvents class
// from the NeoForge game event bus. This removes the synchronous Weeping Well
// check on every living entity tick, completely eliminating 40s server watchdog
// deadlocks during far teleportation / chunk generation in dimensions like the End.
// ==========================================

try {
    Java.loadClass('net.neoforged.neoforge.common.NeoForge').EVENT_BUS.unregister(Java.loadClass('com.sammy.malum.events.RuntimeEvents'));
    console.info('[PEAK Fix] Surgically unregistered com.sammy.malum.events.RuntimeEvents to prevent watchdog hangs.');
} catch (err) {
    console.error('[PEAK Fix] Failed to unregister Malum RuntimeEvents: ' + err);
}
