// ==========================================
// CUSTOM ENCHANTMENT MECHANICS
// Subjugation, Concussive Impact, Midas Touch, Soul Siphon
// ==========================================

function getEnchantLevel(itemStack, enchantId) {
    if (!itemStack || itemStack.isEmpty()) return 0;
    try {
        let lvl = itemStack.getEnchantmentLevel(enchantId);
        if (lvl > 0) return lvl;
    } catch (e) {}
    try {
        let ench = itemStack.components.get('minecraft:enchantments');
        if (ench && ench.levels && ench.levels[enchantId]) {
            return ench.levels[enchantId];
        }
    } catch (e) {}
    return 0;
}

// ==========================================
// 1. SUBJUGATION: CAGE ENTITY CAPTURE
// ==========================================
ItemEvents.entityInteracted(event => {
    let player = event.player;
    let target = event.target;
    let item = event.item;
    let hand = event.hand;

    if (!player || !target || !item || hand.name() !== 'MAIN_HAND') return;
    if (item.id !== 'supplementaries:cage') return;

    let subjugationLvl = getEnchantLevel(item, 'kubejs:subjugation');
    if (subjugationLvl <= 0) return;

    // Prevent capturing if cage already holds an entity
    if (item.nbt && item.nbt.CapturedEntity) {
        player.displayClientMessage(Component.red("This cage is already holding an entity!"), true);
        event.cancel();
        return;
    }

    // Supported entities: Villagers, Wandering Traders, Goblins, and modded merchants
    let typeId = target.type;
    let isCapturable = (
        typeId === 'minecraft:villager' ||
        typeId === 'minecraft:wandering_trader' ||
        typeId === 'goblintraders:goblin_trader' ||
        typeId === 'goblintraders:vein_goblin_trader' ||
        typeId === 'supplementaries:red_merchant' ||
        typeId === 'minecraft:zombie_villager' ||
        typeId === 'vampirism:villager_angry' ||
        typeId === 'vampirism:villager_converted' ||
        typeId.includes('villager') ||
        typeId.includes('trader') ||
        typeId.includes('goblin')
    );

    if (!isCapturable) return;

    // Extract entity NBT data
    let entityNbt = {};
    target.saveWithoutId(entityNbt);
    delete entityNbt.UUID; // Allow fresh UUID generation on respawn
    let entityName = target.customName ? target.customName.string : target.displayName.string;

    // Create filled cage item with preserved enchantments and captured data
    let filledCage = Item.of('supplementaries:cage');
    filledCage.enchant('kubejs:subjugation', 1);
    filledCage.nbt = {
        CapturedEntity: {
            id: typeId,
            nbt: entityNbt,
            name: entityName
        }
    };
    filledCage.setHoverName(Component.gold("Cage (").append(Component.yellow(entityName)).append(Component.gold(")")));
    filledCage.setLore([
        Component.gray("Contains: ").append(Component.yellow(entityName)),
        Component.darkGray("Right-click a block to release.")
    ]);

    // Handle stack size consumption
    item.shrink(1);
    if (item.isEmpty()) {
        player.setItemInHand(hand, filledCage);
    } else {
        player.give(filledCage);
    }

    // Audio & particle feedback
    player.playNotifySound('minecraft:block.iron_trapdoor.close', 'players', 1.0, 1.0);
    player.playNotifySound('minecraft:entity.item.pickup', 'players', 0.8, 1.2);
    player.level.spawnParticles('minecraft:poof', target.x, target.y + 0.5, target.z, 15, 0.2, 0.3, 0.2, 0.05);

    player.displayClientMessage(Component.green("Captured " + entityName + " in the cage!"), true);

    // Remove entity from the world
    target.discard();
    event.cancel();
});

// ==========================================
// 1b. SUBJUGATION: CAGE ENTITY RELEASE
// ==========================================
BlockEvents.rightClicked(event => {
    let player = event.player;
    let item = event.item;
    let hand = event.hand;

    if (!player || !item || hand.name() !== 'MAIN_HAND') return;
    if (item.id !== 'supplementaries:cage') return;

    if (!item.nbt || !item.nbt.CapturedEntity) return;

    let data = item.nbt.CapturedEntity;
    let spawnPos = event.block.pos.relative(event.direction);
    let entity = event.block.createEntity(data.id);

    if (entity) {
        entity.load(data.nbt);
        entity.setPos(spawnPos.x + 0.5, spawnPos.y, spawnPos.z + 0.5);
        entity.spawn();

        // Return empty enchanted cage
        let emptyCage = Item.of('supplementaries:cage');
        emptyCage.enchant('kubejs:subjugation', 1);

        item.shrink(1);
        if (item.isEmpty()) {
            player.setItemInHand(hand, emptyCage);
        } else {
            player.give(emptyCage);
        }

        // Audio & particle feedback
        player.playNotifySound('minecraft:block.iron_trapdoor.open', 'players', 1.0, 1.0);
        player.playNotifySound('minecraft:entity.villager.ambient', 'players', 1.0, 1.0);
        event.level.spawnParticles('minecraft:poof', spawnPos.x + 0.5, spawnPos.y + 0.5, spawnPos.z + 0.5, 12, 0.2, 0.3, 0.2, 0.05);

        player.displayClientMessage(Component.green("Released " + data.name + "!"), true);
        event.cancel();
    }
});

