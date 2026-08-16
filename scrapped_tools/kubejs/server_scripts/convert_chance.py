import os
import re

directory = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\kubejs\server_scripts"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Item.of('item').withChance(X)
    pattern = r"Item\.of\((['\"`].*?['\"`])\)\.withChance\((.*?)\)"
    new_content, count = re.subn(pattern, r"CreateItem.of(\1, \2)", content)

    # Fix experience nugget
    new_content, c2 = re.subn(r"minecraft:experience_nugget", r"create:experience_nugget", new_content)
    count += c2

    # Fix {fluidTag: c:ethanol, amount: 100.0}
    # Create 1.21 Fluid ingredients for tags: Fluid.of('#c:ethanol', 100) or {fluid: "#c:ethanol", amount: 100}
    # Wait, KubeJS 1.21 NeoForge expects fluid tags to be Fluid.of('#c:milk', 250) or similar.
    # The user used {fluidTag: 'c:milk', amount: 250.0} or {fluidTag: c:ethanol, amount: 100.0} in 01_readded_recipes.js
    pattern_fluid = r"\{fluidTag:\s*([c\w:]+),\s*amount:\s*([\d.]+)\}"
    new_content, c3 = re.subn(pattern_fluid, r"Fluid.of('#\1', \2)", new_content)
    count += c3

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced {count} instances in {os.path.basename(filepath)}")

for filename in os.listdir(directory):
    if filename.endswith(".js"):
        process_file(os.path.join(directory, filename))

print("Conversion complete!")
