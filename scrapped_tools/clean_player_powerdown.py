import os
import shutil
import nbtlib

playerdata_dir = r"minecraft/saves/New World (4)/playerdata"

for filename in os.listdir(playerdata_dir):
    if filename.endswith(".dat") or filename.endswith(".dat_old"):
        if filename.endswith(".bak"):
            continue
        filepath = os.path.join(playerdata_dir, filename)
        try:
            nbt_file = nbtlib.load(filepath)
            modified = False

            # Clean active_effects
            if 'active_effects' in nbt_file:
                original_len = len(nbt_file['active_effects'])
                filtered_effects = [
                    eff for eff in nbt_file['active_effects']
                    if eff.get('id') != 'alexsmobs:power_down'
                ]
                if len(filtered_effects) != original_len:
                    nbt_file['active_effects'] = nbtlib.List[nbtlib.Compound](filtered_effects)
                    print(f"Removed alexsmobs:power_down from active_effects in {filename}")
                    modified = True

            # Clean attributes modifiers
            if 'attributes' in nbt_file:
                for attr in nbt_file['attributes']:
                    if 'modifiers' in attr:
                        orig_mods_len = len(attr['modifiers'])
                        filtered_mods = [
                            mod for mod in attr['modifiers']
                            if 'power_down' not in str(mod.get('id', ''))
                        ]
                        if len(filtered_mods) != orig_mods_len:
                            attr['modifiers'] = nbtlib.List[nbtlib.Compound](filtered_mods)
                            print(f"Removed power_down modifier from {attr.get('id')} in {filename}")
                            modified = True

            if modified:
                backup_path = filepath + ".bak"
                shutil.copyfile(filepath, backup_path)
                nbt_file.save(filepath, gzipped=True)
                print(f"Successfully cleaned and saved {filename} (backup at {backup_path})")
            else:
                print(f"No power_down effects found in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