// ==========================================
// 2. CONCUSSIVE IMPACT & 4. SOUL SIPHON
// ==========================================
EntityEvents.hurt(event => {
    let source = event.source;
    if (!source) return;
    let attacker = source.actual;
    let victim = event.entity;
    if (!attacker || !victim) return;

    let weapon = attacker.mainHandItem;
    if (!weapon || weapon.isEmpty()) return;

    // --- Concussive Impact (Stun + Pan Clang Audio) ---
    let concussiveLvl = getEnchantLevel(weapon, 'kubejs:concussive_impact');
    if (concussiveLvl > 0) {
        // Frying pan metallic CLANG sound
        victim.level.playSound(null, victim.x, victim.y, victim.z, 'farmersdelight:item.skillet.attack.strong', 'players', 1.4, 0.9 + Math.random() * 0.2);
        victim.level.playSound(null, victim.x, victim.y, victim.z, 'minecraft:block.anvil.land', 'players', 0.4, 1.8);

        // Stun duration: 1.0s base + 0.5s per level (20 ticks = 1s)
        let stunTicks = Math.floor(20 * (0.5 + concussiveLvl * 0.5));
        victim.potionEffects.add('minecraft:slowness', stunTicks, 4, false, false);
        victim.potionEffects.add('minecraft:weakness', stunTicks, 1, false, false);

        // Daze star particles around victim's head
        victim.level.spawnParticles('minecraft:crit', victim.x, victim.y + victim.eyeHeight, victim.z, 8 + concussiveLvl * 2, 0.2, 0.2, 0.2, 0.1);
    }

    // --- Soul Siphon Feedback ---
    // (Absorption hearts are granted natively via soul_siphon.json post_attack component)
    let soulLvl = getEnchantLevel(weapon, 'kubejs:soul_siphon');
    if (soulLvl > 0 && attacker.isPlayer()) {
        attacker.playNotifySound('minecraft:particle.soul_escape', 'players', 0.6, 1.2);
        victim.level.spawnParticles('minecraft:soul_fire_flame', victim.x, victim.y + 1.0, victim.z, 8 + soulLvl * 3, 0.25, 0.3, 0.25, 0.04);
    }
});

// ==========================================
// 3. MIDAS TOUCH: GOLD TRANSMUTATION
// ==========================================
BlockEvents.broken(event => {
    let player = event.player;
    let block = event.block;
    let level = event.level;
    if (!block) return;

    let tool = player ? player.mainHandItem : null;
    let midasLvl = getEnchantLevel(tool, 'kubejs:midas_touch');
    if (midasLvl <= 0) return;

    let blockId = block.id;
    let isStone = (
        blockId === 'minecraft:stone' ||
        blockId === 'minecraft:cobblestone' ||
        blockId === 'minecraft:deepslate' ||
        blockId === 'minecraft:cobbled_deepslate' ||
        blockId === 'minecraft:andesite' ||
        blockId === 'minecraft:diorite' ||
        blockId === 'minecraft:granite' ||
        blockId === 'minecraft:tuff' ||
        blockId === 'minecraft:calcite'
    );

    if (!isStone) return;

    // Chance: 15% per level (15%, 30%, 45%)
    let chance = midasLvl * 0.15;
    if (Math.random() < chance) {
        let count = 1 + Math.floor(Math.random() * (midasLvl + 1));
        let dropPos = block.pos;

        // Cancel standard stone drop and remove block
        event.cancel();
        block.set('minecraft:air');

        // Spawn gold nuggets
        let dropEntity = block.createEntity('item');
        dropEntity.item = Item.of('minecraft:gold_nugget', count);
        dropEntity.setPos(dropPos.x + 0.5, dropPos.y + 0.5, dropPos.z + 0.5);
        dropEntity.spawn();

        level.playSound(null, dropPos.x, dropPos.y, dropPos.z, 'minecraft:entity.experience_orb.pickup', 'blocks', 0.8, 1.5);
        level.spawnParticles('minecraft:wax_on', dropPos.x + 0.5, dropPos.y + 0.5, dropPos.z + 0.5, 8, 0.3, 0.3, 0.3, 0.05);

        // Consume 1 additional tool durability
        if (tool && tool.isDamageableItem()) {
            tool.damageValue += 1;
        }
    }
});
