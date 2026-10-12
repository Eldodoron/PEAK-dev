// ==========================================
// PEAK SERVER SCRIPT - YAGM XP DEATH PENALTY
// Implements a 20% experience loss on death.
// Stored grave experience is scaled to 80% so players retrieve 80% of their XP.
// ==========================================

const XP_RETENTION_RATIO = 0.80;
const PENALTY_TAG = 'PEAK_XpPenaltyApplied';

function scaleGraveTagExperience(dataTag) {
    if (!dataTag) return false;
    if (dataTag.getBoolean(PENALTY_TAG)) return false;

    let totalXp = dataTag.getLong('TotalExperience');
    if (totalXp > 0) {
        let retainedXp = Math.floor(totalXp * XP_RETENTION_RATIO);
        dataTag.putLong('TotalExperience', retainedXp);
        dataTag.putBoolean(PENALTY_TAG, true);
        return true;
    } else {
        dataTag.putBoolean(PENALTY_TAG, true);
        return false;
    }
}

// -------------------------------------------------------------------------
// 1. ARCHITECTURY GRAVE LIFECYCLE HOOKS (Primary Generation Pipeline)
// -------------------------------------------------------------------------
try {
    let IServerEvent = Java.loadClass('it.hurts.sskirillss.yagm.api.event.IServerEvent');
    let EventResult = Java.loadClass('dev.architectury.event.EventResult');
    let OnPlayerDeath = Java.loadClass('it.hurts.sskirillss.yagm.api.event.IServerEvent$OnPlayerDeath');
    let OnGravePlaced = Java.loadClass('it.hurts.sskirillss.yagm.api.event.IServerEvent$OnGravePlaced');

    let deathListener = new JavaAdapter(OnPlayerDeath, {
        onPlayerDeath: function(player, data) {
            try {
                scaleGraveTagExperience(data);
            } catch (err) {}
            return EventResult.pass();
        }
    });
    IServerEvent.ON_PLAYER_DEATH.register(deathListener);

    let placedListener = new JavaAdapter(OnGravePlaced, {
        onGravePlaced: function(level, pos, state, player, data) {
            try {
                scaleGraveTagExperience(data);
            } catch (err) {}
            return EventResult.pass();
        }
    });
    IServerEvent.ON_GRAVE_PLACED.register(placedListener);
} catch (e) {
    // Architectury hooks initialized with event-based fallbacks active
}

// -------------------------------------------------------------------------
// 2. PLAYER DEATH LISTENER & DATA MANAGER SYNC
// -------------------------------------------------------------------------
EntityEvents.death(event => {
    if (!event.entity.isPlayer()) return;
    let player = event.entity;
    let server = player.server;
    let level = player.level;
    let playerUuid = player.getUUID();

    player.tell(Text.darkRed('Death Penalty: ').append(Text.gray('20% of your experience was lost to the grave.')));

    // Ensure GraveDataManager copy and GraveSaveManager are scaled
    server.scheduleInTicks(2, () => {
        try {
            let GraveDataManager = Java.loadClass('it.hurts.sskirillss.yagm.data.gravedata.GraveDataManager');
            let manager = GraveDataManager.get(level);
            if (manager) {
                let gravesField = GraveDataManager.class.getDeclaredField('graves');
                gravesField.setAccessible(true);
                let map = gravesField.get(manager);
                if (map) {
                    let iter = map.values().iterator();
                    while (iter.hasNext()) {
                        let tag = iter.next();
                        if (tag.hasUUID('PlayerUuid') && tag.getUUID('PlayerUuid').equals(playerUuid)) {
                            if (scaleGraveTagExperience(tag)) {
                                manager.setDirty();
                            }
                        }
                    }
                }
            }
        } catch (e) {}

        try {
            let GraveSaveManager = Java.loadClass('it.hurts.sskirillss.yagm.data.gravedata.GraveSaveManager');
            let latestSave = GraveSaveManager.peekLatestRestoreSave(level, playerUuid);
            if (latestSave) {
                scaleGraveTagExperience(latestSave);
            }
        } catch (e) {}
    });
});

// -------------------------------------------------------------------------
// 3. GRAVE RETRIEVAL HOOKS (Interaction & Destruction Fail-Safe)
// -------------------------------------------------------------------------
function checkAndScaleGraveBlockEntity(level, block) {
    if (!block.id.startsWith('yagm:') || !block.id.includes('grave')) return false;
    let pos = block.pos;
    if (block.properties && block.properties.half === 'upper') {
        pos = pos.below();
    }
    let be = level.getBlockEntity(pos);
    if (!be || be.isDecorative()) return false;
    if (be.getInventoryData) {
        let invData = be.getInventoryData();
        if (scaleGraveTagExperience(invData)) {
            be.setChanged();
        }
    }
    return true;
}

BlockEvents.rightClicked(event => {
    let block = event.block;
    if (block.id.startsWith('yagm:') && block.id.includes('grave')) {
        let player = event.player;
        if (player && !player.isShiftKeyDown()) {
            checkAndScaleGraveBlockEntity(event.level, block);
        }
    }
});

BlockEvents.broken(event => {
    let block = event.block;
    if (block.id.startsWith('yagm:') && block.id.includes('grave')) {
        checkAndScaleGraveBlockEntity(event.level, block);
    }
});
