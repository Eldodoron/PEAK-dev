const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js';
let c = fs.readFileSync(path, 'utf8');

c = c.replace(/if \(id\.includes\('molten'\) \|\| id\.includes\('water'\)/, "if (count > 99 || id.includes('elixir') || id.includes('milk') || id.includes('honey') || id.includes('molten') || id.includes('water')");

c = c.replace(/let recipe = event\.custom\(json\);/, `
            // Check for missing mods
            let jsonString = JSON.stringify(json);
            let missingMod = false;
            let regex = /"([a-z0-9_]+):[^"]+"/g;
            let m;
            while ((m = regex.exec(jsonString)) !== null) {
                let modId = m[1];
                if (modId !== 'c' && modId !== 'forge' && modId !== 'neoforge' && modId !== 'minecraft' && modId !== 'create') {
                    if (!Platform.isLoaded(modId)) {
                        missingMod = true;
                        break;
                    }
                }
            }
            if (missingMod) return;
            let recipe = event.custom(json);
`);

fs.writeFileSync(path, c, 'utf8');
console.log('Fixed fluids 2 and missing mods');
