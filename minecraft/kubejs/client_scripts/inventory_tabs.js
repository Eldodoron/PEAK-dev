let Minecraft = Java.loadClass('net.minecraft.client.Minecraft');

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
        
        let builder = Button.builder(Component.literal("A"), btn => {
            try {
                let WorldTierSelectScreen = Java.loadClass('dev.shadowsoffire.apotheosis.client.WorldTierSelectScreen');
                Minecraft.getInstance().setScreen(new WorldTierSelectScreen());
            } catch (err) {
                console.error("Failed to open Apotheosis World Tier Select Screen: " + err);
            }
        }).bounds(guiLeft - 22, guiTop + 10, 20, 20);

        try {
            let Tooltip = Java.loadClass('net.minecraft.client.gui.components.Tooltip');
            builder.tooltip(Tooltip.create(Component.translatable("title.apotheosis.select_world_tier")));
        } catch (err) {}

        let apothBtn = builder.build();
        event.addListener(apothBtn);
    }
});
