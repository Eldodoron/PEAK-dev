import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK/1.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def check_cf_slug(slug):
    url = f"https://api.curseforge.com/v1/mods/search?gameId=432&slug={slug}"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception:
        return []

def get_cf_files(mod_id):
    url = f"https://api.curseforge.com/v1/mods/{mod_id}/files?gameVersion=1.21.1&modLoaderType=6"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception:
        return []

m = check_cf_slug("create-dreams-desires")
if not m:
    m = check_cf_slug("create-dreams-n-desires")
for mod in m:
    print(f"CF Mod: {mod['name']} ID: {mod['id']}")
    for f in get_cf_files(mod['id'])[:3]:
        print(f"  {f['displayName']} -> {f['fileName']}")
