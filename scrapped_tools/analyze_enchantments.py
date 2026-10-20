import re

with open('minecraft/config/apotheosis/enchantments.cfg', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'"([^"]+)"\s*\{([^}]+)\}', text)
print(f"Total configured enchantments: {len(sections)}")

custom_max_levels = []
custom_powers = []
for name, body in sections:
    max_lvl = re.search(r'I:"Max Level"=(\d+)', body)
    min_power = re.search(r'S:"Min Power Function"=([^\r\n]*)', body)
    max_power = re.search(r'S:"Max Power Function"=([^\r\n]*)', body)
    if max_lvl:
        custom_max_levels.append((name, int(max_lvl.group(1))))
    if (min_power and min_power.group(1).strip()) or (max_power and max_power.group(1).strip()):
        custom_powers.append((name, min_power.group(1).strip() if min_power else '', max_power.group(1).strip() if max_power else ''))

print(f"Enchantments with custom powers: {len(custom_powers)}")
for item in custom_powers[:10]:
    print(item)
print("Sample max levels (first 20):")
for item in custom_max_levels[:20]:
    print(item)
