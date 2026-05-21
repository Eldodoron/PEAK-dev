import json
import os

filepath = r"C:\Users\chris\.gemini\antigravity\brain\8d114a67-432d-452e-9cc0-80f865c0f7fe\.system_generated\steps\605\content.md"

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
