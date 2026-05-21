import json
import sys

filepath = r"C:\Users\chris\.gemini\antigravity\brain\8d114a67-432d-452e-9cc0-80f865c0f7fe\.system_generated\steps\605\content.md"

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
root_idx = server_thread["childrenRefs"][0] # 27643

# We will use the second time window for analysis (e.g. index 1) or first (index 0).
# Let's check which index corresponds to which.
# The total samples at root for each window:
# [8768, 60076, 51104]
# Let's print for all three windows or choose index 1 (usually the 5-minute average, which has the most samples: 60076)
window_idx = 1
total_samples = children[root_idx]["times"][window_idx]
print(f"Analyzing call tree using window index {window_idx} with total samples = {total_samples}")

def get_node_info(idx):
    node = children[idx]
    c_name = node.get("className", "Unknown")
    m_name = node.get("methodName", "Unknown")
    line = node.get("lineNumber", 0)
    samples = node.get("times", [0, 0, 0])[window_idx]
    pct = (samples / total_samples) * 100 if total_samples > 0 else 0
    return f"{c_name}.{m_name}:{line}", samples, pct, node.get("childrenRefs", [])

# Let's print the hot paths recursively. If a child has more than 5% of the total samples, we follow it.
def print_hot_tree(idx, depth=0, min_pct=1.0):
    name, samples, pct, child_refs = get_node_info(idx)
    if pct < min_pct:
        return
    
    indent = "  " * depth
    print(f"{indent}- {name} | {samples} samples ({pct:.2f}%)")
    
    # Sort children by samples descending
    child_info = []
    for cr in child_refs:
        _, c_samples, c_pct, _ = get_node_info(cr)
        child_info.append((c_samples, cr))
    child_info.sort(reverse=True, key=lambda x: x[0])
    
    for c_samples, cr in child_info:
        print_hot_tree(cr, depth + 1, min_pct)

print_hot_tree(root_idx, min_pct=1.0)
