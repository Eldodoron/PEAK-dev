ServerEvents.recipes(event => {
    let recipe = event.recipes.find(r => r.getId() == 'apothsiscreate:epic_to_mythic_material_sequenced');
    if (recipe) {
        console.log("FOUND RECIPE: " + recipe.getId());
    } else {
        console.log("RECIPE NOT FOUND IN MANAGER!");
    }
});
