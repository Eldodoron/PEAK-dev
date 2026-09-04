ServerEvents.recipes(event => { 
    console.log('=== START DUMP ==='); 
    console.log(Item.getList().map(i => i.id).filter(id => id.includes('bronze_ingot') || id.includes('steel_ingot') || id.includes('slag') || id.includes('common_material') || id.includes('epic_material') || id.includes('uncommon_material') || id.includes('rare_material') || id.includes('gem_dust') || id.includes('molten_steel') || id.includes('fragment')).join(', ')); 
    console.log('=== END DUMP ==='); 
});
