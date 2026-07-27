RecipeViewerEvents.removeEntries('item', event => {
    // Hide the player blimp from JEI/EMI so players don't see it as an obtainable item
    event.hide('raidsenhanced:player_blimp');
});
