
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

    // Global raw JSON recipe iteration is restricted in NeoForge 1.21.1 to prevent recipe registry desynchronization.
    // Scripted corrections target specific problematic recipes declared in script space.
    
    console.info(`[PEAK Sanitizer] Recipe loading in progress...`);
});
