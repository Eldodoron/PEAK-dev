import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK-Modpack/1.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def search_cf(name):
    url = f"https://api.curseforge.com/v1/mods/search?gameId=432&searchFilter={urllib.parse.quote(name)}&classId=6"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8')).get('data', [])
    except Exception as e:
        print(f"CF error: {e}")
        return []

def get_cf_files(mod_id):
    url = f"https://api.curseforge.com/v1/mods/{mod_id}/files?gameVersion=1.21.1&modLoaderType=6"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8')).get('data', [])
    except Exception as e:
        print(f"CF files error: {e}")
        return []

def search_modrinth(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        return []

print("=== Modrinth: the-beyond ===")
mr = search_modrinth("the-beyond")
for v in mr[:5]:
    print(f"Modrinth: {v['name']} ({v['version_number']})")
    for f in v['files']:
        print(f"  File: {f['filename']}")

print("\n=== CurseForge: The Beyond ===")
cf = search_cf("The Beyond")
for m in cf[:3]:
    print(f"CF Mod: {m['name']} (ID: {m['id']}, slug: {m['slug']})")
    files = get_cf_files(m['id'])
    for f in files[:5]:
        print(f"  File: {f['displayName']} ({f['fileName']}) Date: {f['fileDate']}")
