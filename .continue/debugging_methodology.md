# Metodología de Debugging para Modpacks en Minecraft

Esta guía documenta el proceso mental estructurado y las mejores prácticas que utilizamos para investigar, aislar y solucionar errores y crasheos en el desarrollo de modpacks (especialmente utilizando KubeJS y NeoForge).

## 1. Identificación de la Causa Raíz (Root Cause Analysis)
El primer paso ante cualquier error, ya sea un crasheo del servidor o cientos de errores de recetas en pantalla, es **leer los registros (logs)** fríamente.

> [!TIP]
> **Crash Reports:** Nunca te quedes solo con el final del documento. El verdadero motivo del crasheo (la *Exception*) siempre está en las primeras 20-30 líneas.
> **Logs de KubeJS:** Cuando hay errores masivos de recetas, el `latest.log` revelará un patrón. En nuestro caso, descubrimos que los datapacks de la versión 1.20 estaban utilizando variables deprecadas (`transitionalItem` vs `transitional_item`) en la versión 1.21.

## 2. Aislamiento del Problema
Una vez detectado el error, hay que aislar a los culpables. Esto requiere entender el ecosistema de mods:
- **¿Es un error de interacción?** (Ejemplo: *Apotheosis* intentando equipar un arma melee a un *Illusioner* de *Friends&Foes*, el cual tiene una IA programada exclusivamente para disparar arcos).
- **¿Es un error de motor?** (Ejemplo: Un cambio en el motor interno de Forge/NeoForge sobre cómo se declaran los fluidos en recetas).

Aislar el problema previene soluciones destructivas, como eliminar mods enteros innecesariamente.

## 3. Intervención Quirúrgica con KubeJS
KubeJS es extremadamente poderoso y nos permite solucionar casi cualquier conflicto del ecosistema inyectando código en el momento exacto.

- **Reescritura en lugar de Eliminación:** En vez de eliminar mods porque sus recetas están rotas, creamos scripts que purgan específicamente sus recetas corruptas (`event.remove()`) e inyectan versiones sanas con sintaxis moderna nativa de KubeJS.
- **Intercepción de Entidades:** Para crasheos generados por entidades corruptas en el mundo (como el Ilusionista), no es necesario corromper el `level.dat` ni borrar la región entera. Utilizamos eventos como `EntityEvents.spawned` para interceptar la entidad en memoria una fracción de segundo antes de que comience a existir (tickear) y "sanarla" (quitándole el arma prohibida).

## 4. Arquitectura Basada en Eventos (Event-Driven vs Loops)
> [!IMPORTANT]
> El rendimiento del servidor (TPS) es sagrado.

- **Evitar los Bucles (Loops):** Escanear el mundo cada 10 ticks con `ServerEvents.tick` para buscar mobs bugueados funciona, pero escala terriblemente mal y causa lag a largo plazo.
- **Eventos Puros:** La mejor metodología dicta usar eventos. `EntityEvents.spawned` solo consume recursos en el microsegundo exacto en que un mob es cargado o generado. Esta es la forma más elegante y eficiente de arreglar entidades y bloques defectuosos.

## 5. Automatización de Tareas Masivas
Enfrentarse a 280 recetas rotas o 40 mejoras de mochilas requeriría horas de programación manual y sería propenso a fallas tipográficas.

La metodología dicta **programar para programar**. Si la tarea es repetitiva, utilizamos pequeños scripts auxiliares (en Python u otras herramientas) que escaneen los archivos originales y auto-generen los scripts de KubeJS perfectamente formateados (`20_fixed_datapacks.js` o `21_backpack_upgrades.js`).

---
**Resumen del Flujo Mental:**
`Leer Logs` ➡️ `Encontrar el Patrón/Conflicto` ➡️ `Diseñar un Fix Quirúrgico (KubeJS)` ➡️ `Optimizar a Nivel de Evento` ➡️ `Automatizar el Código Masivo` ➡️ `Probar en Juego`.
