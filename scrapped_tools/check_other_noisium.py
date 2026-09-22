import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def get_cf_files(mod_id):
    url = f"https://api.curseforge.com/v1/mods/{mod_id}/files?gameVersion=1.21.1"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        return []

for mid in [948812, 951546]:
    files = get_cf_files(mid)
    print(f"Mod {mid}: {len(files)} files for 1.21.1")
    for f in files[:3]:
        print(f"  {f['displayName']} -> loaders: {f.get('gameVersions')}")
