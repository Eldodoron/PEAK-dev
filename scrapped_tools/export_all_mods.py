import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\deep_scan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sort by filename
sorted_mods = sorted(data.values(), key=lambda x: x['filename'].lower())

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\all_mods_summary.txt', 'w', encoding='utf-8') as out:
    for m in sorted_mods:
        fn = m['filename']
        mid = m.get('mod_id')
        name = m.get('display_name')
        desc = (m.get('desc') or '').replace('\n', ' ')[:100]
        has_data = m.get('has_data')
        dt = m.get('display_test')
        dep_side = m.get('dep_side')
        env = m.get('env')
        mixins = m.get('mixins', [])
        client_mix = sum(x.get('client', 0) for x in mixins)
        server_mix = sum(x.get('server', 0) for x in mixins)
        common_mix = sum(x.get('common', 0) for x in mixins)
        
        out.write(f"FILE: {fn}\n")
        out.write(f"  ID: {mid} | NAME: {name}\n")
        out.write(f"  DATA: {has_data} | DT: {dt} | DEP_SIDE: {dep_side} | ENV: {env}\n")
        out.write(f"  MIXINS: client={client_mix}, server={server_mix}, common={common_mix}\n")
        out.write(f"  DESC: {desc}\n\n")

print("Wrote all_mods_summary.txt")
