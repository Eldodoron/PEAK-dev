# PEAK Optimizations — Boss Rifts tick_1s override
# ORIGINAL: scheduled every 12 ticks (~0.6s) and ran 13 compat sub-functions.
# OPTIMIZED: scheduled every 60 ticks (3 seconds). 
# Boss tagging and compat checks don't need sub-second precision.

schedule function boss_rifts_extended_compat:tick_1s 60

# Assign boss tags (moved here from tick.mcfunction to run at 3s intervals instead of every tick)
tag @e[type=#bossrifts:rift_bosses] add bossrifts.rift_bosses
tag @e[type=#c:bosses] add bossrifts.rift_bosses
tag @e[type=#forge:bosses] add bossrifts.rift_bosses
tag @e[type=#neoforge:bosses] add bossrifts.rift_bosses
tag @e[type=elder_guardian,predicate=boss_rifts_extended_compat:isinoceanmonument] add bossrifts.rift_bosses
execute as @e[type=elder_guardian,tag=!bossrifts..bumblezonetested] at @s run function boss_rifts_extended_compat:elderguardiantestforbumblezone
tag @e[type=#boss_rifts_extended_compat:boss_exception] add bossrifts.boss_exception
execute as @e[tag=bossrifts.rift_bosses] if data entity @s RaidId run tag @s add bossrifts.boss_exception

execute as @e[tag=bossrifts.rift_bosses,tag=!bossrifts.boss_exception,tag=!bossrifts.rift_bosses.ready] at @s run function boss_rifts_extended_compat:spawnthethingthatbirthsariftcorewhenthebossdies

function boss_rifts_extended_compat:compat/battle_towers
function boss_rifts_extended_compat:compat/annihilation_recreated
function boss_rifts_extended_compat:compat/stellarity
function boss_rifts_extended_compat:compat/incendium
function boss_rifts_extended_compat:compat/ice_and_fire
function boss_rifts_extended_compat:compat/qliphoth_awakening
function boss_rifts_extended_compat:compat/the_ice_warrior
function boss_rifts_extended_compat:compat/svm_super_powers
function boss_rifts_extended_compat:compat/yungs_better_desert_temples
function boss_rifts_extended_compat:compat/journey_into_the_light
function boss_rifts_extended_compat:compat/multiverse
function boss_rifts_extended_compat:compat/sengoku_jidai
function boss_rifts_extended_compat:compat/dungeons_and_taverns
