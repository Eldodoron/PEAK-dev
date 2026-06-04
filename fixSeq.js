const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js';
let c = fs.readFileSync(path, 'utf8');

let newC = "";
let i = 0;
while (i < c.length) {
    let match = c.substring(i).match(/event\.recipes\.create\.sequenced_assembly\([\s\S]*?\.id\('[^']+'\);/);
    if (match) {
        let block = match[0];
        let idx = c.substring(i).indexOf(block);
        newC += c.substring(i, i + idx);
        
        // Convert the block to event.custom
        // Extract parts
        let resultMatch = block.match(/sequenced_assembly\(\s*'([^']+)'\s*,\s*'([^']+)'\s*,/);
        if (resultMatch) {
            let result = resultMatch[1];
            let ingredient = resultMatch[2];
            
            let seqMatch = block.match(/,\s*(\[[\s\S]*?\])\s*\)\.transitionalItem/);
            let seqStr = seqMatch[1];
            
            // Fix event.recipes.create.deploying -> {type:"create:deploying"...}
            // Actually seqStr has both event.recipes.create... and raw JSON!
            seqStr = seqStr.replace(/event\.recipes\.create\.([a-z_]+)\('([^']+)',\s*\['([^']+)',\s*'([^']+)'\]\)/g, `{ type: 'create:$1', ingredients: [{ item: '$3' }, { item: '$4' }], results: [{ id: '$2' }] }`);
            seqStr = seqStr.replace(/event\.recipes\.create\.([a-z_]+)\('([^']+)',\s*'([^']+)'\)/g, `{ type: 'create:$1', ingredients: [{ item: '$3' }], results: [{ id: '$2' }] }`);
            
            let transMatch = block.match(/\.transitionalItem\('([^']+)'\)/);
            let loopsMatch = block.match(/\.loops\(([0-9]+)\)/);
            let idMatch = block.match(/\.id\('([^']+)'\)/);
            
            let customJson = `    event.custom({
        type: "create:sequenced_assembly",
        ingredient: { item: "${ingredient}" },
        transitionalItem: { item: "${transMatch[1]}" },
        sequence: ${seqStr},
        results: [{ id: "${result}" }],
        loops: ${loopsMatch[1]}
    }).id('${idMatch[1]}');`;
            
            newC += customJson;
        } else {
            newC += block; // skip if it's the other sequence
        }
        i += idx + block.length;
    } else {
        newC += c.substring(i);
        break;
    }
}

fs.writeFileSync(path, newC, 'utf8');
console.log('Fixed sequences!');
