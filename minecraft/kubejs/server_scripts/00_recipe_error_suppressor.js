// 00_recipe_error_suppressor.js
// priority: 100
ServerEvents.recipes(event => {
    const brokenRecipes = [
    ];
    brokenRecipes.forEach(id => event.remove({ id: id }));
});

