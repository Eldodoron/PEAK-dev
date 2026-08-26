// Twilight Forest instant portal teleportation rule
ServerEvents.loaded(event => {
    event.server.runCommandSilent('gamerule playersTfPortalDefaultDelay 0');
    event.server.runCommandSilent('gamerule playersTfPortalCreativeDelay 0');
});
