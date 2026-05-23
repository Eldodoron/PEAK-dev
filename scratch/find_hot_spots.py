import json
import collections
import os
import sys

script_dir = os.path.dirname(__file__)
default_path = os.path.join(script_dir, "content.md")
filepath = sys.argv[1] if len(sys.argv) > 1 else default_path

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

json_str = ""
for line in lines:
    if line.strip().startswith("{"):
        json_str = line.strip()
        break

data = json.loads(json_str)
server_thread = data["threads"][0]
children = server_thread["children"]
root_idx = server_thread["childrenRefs"][0]

window_idx = 1
total_samples = children[root_idx]["times"][window_idx]

print(f"Total samples: {total_samples}")

# Let's aggregate sample counts by class and method to see who is taking the most time overall (flat profile)
class_samples = collections.defaultdict(int)
method_samples = collections.defaultdict(int)

for node in children:
    c_name = node.get("className", "Unknown")
    m_name = node.get("methodName", "Unknown")
    # A node's self time? In Spark, times[window_idx] is the time spent in this node AND its children.
    # Wait, how to compute self time? Self time of a node = samples(node) - sum(samples(children)).
    samples = node.get("times", [0, 0, 0])[window_idx]
    if samples == 0:
        continue
    
    # Calculate sum of child samples
    child_refs = node.get("childrenRefs", [])
    child_sum = 0
    for cr in child_refs:
        child_sum += children[cr].get("times", [0, 0, 0])[window_idx]
    
    self_samples = max(0, samples - child_sum)
    if self_samples > 0:
        class_samples[c_name] += self_samples
        method_samples[f"{c_name}.{m_name}"] += self_samples

print("\n--- TOP 20 FLAT CLASSES (SELF TIME) ---")
sorted_classes = sorted(class_samples.items(), key=lambda x: x[1], reverse=True)
for c, s in sorted_classes[:20]:
    pct = (s / total_samples) * 100
    print(f"{c}: {s} samples ({pct:.2f}%)")

print("\n--- TOP 20 FLAT METHODS (SELF TIME) ---")
sorted_methods = sorted(method_samples.items(), key=lambda x: x[1], reverse=True)
for m, s in sorted_methods[:20]:
    pct = (s / total_samples) * 100
    print(f"{m}: {s} samples ({pct:.2f}%)")

# Let's find which mods these classes belong to
# We can do this by looking at package names.
print("\n--- ESTIMATED MOD CPU BY SELF TIME ---")
mod_samples = collections.defaultdict(int)
for m, s in method_samples.items():
    parts = m.split(".")
    if len(parts) >= 2:
        # Check package structure
        pkg = ".".join(parts[:3])
        # Group common ones
        if pkg.startswith("net.minecraft"):
            pkg = "Minecraft (Vanilla)"
        elif pkg.startswith("java.") or pkg.startswith("sun."):
            pkg = "Java Runtime"
        elif pkg.startswith("org.lwjgl"):
            pkg = "LWJGL (Client/Rendering)"
        elif "apotheosis" in m.lower():
            pkg = "Apotheosis"
        elif "alexsmobs" in m.lower():
            pkg = "Alex's Mobs"
        elif "alexscaves" in m.lower():
            pkg = "Alex's Caves"
        elif "mowziesmobs" in m.lower():
            pkg = "Mowzie's Mobs"
        elif "iceandfire" in m.lower():
            pkg = "Ice and Fire"
        elif "lootr" in m.lower():
            pkg = "Lootr"
        elif "create" in m.lower():
            pkg = "Create"
        elif "vampirism" in m.lower():
            pkg = "Vampirism"
        elif "servercore" in m.lower():
            pkg = "ServerCore"
        elif "c2me" in m.lower():
            pkg = "C2ME"
        elif "irons_spellbooks" in m.lower():
            pkg = "Iron's Spells 'n Spellbooks"
        elif "friendsandfoes" in m.lower():
            pkg = "Friends & Foes"
        elif "gateways" in m.lower():
            pkg = "Gateways to Eternity"
        elif "supplementaries" in m.lower():
            pkg = "Supplementaries"
        else:
            # Package base name
            pkg = ".".join(parts[:2])
        mod_samples[pkg] += s

sorted_mods = sorted(mod_samples.items(), key=lambda x: x[1], reverse=True)
for pkg, s in sorted_mods[:15]:
    pct = (s / total_samples) * 100
    print(f"{pkg}: {s} samples ({pct:.2f}%)")

# Let's print the hierarchical tree but only showing nodes with >= 4.0% total time to avoid truncation
def print_hot_tree_pct(idx, depth=0, min_pct=4.0):
    node = children[idx]
    c_name = node.get("className", "Unknown")
    m_name = node.get("methodName", "Unknown")
    line = node.get("lineNumber", 0)
    samples = node.get("times", [0, 0, 0])[window_idx]
    pct = (samples / total_samples) * 100 if total_samples > 0 else 0
    if pct < min_pct:
        return
    
    indent = "  " * depth
    print(f"{indent}- {c_name}.{m_name}:{line} | {samples} samples ({pct:.2f}%)")
    
    child_refs = node.get("childrenRefs", [])
    # Sort children by samples descending
    child_info = []
    for cr in child_refs:
        c_samples = children[cr].get("times", [0, 0, 0])[window_idx]
        child_info.append((c_samples, cr))
    child_info.sort(reverse=True, key=lambda x: x[0])
    
    for c_samples, cr in child_info:
        print_hot_tree_pct(cr, depth + 1, min_pct)

print("\n--- HIERARCHICAL TREE (>= 4.0% SAMPLES) ---")
print_hot_tree_pct(root_idx, min_pct=4.0)
