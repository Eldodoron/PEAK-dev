NativeEvents.onEvent('net.neoforged.neoforge.client.event.ScreenEvent$Init$Post', event => {
    let screen = event.getScreen();
    if (screen.getClass().getName() === 'net.minecraft.client.gui.screens.inventory.InventoryScreen') {
        
        let Button = Java.loadClass('net.minecraft.client.gui.components.Button');
        let Component = Java.loadClass('net.minecraft.network.chat.Component');
        let Minecraft = Java.loadClass('net.minecraft.client.Minecraft');
        
        let width = screen.width;
        let height = screen.height;
        let guiLeft = Math.floor((width - 176) / 2);
        let guiTop = Math.floor((height - 166) / 2);
        
        function triggerKeybind(keyName) {
            let mc = Minecraft.getInstance();
            let mappings = mc.options.keyMappings;
            for (let i = 0; i < mappings.length; i++) {
                if (mappings[i].getName() === keyName) {
                    // Close the inventory screen first so the keybind can be processed in the game tick
                    mc.setScreen(null);
                    
                    // Increment the internal click count so the game thinks the key was just pressed
                    try {
                        mappings[i].clickCount++;
                    } catch (e) {
                        try {
                            mappings[i].setDown(true);
                        } catch (e2) {}
                    }
                    return;
                }
            }
        }
        
        // Tombstone button
        let tombstoneBtn = Button.builder(Component.literal("T"), btn => {
            triggerKeybind("tombstone.message.knowledge_of_death");
        }).bounds(guiLeft - 22, guiTop + 10, 20, 20).build();
        
        // Apotheosis button
        let apothBtn = Button.builder(Component.literal("A"), btn => {
            triggerKeybind("key.apotheosis.open_world_tier_select");
        }).bounds(guiLeft - 22, guiTop + 35, 20, 20).build();
        
        event.addListener(tombstoneBtn);
        event.addListener(apothBtn);
    }
});
