ServerEvents.recipes(event => {
    // QoL Shapeless recipe for Simulated's Rope Winch
    event.shapeless('simulated:rope_winch', [
        'simulated:rope_connector',
        'create:shaft'
    ]);
});
