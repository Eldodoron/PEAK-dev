PlayerEvents.advancement(event => {
    console.log("=== ADVANCEMENT EVENT TRIGGERED ===");
    try {
        console.log("Event object keys: " + Object.keys(event));
        if (event.advancement) {
            console.log("Advancement class: " + event.advancement.getClass().getName());
            console.log("Advancement keys: " + Object.keys(event.advancement));
            
            // Try different ways to get ID
            try { console.log("advancement.id: " + event.advancement.id); } catch(e) {}
            try { console.log("advancement.getId(): " + event.getAdvancement().getId()); } catch(e) {}
        }
    } catch(e) {
        console.error("Error in test script: " + e);
    }
});
