import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\ambiguous_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fn, info in sorted(data.items()):
    mix = info.get('mixins', [])
    c_list = []
    s_list = []
    comm_list = []
    for m in mix:
        c_list.extend(m.get('client', []))
        s_list.extend(m.get('server', []))
        comm_list.extend(m.get('common', []))
    
    net = info.get('net_classes_count', 0)
    cmd = info.get('cmd_classes_count', 0)
    
    print(f"=== {fn} ===")
    print(f"  Mixins: client={len(c_list)}, server={len(s_list)}, common={len(comm_list)}")
    if c_list:
        print(f"    Sample client mixins: {c_list[:3]}")
    if comm_list:
        print(f"    Sample comm mixins: {comm_list[:3]}")
    if s_list:
        print(f"    Sample server mixins: {s_list[:3]}")
    print(f"  Net classes: {net} | Cmd classes: {cmd}")
    if net > 0:
        print(f"    Sample net: {info.get('net_classes_sample', [])[:3]}")
