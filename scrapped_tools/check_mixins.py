import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\precise_mod_info.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== Mods with client mixins only ===")
for fn, m in sorted(data.items()):
    c_mix = m.get('client_mixins_count', 0)
    s_mix = m.get('server_mixins_count', 0)
    comm_mix = m.get('common_mixins_count', 0)
    mc_side = m.get('mc_dep_side')
    
    if c_mix > 0 and s_mix == 0 and comm_mix == 0:
        print(f"{fn} | c_mix={c_mix}, comm={comm_mix}, mc_side={mc_side}, data={m.get('has_data')}")
