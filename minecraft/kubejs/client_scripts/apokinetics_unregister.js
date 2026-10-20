// priority: 100

// Unregister Apokinetics client donation prompt from NeoForge event bus
// to prevent donation prompts from firing on client tick across all worlds.

if (Platform.isLoaded('apokinetics')) {
    try {
        Java.loadClass('net.neoforged.neoforge.common.NeoForge').EVENT_BUS.unregister(
            Java.loadClass('com.fishguy129.apokinetics.client.DonationPromptClient')
        );
        console.info('[PEAK Fix] Unregistered com.fishguy129.apokinetics.client.DonationPromptClient to disable recurring donation prompts.');
    } catch (err) {
        console.error('[PEAK Fix] Failed to unregister Apokinetics donation prompt: ' + err);
    }
}
