ServerEvents.recipes(event => {
    // Modify Create Metalwork's single-ingot melting recipes to require 'superheated' (Blaze Cake) instead of 'heated'.
    // This resolves the conflict with standard Create Brass alloying where 'heated' would melt copper before it could alloy with zinc.
    // Ingot Melting
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_andesite_alloy', 111), ['create:andesite_alloy']).superheated().id('createmetalwork:create/mixing/ingot_melting/molten_andesite_alloy_from_melting');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_brass', 111), ['#c:ingots/brass']).superheated().id('createmetalwork:create/mixing/ingot_melting/molten_brass_from_melting');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_copper', 111), ['#c:ingots/copper']).superheated().id('createmetalwork:create/mixing/ingot_melting/molten_copper_from_melting');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_gold', 111), ['#c:ingots/gold']).superheated().id('createmetalwork:create/mixing/ingot_melting/molten_gold_from_melting');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_iron', 111), ['#c:ingots/iron']).superheated().id('createmetalwork:create/mixing/ingot_melting/molten_iron_from_melting');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_netherite', 111), ['#c:ingots/netherite']).superheated().id('createmetalwork:create/mixing/ingot_melting/molten_netherite_from_melting');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_zinc', 111), ['#c:ingots/zinc']).superheated().id('createmetalwork:create/mixing/ingot_melting/molten_zinc_from_melting');

    // Crushed Raw Materials Melting (also superheated to prevent normal heated basin conflict and fix empty tags)
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_copper', 222), ['create:crushed_raw_copper']).superheated().id('createmetalwork:create/mixing/molten_copper_from_mixing_heated');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_gold', 222), ['create:crushed_raw_gold']).superheated().id('createmetalwork:create/mixing/molten_gold_from_mixing_heated');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_iron', 222), ['create:crushed_raw_iron']).superheated().id('createmetalwork:create/mixing/molten_iron_from_mixing_heated');
    event.recipes.create.mixing(Fluid.of('createmetalwork:molten_zinc', 222), ['create:crushed_raw_zinc']).superheated().id('createmetalwork:create/mixing/molten_zinc_from_mixing_heated');
});
