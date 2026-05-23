import json
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

# Let's write a recursive function to find all occurrences of java.lang.ThreadLocal.set or similar,
# and print their parent call chains up to 5 levels deep.
matches = []

def find_nodes(idx, path=[]):
    node = children[idx]
    c_name = node.get("className", "Unknown")
    m_name = node.get("methodName", "Unknown")
    full_name = f"{c_name}.{m_name}"
    
    current_path = path + [f"{full_name}:{node.get('lineNumber', 0)} ({node.get('times', [0,0,0])[window_idx]} samples)"]
    
    if "java.lang.ThreadLocal" in c_name and m_name == "set":
        matches.append((node.get("times", [0,0,0])[window_idx], current_path))
    
    for cr in node.get("childrenRefs", []):
        find_nodes(cr, current_path)

find_nodes(root_idx)

# Sort by samples descending
matches.sort(reverse=True, key=lambda x: x[0])
print(f"Total ThreadLocal.set nodes: {len(matches)}")
for s, path in matches[:10]:
    print(f"\n--- {s} samples ---")
    for step in path[-6:]:
        print(f"  {step}")
