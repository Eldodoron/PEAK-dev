// ==========================================
// PEAK EXPERT MODE — SCRIPT 42
// ARMOR UPGRADE ENCHANTMENT & COMPONENT PRESERVATION
// ==========================================

const $Equipable = Java.loadClass('net.minecraft.world.item.Equipable');

ItemEvents.crafted(event => {
    let craftedItem = event.item;
    if (!craftedItem || craftedItem.isEmpty()) return;

    // 1. Guard clause: Target crafted item must be an equippable armor piece
    let outEquip = $Equipable.get(craftedItem);
    if (!outEquip) return;

    let targetSlot = outEquip.getEquipmentSlot();
    if (!targetSlot || !targetSlot.isArmor()) return;

    // 2. Guard clause: Crafting container must be present
    let inventory = event.inventory;
    if (!inventory) return;

    let items = inventory.getAllItems();
    if (!items || items.isEmpty()) return;

    // 3. Find base armor piece of matching slot in the crafting matrix
    let sourceArmor = null;
    let size = items.size();
    for (let i = 0; i < size; i++) {
        let stack = items.get(i);
        if (!stack || stack.isEmpty()) continue;

        // Ignore identical item ID to avoid interfering with 2x2 grid repair
        if (stack.id === craftedItem.id) continue;

        let inEquip = $Equipable.get(stack);
        if (inEquip && inEquip.getEquipmentSlot() === targetSlot) {
            sourceArmor = stack;
            break;
        }
    }

    if (!sourceArmor) return;

    // 4. Transfer modified data components (enchantments, trim, name, apotheosis affixes, sockets)
    let patch = sourceArmor.getComponentsPatch();
    if (patch && !patch.isEmpty()) {
        craftedItem.applyComponents(patch);

        // Clamp damage value if the upgraded armor piece has lower max durability
        let maxDmg = craftedItem.getMaxDamage();
        let curDmg = craftedItem.getDamageValue();
        if (maxDmg > 0 && curDmg >= maxDmg) {
            craftedItem.setDamageValue(Math.max(0, maxDmg - 1));
        }
    }

    // 5. Fallback enchantment merge
    try {
        if (sourceArmor.isEnchanted() && !craftedItem.isEnchanted()) {
            craftedItem.enchant(sourceArmor.getEnchantments());
        }
    } catch (e) {}
});

console.log('[PEAK Expert Mode] Script 42: Armor Upgrade Preservation loaded!');
