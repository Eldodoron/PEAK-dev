import json
import os
import sys

script_dir = os.path.dirname(__file__)
default_path = os.path.join(script_dir, "content.md")
filepath = sys.argv[1] if len(sys.argv) > 1 else default_path

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Skip metadata headers
json_str = ""
for line in lines:
    if line.strip().startswith("{"):
        json_str = line.strip()
        break

if not json_str:
    print("No JSON line found!")
else:
    try:
        data = json.loads(json_str)
        print("Keys:", list(data.keys()))
        if "metadata" in data:
            print("Metadata Keys:", list(data["metadata"].keys()))
        if "threads" in data:
            print("Has threads field!")
            print("Number of threads sampled:", len(data["threads"]))
            # Print info about threads
            for tid, tdata in data["threads"].items():
                print(f"Thread ID {tid}: Name: {tdata.get('name')}, Samples count: {len(tdata.get('samples', []))}")
        else:
            print("Does NOT have threads field.")
    except Exception as e:
        print("Error parsing JSON:", e)
