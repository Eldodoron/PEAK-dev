import re

log_path = 'minecraft/logs/latest.log'
milestones = []

with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if any(w in line for w in ['Loading Minecraft', 'Mod loading', 'Backend library', 'Sound engine', 'Reloading ResourceManager', 'Starting integrated server', 'Time elapsed:', 'logged in with entity id', 'All data packs loaded in:']):
            milestones.append(line.strip())

print(f"Key Startup Milestones ({len(milestones)} events):")
for m in milestones:
    print(" ", m)
