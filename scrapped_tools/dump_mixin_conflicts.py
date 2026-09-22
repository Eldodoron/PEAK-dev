with open('minecraft/logs/latest.log', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines in latest.log: {len(lines)}")
conflicts = []
for l in lines:
    if '[mixin/]' in l and any(k in l for k in ['WARN', 'ERROR', 'conflict', 'Skipping', 'Cannot']):
        conflicts.append(l.strip())

print(f"Total Mixin Warnings/Conflicts: {len(conflicts)}")
for c in conflicts:
    print(c)
