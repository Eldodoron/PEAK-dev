// Priority: 0

const $ArrayList = Java.loadClass('java.util.ArrayList');
const $AttributeModifier = Java.loadClass('net.minecraft.world.entity.ai.attributes.AttributeModifier');
const $Operation = Java.loadClass('net.minecraft.world.entity.ai.attributes.AttributeModifier$Operation');
const $Attributes = Java.loadClass('net.minecraft.world.entity.ai.attributes.Attributes');
const $EquipmentSlotGroup = Java.loadClass('net.minecraft.world.entity.EquipmentSlotGroup');
const $ResourceLocation = Java.loadClass('net.minecraft.resources.ResourceLocation');
const $Entry = Java.loadClass('net.minecraft.world.item.component.ItemAttributeModifiers$Entry');

function setHelmetArmorAttributes(item, armor, toughness, knockbackRes) {
    let oldMods = item.getAttributeModifiers();
    let entries = oldMods.modifiers();
    let list = new $ArrayList();

    for (let i = 0; i < entries.size(); i++) {
        let entry = entries.get(i);
        let attrKey = entry.attribute().unwrapKey().orElse(null);
        let attrLoc = attrKey ? attrKey.location().toString() : '';
        if (attrLoc === 'minecraft:armor' || 
            attrLoc === 'minecraft:armor_toughness' || 
            attrLoc === 'minecraft:knockback_resistance') {
            continue;
        }
        list.add(entry);
    }

    if (armor !== undefined && armor !== null) {
        list.add(new $Entry($Attributes.ARMOR, new $AttributeModifier($ResourceLocation.fromNamespaceAndPath('kubejs', 'buff_armor'), armor, $Operation.ADD_VALUE), $EquipmentSlotGroup.HEAD));
    }
    if (toughness !== undefined && toughness !== null) {
        list.add(new $Entry($Attributes.ARMOR_TOUGHNESS, new $AttributeModifier($ResourceLocation.fromNamespaceAndPath('kubejs', 'buff_toughness'), toughness, $Operation.ADD_VALUE), $EquipmentSlotGroup.HEAD));
    }
    if (knockbackRes !== undefined && knockbackRes !== null) {
        list.add(new $Entry($Attributes.KNOCKBACK_RESISTANCE, new $AttributeModifier($ResourceLocation.fromNamespaceAndPath('kubejs', 'buff_kb_res'), knockbackRes, $Operation.ADD_VALUE), $EquipmentSlotGroup.HEAD));
    }

    item.setAttributeModifiersWithTooltip(list);
}

ItemEvents.modification(event => {
    // Buff Monstrous Helm (Cataclysm)
    event.modify('cataclysm:monstrous_helm', item => {
        setHelmetArmorAttributes(item, 5.0, 4.0, 0.2);
    });

    // Buff Monstrous Wizard Hat (Cataclysm Spellbooks)
    event.modify('cataclysm_spellbooks:monstrous_wizard_hat', item => {
        setHelmetArmorAttributes(item, 4.0, 3.0, 0.1);
    });

    // Buff Monstrous Flamberge (Cataclysm Spellbooks)
    event.modify('cataclysm_spellbooks:monstrous_flamberge', item => {
        item.attackDamage = 20; 
    });
});
