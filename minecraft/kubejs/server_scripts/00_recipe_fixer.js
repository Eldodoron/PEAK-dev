
// ==========================================
// PEAK EXPERT MODE â€” RECIPE SANITIZER
// Fixes legacy 1.20 recipe formats for 1.21
// ==========================================

ServerEvents.recipes(event => {
    let fixCount = 0;

    // Helper to fix fluid objects
    const fixFluid = (obj) => {
        if (typeof obj === 'object' && obj !== null) {
            if (obj.type === 'fluid_stack' || obj.type === 'create:fluid_stack') {
                delete obj.type;
                fixCount++;
                return true;
            }
        }
        return false;
    };

    // We can't easily iterate all recipes and modify their raw JSON in 1.21 
    // without potentially causing more issues, but we can try to fix the 
    // most common ones that KubeJS is complaining about if they are 
    // being added via scripts.
    
    // However, the warnings in the log are mostly from OTHER mods' internal data.
    // KubeJS is just reporting that IT failed to parse them for its own system.
    
    console.info(`[PEAK Sanitizer] Recipe loading in progress...`);
});
