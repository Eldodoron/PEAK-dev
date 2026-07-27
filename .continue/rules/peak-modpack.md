---
description: Reglas para el desarrollo del modpack PEAK (NeoForge 1.21.1)
globs: "**/*.js,**/*.json,**/*.toml,**/*.cfg"
---

# PEAK Modpack - Reglas de Desarrollo

## Contexto del Proyecto
- Modpack de Minecraft llamado **PEAK** en NeoForge 1.21.1
- Contiene 362+ mods
- Usa KubeJS para scripting personalizado (recipes, eventos, etc.)
- Prioridad absoluta: rendimiento y estabilidad

## Estructura de Archivos
- `minecraft/local/kubejs/startup_scripts/` → Scripts que corren al iniciar el juego (registros)
- `minecraft/local/kubejs/server_scripts/` → Scripts del servidor (recipes, eventos)
- `minecraft/local/kubejs/client_scripts/` → Scripts del cliente (UI, rendering)
- `minecraft/local/kubejs/assets/` → Recursos personalizados
- `minecraft/config/` → Configuraciones de mods (.toml, .json, .cfg)

## Reglas de KubeJS
- Usa la API de KubeJS para NeoForge 1.21.1 (no Forge legacy)
- Los event handlers deben ser eficientes, evita loops innecesarios
- Prefiere `event.remove({})` con filtros específicos en vez de iterar todos los recipes
- Siempre valida que los item IDs existan antes de usarlos (mod:item_name)

## Reglas de Configuración
- Archivos TOML: respeta la estructura existente del mod
- Archivos JSON: valida sintaxis antes de guardar
- No modifiques archivos dentro de `minecraft/mods/` directamente
- **Importante (Prism Launcher)**: La configuración de memoria, Java Path y JVM Arguments dentro de `instance.cfg` **será sobrescrita por el propio Prism Launcher** al iniciar el juego. Modificar `instance.cfg` directamente en el código no servirá de nada. En su lugar, el asistente **DEBE pedirle al usuario que aplique estos cambios manualmente** a través de la interfaz de usuario (UI) de Prism Launcher (Edit Instance -> Java).
- **Importante (ModernFix)**: El mixin `mixin.perf.dynamic_languages` **DEBE PERMANECER DESACTIVADO** (o ausente). Activarlo (`true`) provoca un crasheo inmediato del juego en esta instalación de NeoForge 1.21.1.

## Rendimiento y Optimización de Entidades
- Si una solución impacta TPS, descártala y busca alternativa
- Prefiere soluciones server-side sobre client-side cuando sea posible
- Evita scheduled ticks frecuentes en KubeJS
- **Distancia de Simulación:** Mantener la `Simulation Distance` en 5 o 6 chunks como máximo. Valores más altos ahogan la CPU procesando inteligencias artificiales complejas lejanas.
- **Rendimiento de Entidades (Hallazgos de Spark):**
  - **Guard Villagers y Aldeanos Vanilla:** Son los mayores destructores de CPU del modpack (suman hasta un 15% de uso del servidor). Limitar la cantidad de Guardias por zona es vital.
  - **Alex's Caves & Vampirism:** Las IA de vampiros y dinosaurios/monstruos consumen CPU moderada-alta (5% a 8%).
- **Gestión de RAM:** En sistemas con 64 GB de RAM física, asignar entre 10 GB y 12 GB máximo (`-Xmx`). Recomendar siempre **G1GC** optimizado (-XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1).

