const fs = require('fs');
const path = 'minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js';
let content = fs.readFileSync(path, 'utf8');

content = content.replace(/Fluid\.of\('#([^']+)',\s*(\d+)\)/g, "{ tag: '$1', amount: $2 }");
content = content.replace(/Fluid\.of\('([^#][^']+)',\s*(\d+)\)/g, "{ fluid: '$1', amount: $2 }");

fs.writeFileSync(path, content, 'utf8');
console.log('Done!');
