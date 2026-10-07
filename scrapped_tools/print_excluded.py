import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\classification_results.json', 'r', encoding='utf-8') as f:
    res = json.load(f)

print(f"=== 67 EXCLUDED MODS ===")
for i, m in enumerate(res['excluded'], 1):
    dis = " [DISABLED]" if m['is_disabled'] else ""
    bak = " [BACKUP/MODIFIED]" if m['is_backup'] else ""
    print(f"{i:2d}. {m['filename']}{dis}{bak} | Cat: {m['category']} | Reason: {m['reason']}")
