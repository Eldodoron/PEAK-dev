const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js';
let c = fs.readFileSync(path, 'utf8');

c = c.replace(/event\.recipes\.create\.mechanical_crafting\(\s*\[\]\s*,\s*\[\]\s*\)\.id\((['"][^'"]+['"])\)/g, "event.remove({id: $1})");
c = c.replace(/event\.recipes\.create\.sequenced_assembly\([^)]+,\s*\[\]\s*\)\.id\((['"][^'"]+['"])\)/g, "event.remove({id: $1})");

fs.writeFileSync(path, c, 'utf8');
console.log('Replaced empty recipes with event.remove()');
