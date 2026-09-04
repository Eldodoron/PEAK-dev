let Minecraft = Java.loadClass('net.minecraft.client.Minecraft');

function triggerKeybind(keyName) {
    let mc = Minecraft.getInstance();
    let mappings = mc.options.keyMappings;
    for (let i = 0; i < mappings.length; i++) {
        if (mappings[i].getName() === keyName) {
            mc.setScreen(null);
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

NativeEvents.onEvent('net.neoforged.neoforge.client.event.ScreenEvent$Init$Post', event => {
    let screen = event.getScreen();
    let InventoryScreen = Java.loadClass('net.minecraft.client.gui.screens.inventory.InventoryScreen');
    if (screen instanceof InventoryScreen) {
        let Button = Java.loadClass('net.minecraft.client.gui.components.Button');
        let Component = Java.loadClass('net.minecraft.network.chat.Component');
        let width = screen.width;
        let height = screen.height;
        let guiLeft = Math.floor((width - 176) / 2);
        let guiTop = Math.floor((height - 166) / 2);
        
        let tombstoneBtn = Button.builder(Component.literal("T"), btn => {
            triggerKeybind("tombstone.message.knowledge_of_death");
        }).bounds(guiLeft - 22, guiTop + 10, 20, 20).build();
        
        let apothBtn = Button.builder(Component.literal("A"), btn => {
            triggerKeybind("key.apotheosis.open_world_tier_select");
        }).bounds(guiLeft - 22, guiTop + 35, 20, 20).build();
        
        event.addListener(tombstoneBtn);
        event.addListener(apothBtn);
    }
});
