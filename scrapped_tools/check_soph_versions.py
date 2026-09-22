import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def get_mod_files(mod_id):
    url = f"https://api.curseforge.com/v1/mods/{mod_id}/files?gameVersion=1.21.1&modLoaderType=6"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print(f"Error: {e}")
        return []

print("=== Sophisticated Backpacks (CF: 422301) ===")
sb_files = get_mod_files(422301)
for f in sb_files[:8]:
    print(f"File: {f['displayName']} ({f['fileName']}) ID: {f['id']} Date: {f['fileDate']}")

print("\n=== Sophisticated Core (CF: 618298) ===")
sc_files = get_mod_files(618298)
for f in sc_files[:8]:
    print(f"File: {f['displayName']} ({f['fileName']}) ID: {f['id']} Date: {f['fileDate']}")
