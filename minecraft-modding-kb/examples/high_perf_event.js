// Minecraft 1.21.1 - NeoForge Mojmap - KubeJS Example
// Location: minecraft-modding-kb/examples/high_perf_event.js

// 1. REGISTRAR RECETAS (Server Script)
ServerEvents.recipes(event => {
    // Receta por forma (Shaped) que genera una espada especial con Data Components
    event.shaped(
        Item.of('minecraft:netherite_sword').withComponents({
            'minecraft:custom_name': '"§4PEAK Oblivion Blade§r"',
            'minecraft:lore': [
                '"§7A sword of ultimate power.§r"',
                '"§8Every swing shatters realities.§r"'
            ],
            'minecraft:enchantments': {
                levels: {
                    'minecraft:sharpness': 10,
                    'minecraft:fire_aspect': 2
                }
            },
            'minecraft:unbreakable': {}
        }),
        [
            ' N ',
            ' N ',
            ' S '
        ], {
            N: 'minecraft:netherite_ingot',
            S: 'minecraft:stick'
        }
    );
});

// 2. ESCUCHADOR DE EVENTOS CON CLÁUSULA DE ESCAPE (Guard Clause)
// El evento ItemEvents.crafted se ejecuta CADA VEZ que cualquier jugador craftea algo.
ItemEvents.crafted(event => {
    // ¡CLÁUSULA DE ESCAPE CRÍTICA!
    // Si el ítem crafteado NO es nuestra espada especial de PEAK, salimos de inmediato (microsegundos).
    if (event.item.id !== 'minecraft:netherite_sword') return;
    
    // Verificamos si tiene el nombre personalizado correcto para evitar falsos positivos
    let nameComponent = event.item.getComponents().get('minecraft:custom_name');
    if (!nameComponent || !nameComponent.toString().contains("Oblivion")) return;

    // Lógica pesada: solo se ejecuta cuando craftean esta espada específica.
    let player = event.player;
    let server = event.server;
    
    player.tell("§c[PEAK]§r ¡Has forjado la legendaria Oblivion Blade! Las fuerzas de la oscuridad tiemblan.");
    
    // Reproducimos un sonido dramático
    server.runCommandSilent(`execute at ${player.username} run playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1 0.5`);
});
