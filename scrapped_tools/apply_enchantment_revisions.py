import re

CONFIG_PATH = "minecraft/config/apotheosis/enchantments.cfg"

# Base definitions for min/max power functions
# Format: (min_base, min_step, max_offset) -> 
#   min_func: f"{min_base} + (x - 1) * {min_step}" (if min_step > 0 else f"{min_base}")
#   max_func: f"{min_base + max_offset} + (x - 1) * {min_step}" (if min_step > 0 else f"{min_base + max_offset}")

# Default window offset is 35 for scaling enchants, 100 for single level enchants.

RULES = {
    # ====================
    # VANILLA ESSENTIALS
    # ====================
    # Sharpness, Efficiency, Power: Early Wood (1-3) -> Nether (4-5) -> Ocean/End (6+)
    "minecraft:sharpness": (1, 10, 35),
    "minecraft:efficiency": (1, 10, 35),
    "minecraft:power": (1, 10, 35),
    "minecraft:protection": (1, 11, 35),
    "minecraft:projectile_protection": (1, 10, 35),
    "minecraft:blast_protection": (5, 10, 35),
    "minecraft:fire_protection": (5, 10, 35),
    "minecraft:feather_falling": (5, 9, 35),
    "minecraft:respiration": (10, 10, 35),
    "minecraft:aqua_affinity": (1, 0, 100),
    "minecraft:thorns": (10, 15, 35),
    "minecraft:depth_strider": (10, 10, 35),
    "minecraft:unbreaking": (5, 13, 35), # Lvl 1: 5, Lvl 2: 18 (wood), Lvl 3: 31 (Hellshelves!)
    "minecraft:fortune": (16, 12, 35),  # Lvl 1: 16 (Late wood), Lvl 2: 28 (End of wood), Lvl 3: 40 (Nether!)
    "minecraft:looting": (16, 12, 35),  # Lvl 1: 16 (Late wood), Lvl 2: 28, Lvl 3: 40 (Nether!)
    "minecraft:sweeping_edge": (10, 10, 35),
    "minecraft:punch": (12, 15, 35),
    "minecraft:knockback": (5, 15, 35),
    "minecraft:smite": (5, 9, 35),
    "minecraft:bane_of_arthropods": (5, 9, 35),
    "minecraft:impaling": (10, 10, 35),
    "minecraft:loyalty": (12, 9, 35),
    "minecraft:channeling": (25, 0, 100),
    "minecraft:riptide": (15, 12, 35),
    "minecraft:luck_of_the_sea": (15, 10, 35),
    "minecraft:lure": (15, 10, 35),
    "minecraft:multishot": (20, 0, 100),
    "minecraft:piercing": (10, 10, 35),
    "minecraft:quick_charge": (12, 12, 35),
    "minecraft:breach": (15, 10, 35),
    "minecraft:density": (15, 10, 35),
    "minecraft:wind_burst": (35, 10, 40), # Trial / Wind burst requires Nether setup
    
    # Tier 2 Rare / Gatekeeper Vanilla:
    "minecraft:silk_touch": (36, 0, 100), # Tier 2 strictly! Cannot roll on basic wood shelves (cap 30)
    "minecraft:fire_aspect": (32, 10, 40), # Tier 2 Nether
    "minecraft:flame": (34, 0, 100),      # Tier 2 Nether
    "minecraft:infinity": (36, 0, 100),   # Tier 2 Nether

    # ====================
    # ARS NOUVEAU
    # ====================
    "ars_nouveau:mana_boost": (12, 8, 35), # Lvl 1 at 12 (mid wood), Lvl 2 at 20, Lvl 3 at 28 (late wood)
    "ars_nouveau:mana_regen": (16, 8, 35), # Lvl 1 at 16 (mid-late wood), Lvl 2 at 24, Lvl 3 at 32 (Nether)
    "ars_nouveau:reactive": (45, 5, 40),   # Tier 3 (Ocean / Seashelves)

    # ====================
    # MALUM
    # ====================
    "malum:spirit_plunder": (22, 10, 35), # Lvl 1 at 22 (late wood - early spirit harvest), Lvl 2 at 32 (Nether), Lvl 3 at 42
    "malum:animated": (32, 8, 35),
    "malum:rebound": (34, 8, 35),
    "malum:haunted": (35, 8, 35),
    "malum:replenishing": (36, 8, 35),
    "malum:weavers_haste": (35, 7, 35),
    "malum:weavers_propagation": (38, 7, 35),
    "malum:ascension": (50, 8, 40), # Tier 3 Seashelves
    "malum:capacitor": (50, 8, 40), # Tier 3 Seashelves

    # ====================
    # KUBEJS CUSTOM
    # ====================
    "kubejs:subjugation": (20, 0, 100), # Late wood (Power 20) - early villager transport
    "kubejs:concussive_impact": (32, 6, 35), # Tier 2 Hellshelves
    "kubejs:soul_siphon": (35, 7, 35),      # Tier 2 Hellshelves
    "kubejs:midas_touch": (50, 8, 40),      # Tier 3 Seashelves

    # ====================
    # ALEX'S MOBS
    # ====================
    "alexsmobs:board_return": (15, 0, 100), # Mid wood
    "alexsmobs:serpentfriend": (20, 0, 100), # Late wood
    "alexsmobs:straddle_jump": (32, 6, 35), # Tier 2 Nether
    "alexsmobs:lavawax": (35, 0, 100),      # Tier 2 Nether

    # ====================
    # ALEX'S CAVES
    # ====================
    # Early Cave Utility (16-26 Power, Mid/Late Wood)
    "alexscaves:energy_efficiency": (16, 6, 35),
    "alexscaves:bouncy_ball": (18, 0, 100),
    "alexscaves:sharp_cane": (18, 7, 35),
    "alexscaves:seekcandy": (22, 0, 100),
    "alexscaves:charting_call": (24, 6, 35),
    "alexscaves:ferrous_haste": (22, 6, 35),
    
    # Mid Cave / Dinosaur / Magnetic / Candy (32-42 Power, Early/Mid Hellshelves)
    "alexscaves:chomping_spirit": (32, 0, 100),
    "alexscaves:double_stab": (34, 0, 100),
    "alexscaves:far_flung": (32, 6, 35),
    "alexscaves:flinging": (34, 6, 35),
    "alexscaves:heavy_slam": (35, 0, 100),
    "alexscaves:herd_phalanx": (34, 6, 35),
    "alexscaves:impending_stab": (35, 6, 35),
    "alexscaves:lasting_morale": (32, 6, 35),
    "alexscaves:multiple_mint": (32, 0, 100),
    "alexscaves:peppermint_punting": (34, 0, 100),
    "alexscaves:sated_blade": (35, 0, 100),
    "alexscaves:relentless_darkness": (36, 0, 100),
    "alexscaves:shaded_respite": (34, 0, 100),
    "alexscaves:straight_hook": (32, 0, 100),
    "alexscaves:swiftwood": (32, 6, 35),
    "alexscaves:targeted_ricochet": (35, 6, 35),
    "alexscaves:bonking": (32, 6, 35),
    "alexscaves:bouncing_bolt": (34, 0, 100),
    "alexscaves:dazing_sweep": (35, 0, 100),
    "alexscaves:detonating_death": (36, 0, 100),
    "alexscaves:enveloping_bubble": (35, 0, 100),
    "alexscaves:explosive_flavor": (34, 0, 100),
    "alexscaves:humungous_hex": (36, 0, 100),
    "alexscaves:rapid_possession": (34, 6, 35),
    "alexscaves:sightless": (35, 0, 100),
    "alexscaves:solar": (32, 0, 100),
    "alexscaves:spell_lasting": (34, 6, 35),
    "alexscaves:taxing_bellow": (35, 0, 100),
    "alexscaves:second_wave": (35, 0, 100),
    "alexscaves:triple_split": (36, 0, 100),

    # Abyssal Ocean / Toxic / Radiation / Late Cave (46-55 Power, Seashelves - Capped <= 55)
    "alexscaves:tsunami": (46, 0, 100),
    "alexscaves:sea_swing": (46, 6, 35),
    "alexscaves:seapairing": (48, 0, 100),
    "alexscaves:soak_seeking": (46, 0, 100),
    "alexscaves:triple_splash": (48, 0, 100),
    "alexscaves:gamma_ray": (50, 0, 100),
    "alexscaves:x_ray": (52, 0, 100),
    "alexscaves:crystallization": (48, 6, 35),
    "alexscaves:dark_nock": (48, 6, 35),
    "alexscaves:field_extension": (46, 6, 35),
    "alexscaves:plummeting_flight": (48, 0, 100),
    "alexscaves:twilight_perfection": (48, 6, 35),
    "alexscaves:astral_transferring": (50, 0, 100),
    "alexscaves:arrow_inducting": (48, 0, 100),
    "alexscaves:precise_volley": (48, 0, 100),

    # ====================
    # RELIQUARY & APOTHIC SPAWNERS
    # ====================
    "reliquary:severing": (34, 6, 35),
    "apothic_spawners:capturing": (35, 7, 35),

    # ====================
    # DEEPER AND DARKER
    # ====================
    "deeperdarker:sculk_smite": (32, 5, 35), # Prep weapon in Nether before Deep Dark
    "deeperdarker:volume": (35, 5, 35),
    "deeperdarker:catalysis": (62, 7, 35),   # Endgame Otherside
    "deeperdarker:reverberation": (65, 6, 35), # Endgame Otherside

    # ====================
    # CREATE & ADDONS
    # ====================
    "create:capacity": (12, 6, 35),
    "create:potato_recovery": (12, 6, 35),
    "create_ltab:wanderer": (18, 6, 35),
    "create_ltab:enchantment_luck": (35, 6, 35),
    "create_sa:above_the_clouds": (32, 0, 100),
    "create_sa:digging": (32, 0, 100),
    "create_sa:impact": (34, 6, 35),
    "create_sa:hellfire": (35, 0, 100),
    "create_sa:gravity_gun": (50, 0, 100),
    "create_sa:chunk_eater": (55, 4, 35),

    # ====================
    # FARMER'S & MY NETHER'S DELIGHT
    # ====================
    "farmersdelight:backstabbing": (12, 6, 35),
    "mynethersdelight:poaching": (34, 0, 100),

    # ====================
    # DARKER DEPTHS
    # ====================
    "darkerdepths:quick_dash": (32, 5, 35),
    "darkerdepths:swift_strike": (35, 0, 100),

    # ====================
    # UNDERGARDEN
    # ====================
    "undergarden:longevity": (48, 5, 35),
    "undergarden:ricochet": (48, 5, 35),
    "undergarden:self_sling": (46, 0, 100),

    # ====================
    # TWILIGHT FOREST
    # ====================
    "twilightforest:chill_aura": (32, 5, 35),
    "twilightforest:fire_react": (32, 5, 35),
    "twilightforest:destruction": (48, 6, 35),
    "twilightforest:renewal": (50, 0, 100),

    # ====================
    # APOTHIC ENCHANTING
    # ====================
    "apothic_enchanting:miners_fervor": (32, 6, 35),
    "apothic_enchanting:berserkers_fury": (35, 7, 35),
    "apothic_enchanting:scavenger": (34, 8, 35),
    "apothic_enchanting:shield_bash": (32, 6, 35),
    "apothic_enchanting:icy_thorns": (34, 6, 35),
    "apothic_enchanting:stable_footing": (32, 0, 100),
    "apothic_enchanting:tempting": (25, 0, 100),
    "apothic_enchanting:boon_of_the_earth": (36, 6, 35),
    "apothic_enchanting:rebounding": (35, 6, 35),
    "apothic_enchanting:worker_exploitation": (45, 0, 100),
    "apothic_enchanting:chromatic": (30, 0, 100),
    "apothic_enchanting:life_mending": (50, 8, 35),
    "apothic_enchanting:knowledge_of_the_ages": (48, 8, 35),
    "apothic_enchanting:chainsaw": (50, 0, 100),
    "apothic_enchanting:endless_quiver": (52, 0, 100),
    "apothic_enchanting:natures_blessing": (48, 6, 35),
    "apothic_enchanting:reflective_defenses": (48, 6, 35),
    "apothic_enchanting:crescendo_of_bolts": (60, 8, 35),
    "apothic_enchanting:growth_serum": (62, 0, 100),
    "apothic_enchanting:infusion": (65, 0, 100),

    # ====================
    # DUNGEONS ARISE
    # ====================
    "dungeons_arise:discharge": (32, 6, 35),
    "dungeons_arise:ensnaring": (34, 6, 35),
    "dungeons_arise:purification": (35, 6, 35),
    "dungeons_arise:voltaic_shot": (36, 0, 100),
    "dungeons_arise:lolths_curse": (40, 0, 100),

    # ====================
    # MINECOLONIES & NORTHSTAR & SUPPLEMENTARIES
    # ====================
    "minecolonies:raider_damage_enchant": (25, 6, 35),
    "northstar:frostbite": (35, 6, 35),
    "supplementaries:stasis": (20, 0, 100),

    # ====================
    # NOVA STRUCTURES
    # ====================
    "nova_structures:boss_behaviour": (9999, 0, 0), # Internal boss trait - completely locked out
    "nova_structures:shulker_boss": (9999, 0, 0),   # Internal boss trait - completely locked out
    "nova_structures:shulker_miniboss": (9999, 0, 0), # Internal boss trait - completely locked out
    "nova_structures:antidote": (32, 0, 100),
    "nova_structures:photosynthesis": (34, 0, 100),
    "nova_structures:wax_wings": (35, 0, 100),
    "nova_structures:conductivity_curse": (36, 0, 100),
    "nova_structures:illagers_bane": (32, 5, 35),
    "nova_structures:traveler": (35, 6, 35),
    "nova_structures:gravity": (50, 6, 35),
    "nova_structures:outreach": (50, 6, 35),
    "nova_structures:ghasted": (52, 6, 35),
    "nova_structures:wither_coated": (55, 0, 100),

    # ====================
    # DRACONIC EVOLUTION
    # ====================
    "draconicevolution:reaper": (65, 6, 35), # True endgame (Tier 4)

    # ====================
    # UNUSUAL END
    # ====================
    "unusualend:arcane_recovery": (55, 4, 35),
    "unusualend:benevolence": (55, 0, 100),
    "unusualend:boloks_fury": (58, 4, 35),
    "unusualend:boloks_head": (58, 4, 35),
    "unusualend:boloks_wings": (58, 4, 35),
    "unusualend:bonding": (55, 0, 100),
    "unusualend:everlasting": (70, 0, 100), # Tier 4 Endgame
    "unusualend:joust": (55, 4, 35),
}

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    text = f.read()

