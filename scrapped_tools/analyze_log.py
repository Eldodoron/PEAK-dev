import re

log_path = 'minecraft/logs/latest.log'
cant_keep_up = []
mixin_errors = []
slow_events = []
gc_warnings = []
other_warnings = []

with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if "Can't keep up!" in line:
            cant_keep_up.append(line.strip())
        elif 'Mixin' in line and any(w in line for w in ['Error', 'Failed', 'conflict', 'Cannot']):
            mixin_errors.append(line.strip())
        elif 'took' in line and any(w in line for w in ['ms', 'seconds']):
            slow_events.append(line.strip())
        elif 'OutOfMemory' in line or 'GC' in line:
            gc_warnings.append(line.strip())

print(f"Total 'Can't keep up!' occurrences: {len(cant_keep_up)}")
for line in cant_keep_up[:10]:
    print("  ", line)

print(f"\nTotal Mixin errors/conflicts: {len(mixin_errors)}")
for line in mixin_errors[:10]:
    print("  ", line)

print(f"\nSlow events sample:")
for line in [l for l in slow_events if any(k in l.lower() for k in ['time', 'slow', 'warning', 'lag'])][:10]:
    print("  ", line)
