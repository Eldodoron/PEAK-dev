import os
import re

COLOR_CODES = {
    'black': '0',
    'darkBlue': '1',
    'darkGreen': '2',
    'darkAqua': '3',
    'darkRed': '4',
    'darkPurple': '5',
    'gold': '6',
    'gray': '7',
    'darkGray': '8',
    'blue': '9',
    'green': 'a',
    'aqua': 'b',
    'red': 'c',
    'lightPurple': 'd',
    'yellow': 'e',
    'white': 'f'
}

TARGET_FILES = [
    'minecraft/kubejs/server_scripts/09_custom_loot_tables.js',
    'minecraft/kubejs/server_scripts/12_admin_commands.js',
    'minecraft/kubejs/server_scripts/12_food_buffs.js',
    'minecraft/kubejs/server_scripts/20_disable_bugged_spells.js',
    'minecraft/kubejs/server_scripts/23_zenith_saber.js',
    'minecraft/kubejs/server_scripts/64_anvil_cost_cap.js',
    'minecraft/kubejs/server_scripts/apotheosis_auto_tiers.js',
    'minecraft/kubejs/server_scripts/void_teleport_pad.js',
    'minecraft/kubejs/server_scripts/yagm_xp_death_penalty.js',
    'minecraft/kubejs/server_scripts/65_sable_physics_tick_rate.js',
    'minecraft/kubejs/server_scripts/custom_enchantment_mechanics.js'
]

def fix_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    for color, code in COLOR_CODES.items():
        sec = '\u00A7'
        
        # 1. Single quotes: (Text|Component)\.<color>\('([^']*)'\)
        pattern_single = re.compile(rf'\b(Text|Component)\.{color}\(\'([^\']*)\'\)')
        content = pattern_single.sub(lambda m: f"Component.literal('{sec}{code}{m.group(2)}{sec}r')", content)

        # 2. Double quotes: (Text|Component)\.<color>\("([^"]*)"\)
        pattern_double = re.compile(rf'\b(Text|Component)\.{color}\("([^"]*)"\)')
        content = pattern_double.sub(lambda m: f'Component.literal("{sec}{code}{m.group(2)}{sec}r")', content)

        # 3. Backticks: (Text|Component)\.<color>\(`([^`]*)`\)
        pattern_backtick = re.compile(rf'\b(Text|Component)\.{color}\(`([^`]*)`\)')
        content = pattern_backtick.sub(lambda m: f'Component.literal(`{sec}{code}{m.group(2)}{sec}r`)', content)

        # 4. Expressions / variables: (Text|Component)\.<color>\(([^()]+)\)
        pattern_expr = re.compile(rf'\b(Text|Component)\.{color}\(([^()]+)\)')
        content = pattern_expr.sub(lambda m: f"Component.literal('{sec}{code}').append(Component.literal(String({m.group(2)}))).append(Component.literal('{sec}r'))", content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
    else:
        print(f"No changes: {filepath}")

def main():
    for f in TARGET_FILES:
        fix_file(f)

if __name__ == '__main__':
    main()

# Fix remaining nested calls
with open('minecraft/kubejs/server_scripts/apotheosis_auto_tiers.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("Text.darkGray('\\u00A7m' + '\\u2500'.repeat(40))", "Component.literal('\u00A78\u00A7m' + '\u2500'.repeat(40) + '\u00A7r')")

with open('minecraft/kubejs/server_scripts/apotheosis_auto_tiers.js', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(text)

with open('minecraft/kubejs/server_scripts/25_hardcoded_minibosses.js', 'r', encoding='utf-8') as f:
    text = f.read()

mapping = {
    'Text.gold': "'\\u00A76'",
    'Text.darkGreen': "'\\u00A72'",
    'Text.darkPurple': "'\\u00A75'",
    'Text.aqua': "'\\u00A7b'",
    'Text.darkRed': "'\\u00A74'",
    'Text.darkGray': "'\\u00A78'",
    'Text.red': "'\\u00A7c'",
    'Text.darkAqua': "'\\u00A73'",
    'Text.darkBlue': "'\\u00A71'",
    'Text.black': "'\\u00A70'",
    'Text.green': "'\\u00A7a'",
    'Text.yellow': "'\\u00A7e'",
}

for k, v in mapping.items():
    text = text.replace(f'color: {k}', f'color: {v}')

text = text.replace('entity.customName = config.color(config.name).bold();', 'entity.customName = Component.literal(`${config.color}\\u00A7l${config.name}\\u00A7r`);')
text = text.replace('entity.customName = set.color(set.name).bold();', 'entity.customName = Component.literal(`${set.color}\\u00A7l${set.name}\\u00A7r`);')

with open('minecraft/kubejs/server_scripts/25_hardcoded_minibosses.js', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(text)
print('Updated 25_hardcoded_minibosses.js')