updated_count = 0

def update_block(match):
    global updated_count
    name = match.group(1)
    body = match.group(2)
    
    if name not in RULES:
        return match.group(0)
    
    min_base, min_step, max_offset = RULES[name]
    
    if min_base >= 9999:
        # Disable/Lock completely
        min_formula = "9999"
        max_formula = "9999"
    elif min_step > 0:
        min_formula = f"{min_base} + (x - 1) * {min_step}"
        max_formula = f"{min_base + max_offset} + (x - 1) * {min_step}"
    else:
        min_formula = f"{min_base}"
        max_formula = f"{min_base + max_offset}"

    # Replace S:"Min Power Function"=... and S:"Max Power Function"=...
    body = re.sub(r'S:"Min Power Function"=.*', f'S:"Min Power Function"={min_formula}', body)
    body = re.sub(r'S:"Max Power Function"=.*', f'S:"Max Power Function"={max_formula}', body)
    
    # If it was an internal boss trait, also set Forced Level Cap to 0
    if min_base >= 9999:
        body = re.sub(r'I:"Forced Level Cap"=-?\d+', 'I:"Forced Level Cap"=0', body)
        body = re.sub(r'I:"Max Level"=\d+', 'I:"Max Level"=0', body)

    updated_count += 1
    return f'"{name}" {{{body}}}'

new_text = re.sub(r'"([^"]+)"\s*\{([^}]+)\}', update_block, text)

with open(CONFIG_PATH, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Successfully updated {updated_count} enchantments in {CONFIG_PATH}!")
