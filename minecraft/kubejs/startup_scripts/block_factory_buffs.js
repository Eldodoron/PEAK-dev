ItemEvents.modification(event => {
    let AttributeModifier = Java.loadClass('net.minecraft.world.entity.ai.attributes.AttributeModifier');
    let Attributes = Java.loadClass('net.minecraft.world.entity.ai.attributes.Attributes');
    let EquipmentSlotGroup = Java.loadClass('net.minecraft.world.entity.EquipmentSlotGroup');
    let ResourceLocation = Java.loadClass('net.minecraft.resources.ResourceLocation');
    let DataComponents = Java.loadClass('net.minecraft.core.component.DataComponents');
    
    function setArmorStats(itemId, armor, toughness, knockbackResist, slotGroup) {
        event.modify(itemId, item => {
            // Remove existing attribute modifiers to prevent stacking
            item.remove(DataComponents.ATTRIBUTE_MODIFIERS);

            // Attach rebalanced attribute modifiers
            item.addAttributeModifier(Attributes.ARMOR, new AttributeModifier(ResourceLocation.parse("kubejs:armor"), armor, AttributeModifier.Operation.ADD_VALUE), slotGroup);
            
            if (toughness > 0) {
                item.addAttributeModifier(Attributes.ARMOR_TOUGHNESS, new AttributeModifier(ResourceLocation.parse("kubejs:armor_toughness"), toughness, AttributeModifier.Operation.ADD_VALUE), slotGroup);
            }
            if (knockbackResist > 0) {
                item.addAttributeModifier(Attributes.KNOCKBACK_RESISTANCE, new AttributeModifier(ResourceLocation.parse("kubejs:knockback_resistance"), knockbackResist, AttributeModifier.Operation.ADD_VALUE), slotGroup);
            }
        });
    }

    // Armor Sets
    setArmorStats('block_factorys_bosses:dragon_bones_boots', 9, 4.0, 0.2, EquipmentSlotGroup.FEET);
    setArmorStats('block_factorys_bosses:dragon_bones_leggings', 11, 4.0, 0.2, EquipmentSlotGroup.LEGS);
    setArmorStats('block_factorys_bosses:dragon_bones_chestplate', 14, 4.0, 0.2, EquipmentSlotGroup.CHEST);
    setArmorStats('block_factorys_bosses:dragon_skull', 9, 4.0, 0.2, EquipmentSlotGroup.HEAD);

    // Weapons - Gauntlets
    event.modify('block_factorys_bosses:sandworm_gauntlet', item => {
        item.setAttackDamage(25);
        item.setAttackSpeed(-2.8);
    });
    event.modify('block_factorys_bosses:ice_gauntlet', item => {
        item.setAttackDamage(22);
        item.setAttackSpeed(-2.8);
    });

    // Weapons - Trident
    event.modify('block_factorys_bosses:kraken_trident', item => {
        item.setAttackDamage(16);
        item.setAttackSpeed(-2.9);
    });

    // Weapons - Swords
    event.modify('block_factorys_bosses:large_sword', item => {
        item.setAttackDamage(12);
        item.setAttackSpeed(-2.8);
    });
    event.modify('block_factorys_bosses:knight_sword', item => {
        item.setAttackDamage(10);
        item.setAttackSpeed(-2.4);
    });
    event.modify('block_factorys_bosses:warrior_sword', item => {
        item.setAttackDamage(10);
        item.setAttackSpeed(-2.4);
    });
});
