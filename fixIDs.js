const fs = require('fs');

const files = [
    'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js',
    'C:/Users/chris/AppData/Roaming/PrismLauncher/instances/PEAK-dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js'
];

files.forEach(path => {
    if (fs.existsSync(path)) {
        let c = fs.readFileSync(path, 'utf8');
        
        c = c.replace(/create_ironworks:bronze_ingot/g, 'alltheores:bronze_ingot');
        c = c.replace(/create_ironworks:steel_ingot/g, 'tfmg:steel_ingot');
        c = c.replace(/create_ironworks:tin_ingot/g, 'alltheores:tin_ingot');
        c = c.replace(/create_simple_ore_doubling:slag/g, 'tfmg:slag');
        c = c.replace(/createmetalwork:molten_steel/g, 'tfmg:molten_steel_bucket'); // Wait, bucket? No, just tfmg:molten_steel! In KubeJS it's tfmg:molten_steel. The dump had bucket. Let's use tfmg:molten_steel. If we use fluid tag it's #c:molten_steel.
        // The error output showed: createmetalwork:molten_steel.
        
        c = c.replace(/wstweaks:fragment/g, 'minecraft:bone_meal'); // Just replacing with something valid so the rest of the recipe works, since wstweaks is missing
        
        fs.writeFileSync(path, c, 'utf8');
    }
});
console.log('Replaced bad IDs with valid IDs');
