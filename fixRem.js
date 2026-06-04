const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js';
let c = fs.readFileSync(path, 'utf8');

// 1. Fix Fluid.of('#c:...')
c = c.replace(/Fluid\.of\('#([a-z0-9_:]+)',\s*([0-9]+)\)/g, "{ type: 'neoforge:tag', tag: '$1', amount: $2 }");

// 2. Fix create.filling outputs getting confused as fluids
c = c.replace(/event\.recipes\.create\.filling\('1x ([a-z0-9_:]+)',/g, "event.recipes.create.filling(Item.of('$1'),");

// 3. Fix the remaining sequenced assemblies
let i = 0;
let newC = "";
while (i < c.length) {
    let match = c.substring(i).match(/event\.recipes\.create\.sequenced_assembly\([\s\S]*?\.id\('[^']+'\);/);
    if (match) {
        let block = match[0];
        let idx = c.substring(i).indexOf(block);
        newC += c.substring(i, i + idx);
        
        let transMatch = block.match(/\.transitionalItem\('([^']+)'\)/);
        let loopsMatch = block.match(/\.loops\(([0-9]+)\)/);
        let idMatch = block.match(/\.id\('([^']+)'\)/);
        let inputMatch = block.match(/,\s*'([^']+)',\s*\[/);
        
        if (inputMatch) {
            let inputItem = inputMatch[1];
            
            // Extract the result array!
            // It looks like: [CreateItem.of('apotheosis:common_material', 0.85), CreateItem.of('minecraft:gold_nugget', 0.15)]
            let resultArrMatch = block.match(/sequenced_assembly\(\s*\[([^\]]+)\],\s*'[^']+',/);
            let resultJson = "[{ id: 'ERROR' }]"; // fallback
            if (resultArrMatch) {
                let inner = resultArrMatch[1];
                let chunks = [...inner.matchAll(/CreateItem\.of\('([^']+)',\s*([0-9.]+)\)/g)];
                let resArr = chunks.map(m => `{ id: "${m[1]}", chance: ${m[2]} }`);
                resultJson = `[${resArr.join(", ")}]`;
            } else {
                let simpleResultMatch = block.match(/sequenced_assembly\(\s*'([^']+)'\s*,\s*'([^']+)'\s*,/);
                if (simpleResultMatch) {
                    resultJson = `[{ id: "${simpleResultMatch[1]}" }]`;
                }
            }
            
            let seqMatch = block.match(/,\s*(\[[\s\S]*?\])\s*\)\.transitionalItem/);
            let seqStr = seqMatch[1];
            seqStr = seqStr.replace(/event\.recipes\.create\.([a-z_]+)\('([^']+)',\s*\['([^']+)',\s*'([^']+)'\]\)/g, `{ type: 'create:$1', ingredients: [{ item: '$3' }, { item: '$4' }], results: [{ id: '$2' }] }`);
            seqStr = seqStr.replace(/event\.recipes\.create\.([a-z_]+)\('([^']+)',\s*'([^']+)'\)/g, `{ type: 'create:$1', ingredients: [{ item: '$3' }], results: [{ id: '$2' }] }`);
            
            let customJson = `    event.custom({
        type: "create:sequenced_assembly",
        ingredient: { item: "${inputItem}" },
        transitionalItem: { item: "${transMatch[1]}" },
        sequence: ${seqStr},
        results: ${resultJson},
        loops: ${loopsMatch[1]}
    }).id('${idMatch[1]}');`;
            
            newC += customJson;
        } else {
            newC += block;
        }
        i += idx + block.length;
    } else {
        newC += c.substring(i);
        break;
    }
}

fs.writeFileSync(path, newC, 'utf8');
console.log('Fixed remaining sequences and fluid issues!');
