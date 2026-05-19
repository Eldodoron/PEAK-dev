# PEAK Optimizations — Dungeons and Taverns nova_structures tick override
# ORIGINAL: scheduled every 5 ticks (4x per second!) 
# OPTIMIZED: scheduled every 40 ticks (2 seconds).
# Lightning bolt and wither skeleton checks don't need 4x/second precision.
# Lightning bolts exist for <2 seconds total, so checking every 2s is still safe.

execute as @e[type=lightning_bolt] at @s run function nova_structures:find_allays
execute as @e[type=wither_skeleton, tag=!withering] run function nova_structures:add_withering
schedule function nova_structures:tick 40t
