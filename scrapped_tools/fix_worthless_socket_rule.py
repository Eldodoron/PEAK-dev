import os
import json

base_dir = os.path.abspath('minecraft/kubejs/data')
fixed_files = []

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.json') and 'rarity_override' in root:
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            
            overrides = data.get('overrides', {})
            modified = False
            
            if 'nadir:worthless' in overrides:
                worthless_rules = overrides['nadir:worthless']
                # Check if it has the invalid socket rule with min=0, max=0
                cleaned_rules = []
                for rule in worthless_rules:
                    if rule.get('type') == 'apotheosis:socket' and rule.get('max', 1) < 1:
                        modified = True
                    else:
                        cleaned_rules.append(rule)
                if modified:
                    overrides['nadir:worthless'] = cleaned_rules
            
            if modified:
                with open(path, 'w', encoding='utf-8') as fh:
                    json.dump(data, fh, indent=4)
                fixed_files.append(path)

print(f"Fixed {len(fixed_files)} files:")
for f in fixed_files:
    print("  ->", f)
