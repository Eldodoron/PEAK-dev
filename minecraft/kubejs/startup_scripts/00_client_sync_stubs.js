// priority: 100

// Registers dummy particle types and sound events for client-side visual mods.
// Prevents NeoForge FrozenRegistrySyncCompletedPayload network disconnects
// when connecting between PEAK Lite and PEAK Dev clients over LAN or P2P multiplayer.

StartupEvents.registry('particle_type', event => {
    if (!Platform.isLoaded('particular')) {
        [
            'particular:acacia_leaf',
            'particular:azalea_leaf',
            'particular:bamboo_leaf',
            'particular:birch_leaf',
            'particular:brimwood_leaf',
            'particular:cascade',
            'particular:cave_dust',
            'particular:cuboid',
            'particular:dark_oak_leaf',
            'particular:ender_bubble',
            'particular:ender_bubble_pop',
            'particular:eucalyptus_leaf',
            'particular:firefly',
            'particular:golden_larch_leaf',
            'particular:jungle_leaf',
            'particular:kapok_leaf',
            'particular:larch_leaf',
            'particular:magnolia_leaf',
            'particular:mangrove_leaf',
            'particular:maple_leaf',
            'particular:oak_leaf',
            'particular:redwood_leaf',
            'particular:ru_baobab_leaf',
            'particular:ru_cypress_leaf',
            'particular:ru_palm_leaf',
            'particular:socotra_leaf',
            'particular:spruce_leaf',
            'particular:water_ripple',
            'particular:water_splash',
            'particular:water_splash_emitter',
            'particular:water_splash_foam',
            'particular:water_splash_ring',
            'particular:waterfall_spray',
            'particular:white_oak_leaf',
            'particular:white_spruce_leaf',
            'particular:willow_leaf',
            'particular:ww_baobab_leaf',
            'particular:ww_cypress_leaf',
            'particular:ww_palm_leaf'
        ].forEach(id => event.create(id));
    }

    if (!Platform.isLoaded('atmospherics')) {
        [
            'atmospherics:cave_fog',
            'atmospherics:deep_dark_fog',
            'atmospherics:desert_dust',
            'atmospherics:desert_dust_ground',
            'atmospherics:desert_sandstorm',
            'atmospherics:desert_sandstorm_feet',
            'atmospherics:desert_sandstorm_ground',
            'atmospherics:desert_sandstorm_haze',
            'atmospherics:desert_sandstorm_surface',
            'atmospherics:fog',
            'atmospherics:forest_fog',
            'atmospherics:pale_fog',
            'atmospherics:plains_fog',
            'atmospherics:rain_fog',
            'atmospherics:strong_wind_streak',
            'atmospherics:swamp_fog',
            'atmospherics:wind_streak'
        ].forEach(id => event.create(id));
    }

    if (!Platform.isLoaded('cosycritters')) {
        [
            'cosycritters:bird',
            'cosycritters:hat_man',
            'cosycritters:moth',
            'cosycritters:spider'
        ].forEach(id => event.create(id));
    }
});

StartupEvents.registry('sound_event', event => {
    if (!Platform.isLoaded('atmospherics')) {
        [
            'atmospherics:weather.desert_rain',
            'atmospherics:weather.desert_rain_loop',
            'atmospherics:weather.desert_rain_start',
            'atmospherics:weather.desert_thunder',
            'atmospherics:weather.desert_thunder_loop',
            'atmospherics:weather.desert_thunder_start'
        ].forEach(id => event.create(id));
    }
});
