const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js';
let c = fs.readFileSync(path, 'utf8');

// Fix the fluid tags that broke event.recipes.create.mixing
c = c.replace(/\{\s*type:\s*'neoforge:tag',\s*tag:\s*'c:molten_andesite',\s*amount:\s*([0-9.]+)\s*\}/g, "Fluid.of('createmetalwork:molten_andesite_alloy', $1)");
c = c.replace(/\{\s*type:\s*'neoforge:tag',\s*tag:\s*'c:milk',\s*amount:\s*([0-9.]+)\s*\}/g, "Fluid.of('minecraft:milk', $1)");
c = c.replace(/\{\s*type:\s*'neoforge:tag',\s*tag:\s*'c:honey',\s*amount:\s*([0-9.]+)\s*\}/g, "Fluid.of('create:honey', $1)");

// Fix any other stray { type: 'neoforge:tag', tag: 'c:...', amount: X } just in case
c = c.replace(/\{\s*type:\s*'neoforge:tag',\s*tag:\s*'c:([^']+)',\s*amount:\s*([0-9.]+)\s*\}/g, "Fluid.of('minecraft:$1', $2)");

// Fix the invalid JSON result structure in sequenced assembly outputs
// Sometimes it's {"chance": 120, "item": {"id": "foo"}}
c = c.replace(/"item"\s*:\s*\{\s*"id"\s*:\s*"([^"]+)"\s*\}/g, '"id": "$1"');

fs.writeFileSync(path, c, 'utf8');
console.log('Fixed fluid tags and item output format!');
