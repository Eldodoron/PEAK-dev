// Minecraft 1.21.1 - NeoForge Mojmap - KubeJS Example
// Location: minecraft-modding-kb/examples/component_item.js

// REGISTRO EN STARTUP (Startup Script)
StartupEvents.registry('item', event => {
    // Registrar un material de crafteo especial para el modpack
    event.create('peak_core')
        .displayName('§6Núcleo del Destino (PEAK Core)§r')
        .tooltip('§7Un núcleo inestable de energía cuántica.§r')
        .tooltip('§8Utilizado para crafteos de tier final.§r')
        .rarity('epic')
        .glow(true)
        .maxStackSize(16);
});

StartupEvents.registry('block', event => {
    // Registrar un bloque funcional o decorativo para el modpack
    event.create('peak_stabilizer')
        .displayName('§bEstabilizador Cuántico PEAK§r')
        .soundType('metal')
        .hardness(5.0)
        .resistance(10.0)
        .requiresTool(true)
        .tagBlock('minecraft:mineable/pickaxe')
        .tagBlock('minecraft:needs_diamond_tool')
        .lightLevel(0.8); // Brilla suavemente en la oscuridad
});
