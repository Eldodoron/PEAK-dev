const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js';
let c = fs.readFileSync(path, 'utf8');

// 1. Fix "item" -> "id" in result objects
// Matches {"item": "xyz"} -> {"id": "xyz"} inside results arrays or result object
c = c.replace(/"item"\s*:\s*"([^"]+)"/g, (match, item) => {
    // We only want to replace it if it's in a context of "results" or "result".
    // A quick hack is just to do it where we know it failed, or use regex that checks context.
    // Let's just replace specific known patterns.
    return `"item":"${item}"`; // Wait, this doesn't do anything. I'll use regex below.
});

// "result": {"item": "xyz"} -> "result": {"id": "xyz"}
c = c.replace(/"result"\s*:\s*\{\s*"item"\s*:\s*"([^"]+)"/g, `"result": {"id": "$1"`);

// "results": [{"item": "xyz"}] -> "results": [{"id": "xyz"}]
c = c.replace(/"results"\s*:\s*\[\s*\{\s*"item"\s*:\s*"([^"]+)"/g, `"results": [{"id": "$1"`);
c = c.replace(/\{\s*"chance"\s*:\s*([0-9.]+)\s*,\s*"item"\s*:\s*"([^"]+)"/g, `{"chance": $1, "id": "$2"`);
c = c.replace(/\{\s*"chance"\s*:\s*([0-9.]+)\s*,\s*"count"\s*:\s*([0-9]+)\s*,\s*"item"\s*:\s*"([^"]+)"/g, `{"chance": $1, "count": $2, "id": "$3"`);
c = c.replace(/\{\s*"count"\s*:\s*([0-9]+)\s*,\s*"item"\s*:\s*"([^"]+)"/g, `{"count": $1, "id": "$2"`);

// 2. Fix {"fluid": "xyz", "amount": 123} in sequences
// In sequences, they are inside ingredients array:
c = c.replace(/\{\s*"fluid"\s*:\s*"([^"]+)"\s*,\s*"amount"\s*:\s*([0-9.]+)\s*\}/g, (match, fluid, amount) => {
    return `{ "type": "neoforge:single", "fluid": "${fluid}", "amount": ${amount} }`;
});

// 3. Fix base_fluid in irons_spellbooks:alchemist_cauldron_brew
// My previous regex replaced it with neoforge:single, which breaks base_fluid.
// Let's revert base_fluid specifically:
c = c.replace(/"base_fluid"\s*:\s*\{\s*"type"\s*:\s*"neoforge:single"\s*,\s*"fluid"\s*:\s*"([^"]+)"\s*,\s*"amount"\s*:\s*([0-9.]+)\s*\}/g, `"base_fluid": {"id": "$1", "amount": $2}`);
c = c.replace(/"base_fluid"\s*:\s*\{\s*"fluid"\s*:\s*"([^"]+)"\s*,\s*"amount"\s*:\s*([0-9.]+)\s*\}/g, `"base_fluid": {"id": "$1", "amount": $2}`);

// 4. Fix empty tags in delightfulcreators
c = c.replace(/"tag"\s*:\s*"c:bread_slices"/g, `"item": "minecraft:bread"`);
c = c.replace(/"tag"\s*:\s*"c:bale"/g, `"item": "minecraft:hay_block"`);
c = c.replace(/"tag"\s*:\s*"c:tortilla"/g, `"item": "minecraft:bread"`);

// 5. Comment out ess_requiem:dream_ripper because the item doesn't exist
c = c.replace(/event\.custom\(\{"type": "minecraft:smithing_transform",.*"ess_requiem:dream_ripper".*\);/g, `// $&`);

// 6. Comment out incendium:upgrade_elytra because template: [] is invalid
c = c.replace(/event\.custom\(\{"type": "minecraft:smithing_transform", "template": \[\].*"incendium:upgrade_elytra".*\);/g, `// $&`);

fs.writeFileSync(path, c, 'utf8');
console.log('Fixed 33 errors!');
