import json

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
root_idx = server_thread["childrenRefs"][0]
window_idx = 1

matches = []

def find_nodes(idx, path=[]):
    node = children[idx]
    c_name = node.get("className", "Unknown")
    m_name = node.get("methodName", "Unknown")
    full_name = f"{c_name}.{m_name}"
    
    current_path = path + [f"{full_name}:{node.get('lineNumber', 0)} ({node.get('times', [0,0,0])[window_idx]} samples)"]
    
    if "mimic" in c_name.lower() or "artifact" in c_name.lower():
        matches.append((node.get("times", [0,0,0])[window_idx], current_path))
    
    for cr in node.get("childrenRefs", []):
        find_nodes(cr, current_path)

find_nodes(root_idx)

# Sort by samples descending
matches.sort(reverse=True, key=lambda x: x[0])
print(f"Total Mimic/Artifacts nodes: {len(matches)}")
for s, path in matches[:10]:
    print(f"\n--- {s} samples ---")
    for step in path[-5:]:
        print(f"  {step}")
