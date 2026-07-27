ServerEvents.recipes(event => {
    // Remove Vampirism weapon coating recipes which flood JEI
    // They are usually of a specific type or shapeless crafting involving specific items
    
    // Remove custom weapon table recipes
    event.remove({ type: 'vampirism:weapon_table' });
    
    // If they are vanilla crafting recipes, we can remove them by their specific output tags if the recipe is from the vampirism mod
    event.remove({ mod: 'vampirism', type: 'minecraft:crafting_shapeless', output: '#c:swords' });
    event.remove({ mod: 'vampirism', type: 'minecraft:crafting_shapeless', output: '#c:tools' });
    event.remove({ mod: 'vampirism', type: 'minecraft:crafting_shaped', output: '#c:swords' });
    event.remove({ mod: 'vampirism', type: 'minecraft:crafting_shaped', output: '#c:tools' });
    
    // For good measure, we'll also specifically target the "weapon_coating" or similar named ones
    event.remove({ id: /vampirism:.*coating.*/ });
    event.remove({ id: /vampirism:.*weapon_table.*/ });
});
