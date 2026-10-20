import re

CONFIG_PATH = "minecraft/config/apotheosis/enchantments.cfg"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    text = f.read()

checks = [
    "minecraft:silk_touch",
    "minecraft:sharpness",
    "minecraft:unbreaking",
    "reliquary:severing",
    "apothic_spawners:capturing",
    "malum:spirit_plunder",
    "kubejs:subjugation",
    "deeperdarker:sculk_smite",
    "alexscaves:energy_efficiency",
    "alexscaves:gamma_ray",
    "nova_structures:boss_behaviour"
]

for name in checks:
    pattern = rf'"{re.escape(name)}"\s*\{{([^}}]+)\}}'
    m = re.search(pattern, text)
    if m:
        body = m.group(1)
        min_p = re.search(r'S:"Min Power Function"=(.*)', body)
        max_p = re.search(r'S:"Max Power Function"=(.*)', body)
        max_l = re.search(r'I:"Max Level"=(.*)', body)
        forced = re.search(r'I:"Forced Level Cap"=(.*)', body)
        print(f"[{name}]")
        print(f"  Max Level: {max_l.group(1).strip() if max_l else 'N/A'}")
        print(f"  Forced Cap: {forced.group(1).strip() if forced else 'N/A'}")
        print(f"  Min Power: {min_p.group(1).strip() if min_p else 'N/A'}")
        print(f"  Max Power: {max_p.group(1).strip() if max_p else 'N/A'}")
    else:
        print(f"[{name}] NOT FOUND!")
