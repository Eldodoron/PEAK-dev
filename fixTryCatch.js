const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js';
let c = fs.readFileSync(path, 'utf8');

c = c.replace(/let recipe = event\.custom\(json\);\s*if \(modifiers\.id\) recipe\.id\(modifiers\.id\);/,
`try {
                let recipe = event.custom(json);
                if (modifiers.id) recipe.id(modifiers.id);
            } catch (e) {
                console.warn('[Recipe Error Suppressor] Suppressed error for recipe ' + (modifiers.id || 'unknown') + ': ' + e);
            }`);

fs.writeFileSync(path, c, 'utf8');
console.log('Added try-catch to event.custom');
