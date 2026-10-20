import re

with open("minecraft/ct_dumps/enchantment.txt", "r", encoding="utf-8") as f:
    active_enchants = set(line.strip()[13:-1] for line in f if line.strip().startswith("<enchantment:"))

with open("minecraft/config/apotheosis/enchantments.cfg", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'"([^"]+)"\s*\{([^}]+)\}', re.MULTILINE)
matches = pattern.findall(content)

ench_data = {}
for name, block in matches:
    if name not in active_enchants or name.startswith("minecraft:"):
        continue
    max_lvl = re.search(r'I:"Max Level"=(\d+)', block)
    max_loot = re.search(r'I:"Max Loot Level"=(\d+)', block)
    min_pow = re.search(r'S:"Min Power Function"=(.*)', block)
    max_pow = re.search(r'S:"Max Power Function"=(.*)', block)
    ench_data[name] = {
        "max_lvl": int(max_lvl.group(1)) if max_lvl else 1,
        "max_loot": int(max_loot.group(1)) if max_loot else 1,
        "min_pow": min_pow.group(1).strip() if min_pow else "",
        "max_pow": max_pow.group(1).strip() if max_pow else ""
    }

print(f"Total modded active enchantments: {len(ench_data)}")
# Group by mod
by_mod = {}
for name, data in ench_data.items():
    mod = name.split(":")[0]
    by_mod.setdefault(mod, []).append((name, data))

for mod, items in sorted(by_mod.items()):
    print(f"\n=== {mod} ({len(items)}) ===")
    for name, d in sorted(items):
        print(f"  {name}: max_lvl={d['max_lvl']}")
