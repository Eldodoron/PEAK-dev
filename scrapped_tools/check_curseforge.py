import urllib.request
import json
import os
import zipfile

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# CurseForge API key (public Eternal key commonly used in tools if accessible)
# Or we can query CurseForge API / Modrinth API
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm" # standard CF proxy key

def search_curseforge(query):
    url = f"https://api.curseforge.com/v1/mods/search?gameId=432&searchFilter={urllib.parse.quote(query)}&classId=6"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print(f"CurseForge search error for {query}: {e}")
        return []

def get_cf_files(mod_id):
    url = f"https://api.curseforge.com/v1/mods/{mod_id}/files?gameVersion=1.21.1&modLoaderType=6" # 6 is NeoForge
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print(f"CurseForge files error for mod {mod_id}: {e}")
        return []

def query_modrinth(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data:
                return data[0]
    except Exception as e:
        print(f"Modrinth error for {slug}: {e}")
    return None

print("Checking CurseForge for BadOptimizations...")
cf_mods = search_curseforge("BadOptimizations")
for m in cf_mods[:3]:
    print(f"CF Mod: {m['name']} (ID: {m['id']}, slug: {m['slug']})")
    files = get_cf_files(m['id'])
    for f in files[:2]:
        print(f"  CF File: {f['displayName']} -> downloadUrl: {f.get('downloadUrl')}")

print("\nChecking CurseForge for Noisium...")
cf_mods_noise = search_curseforge("Noisium")
for m in cf_mods_noise[:3]:
    print(f"CF Mod: {m['name']} (ID: {m['id']}, slug: {m['slug']})")
    files = get_cf_files(m['id'])
    for f in files[:2]:
        print(f"  CF File: {f['displayName']} -> downloadUrl: {f.get('downloadUrl')}")

print("\nChecking CurseForge for Dynamic FPS...")
cf_mods_fps = search_curseforge("Dynamic FPS")
for m in cf_mods_fps[:3]:
    print(f"CF Mod: {m['name']} (ID: {m['id']}, slug: {m['slug']})")
    files = get_cf_files(m['id'])
    for f in files[:2]:
        print(f"  CF File: {f['displayName']} -> downloadUrl: {f.get('downloadUrl')}")
