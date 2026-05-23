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
