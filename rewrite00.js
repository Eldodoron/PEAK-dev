const fs = require('fs');

let path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js';
let content = fs.readFileSync(path, 'utf8');

// Replace event.recipes.create with myCreate
content = content.replace(/event\.recipes\.create/g, 'myCreate');

let header = `
// Archivo generado automáticamente para corregir las recetas rotas de Create en 1.21.1
ServerEvents.recipes(event => {
    let myCreate = {
        mixing: (res, ing) => createRecipeBuilder(event, 'create:mixing', res, ing),
        compacting: (res, ing) => createRecipeBuilder(event, 'create:compacting', res, ing),
        filling: (res, ing) => createRecipeBuilder(event, 'create:filling', res, ing),
        emptying: (res, ing) => createRecipeBuilder(event, 'create:emptying', res, ing),
        pressing: (res, ing) => createRecipeBuilder(event, 'create:pressing', res, ing),
        crushing: (res, ing) => createRecipeBuilder(event, 'create:crushing', res, ing),
        cutting: (res, ing) => createRecipeBuilder(event, 'create:cutting', res, ing),
        deploying: (res, ing) => createRecipeBuilder(event, 'create:deploying', res, ing),
        haunting: (res, ing) => createRecipeBuilder(event, 'create:haunting', res, ing),
        splashing: (res, ing) => createRecipeBuilder(event, 'create:splashing', res, ing),
        mechanical_crafting: (res, ing) => createRecipeBuilder(event, 'create:mechanical_crafting', res, ing),
        sequenced_assembly: (res, ing) => createRecipeBuilder(event, 'create:sequenced_assembly', res, ing)
    };

    function createRecipeBuilder(event, type, results, ingredients) {
        let modifiers = {};
        let builder = {
            heated: function() { modifiers.heated = true; return this; },
            superheated: function() { modifiers.superheated = true; return this; },
            id: function(id) { modifiers.id = id; submit(); return this; }
        };
        
        let submitted = false;
        function submit() {
            if (submitted) return;
            submitted = true;
            
            let parseRes = (r) => {
                if (typeof r === 'string') {
                    let count = 1;
                    let id = r;
                    let match = r.match(/^([0-9]+(?:\\.[0-9]+)?)x (.*)/);
                    if (match) { count = parseInt(match[1]); id = match[2]; }
                    
                    if (id.includes('molten') || id.includes('water') || id.includes('lava') || id.includes('oil') || id.includes('chocolate') || id.includes('caramel') || id.includes('potion') || id.includes('ethanol') || id.includes('biodiesel') || id.includes('blood') || id.includes('ink') || id.includes('slurry') || id.includes('venom')) {
                        return { id: id, amount: count };
                    }
                    return { id: id, count: count };
                }
                if (r.fluid) return { id: r.fluid, amount: r.amount };
                if (r.item) return { id: r.item, count: r.count || 1 };
                return r;
            };
            
            let parseIng = (i) => {
                if (typeof i === 'string') {
                    if (i.startsWith('#')) return { tag: i.substring(1) };
                    let match = i.match(/^([0-9]+(?:\\.[0-9]+)?)x (.*)/);
                    if (match) {
                        let count = parseInt(match[1]);
                        let id = match[2];
                        if (id.startsWith('#')) return { tag: id.substring(1), count: count };
                        return { item: id, count: count };
                    }
                    return { item: i };
                }
                if (i.fluid) return { fluid: i.fluid, amount: i.amount };
                if (i.tag) return { tag: i.tag, amount: i.amount };
                if (i.item) return { item: i.item };
                if (Array.isArray(i)) return i.map(parseIng);
                return i;
            };
            
            let json = { type: type };
            if (ingredients !== undefined) {
                json.ingredients = Array.isArray(ingredients) ? ingredients.map(parseIng) : [parseIng(ingredients)];
            }
            if (results !== undefined) {
                json.results = Array.isArray(results) ? results.map(parseRes) : [parseRes(results)];
            }
            
            if (modifiers.heated) json.heatRequirement = 'heated';
            if (modifiers.superheated) json.heatRequirement = 'superheated';
            
            let recipe = event.custom(json);
            if (modifiers.id) recipe.id(modifiers.id);
        }
        return builder;
    }
`;

content = content.replace(/ServerEvents\.recipes\(event => \{/, header);

fs.writeFileSync(path, content, 'utf8');
console.log("Rewritten successfully!");
