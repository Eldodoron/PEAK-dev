const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js';
let content = fs.readFileSync(path, 'utf8');

// For fluids in parseIng
content = content.replace(/if \(i\.fluid\) return \{ fluid: i\.fluid, amount: i\.amount \};/g, "if (i.fluid) return { type: 'neoforge:single', fluid: i.fluid, amount: i.amount };");

// For fluid tags in parseIng
content = content.replace(/if \(i\.fluidTag\) return \{ fluidTag: i\.fluidTag, amount: i\.amount \};/g, "if (i.fluidTag) return { type: 'neoforge:tag', tag: i.fluidTag, amount: i.amount };");

// Add cement to fluid list
content = content.replace(/includes\('venom'\)/g, "includes('venom') || id.includes('cement')");

fs.writeFileSync(path, content, 'utf8');
console.log('Fixed fluid ingredients in ' + path);
