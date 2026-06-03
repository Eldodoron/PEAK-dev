import os
import glob

# Map of old broken items to deduced new items for 1.21.1
replacements = {
    "pneumaticcraft:compressor": "pneumaticcraft:air_compressor",
    "iceandfire:dragon_bone": "iceandfire:dragonbone",
    "create_enchantment_industry:experience_rotor": "create_enchantment_industry:experience_hatch",
    "alexscaves:pulse_laser": "alexscaves:raygun",
    "kubejs:chaos_essence": "draconicevolution:chaos_shard"
}

scripts_dir = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts"
files = glob.glob(os.path.join(scripts_dir, "*.js"))

files_modified = 0

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_content = content
    for old, new in replacements.items():
        if old in new_content:
            new_content = new_content.replace(old, new)
            
    if content != new_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        files_modified += 1
        print(f"Updated {os.path.basename(file_path)}")

print(f"Total files modified: {files_modified}")
