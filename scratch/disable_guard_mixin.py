import zipfile
import json
import shutil
import os

jar_path = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/mods/mobplayeranimator-neoforge-1.21.1-1.4.0.jar"
backup_path = jar_path + ".bak"

def patch_jar():
    # 1. Backup the original jar if not already backed up
    if not os.path.exists(backup_path):
        shutil.copy2(jar_path, backup_path)
        print(f"Backup created at {backup_path}")
    else:
        print(f"Backup already exists at {backup_path}")

    temp_jar_path = jar_path + ".tmp"

    with zipfile.ZipFile(backup_path, 'r') as yin, zipfile.ZipFile(temp_jar_path, 'w') as yout:
        for item in yin.infolist():
            data = yin.read(item.filename)
            if item.filename == "mobplayeranimator.neoforge.mixins.json":
                # Modify the json
                config = json.loads(data.decode('utf-8'))
                if "client" in config:
                    original_len = len(config["client"])
                    config["client"] = [m for m in config["client"] if "GuardModelMixin" not in m]
                    if len(config["client"]) < original_len:
                        print("Successfully removed GuardModelMixin from client mixins list")
                    else:
                        print("GuardModelMixin not found in config, no changes made")
                data = json.dumps(config, indent=2).encode('utf-8')
            yout.writestr(item, data)

    # Replace the original jar with the modified one
    if os.path.exists(jar_path):
        os.remove(jar_path)
    os.rename(temp_jar_path, jar_path)
    print("Jar successfully patched and replaced!")

if __name__ == "__main__":
    patch_jar()
