# PEAK Optimizations — Boss Rifts Compat+ tick override
# ORIGINAL ran every tick with 5+ global @e selectors over ALL entities.
# OPTIMIZED: Uses tag-based filtering so entities are only scanned once on spawn,
# not re-tagged every tick. Persistent tags are maintained by the boss rift system itself.

# Only run the rift position fixes on actual active rifts (cheap — filtered by type, not @e global)
scoreboard players add @e[type=bossrifts:boss_rift,scores={bossriftsextendedcompat_stuff=..300}] bossriftsextendedcompat_stuff 1
execute as @e[type=bossrifts:boss_rift] at @s unless block ~ ~-0.1 ~ #boss_rifts_extended_compat:phasethrough run tp @s ^ ^0.11111111111111 ^
execute as @e[type=bossrifts:boss_rift] at @s if block ~ ~-0.1 ~ lava run tp @s ^ ^0.11111111111111 ^
execute as @e[type=bossrifts:boss_rift,scores={bossriftsextendedcompat_stuff=..300}] at @s if block ~ ~-2 ~ #boss_rifts_extended_compat:phasethrough unless block ~ ~-2 ~ lava run tp @s ^ ^-0.08 ^

# Only process rift spawner entities (should be rare/none most of the time)
execute as @e[tag=bossriftsextendedcompat_thingthatmakerift] at @s run function boss_rifts_extended_compat:tickupdatethethingthatbirthsariftcorewhenthebossdies

# Phase 2 rift spawn check (filtered to specific tagged entities only)
execute as @e[tag=bossrifts_riftspawn_tocheckifthereisphase2...] at @s run execute unless entity @e[type=#boss_rifts_extended_compat:is_phase_2,tag=!bossrifts.boss_exception,distance=..88] unless entity @e[tag=bossrifts.rift_bosses,distance=0.1..88,tag=!bossrifts.boss_exception] unless entity @e[type=bossrifts:boss_rift,distance=0.00000000001..88] run summon bossrifts:boss_rift ~ ~2 ~
kill @e[tag=bossrifts_riftspawn_tocheckifthereisphase2...]
tag @e[tag=bossrifts_riftspawn_tocheckifthereisphase2..] add bossrifts_riftspawn_tocheckifthereisphase2...
tag @e[tag=bossrifts_riftspawn_tocheckifthereisphase2.] add bossrifts_riftspawn_tocheckifthereisphase2..
tag @e[tag=bossrifts_riftspawn_tocheckifthereisphase2] add bossrifts_riftspawn_tocheckifthereisphase2.

# Initialize new rifts (type-filtered, not global @e)
execute as @e[type=bossrifts:boss_rift,tag=!bossrifts.bossriftinitialized] run scoreboard players set @s bossriftsextendedcompat_stuff 0
tag @e[type=bossrifts:boss_rift,tag=!bossrifts.bossriftinitialized] add bossrifts.bossriftinitialized

# NOTE: Removed the 5 global @e[type=#tag] tag-assignment lines that ran every tick.
# Boss tags are now only assigned via the tick_1s function (every 60 ticks instead of every tick).
# Compat functions still run via tick_1s at reduced frequency.
