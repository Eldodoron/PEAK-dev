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
server_thread = data["threads"][0]

print("Server thread keys:", list(server_thread.keys()))
print("Type of children:", type(server_thread["children"]))
print("Length of children:", len(server_thread["children"]))

# Let's inspect the first 10 elements in children
for i in range(min(10, len(server_thread["children"]))):
    print(f"Child {i}: type={type(server_thread['children'][i])}, value={str(server_thread['children'][i])[:200]}")

# Let's inspect childrenRefs
if "childrenRefs" in server_thread:
    print("childrenRefs type:", type(server_thread["childrenRefs"]))
    print("childrenRefs length:", len(server_thread["childrenRefs"]))
    print("childrenRefs first few:", str(server_thread["childrenRefs"])[:500])
