// --- UNIFY & INTEGRATE ALL XP FLUIDS (CREATE, SOPHISTICATED, RELIQUARY, ENDER IO, PNEUMATICCRAFT) ---

ServerEvents.tags('fluid', event => {
    const xpFluids = [
        'create_enchantment_industry:experience',
        'sophisticatedcore:xp_still',
        'reliquary:xp_still',
        'enderio:fluid_xp_juice_still',
        'pneumaticcraft:memory_essence'
    ];

    // Add all fluids to standard NeoForge tags so all machines/tanks accept them universally
    event.add('c:experience', xpFluids);
    event.add('c:xp', xpFluids);
    event.add('c:liquid_experience', xpFluids);
});

ServerEvents.recipes(event => {
    const xpFluids = [
        'create_enchantment_industry:experience',
        'sophisticatedcore:xp_still',
        'reliquary:xp_still',
        'enderio:fluid_xp_juice_still',
        'pneumaticcraft:memory_essence'
    ];

    // Create 1:1 conversion recipes in Create Mixing (100mB -> 100mB)
    // Allows seamless conversion between any XP fluid type without loss
    xpFluids.forEach(targetFluid => {
        xpFluids.forEach(sourceFluid => {
            if (sourceFluid !== targetFluid) {
                event.recipes.create.mixing(
                    Fluid.of(targetFluid, 100),
                    [Fluid.of(sourceFluid, 100)]
                );
            }
        });
    });
});
