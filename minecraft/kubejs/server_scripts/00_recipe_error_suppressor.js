// Archivo generado automáticamente para corregir las recetas rotas de Create en 1.21.1

// Archivo generado automáticamente para corregir las recetas rotas de Create en 1.21.1
ServerEvents.recipes(event => {
    let myCreate = {
        mixing: (res, ing) => createRecipeBuilder(event, 'create:mixing', res, ing),
        compacting: (res, ing) => createRecipeBuilder(event, 'create:compacting', res, ing),
        filling: (res, ing) => createRecipeBuilder(event, 'create:filling', res, ing),
        emptying: (res, ing) => createRecipeBuilder(event, 'create:emptying', res, ing),
        pressing: (res, ing) => createRecipeBuilder(event, 'create:pressing', res, ing),
        crushing: (res, ing) => createRecipeBuilder(event, 'create:crushing', res, ing),
        cutting: (res, ing) => createRecipeBuilder(event, 'create:cutting', res, ing),
        deploying: (res, ing) => createRecipeBuilder(event, 'create:deploying', res, ing),
        haunting: (res, ing) => createRecipeBuilder(event, 'create:haunting', res, ing),
        splashing: (res, ing) => createRecipeBuilder(event, 'create:splashing', res, ing),
        mechanical_crafting: (res, ing) => createRecipeBuilder(event, 'create:mechanical_crafting', res, ing),
        sequenced_assembly: (res, ing) => createRecipeBuilder(event, 'create:sequenced_assembly', res, ing)
    };

    function createRecipeBuilder(event, type, results, ingredients) {
        let modifiers = {};
        let builder = {
            heated: function() { modifiers.heated = true; return this; },
            superheated: function() { modifiers.superheated = true; return this; },
            id: function(id) { modifiers.id = id; submit(); return this; }
        };
        
        let submitted = false;
        function submit() {
            if (submitted) return;
            submitted = true;
            
            let parseRes = (r) => {
                if (typeof r === 'string') {
                    let count = 1;
                    let id = r;
                    let match = r.match(/^([0-9]+(?:\.[0-9]+)?)x (.*)/);
                    if (match) { count = parseInt(match[1]); id = match[2]; }
                    
                    if (count > 99 || id.includes('elixir') || id.includes('milk') || id.includes('honey') || id.includes('molten') || id.includes('water') || id.includes('lava') || id.includes('oil') || id.includes('chocolate') || id.includes('caramel') || id.includes('potion') || id.includes('ethanol') || id.includes('biodiesel') || id.includes('blood') || id.includes('ink') || id.includes('slurry') || id.includes('venom') || id.includes('cement')) {
                        return { id: id, amount: count };
                    }
                    return { id: id, count: count };
                }
                if (r.fluid) return { id: r.fluid, amount: r.amount };
                if (r.item) return { id: r.item, count: r.count || 1 };
                return r;
            };
            
            let parseIng = (i) => {
                if (typeof i === 'string') {
                    if (i.startsWith('#')) return { tag: i.substring(1) };
                    let match = i.match(/^([0-9]+(?:\.[0-9]+)?)x (.*)/);
                    if (match) {
                        let count = parseInt(match[1]);
                        let id = match[2];
                        if (id.startsWith('#')) return { tag: id.substring(1), count: count };
                        return { item: id, count: count };
                    }
                    return { item: i };
                }
                if (i.fluid) return { type: 'neoforge:single', fluid: i.fluid, amount: i.amount };
                if (i.fluidTag) return { type: 'neoforge:tag', tag: i.fluidTag, amount: i.amount };
                if (i.tag) return { tag: i.tag, amount: i.amount };
                if (i.item) return { item: i.item };
                if (Array.isArray(i)) return i.map(parseIng);
                return i;
            };
            
            let json = { type: type };
            if (ingredients !== undefined) {
                json.ingredients = Array.isArray(ingredients) ? ingredients.map(parseIng) : [parseIng(ingredients)];
            }
            if (results !== undefined) {
                json.results = Array.isArray(results) ? results.map(parseRes) : [parseRes(results)];
            }
            
            if (modifiers.heated) json.heatRequirement = 'heated';
            if (modifiers.superheated) json.heatRequirement = 'superheated';
            
            try {
                
            // Check for missing mods
            let jsonString = JSON.stringify(json);
            let missingMod = false;
            let regex = /"([a-z0-9_]+):[^"]+"/g;
            let m;
            while ((m = regex.exec(jsonString)) !== null) {
                let modId = m[1];
                if (modId !== 'c' && modId !== 'forge' && modId !== 'neoforge' && modId !== 'minecraft' && modId !== 'create') {
                    if (!Platform.isLoaded(modId)) {
                        missingMod = true;
                        break;
                    }
                }
            }
            if (missingMod) return;
            let recipe = event.custom(json);

                if (modifiers.id) recipe.id(modifiers.id);
            } catch (e) {
                console.warn('[Recipe Error Suppressor] Suppressed error for recipe ' + (modifiers.id || 'unknown') + ': ' + e);
            }
        }
        return builder;
    }

    myCreate.mixing('4x createdieselgenerators:asphalt_block', ['minecraft:gravel', 'minecraft:gravel', 'minecraft:sand', 'minecraft:sand', { fluid: 'createdieselgenerators:crude_oil', amount: 100 }]).id('createdieselgenerators:mixing/asphalt_block')
    myCreate.mixing('200x createdieselgenerators:biodiesel', [{ fluid: 'createdieselgenerators:plant_oil', amount: 100 }, { fluid: 'createdieselgenerators:ethanol', amount: 100 }]).id('createdieselgenerators:mixing/biodiesel')
    myCreate.mixing(['1000x createdieselgenerators:black_cement', 'minecraft:black_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:black_concrete_powder']).id('createdieselgenerators:mixing/black_concrete')
    myCreate.mixing(['1000x createdieselgenerators:blue_cement', 'minecraft:blue_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:blue_concrete_powder']).id('createdieselgenerators:mixing/blue_concrete')
    myCreate.mixing(['1000x createdieselgenerators:brown_cement', 'minecraft:brown_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:brown_concrete_powder']).id('createdieselgenerators:mixing/brown_concrete')
    myCreate.mixing(['1000x createdieselgenerators:cyan_cement', 'minecraft:cyan_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:cyan_concrete_powder']).id('createdieselgenerators:mixing/cyan_concrete')
    myCreate.mixing(['1000x createdieselgenerators:gray_cement', 'minecraft:gray_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:gray_concrete_powder']).id('createdieselgenerators:mixing/gray_concrete')
    myCreate.mixing(['1000x createdieselgenerators:green_cement', 'minecraft:green_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:green_concrete_powder']).id('createdieselgenerators:mixing/green_concrete')
    myCreate.mixing(['1000x createdieselgenerators:light_blue_cement', 'minecraft:light_blue_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:light_blue_concrete_powder']).id('createdieselgenerators:mixing/light_blue_concrete')
    myCreate.mixing(['1000x createdieselgenerators:light_gray_cement', 'minecraft:light_gray_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:light_gray_concrete_powder']).id('createdieselgenerators:mixing/light_gray_concrete')
    myCreate.mixing(['1000x createdieselgenerators:lime_cement', 'minecraft:lime_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:lime_concrete_powder']).id('createdieselgenerators:mixing/lime_concrete')
    myCreate.mixing(['1000x createdieselgenerators:magenta_cement', 'minecraft:magenta_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:magenta_concrete_powder']).id('createdieselgenerators:mixing/magenta_concrete')
    myCreate.mixing(['1000x createdieselgenerators:orange_cement', 'minecraft:orange_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:orange_concrete_powder']).id('createdieselgenerators:mixing/orange_concrete')
    myCreate.mixing(['1000x createdieselgenerators:pink_cement', 'minecraft:pink_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:pink_concrete_powder']).id('createdieselgenerators:mixing/pink_concrete')
    myCreate.mixing(['1000x createdieselgenerators:purple_cement', 'minecraft:purple_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:purple_concrete_powder']).id('createdieselgenerators:mixing/purple_concrete')
    myCreate.mixing(['1000x createdieselgenerators:red_cement', 'minecraft:red_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:red_concrete_powder']).id('createdieselgenerators:mixing/red_concrete')
    myCreate.mixing(['1000x createdieselgenerators:white_cement', 'minecraft:white_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:white_concrete_powder']).id('createdieselgenerators:mixing/white_concrete')
    myCreate.mixing(['1000x createdieselgenerators:yellow_cement', 'minecraft:yellow_concrete_powder'], [{ fluid: 'minecraft:water', amount: 100 }, 'minecraft:yellow_concrete_powder']).id('createdieselgenerators:mixing/yellow_concrete')
    myCreate.compacting('create:andesite_alloy', ['#c:crushed_raw_materials/andesite', '#c:andesite_alloy_nuggets']).heated().id('createmetalwork:create/compacting/andesite_alloy_from_compacting_heated')
    myCreate.compacting('create:andesite_alloy', [{ fluidTag: 'c:molten_andesite_alloy', amount: 111 }]).id('createmetalwork:create/compacting/andesite_alloy_from_compacting_molten')
    myCreate.compacting('create:brass_ingot', [{ fluidTag: 'c:molten_brass', amount: 111 }]).id('createmetalwork:create/compacting/brass_ingot_from_compacting_molten')
    myCreate.compacting('minecraft:copper_ingot', ['#c:crushed_raw_materials/copper']).heated().id('createmetalwork:create/compacting/copper_ingot_from_compacting_heated')
    myCreate.compacting('minecraft:copper_ingot', [{ fluidTag: 'c:molten_copper', amount: 111 }]).id('createmetalwork:create/compacting/copper_ingot_from_compacting_molten')
    myCreate.compacting('minecraft:gold_ingot', ['#c:crushed_raw_materials/gold']).heated().id('createmetalwork:create/compacting/gold_ingot_from_compacting_heated')
    myCreate.compacting('minecraft:gold_ingot', [{ fluidTag: 'c:molten_gold', amount: 111 }]).id('createmetalwork:create/compacting/gold_ingot_from_compacting_molten')
    myCreate.compacting('minecraft:iron_ingot', ['#c:crushed_raw_materials/iron']).heated().id('createmetalwork:create/compacting/iron_ingot_from_compacting_heated')
    myCreate.compacting('minecraft:iron_ingot', [{ fluidTag: 'c:molten_iron', amount: 111 }]).id('createmetalwork:create/compacting/iron_ingot_from_compacting_molten')
    myCreate.compacting('minecraft:netherite_ingot', [{ fluidTag: 'c:molten_netherite', amount: 111 }]).id('createmetalwork:create/compacting/netherite_ingot_from_compacting_molten')
    myCreate.compacting('create:zinc_ingot', ['#c:crushed_raw_materials/zinc']).heated().id('createmetalwork:create/compacting/zinc_ingot_from_compacting_heated')
    myCreate.compacting('create:zinc_ingot', [{ fluidTag: 'c:molten_zinc', amount: 111 }]).id('createmetalwork:create/compacting/zinc_ingot_from_compacting_molten')
    myCreate.compacting('create_ironworks:bronze_ingot', [{ fluidTag: 'c:molten_bronze', amount: 111 }]).id('createmetalwork:create/compat/create_ironworks/compacting/bronze_ingot_from_compacting_molten_bronze_ironworks')
    myCreate.compacting('create_ironworks:steel_ingot', [{ fluidTag: 'c:molten_steel', amount: 111 }]).id('createmetalwork:create/compat/create_ironworks/compacting/steel_ingot_from_compacting_molten_steel_ironworks')
    myCreate.compacting('create_ironworks:tin_ingot', ['#c:crushed_raw_materials/tin']).heated().id('createmetalwork:create/compat/create_ironworks/compacting/tin_ingot_from_compacting_heated_ironworks')
    myCreate.compacting('create_ironworks:tin_ingot', [{ fluidTag: 'c:molten_tin', amount: 111 }]).id('createmetalwork:create/compat/create_ironworks/compacting/tin_ingot_from_compacting_molten_tin_ironworks')
    myCreate.mixing('222x createmetalwork:molten_bronze', ['#c:crushed_raw_materials/copper', '#c:crushed_raw_materials/tin']).heated().id('createmetalwork:create/compat/create_ironworks/mixing/molten_bronze_from_mixing_heated')
    myCreate.mixing('111x createmetalwork:molten_steel', [{ fluidTag: 'c:molten_iron', amount: 111 }, '#minecraft:coal']).heated().id('createmetalwork:create/compat/create_ironworks/mixing/molten_steel_from_mixing_heated_molten')
    myCreate.mixing('222x createmetalwork:molten_tin', ['#c:crushed_raw_materials/tin']).heated().id('createmetalwork:create/compat/create_ironworks/mixing/molten_tin_from_mixing_heated')
    myCreate.mixing('111x createmetalwork:molten_bronze', ['#c:ingots/bronze']).heated().id('createmetalwork:create/compat/create_ironworks/mixing/ingot_melting/molten_bronze_from_melting')
    myCreate.mixing('111x createmetalwork:molten_steel', ['#c:ingots/steel']).heated().id('createmetalwork:create/compat/create_ironworks/mixing/ingot_melting/molten_steel_from_melting')
    myCreate.mixing('111x createmetalwork:molten_tin', ['#c:ingots/tin']).heated().id('createmetalwork:create/compat/create_ironworks/mixing/ingot_melting/molten_tin_from_melting')
    myCreate.compacting(['2x createmetalwork:crushed_andesite', 'create_simple_ore_doubling:slag'], ['minecraft:andesite', { fluid: 'minecraft:lava', amount: 50 }]).id('createmetalwork:create/compat/create_simple_ore_doubling/compacting/crushed_andesite_from_compacting')
    myCreate.compacting(['3x createmetalwork:crushed_andesite', 'create_simple_ore_doubling:slag'], ['minecraft:andesite']).heated().id('createmetalwork:create/compat/create_simple_ore_doubling/compacting/crushed_andesite_from_compacting_heated')
    myCreate.compacting(['2x createmetalwork:crushed_netherite_scrap', 'createmetalwork:crushed_netherite_scrap', 'create_simple_ore_doubling:slag', 'create_simple_ore_doubling:slag'], ['minecraft:netherite_scrap', { fluid: 'minecraft:lava', amount: 50 }]).id('createmetalwork:create/compat/create_simple_ore_doubling/compacting/crushed_netherite_scrap_from_compacting')
    myCreate.compacting(['3x createmetalwork:crushed_netherite_scrap', 'createmetalwork:crushed_netherite_scrap', 'create_simple_ore_doubling:slag', 'create_simple_ore_doubling:slag'], ['minecraft:netherite_scrap']).heated().id('createmetalwork:create/compat/create_simple_ore_doubling/compacting/crushed_netherite_scrap_from_compacting_heated')
    myCreate.compacting(['2x create:crushed_raw_tin', 'create_simple_ore_doubling:slag'], ['#c:raw_materials/tin', { fluid: 'minecraft:lava', amount: 50 }]).id('createmetalwork:create/compat/create_simple_ore_doubling/compacting/crushed_raw_tin_from_compacting')
    myCreate.compacting(['3x create:crushed_raw_tin', 'create_simple_ore_doubling:slag'], ['#c:raw_materials/tin']).heated().id('createmetalwork:create/compat/create_simple_ore_doubling/compacting/crushed_raw_tin_from_compacting_heated')
    myCreate.crushing(['9x createmetalwork:crushed_andesite', 'createmetalwork:crushed_andesite', 'create:experience_nugget'], ['minecraft:andesite']).id('createmetalwork:create/crushing/crushed_andesite_from_crushing')
    myCreate.crushing(['createmetalwork:crushed_netherite_scrap', 'createmetalwork:crushed_netherite_scrap', 'create:experience_nugget', 'create:experience_nugget'], ['minecraft:netherite_scrap']).id('createmetalwork:create/crushing/crushed_netherite_scrap_from_crushing')
    myCreate.crushing(['2x create:crushed_raw_gold', 'create:crushed_raw_gold', '2x create:experience_nugget', 'minecraft:netherrack'], ['minecraft:nether_gold_ore']).id('createmetalwork:create/crushing/crushed_raw_gold_from_crushing_nether_gold_ore')
    myCreate.mixing('222x createmetalwork:molten_andesite_alloy', ['#c:crushed_raw_materials/andesite', '#c:andesite_alloy_nuggets']).heated().id('createmetalwork:create/mixing/molten_andesite_alloy_from_mixing_heated')
    myCreate.mixing('222x createmetalwork:molten_andesite_alloy', [{ fluidTag: 'c:molten_andesite', amount: 111 }, { fluidTag: 'c:molten_iron', amount: 12 }]).heated().id('createmetalwork:create/mixing/molten_andesite_alloy_from_mixing_heated_molten_iron')
    myCreate.mixing('222x createmetalwork:molten_andesite_alloy', [{ fluidTag: 'c:molten_andesite', amount: 111 }, { fluidTag: 'c:molten_zinc', amount: 12 }]).heated().id('createmetalwork:create/mixing/molten_andesite_alloy_from_mixing_heated_molten_zinc')
    myCreate.mixing('222x createmetalwork:molten_andesite', ['#c:crushed_raw_materials/andesite']).heated().id('createmetalwork:create/mixing/molten_andesite_from_mixing_heated')
    myCreate.mixing('1000x createmetalwork:molten_andesite', ['minecraft:andesite']).heated().id('createmetalwork:create/mixing/molten_andesite_from_mixing_heated_alt')
    myCreate.mixing('444x createmetalwork:molten_brass', ['#c:crushed_raw_materials/copper', '#c:crushed_raw_materials/zinc']).heated().id('createmetalwork:create/mixing/molten_brass_from_mixing_heated')
    myCreate.mixing('444x createmetalwork:molten_brass', [{ fluidTag: 'c:molten_copper', amount: 111 }, { fluidTag: 'c:molten_zinc', amount: 111 }]).heated().id('createmetalwork:create/mixing/molten_brass_from_mixing_heated_molten')
    myCreate.mixing('222x createmetalwork:molten_copper', ['#c:crushed_raw_materials/copper']).heated().id('createmetalwork:create/mixing/molten_copper_from_mixing_heated')
    myCreate.mixing('222x createmetalwork:molten_gold', ['#c:crushed_raw_materials/gold']).heated().id('createmetalwork:create/mixing/molten_gold_from_mixing_heated')
    myCreate.mixing('222x createmetalwork:molten_iron', ['#c:crushed_raw_materials/iron']).heated().id('createmetalwork:create/mixing/molten_iron_from_mixing_heated')
    myCreate.mixing('222x createmetalwork:molten_netherite', ['#c:crushed_raw_materials/gold', '#c:crushed_raw_materials/gold', '#c:crushed_raw_materials/gold', '#c:crushed_raw_materials/gold', '#c:crushed_raw_materials/netherite_scrap', '#c:crushed_raw_materials/netherite_scrap', '#c:crushed_raw_materials/netherite_scrap', '#c:crushed_raw_materials/netherite_scrap']).heated().id('createmetalwork:create/mixing/molten_netherite_from_mixing_heated')
    myCreate.mixing('222x createmetalwork:molten_netherite', [{ fluidTag: 'c:molten_gold', amount: 444 }, '#c:crushed_raw_materials/netherite_scrap', '#c:crushed_raw_materials/netherite_scrap', '#c:crushed_raw_materials/netherite_scrap', '#c:crushed_raw_materials/netherite_scrap']).heated().id('createmetalwork:create/mixing/molten_netherite_from_mixing_heated_molten')
    myCreate.mixing('222x createmetalwork:molten_zinc', ['#c:crushed_raw_materials/zinc']).heated().id('createmetalwork:create/mixing/molten_zinc_from_mixing_heated')
    myCreate.mixing('111x createmetalwork:molten_andesite_alloy', ['create:andesite_alloy']).heated().id('createmetalwork:create/mixing/ingot_melting/molten_andesite_alloy_from_melting')
    myCreate.mixing('111x createmetalwork:molten_brass', ['#c:ingots/brass']).heated().id('createmetalwork:create/mixing/ingot_melting/molten_brass_from_melting')
    myCreate.mixing('111x createmetalwork:molten_copper', ['#c:ingots/copper']).heated().id('createmetalwork:create/mixing/ingot_melting/molten_copper_from_melting')
    myCreate.mixing('111x createmetalwork:molten_gold', ['#c:ingots/gold']).heated().id('createmetalwork:create/mixing/ingot_melting/molten_gold_from_melting')
    myCreate.mixing('111x createmetalwork:molten_iron', ['#c:ingots/iron']).heated().id('createmetalwork:create/mixing/ingot_melting/molten_iron_from_melting')
    myCreate.mixing('111x createmetalwork:molten_netherite', ['#c:ingots/netherite']).heated().id('createmetalwork:create/mixing/ingot_melting/molten_netherite_from_melting')
    myCreate.mixing('111x createmetalwork:molten_zinc', ['#c:ingots/zinc']).heated().id('createmetalwork:create/mixing/ingot_melting/molten_zinc_from_melting')
    myCreate.compacting('3.0x ae2:fluix_glass_cable', ['ae2:quartz_fiber', 'ae2:fluix_crystal']).heated().id('create_ae2recipes:compacting/fluix_glass_cable')
    myCreate.compacting('3.0x ae2:quartz_fiber', ['#c:glass_blocks', '#c:glass_blocks', '#c:glass_blocks', 'ae2:certus_quartz_dust', 'ae2:certus_quartz_dust']).heated().id('create_ae2recipes:compacting/quartz_fiber')
    myCreate.cutting('4x ae2:cable_anchor', ['#ae2:metal_ingots']).id('create_ae2recipes:cutting/cable_anchor')
    myCreate.deploying('ae2:fluix_covered_cable', ['ae2:fluix_glass_cable', '#minecraft:wool']).id('create_ae2recipes:deploying/cable/fluix_covered_cable')
    myCreate.deploying('ae2:fluix_smart_cable', ['ae2:fluix_covered_cable', 'ae2:semi_dark_monitor']).id('create_ae2recipes:deploying/cable/fluix_smart_cable')
    myCreate.deploying('ae2:fluix_smart_dense_cable', ['ae2:fluix_covered_dense_cable', 'ae2:semi_dark_monitor']).id('create_ae2recipes:deploying/cable/fluix_smart_dense_cable')
    myCreate.deploying('ae2:capacity_card', ['ae2:basic_card', [{'item': 'ae2:certus_quartz_crystal'}, {'item': 'ae2:charged_certus_quartz_crystal'}]]).id('create_ae2recipes:deploying/card/capacity_card')
    myCreate.deploying('ae2:crafting_card', ['ae2:basic_card', 'minecraft:crafting_table']).id('create_ae2recipes:deploying/card/crafting_card')
    myCreate.deploying('ae2:energy_card', ['ae2:advanced_card', 'ae2:dense_energy_cell']).id('create_ae2recipes:deploying/card/energy_card')
    myCreate.deploying('ae2:equal_distribution_card', ['ae2:advanced_card', 'ae2:calculation_processor']).id('create_ae2recipes:deploying/card/equal_distribution_card')
    myCreate.deploying('ae2:fuzzy_card', ['ae2:advanced_card', '#minecraft:wool']).id('create_ae2recipes:deploying/card/fuzzy_card')
    myCreate.deploying('ae2:inverter_card', ['ae2:advanced_card', 'minecraft:redstone_torch']).id('create_ae2recipes:deploying/card/inverter_card')
    myCreate.deploying('ae2:redstone_card', ['ae2:basic_card', 'minecraft:redstone_torch']).id('create_ae2recipes:deploying/card/redstone_card')
    myCreate.deploying('ae2:speed_card', ['ae2:advanced_card', 'ae2:fluix_crystal']).id('create_ae2recipes:deploying/card/speed_card')
    myCreate.deploying('ae2:void_card', ['ae2:basic_card', 'ae2:calculation_processor']).id('create_ae2recipes:deploying/card/void_card')
    myCreate.deploying('ae2:fluid_storage_cell_16k', ['ae2:fluid_cell_housing', 'ae2:cell_component_16k']).id('create_ae2recipes:deploying/cell/fluid_storage_cell_16k')
    myCreate.deploying('ae2:fluid_storage_cell_1k', ['ae2:fluid_cell_housing', 'ae2:cell_component_1k']).id('create_ae2recipes:deploying/cell/fluid_storage_cell_1k')
    myCreate.deploying('ae2:fluid_storage_cell_256k', ['ae2:fluid_cell_housing', 'ae2:cell_component_256k']).id('create_ae2recipes:deploying/cell/fluid_storage_cell_256k')
    myCreate.deploying('ae2:fluid_storage_cell_4k', ['ae2:fluid_cell_housing', 'ae2:cell_component_4k']).id('create_ae2recipes:deploying/cell/fluid_storage_cell_4k')
    myCreate.deploying('ae2:fluid_storage_cell_64k', ['ae2:fluid_cell_housing', 'ae2:cell_component_64k']).id('create_ae2recipes:deploying/cell/fluid_storage_cell_64k')
    myCreate.deploying('ae2:item_storage_cell_16k', ['ae2:item_cell_housing', 'ae2:cell_component_16k']).id('create_ae2recipes:deploying/cell/item_storage_cell_16k')
    myCreate.deploying('ae2:item_storage_cell_1k', ['ae2:item_cell_housing', 'ae2:cell_component_1k']).id('create_ae2recipes:deploying/cell/item_storage_cell_1k')
    myCreate.deploying('ae2:item_storage_cell_256k', ['ae2:item_cell_housing', 'ae2:cell_component_256k']).id('create_ae2recipes:deploying/cell/item_storage_cell_256k')
    myCreate.deploying('ae2:item_storage_cell_4k', ['ae2:item_cell_housing', 'ae2:cell_component_4k']).id('create_ae2recipes:deploying/cell/item_storage_cell_4k')
    myCreate.deploying('ae2:item_storage_cell_64k', ['ae2:item_cell_housing', 'ae2:cell_component_64k']).id('create_ae2recipes:deploying/cell/item_storage_cell_64k')
    myCreate.deploying('ae2:spatial_storage_cell_128', ['ae2:item_cell_housing', 'ae2:spatial_cell_component_128']).id('create_ae2recipes:deploying/cell/spatial_storage_cell_128')
    myCreate.deploying('ae2:spatial_storage_cell_16', ['ae2:item_cell_housing', 'ae2:spatial_cell_component_16']).id('create_ae2recipes:deploying/cell/spatial_storage_cell_16')
    myCreate.deploying('ae2:spatial_storage_cell_2', ['ae2:item_cell_housing', 'ae2:spatial_cell_component_2']).id('create_ae2recipes:deploying/cell/spatial_storage_cell_2')
    myCreate.deploying('ae2:view_cell', ['ae2:item_cell_housing', [{'item': 'ae2:certus_quartz_crystal'}, {'item': 'ae2:charged_certus_quartz_crystal'}]]).id('create_ae2recipes:deploying/cell/view_cell')
    myCreate.deploying('ae2:16k_crafting_storage', ['ae2:crafting_unit', 'ae2:cell_component_16k']).id('create_ae2recipes:deploying/craft_unit/16k_crafting_storage')
    myCreate.deploying('ae2:1k_crafting_storage', ['ae2:crafting_unit', 'ae2:cell_component_1k']).id('create_ae2recipes:deploying/craft_unit/1k_crafting_storage')
    myCreate.deploying('ae2:256k_crafting_storage', ['ae2:crafting_unit', 'ae2:cell_component_256k']).id('create_ae2recipes:deploying/craft_unit/256k_crafting_storage')
    myCreate.deploying('ae2:4k_crafting_storage', ['ae2:crafting_unit', 'ae2:cell_component_4k']).id('create_ae2recipes:deploying/craft_unit/4k_crafting_storage')
    myCreate.deploying('ae2:64k_crafting_storage', ['ae2:crafting_unit', 'ae2:cell_component_64k']).id('create_ae2recipes:deploying/craft_unit/64k_crafting_storage')
    myCreate.deploying('ae2:crafting_accelerator', ['ae2:crafting_unit', 'ae2:engineering_processor']).id('create_ae2recipes:deploying/craft_unit/crafting_accelerator')
    myCreate.deploying('ae2:crafting_monitor', ['ae2:crafting_unit', 'ae2:storage_monitor']).id('create_ae2recipes:deploying/craft_unit/crafting_monitor')
    myCreate.deploying('ae2:crafting_terminal', [[{'item': 'ae2:terminal'}], 'ae2:crafting_card']).id('create_ae2recipes:deploying/network/crafting_terminal')
    myCreate.deploying('ae2:energy_level_emitter', ['ae2:level_emitter', 'ae2:charged_certus_quartz_crystal']).id('create_ae2recipes:deploying/network/energy_level_emitter')
    myCreate.deploying('ae2:level_emitter', ['ae2:calculation_processor', 'minecraft:redstone_torch']).id('create_ae2recipes:deploying/network/level_emitter')
    myCreate.deploying('ae2:pattern_encoding_terminal', ['ae2:crafting_terminal', 'ae2:engineering_processor']).id('create_ae2recipes:deploying/network/pattern_encoding_terminal')
    myCreate.deploying('ae2:storage_bus', [[{'item': 'ae2:interface'}, {'item': 'ae2:cable_interface'}], 'minecraft:piston']).id('create_ae2recipes:deploying/network/storage_bus')
    myCreate.deploying('ae2:storage_monitor', [[{'item': 'ae2:monitor'}, {'item': 'ae2:dark_monitor'}, {'item': 'ae2:semi_dark_monitor'}], 'ae2:level_emitter']).id('create_ae2recipes:deploying/network/storage_monitor')
    myCreate.deploying('ae2:toggle_bus', ['ae2:fluix_glass_cable', 'create:powered_toggle_latch']).id('create_ae2recipes:deploying/network/toggle_bus')
    myCreate.deploying('ae2:calculation_processor_press', ['minecraft:iron_block', 'ae2:calculation_processor_press']).id('create_ae2recipes:deploying/processor/calculation_processer_press')
    myCreate.deploying('ae2:engineering_processor_press', ['minecraft:iron_block', 'ae2:engineering_processor_press']).id('create_ae2recipes:deploying/processor/engineering_processor_press')
    myCreate.deploying('ae2:logic_processor_press', ['minecraft:iron_block', 'ae2:logic_processor_press']).id('create_ae2recipes:deploying/processor/logic_processor_press')
    myCreate.deploying('ae2:printed_calculation_processor', ['ae2:certus_quartz_crystal', 'ae2:calculation_processor_press']).id('create_ae2recipes:deploying/processor/printed_calculation_processor')
    myCreate.deploying('ae2:printed_engineering_processor', ['minecraft:diamond', 'ae2:engineering_processor_press']).id('create_ae2recipes:deploying/processor/printed_engineering_processor')
    myCreate.deploying('ae2:printed_logic_processor', ['minecraft:gold_ingot', 'ae2:logic_processor_press']).id('create_ae2recipes:deploying/processor/printed_logic_processor')
    myCreate.deploying('ae2:printed_silicon', ['#c:silicon', 'ae2:silicon_press']).id('create_ae2recipes:deploying/processor/printed_silicon')
    myCreate.deploying('ae2:silicon_press', ['minecraft:iron_block', 'ae2:silicon_press']).id('create_ae2recipes:deploying/processor/silicon_press')
    myCreate.haunting('ae2:sky_stone_block', ['minecraft:iron_block']).id('create_ae2recipes:haunting/sky_stone_block')
    event.remove({id: 'create_ae2recipes:mechanical_crafting/conversion_monitor'})
    event.remove({id: 'create_ae2recipes:mechanical_crafting/pattern_access_terminal'})
    event.remove({id: 'create_ae2recipes:mechanical_crafting/terminal'})
    myCreate.mixing('minecraft:basalt', ['minecraft:calcite', 'minecraft:iron_ingot', { fluid: 'minecraft:lava', amount: 250 }]).id('create_ae2recipes:mixing/basalt')
    myCreate.mixing('2x ae2:certus_quartz_crystal', ['ae2:certus_quartz_dust', 'ae2:charged_certus_quartz_crystal', { fluid: 'minecraft:water', amount: 250 }]).id('create_ae2recipes:mixing/certus_quartz_crystal')
    myCreate.mixing('ae2:chipped_budding_quartz', ['ae2:damaged_budding_quartz', 'ae2:charged_certus_quartz_crystal', { fluid: 'minecraft:water', amount: 500 }]).id('create_ae2recipes:mixing/chipped_budding_quartz')
    myCreate.mixing('ae2:damaged_budding_quartz', ['ae2:quartz_block', 'ae2:charged_certus_quartz_crystal', { fluid: 'minecraft:water', amount: 500 }]).id('create_ae2recipes:mixing/damaged_budding_quartz')
    myCreate.mixing('ae2:flawed_budding_quartz', ['ae2:chipped_budding_quartz', 'ae2:charged_certus_quartz_crystal', { fluid: 'minecraft:water', amount: 500 }]).id('create_ae2recipes:mixing/flawed_budding_quartz')
    myCreate.mixing('ae2:flawless_budding_quartz', ['ae2:flawed_budding_quartz', 'ae2:fluix_pearl', 'create:rose_quartz', 'create:experience_nugget', 'minecraft:amethyst_block', { fluid: 'create:potion', amount: 1000 }]).superheated().id('create_ae2recipes:mixing/flawless_budding_quartz')
    myCreate.mixing('ae2:fluix_crystal', ['ae2:fluix_dust', 'ae2:charged_certus_quartz_crystal', { fluid: 'minecraft:water', amount: 250 }]).id('create_ae2recipes:mixing/fluix_crystal')
    myCreate.mixing('ae2:fluix_pearl', ['minecraft:ender_pearl', 'ae2:fluix_dust', 'ae2:fluix_dust', 'ae2:fluix_dust', 'ae2:fluix_dust', { fluid: 'minecraft:water', amount: 250 }]).superheated().id('create_ae2recipes:mixing/fluix_pearl')
    myCreate.mixing('2.0x ae2:quartz_glass', ['ae2:certus_quartz_dust', 'ae2:certus_quartz_dust', '#c:glass_blocks', '#c:glass_blocks']).heated().id('create_ae2recipes:mixing/quartz_glass')
    myCreate.mixing('ae2:quartz_vibrant_glass', ['ae2:quartz_glass', 'minecraft:glowstone_dust']).heated().id('create_ae2recipes:mixing/quartz_vibrant_glass')
    event.remove({id: 'create_ae2recipes:sequenced_assembly/advanced_card'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/basic_card'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/blank_pattern'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/calculation_processor'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/cell_component_16k'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/cell_component_1k'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/cell_component_256k'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/cell_component_4k'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/cell_component_64k'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/engineering_processor'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/fluid_cell_housing'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/item_cell_housing'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/logic_processor'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/spatial_cell_component_128'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/spatial_cell_component_16'})
    event.remove({id: 'create_ae2recipes:sequenced_assembly/spatial_cell_component_2'})
    myCreate.compacting('create_confectionery:bar_of_black_chocolate', [{ fluid: 'create_confectionery:black_chocolate', amount: 250 }]).id('create_confectionery:bar_of_black_chocolate_recipe')
    myCreate.compacting('create_confectionery:bar_of_caramel', [{ fluid: 'create_confectionery:caramel', amount: 250 }]).id('create_confectionery:bar_of_caramel_recipe')
    myCreate.compacting('create_confectionery:bar_of_ruby_chocolate', [{ fluid: 'create_confectionery:ruby_chocolate', amount: 250 }]).id('create_confectionery:bar_of_ruby_chocolate_recipe')
    myCreate.compacting('create_confectionery:bar_of_white_chocolate', [{ fluid: 'create_confectionery:white_chocolate', amount: 250 }]).id('create_confectionery:bar_of_white_chocolate_recipe')
    myCreate.filling('create_confectionery:black_chocolate_candy_1', ['create:bar_of_chocolate', { fluid: 'create_confectionery:black_chocolate', amount: 250 }]).id('create_confectionery:black_chocolate_candy_1_recipe')
    myCreate.filling('create_confectionery:black_chocolate_candy_2', ['create_confectionery:bar_of_white_chocolate', { fluid: 'create_confectionery:black_chocolate', amount: 250 }]).id('create_confectionery:black_chocolate_candy_2_recipe')
    myCreate.filling('create_confectionery:black_chocolate_candy_3', ['create_confectionery:bar_of_ruby_chocolate', { fluid: 'create_confectionery:black_chocolate', amount: 250 }]).id('create_confectionery:black_chocolate_candy_3_recipe')
    myCreate.filling('create_confectionery:black_chocolate_candy', ['create_confectionery:bar_of_caramel', { fluid: 'create_confectionery:black_chocolate', amount: 250 }]).id('create_confectionery:black_chocolate_candy_recipe')
    myCreate.emptying(['minecraft:bucket', '1000x create_confectionery:black_chocolate'], ['create_confectionery:black_chocolate_bucket']).id('create_confectionery:black_chocolate_emptying')
    myCreate.filling('create_confectionery:black_chocolate_glazed_berries', ['minecraft:sweet_berries', { fluid: 'create_confectionery:black_chocolate', amount: 250 }]).id('create_confectionery:black_chocolate_glazed_berries_recipe')
    myCreate.filling('create_confectionery:black_chocolate_glazed_marshmallow', ['create_confectionery:marshmallow', { fluid: 'create_confectionery:black_chocolate', amount: 250 }]).id('create_confectionery:black_chocolate_glazed_marshmallow_recipe')
    myCreate.mixing('250x create_confectionery:black_chocolate', ['minecraft:sugar', 'create_confectionery:cocoa_butter', 'minecraft:cocoa_beans', 'minecraft:cocoa_beans', { fluidTag: 'c:milk', amount: 250 }]).heated().id('create_confectionery:black_chocolate_recipe')
    myCreate.mixing('250x create_confectionery:black_chocolate', ['create_confectionery:bar_of_black_chocolate']).heated().id('create_confectionery:black_chocolate_recipe_2')
    myCreate.mixing('1000x create_confectionery:black_chocolate', ['create_confectionery:black_chocolate_bricks']).heated().id('create_confectionery:black_chocolate_recipe_3')
    myCreate.mixing('1000x create_confectionery:black_chocolate', ['create_confectionery:black_chocolate_bricks_stairs']).heated().id('create_confectionery:black_chocolate_recipe_4')
    myCreate.mixing('500x create_confectionery:black_chocolate', ['create_confectionery:black_chocolate_bricks_slab']).heated().id('create_confectionery:black_chocolate_recipe_5')
    myCreate.mixing('4x create_confectionery:candy_cane', ['minecraft:sugar', 'minecraft:sugar', 'minecraft:slime_ball', { fluid: 'create:potion', amount: 250 }]).heated().id('create_confectionery:candy_cane_recipe')
    myCreate.emptying(['minecraft:bucket', '1000x create_confectionery:caramel'], ['create_confectionery:caramel_bucket']).id('create_confectionery:caramel_emptying')
    myCreate.filling('create_confectionery:caramel_glazed_berries', ['minecraft:sweet_berries', { fluid: 'create_confectionery:caramel', amount: 250 }]).id('create_confectionery:caramel_glazed_berries_recipe')
    myCreate.mixing('250x create_confectionery:caramel', ['minecraft:sugar', 'minecraft:sugar', { fluid: 'minecraft:water', amount: 250 }]).heated().id('create_confectionery:caramel_recipe')
    myCreate.mixing('250x create_confectionery:caramel', ['create_confectionery:bar_of_caramel']).heated().id('create_confectionery:caramel_recipe_2')
    myCreate.filling('create_confectionery:chocolate_candy_1', ['create_confectionery:bar_of_white_chocolate', { fluid: 'create:chocolate', amount: 250 }]).id('create_confectionery:chocolate_candy_1_recipe')
    myCreate.filling('create_confectionery:chocolate_candy_2', ['create_confectionery:bar_of_black_chocolate', { fluid: 'create:chocolate', amount: 250 }]).id('create_confectionery:chocolate_candy_2_recipe')
    myCreate.filling('create_confectionery:chocolate_candy_3', ['create_confectionery:bar_of_ruby_chocolate', { fluid: 'create:chocolate', amount: 250 }]).id('create_confectionery:chocolate_candy_3_recipe')
    myCreate.filling('create_confectionery:chocolate_candy', ['create_confectionery:bar_of_caramel', { fluid: 'create:chocolate', amount: 250 }]).id('create_confectionery:chocolate_candy_recipe')
    myCreate.filling('create_confectionery:chocolate_glazed_marshmallow', ['create_confectionery:marshmallow', { fluid: 'create:chocolate', amount: 250 }]).id('create_confectionery:chocolate_glazed_marshmallow_recipe')
    myCreate.mixing('1000x create:chocolate', ['create_confectionery:chocolate_bricks']).heated().id('create_confectionery:chocolate_recipe_3')
    myCreate.mixing('1000x create:chocolate', ['create_confectionery:chocolate_bricks_stairs']).heated().id('create_confectionery:chocolate_recipe_4')
    myCreate.mixing('500x create:chocolate', ['create_confectionery:chocolate_bricks_slab']).heated().id('create_confectionery:chocolate_recipe_5')
    myCreate.crushing(['create_confectionery:cocoa_powder', 'create_confectionery:cocoa_butter'], ['create_confectionery:crushed_cocoa']).id('create_confectionery:cocoa_powder_and_butter_recipe')
    myCreate.pressing('create_confectionery:crushed_cocoa', ['minecraft:cocoa_beans']).id('create_confectionery:crushed_cocoa_recipe')
    myCreate.pressing('create_confectionery:gingerbread_man', ['create_confectionery:gingerdough']).id('create_confectionery:gingerbread_man_recipe')
    myCreate.mixing('create_confectionery:gingerdough', ['minecraft:sugar', 'create:cinder_flour', 'create:wheat_flour', { fluidTag: 'c:honey', amount: 250 }]).id('create_confectionery:gingerdough_recipe')
    myCreate.mixing('4x create_confectionery:honey_candy', ['minecraft:sugar', 'minecraft:sugar', 'create:wheat_flour', { fluidTag: 'c:honey', amount: 250 }]).heated().id('create_confectionery:honey_candy_recipe')
    myCreate.filling('create_confectionery:hot_chocolate_bottle', ['minecraft:glass_bottle', { fluid: 'create_confectionery:hot_chocolate', amount: 250 }]).id('create_confectionery:hot_chocolate_bottle_recipe')
    myCreate.emptying(['minecraft:glass_bottle', '250x create_confectionery:hot_chocolate'], ['create_confectionery:hot_chocolate_bottle']).id('create_confectionery:hot_chocolate_drain')
    myCreate.mixing('250x create_confectionery:hot_chocolate', ['minecraft:sugar', 'create_confectionery:cocoa_powder', 'create_confectionery:cocoa_powder', { fluidTag: 'c:milk', amount: 250 }]).heated().id('create_confectionery:hot_chocolate_recipe')
    myCreate.mixing('8x create_confectionery:marshmallow', ['minecraft:sugar', 'minecraft:sugar', 'minecraft:slime_ball', { fluid: 'minecraft:water', amount: 250 }]).heated().id('create_confectionery:marshmallow_recipe')
    myCreate.filling('create_confectionery:ruby_chocolate_candy_1', ['create:bar_of_chocolate', { fluid: 'create_confectionery:ruby_chocolate', amount: 250 }]).id('create_confectionery:ruby_chocolate_candy_1_recipe')
    myCreate.filling('create_confectionery:ruby_chocolate_candy_2', ['create_confectionery:bar_of_white_chocolate', { fluid: 'create_confectionery:ruby_chocolate', amount: 250 }]).id('create_confectionery:ruby_chocolate_candy_2_recipe')
    myCreate.filling('create_confectionery:ruby_chocolate_candy_3', ['create_confectionery:bar_of_black_chocolate', { fluid: 'create_confectionery:ruby_chocolate', amount: 250 }]).id('create_confectionery:ruby_chocolate_candy_3_recipe')
    myCreate.filling('create_confectionery:ruby_chocolate_candy', ['create_confectionery:bar_of_caramel', { fluid: 'create_confectionery:ruby_chocolate', amount: 250 }]).id('create_confectionery:ruby_chocolate_candy_recipe')
    myCreate.emptying(['minecraft:bucket', '1000x create_confectionery:ruby_chocolate'], ['create_confectionery:ruby_chocolate_bucket']).id('create_confectionery:ruby_chocolate_emptying')
    myCreate.filling('create_confectionery:ruby_chocolate_glazed_berries', ['minecraft:sweet_berries', { fluid: 'create_confectionery:ruby_chocolate', amount: 250 }]).id('create_confectionery:ruby_chocolate_glazed_berries_recipe')
    myCreate.filling('create_confectionery:ruby_chocolate_glazed_marshmallow', ['create_confectionery:marshmallow', { fluid: 'create_confectionery:ruby_chocolate', amount: 250 }]).id('create_confectionery:ruby_chocolate_glazed_marshmallow_recipe')
    myCreate.mixing('250x create_confectionery:ruby_chocolate', ['minecraft:sugar', 'minecraft:dragon_breath', 'minecraft:cocoa_beans', { fluidTag: 'c:milk', amount: 250 }]).heated().id('create_confectionery:ruby_chocolate_recipe')
    myCreate.mixing('250x create_confectionery:ruby_chocolate', ['create_confectionery:bar_of_ruby_chocolate']).heated().id('create_confectionery:ruby_chocolate_recipe_2')
    myCreate.mixing('1000x create_confectionery:ruby_chocolate', ['create_confectionery:ruby_chocolate_bricks']).heated().id('create_confectionery:ruby_chocolate_recipe_3')
    myCreate.mixing('500x create_confectionery:ruby_chocolate', ['create_confectionery:ruby_chocolate_brick_stairs']).heated().id('create_confectionery:ruby_chocolate_recipe_4')
    myCreate.mixing('500x create_confectionery:ruby_chocolate', ['create_confectionery:ruby_chocolate_brick_slab']).heated().id('create_confectionery:ruby_chocolate_recipe_5')
    myCreate.filling('create_confectionery:white_chocolate_candy_1', ['create:bar_of_chocolate', { fluid: 'create_confectionery:white_chocolate', amount: 250 }]).id('create_confectionery:white_chocolate_candy_1_recipe')
    myCreate.filling('create_confectionery:white_chocolate_candy_2', ['create_confectionery:bar_of_black_chocolate', { fluid: 'create_confectionery:white_chocolate', amount: 250 }]).id('create_confectionery:white_chocolate_candy_2_recipe')
    myCreate.filling('create_confectionery:white_chocolate_candy_3', ['create_confectionery:bar_of_ruby_chocolate', { fluid: 'create_confectionery:white_chocolate', amount: 250 }]).id('create_confectionery:white_chocolate_candy_3_recipe')
    myCreate.filling('create_confectionery:white_chocolate_candy', ['create_confectionery:bar_of_caramel', { fluid: 'create_confectionery:white_chocolate', amount: 250 }]).id('create_confectionery:white_chocolate_candy_recipe')
    myCreate.emptying(['minecraft:bucket', '1000x create_confectionery:white_chocolate'], ['create_confectionery:white_chocolate_bucket']).id('create_confectionery:white_chocolate_emptying')
    myCreate.filling('create_confectionery:white_chocolate_glazed_berries', ['minecraft:sweet_berries', { fluid: 'create_confectionery:white_chocolate', amount: 250 }]).id('create_confectionery:white_chocolate_glazed_berries_recipe')
    myCreate.filling('create_confectionery:white_chocolate_glazed_marshmallow', ['create_confectionery:marshmallow', { fluid: 'create_confectionery:white_chocolate', amount: 250 }]).id('create_confectionery:white_chocolate_glazed_marshmallow_recipe')
    myCreate.mixing('250x create_confectionery:white_chocolate', ['minecraft:sugar', 'create_confectionery:cocoa_butter', { fluidTag: 'c:milk', amount: 250 }]).heated().id('create_confectionery:white_chocolate_recipe')
    myCreate.mixing('250x create_confectionery:white_chocolate', ['create_confectionery:bar_of_white_chocolate']).heated().id('create_confectionery:white_chocolate_recipe_2')
    myCreate.mixing('1000x create_confectionery:white_chocolate', ['create_confectionery:white_chocolate_bricks']).heated().id('create_confectionery:white_chocolate_recipe_3')
    myCreate.mixing('1000x create_confectionery:white_chocolate', ['create_confectionery:white_chocolate_bricks_stairs']).heated().id('create_confectionery:white_chocolate_recipe_4')
    myCreate.mixing('500x create_confectionery:white_chocolate', ['create_confectionery:white_chocolate_bricks_slab']).heated().id('create_confectionery:white_chocolate_recipe_5')
    event.remove({id: 'create_sa:andesite_exoskeleton_recipe'})
    event.remove({id: 'create_sa:andesite_jetpack_recipe'})
    myCreate.mixing('create_sa:blazing_axe', ['minecraft:golden_axe', 'create:powdered_obsidian']).heated().id('create_sa:blazing_axe_recipe')
    myCreate.mixing('create_sa:blazing_pickaxe', ['minecraft:golden_pickaxe', 'create:powdered_obsidian']).heated().id('create_sa:blazing_pickaxe_recipe')
    myCreate.mixing('create_sa:blazing_shovel', ['minecraft:golden_shovel', 'create:powdered_obsidian']).heated().id('create_sa:blazing_shovel_recipe')
    myCreate.mixing('create_sa:blazing_cleaver', ['minecraft:golden_sword', 'create:powdered_obsidian']).heated().id('create_sa:blazing_sword_recipe')
    myCreate.haunting('minecraft:name_tag', ['minecraft:writable_book']).id('create_sa:book_and_quill_haunting')
    myCreate.filling('minecraft:brain_coral_block', ['minecraft:dead_brain_coral_block', { fluid: 'create:potion', amount: 25 }]).id('create_sa:brain_tube_coral_revive')
    event.remove({id: 'create_sa:brass_drone_recipe'})
    event.remove({id: 'create_sa:brass_exoskeleton_recipe'})
    event.remove({id: 'create_sa:brass_jetpack_recipe'})
    myCreate.filling('minecraft:bubble_coral_block', ['minecraft:dead_bubble_coral_block', { fluid: 'create:potion', amount: 25 }]).id('create_sa:dead_bubble_coral_revive')
    myCreate.filling('minecraft:fire_coral_block', ['minecraft:dead_fire_coral_block', { fluid: 'create:potion', amount: 25 }]).id('create_sa:dead_fire_coral_revive')
    myCreate.filling('minecraft:horn_coral_block', ['minecraft:dead_horn_coral_block', { fluid: 'create:potion', amount: 25 }]).id('create_sa:dead_horn_coral_revive')
    myCreate.filling('minecraft:tube_coral_block', ['minecraft:dead_tube_coral_block', { fluid: 'create:potion', amount: 25 }]).id('create_sa:dead_tube_coral_revive')
    myCreate.compacting('minecraft:deepslate', ['minecraft:flint', 'minecraft:flint', 'minecraft:flint', { fluid: 'minecraft:lava', amount: 250 }]).id('create_sa:deepslate_pressing_recipe')
    event.remove({id: 'create_sa:flamethrower_recipe'})
    event.remove({id: 'create_sa:grapplin_whisk_recipe'})
    event.remove({id: 'create_sa:heat_engine_recipe'})
    event.remove({id: 'create_sa:hydraulic_engine_recipe'})
    event.remove({id: 'create_sa:incomplete_book_recipe'})
    event.remove({id: 'create_sa:incomplete_web_recipe'})
    myCreate.haunting('minecraft:chainmail_boots', ['minecraft:iron_boots']).id('create_sa:iron_boots_haunting')
    myCreate.haunting('minecraft:chainmail_chestplate', ['minecraft:iron_chestplate']).id('create_sa:iron_chestplate_haunting')
    myCreate.haunting('minecraft:chainmail_helmet', ['minecraft:iron_helmet']).id('create_sa:iron_helmet_haunting')
    myCreate.haunting('minecraft:chainmail_leggings', ['minecraft:iron_leggings']).id('create_sa:iron_leggings_haunting')
    myCreate.mixing('minecraft:magma_cream', ['minecraft:slime_ball']).heated().id('create_sa:magma_cream_recipe')
    myCreate.filling('minecraft:netherrack', ['minecraft:cobblestone', { fluid: 'create:potion', amount: 25 }]).id('create_sa:netherrack_recipe')
    myCreate.haunting('minecraft:crying_obsidian', ['minecraft:obsidian']).id('create_sa:obsidian_haunting')
    myCreate.crushing('create:experience_nugget', ['#c:gems/quartz']).id('create_sa:quartz_gem_crushing')
    event.remove({id: 'create_sa:rose_quartz_axe_recipe'})
    event.remove({id: 'create_sa:rose_quartz_pickaxe_recipe'})
    event.remove({id: 'create_sa:rose_quartz_shovel_recipe'})
    event.remove({id: 'create_sa:rose_quartz_sword_recipe'})
    myCreate.filling('minecraft:wet_sponge', ['minecraft:sponge', { fluid: 'minecraft:water', amount: 1000 }]).id('create_sa:sponge_filling')
    myCreate.compacting(['minecraft:sponge', '500x minecraft:water'], ['minecraft:wet_sponge']).id('create_sa:sponge_pressing')
    event.remove({id: 'create_sa:steam_engine_recipe'})
    myCreate.compacting('2x create:asurine', ['create:zinc_nugget', 'create:zinc_nugget', 'create:zinc_nugget', 'create:zinc_nugget', 'minecraft:gravel', 'minecraft:gravel', { fluid: 'minecraft:water', amount: 100 }]).id('create_ultimate_factory:compacting_asurine')
    myCreate.compacting('minecraft:blaze_rod', ['minecraft:blaze_powder', 'minecraft:blaze_powder', 'minecraft:blaze_powder', 'minecraft:blaze_powder', 'minecraft:blaze_powder', 'minecraft:blaze_powder']).id('create_ultimate_factory:compacting_blazepowder')
    myCreate.compacting('minecraft:calcite', ['minecraft:gravel', 'minecraft:bone_meal', 'minecraft:bone_meal', 'minecraft:bone_meal']).id('create_ultimate_factory:compacting_calcite')
    myCreate.compacting('minecraft:diamond', ['minecraft:coal_block', 'minecraft:coal_block', 'minecraft:coal_block', 'minecraft:coal_block', 'minecraft:coal_block', 'minecraft:coal_block', 'minecraft:coal_block', 'minecraft:coal_block', 'minecraft:coal_block', { fluid: 'minecraft:lava', amount: 100 }]).heated().id('create_ultimate_factory:compacting_coalblock')
    myCreate.compacting('2x create:crimsite', ['minecraft:iron_nugget', 'minecraft:iron_nugget', 'minecraft:iron_nugget', 'minecraft:iron_nugget', 'minecraft:iron_nugget', 'minecraft:gravel', 'minecraft:gravel', { fluid: 'minecraft:lava', amount: 100 }]).id('create_ultimate_factory:compacting_crimsite')
    myCreate.compacting('minecraft:deepslate', ['minecraft:stone', { fluid: 'minecraft:lava', amount: 50 }]).id('create_ultimate_factory:compacting_deepslate')
    myCreate.compacting('2x create:ochrum', ['minecraft:gold_nugget', 'minecraft:gold_nugget', 'minecraft:gravel', 'minecraft:gravel', { fluid: 'minecraft:lava', amount: 100 }]).id('create_ultimate_factory:compacting_ochrum')
    myCreate.compacting('minecraft:tuff', ['minecraft:cobblestone', 'minecraft:cobblestone', 'minecraft:cobblestone', 'minecraft:cobblestone', 'minecraft:cobblestone', 'minecraft:cobblestone', 'minecraft:cobblestone', 'minecraft:cobblestone', 'minecraft:cobblestone', { fluid: 'minecraft:lava', amount: 50 }]).id('create_ultimate_factory:compacting_tuff')
    myCreate.compacting('2x create:veridium', ['create:copper_nugget', 'create:copper_nugget', 'create:copper_nugget', 'create:copper_nugget', 'create:copper_nugget', 'create:copper_nugget', 'create:copper_nugget', 'minecraft:gravel', 'minecraft:gravel', { fluid: 'minecraft:lava', amount: 100 }]).id('create_ultimate_factory:compacting_veridium')
    myCreate.crushing(['minecraft:wither_skeleton_skull', 'minecraft:blackstone'], ['minecraft:blackstone']).id('create_ultimate_factory:crushing_blackstone')
    myCreate.crushing(['2x minecraft:brown_mushroom', 'minecraft:brown_mushroom', 'minecraft:red_mushroom'], ['minecraft:brown_mushroom_block']).id('create_ultimate_factory:crushing_brownmushroom')
    myCreate.crushing('minecraft:heart_of_the_sea', ['#create_ultimate_factory:corals']).id('create_ultimate_factory:crushing_coral')
    myCreate.crushing(['create:powdered_obsidian', 'create:powdered_obsidian', 'minecraft:amethyst_shard'], ['minecraft:crying_obsidian']).id('create_ultimate_factory:crushing_cryingobsidian')
    myCreate.crushing(['3x minecraft:bone_meal', '3x minecraft:bone_meal'], ['#create_ultimate_factory:dead_corals']).id('create_ultimate_factory:crushing_deadcorals')
    myCreate.crushing(['minecraft:ender_pearl', 'minecraft:end_stone'], ['minecraft:end_stone']).id('create_ultimate_factory:crushing_endstone')
    myCreate.crushing(['minecraft:quartz', 'minecraft:lapis_lazuli'], ['create:limestone']).id('create_ultimate_factory:crushing_limestone')
    myCreate.crushing(['minecraft:nether_brick', 'minecraft:nether_brick', 'minecraft:netherite_scrap'], ['minecraft:nether_bricks']).id('create_ultimate_factory:crushing_netherite')
    myCreate.crushing(['2x minecraft:red_mushroom', 'minecraft:red_mushroom', 'minecraft:brown_mushroom'], ['minecraft:red_mushroom_block']).id('create_ultimate_factory:crushing_redmushroom')
    myCreate.crushing(['minecraft:red_sand', 'minecraft:nautilus_shell'], ['minecraft:red_sandstone']).id('create_ultimate_factory:crushing_redsandstone')
    myCreate.crushing('minecraft:blaze_powder', ['create:scoria']).id('create_ultimate_factory:crushing_scoria')
    myCreate.crushing('minecraft:glowstone_dust', ['minecraft:soul_sand']).id('create_ultimate_factory:crushing_soulsand')
    myCreate.haunting('minecraft:chorus_fruit', ['minecraft:apple']).id('create_ultimate_factory:haunting_apple')
    myCreate.haunting('minecraft:coal', ['minecraft:charcoal']).id('create_ultimate_factory:haunting_charcoal')
    myCreate.haunting('minecraft:netherrack', ['minecraft:basalt']).id('create_ultimate_factory:haunting_netherrack')
    myCreate.haunting('minecraft:crying_obsidian', ['minecraft:obsidian']).id('create_ultimate_factory:haunting_obsidian')
    myCreate.haunting('minecraft:fermented_spider_eye', ['minecraft:spider_eye']).id('create_ultimate_factory:haunting_spidereye')
    myCreate.haunting('minecraft:wither_rose', ['minecraft:poppy']).id('create_ultimate_factory:haunting_witherrose')
    myCreate.mixing('minecraft:dripstone_block', ['minecraft:calcite', { fluid: 'minecraft:water', amount: 200 }]).id('create_ultimate_factory:mixing_dripstone')
    myCreate.mixing('3x minecraft:gunpowder', ['#minecraft:coals', '#minecraft:coals', 'minecraft:blaze_powder']).id('create_ultimate_factory:mixing_gunpowder')
    myCreate.mixing('minecraft:redstone', ['minecraft:netherrack', 'minecraft:flint', { fluid: 'minecraft:lava', amount: 50 }]).id('create_ultimate_factory:mixing_redstone')
    myCreate.splashing('minecraft:slime_ball', ['minecraft:magma_cream']).id('create_ultimate_factory:splashing_magma_cream')
    myCreate.splashing('minecraft:blue_ice', ['minecraft:packed_ice']).id('create_ultimate_factory:splashing_packed_ice')
    myCreate.splashing('minecraft:terracotta', ['#minecraft:terracotta']).id('create_ultimate_factory:splashing_terracotta')
    myCreate.crushing(['aeronautics:end_stone_powder', 'aeronautics:end_stone_powder', 'minecraft:ender_pearl'], ['minecraft:end_stone']).id('create_ultimate_factory:compat/aeronautics_crushing_endstone')
    myCreate.mixing('minecraft:end_stone', ['#c:cobblestones', 'aeronautics:end_stone_powder', { fluid: 'minecraft:water', amount: 25 }]).id('create_ultimate_factory:compat/aeronautics_mixing_endstonepowder')
    myCreate.crushing(['tfmg:limesand', 'minecraft:quartz', 'minecraft:lapis_lazuli'], ['create:limestone']).id('create_ultimate_factory:compat/tfmg_crushing_limestone')
    myCreate.crushing(['wstweaks:fragment', 'minecraft:blackstone'], ['minecraft:blackstone']).id('create_ultimate_factory:compat/wst_crushing_blackstone')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:blood'], ['irons_spellbooks:blood_vial']).id('irons_spellbooks:create_compat/create_empty_blood_vial')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:common_ink'], ['irons_spellbooks:common_ink']).id('irons_spellbooks:create_compat/create_empty_common_ink')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:epic_ink'], ['irons_spellbooks:epic_ink']).id('irons_spellbooks:create_compat/create_empty_epic_ink')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:evasion_elixir'], ['irons_spellbooks:evasion_elixir']).id('irons_spellbooks:create_compat/create_empty_evasion_elixir')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:greater_evasion_elixir'], ['irons_spellbooks:greater_evasion_elixir']).id('irons_spellbooks:create_compat/create_empty_greater_evasion_elixir')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:greater_healing_elixir'], ['irons_spellbooks:greater_healing_potion']).id('irons_spellbooks:create_compat/create_empty_greater_healing_potion')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:greater_invisibility_elixir'], ['irons_spellbooks:greater_invisibility_elixir']).id('irons_spellbooks:create_compat/create_empty_greater_invisibility_elixir')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:greater_oakskin_elixir'], ['irons_spellbooks:greater_oakskin_elixir']).id('irons_spellbooks:create_compat/create_empty_greater_oakskin_elixir')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:ice_venom'], ['irons_spellbooks:ice_venom_vial']).id('irons_spellbooks:create_compat/create_empty_ice_venom_vial')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:invisibility_elixir'], ['irons_spellbooks:invisibility_elixir']).id('irons_spellbooks:create_compat/create_empty_invisibility_elixir')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:legendary_ink'], ['irons_spellbooks:legendary_ink']).id('irons_spellbooks:create_compat/create_empty_legendary_ink')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:oakskin_elixir'], ['irons_spellbooks:oakskin_elixir']).id('irons_spellbooks:create_compat/create_empty_oakskin_elixir')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:rare_ink'], ['irons_spellbooks:rare_ink']).id('irons_spellbooks:create_compat/create_empty_rare_ink')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:timeless_slurry'], ['irons_spellbooks:timeless_slurry']).id('irons_spellbooks:create_compat/create_empty_timeless_slurry')
    myCreate.emptying(['minecraft:glass_bottle', '250x irons_spellbooks:uncommon_ink'], ['irons_spellbooks:uncommon_ink']).id('irons_spellbooks:create_compat/create_empty_uncommon_ink')
    myCreate.filling('irons_spellbooks:blood_vial', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:blood', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_blood_vial')
    myCreate.filling('irons_spellbooks:common_ink', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:common_ink', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_common_ink')
    myCreate.filling('irons_spellbooks:epic_ink', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:epic_ink', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_epic_ink')
    myCreate.filling('irons_spellbooks:evasion_elixir', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:evasion_elixir', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_evasion_elixir')
    myCreate.filling('irons_spellbooks:greater_evasion_elixir', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:greater_evasion_elixir', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_greater_evasion_elixir')
    myCreate.filling('irons_spellbooks:greater_healing_potion', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:greater_healing_elixir', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_greater_healing_potion')
    myCreate.filling('irons_spellbooks:greater_invisibility_elixir', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:greater_invisibility_elixir', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_greater_invisibility_elixir')
    myCreate.filling('irons_spellbooks:greater_oakskin_elixir', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:greater_oakskin_elixir', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_greater_oakskin_elixir')
    myCreate.filling('irons_spellbooks:ice_venom_vial', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:ice_venom', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_ice_venom_vial')
    myCreate.filling('irons_spellbooks:invisibility_elixir', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:invisibility_elixir', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_invisibility_elixir')
    myCreate.filling('irons_spellbooks:legendary_ink', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:legendary_ink', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_legendary_ink')
    myCreate.filling('irons_spellbooks:oakskin_elixir', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:oakskin_elixir', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_oakskin_elixir')
    myCreate.filling('irons_spellbooks:rare_ink', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:rare_ink', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_rare_ink')
    myCreate.filling('irons_spellbooks:timeless_slurry', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:timeless_slurry', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_timeless_slurry')
    myCreate.filling('irons_spellbooks:uncommon_ink', ['minecraft:glass_bottle', { fluid: 'irons_spellbooks:uncommon_ink', amount: 250 }]).id('irons_spellbooks:create_compat/create_fill_uncommon_ink')
})
