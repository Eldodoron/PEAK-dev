import zipfile
import json
import os

KUBEJS_DATA = os.path.abspath('minecraft/kubejs/data')

def fix_ida_tables():
    print("Fixing IDA Dungeons Arise loot tables (1.20 'name' -> 1.21 'value')...")
    ida_jar = 'minecraft/mods/IDA v2.1.1-1.21.1.jar'
    targets = [
        'data/dungeons_arise/loot_table/chests/plague_asylum/plague_asylum_cells.json',
        'data/dungeons_arise/loot_table/chests/plague_asylum/plague_asylum_potions.json',
        'data/dungeons_arise/loot_table/chests/plague_asylum/plague_asylum_treasure.json',
        'data/dungeons_arise/loot_table/chests/thornborn_towers/thornborn_towers_top_rooms.json',
        'data/dungeons_arise/loot_table/chests/typhon/typhon_treasure.json'
    ]
    with zipfile.ZipFile(ida_jar) as z:
        for path in targets:
            data = json.loads(z.read(path).decode('utf-8'))
            for pool in data.get('pools', []):
                for entry in pool.get('entries', []):
                    if entry.get('type') == 'minecraft:loot_table' and 'name' in entry:
                        entry['value'] = entry.pop('name')
            
            # Destination path: kubejs/data/dungeons_arise/loot_table/...
            rel_path = path[len('data/'):]
            dest = os.path.join(KUBEJS_DATA, rel_path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"  -> Fixed and wrote: {dest}")

def fix_iss_tables():
    print("Fixing ISS Dungeons Arise Seven Seas loot tables (replace missing upgrade_aquatic:pickerelweed with minecraft:seagrass)...")
    iss_jar = 'minecraft/mods/ISS-1.21.1.jar'
    targets = [
        'data/dungeons_arise_seven_seas/loot_table/chests/pirate_junk/pirate_junk_supply.json',
        'data/dungeons_arise_seven_seas/loot_table/chests/unicorn_galleon/unicorn_galleon_supply.json'
    ]
    with zipfile.ZipFile(iss_jar) as z:
        for path in targets:
            data = json.loads(z.read(path).decode('utf-8'))
            for pool in data.get('pools', []):
                for entry in pool.get('entries', []):
                    if entry.get('name') == 'upgrade_aquatic:pickerelweed':
                        entry['name'] = 'minecraft:seagrass'
            
            rel_path = path[len('data/'):]
            dest = os.path.join(KUBEJS_DATA, rel_path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"  -> Fixed and wrote: {dest}")

if __name__ == '__main__':
    fix_ida_tables()
    fix_iss_tables()
    print("All IDA & ISS loot table overrides generated successfully!")
