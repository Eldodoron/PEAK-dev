import gzip
import json
import os

panoptic_json = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\panoptic\inspections.json"
output_txt = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\scrapped_tools\villager_trades_dump.txt"
output_continue = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.continue\villager_trades_dump.txt"

with gzip.open(panoptic_json, "rt", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Try parsing json
try:
    data = json.loads(content)
    print(f"Parsed JSON successfully! Type: {type(data)}")
    if isinstance(data, dict):
        print("Keys:", list(data.keys()))
except Exception as e:
    print(f"Not raw JSON after gzip: {e}")
    data = content

# Write formatted txt to scrapped_tools and .continue
with open(output_txt, "w", encoding="utf-8") as out:
    if isinstance(data, (dict, list)):
        json.dump(data, out, indent=2)
    else:
        out.write(data)

with open(output_continue, "w", encoding="utf-8") as out:
    if isinstance(data, (dict, list)):
        json.dump(data, out, indent=2)
    else:
        out.write(data)

print(f"Successfully saved {len(content)} characters of trade/inspection data to {output_txt} and {output_continue}")
