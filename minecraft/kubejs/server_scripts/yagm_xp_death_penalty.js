// Native NeoForge LivingDeathEvent listener for YAGM grave experience scaling.
// Deducts 20% total experience on death before YAGM captures player inventory,
// ensuring the grave retains exactly 80% whether retrieved via right-click or broken.

const XP_RETENTION_RATIO = 0.80;

function getXpForLevel(level) {
    if (level >= 30) return 112 + (level - 30) * 9;
    if (level >= 15) return 37 + (level - 15) * 5;
    return 7 + level * 2;
}

function getTotalXpToReachLevel(level) {
    if (level <= 0) return 0;
    if (level <= 16) return level * level + 6 * level;
    if (level <= 31) return Math.floor((5 * level * level - 81 * level + 720) / 2);
    return Math.floor((9 * level * level - 325 * level + 4440) / 2);
}

function getTotalPlayerXp(level, progress) {
    return getTotalXpToReachLevel(level) + Math.floor(progress * getXpForLevel(level));
}

function decodeTotalXp(totalXp) {
    if (totalXp <= 0) return { level: 0, points: 0, progress: 0.0 };
    let level = 0;
    while (getTotalXpToReachLevel(level + 1) <= totalXp) {
        level++;
    }
    let points = totalXp - getTotalXpToReachLevel(level);
    let needed = getXpForLevel(level);
    let progress = needed > 0 ? points / needed : 0.0;
    return { level: level, points: points, progress: progress };
}

try {
    let LivingDeathEvent = Java.loadClass('net.neoforged.neoforge.event.entity.living.LivingDeathEvent');
    let EventPriority = Java.loadClass('net.neoforged.bus.api.EventPriority');
    let GameRules = Java.loadClass('net.minecraft.world.level.GameRules');

    NativeEvents.onEvent(EventPriority.HIGH, LivingDeathEvent, event => {
        try {
            let entity = event.entity;
            if (!entity || !entity.isPlayer()) return;
            if (event.canceled || (event.isCanceled && event.isCanceled())) return;

            let player = entity;
            let level = player.level;
            if (!level || level.clientSide) return;
            if (player.spectator || (player.isSpectator && player.isSpectator())) return;

            // Skip penalty if keepInventory gamerule is enabled
            try {
                let gr = level.gameRules || level.getGameRules();
                if (gr && gr.getBoolean(GameRules.RULE_KEEPINVENTORY)) return;
            } catch (e) {}

            // Skip penalty if Twilight Forest Charm of Keeping suppresses grave creation
            try {
                let tfEventsClass = Java.loadClass('it.hurts.sskirillss.yagm.neoforge.compat.twilight.TwilightForestNeoForgeEvents');
                let ServerPlayerClass = Java.loadClass('net.minecraft.server.level.ServerPlayer');
                let suppressMethod = tfEventsClass.getDeclaredMethod('SuppressGrave', ServerPlayerClass);
                suppressMethod.setAccessible(true);
                if (suppressMethod.invoke(null, player)) return;
            } catch (e) {}

            let totalXp = getTotalPlayerXp(player.experienceLevel, player.experienceProgress);
            if (totalXp > 0) {
                let retainedXp = Math.floor(totalXp * XP_RETENTION_RATIO);
                let decoded = decodeTotalXp(retainedXp);

                if (player.setExperienceLevels) {
                    player.setExperienceLevels(decoded.level);
                } else {
                    player.experienceLevel = decoded.level;
                }

                if (player.setExperiencePoints) {
                    player.setExperiencePoints(decoded.points);
                }
                player.experienceProgress = decoded.progress;
                player.totalExperience = retainedXp;

                player.tell(Text.darkRed('Death Penalty: ').append(Text.gray('20% of your experience was lost to the grave.')));
            }
        } catch (err) {
            console.error('Error handling YAGM XP death penalty: ' + err);
        }
    });
} catch (err) {
    console.error('Failed to register YAGM XP death penalty listener: ' + err);
}
