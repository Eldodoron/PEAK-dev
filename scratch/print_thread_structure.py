import json
import os

filepath = r"C:\Users\chris\.gemini\antigravity\brain\8d114a67-432d-452e-9cc0-80f865c0f7fe\.system_generated\steps\605\content.md"

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
