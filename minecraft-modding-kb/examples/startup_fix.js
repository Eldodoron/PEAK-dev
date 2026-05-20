// Minecraft 1.21.1 - NeoForge Mojmap - KubeJS Example
// Location: minecraft-modding-kb/examples/startup_fix.js

// DYNAMIC EVENT UNREGISTERING IN STARTUP (Startup Script)
// Útil para deshabilitar hilos de ticking rotos de mods de forma quirúrgica sin remover el mod completo.

StartupEvents.postInit(event => {
    console.log("§c[PEAK-FIX]§r Iniciando parcheo dinámico de eventos de compatibilidad...");

    try {
        // En NeoForge 1.21.1, los buses de eventos son de NeoForge EventBus
        let NeoForge = Java.loadClass('net.neoforged.neoforge.common.NeoForge');
        let EVENT_BUS = NeoForge.EVENT_BUS;
        
        // Identificar la clase que causa el problema de rendimiento o crash (ej. Malum runtime events)
        let TargetClass = 'com.sammy.malum.events.RuntimeEvents';
        
        // Obtenemos todos los listeners registrados
        let listenersField = EVENT_BUS.getClass().getDeclaredField('listeners');
        listenersField.setAccessible(true);
        let listeners = listenersField.get(EVENT_BUS); // Retorna un mapa o set de listeners

        let removedCount = 0;
        let iterator = listeners.iterator();
        
        while (iterator.hasNext()) {
            let listener = iterator.next();
            // Verificamos si el listener pertenece a la clase problemática
            if (listener.toString().contains(TargetClass)) {
                iterator.remove(); // Desregistramos el listener del bus en caliente
                removedCount++;
            }
        }
        
        console.log(`§c[PEAK-FIX]§r Se han deshabilitado quirúrgicamente ${removedCount} listeners de la clase ${TargetClass}. ¡Watchdog mitigado!`);
    } catch (e) {
        console.error("§c[PEAK-FIX]§r Error al aplicar el parche dinámico de eventos: " + e);
    }
});
