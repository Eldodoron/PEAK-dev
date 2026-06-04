const fs = require('fs');
const path = 'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js';
let content = fs.readFileSync(path, 'utf8');

// The previous script wrote { tag: '$1', amount: $2 }
// Let's replace any instance of { tag: '...', amount: ... } that came from Fluid.of (which means they are fluid tags)
// Wait, the previous script replaced Fluid.of('#tag', 100) with { tag: 'tag', amount: 100 }
// So we just replace { tag: ' with { fluidTag: '
content = content.replace(/\{ tag: '([^']+)', amount: (\d+) \}/g, "{ fluidTag: '$1', amount: $2 }");

// And update myCreate's parseIng as well so it propagates fluidTag!
content = content.replace(/if \(i\.tag\) return \{ tag: i\.tag, amount: i\.amount \};/g, "if (i.fluidTag) return { fluidTag: i.fluidTag, amount: i.amount };\n                if (i.tag) return { tag: i.tag, amount: i.amount };");

fs.writeFileSync(path, content, 'utf8');
console.log('Fixed fluidTags');
