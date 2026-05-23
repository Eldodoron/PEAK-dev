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
print("timeWindows:", data.get("timeWindows"))
server_thread = data["threads"][0]
children = server_thread["children"]
print("Total children:", len(children))
last_idx = len(children) - 1
print(f"Child {last_idx} (last child):", children[last_idx])
print(f"childrenRefs of Server thread:", server_thread["childrenRefs"])
