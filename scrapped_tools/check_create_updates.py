import os
import urllib.request
import json
import re

HEADERS = {'User-Agent': 'PEAK-Modpack/1.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def search_cf_files(slug_or_id):
    url = f"https://api.curseforge.com/v1/mods/{slug_or_id}/files?gameVersion=1.21.1&modLoaderType=6"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception:
        return []

def search_modrinth_version(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception:
        return []

# List of prominent Create addons to check
addons = [
    ("create", "create", "6.0.10"),
    ("create_central_kitchen", "create-central-kitchen", "2.5.0"),
    ("create_confectionery", "create-confectionery", "1.1.0"),
    ("create_enchantment_industry", "create-enchantment-industry", "2.5.0-preview-alpha1"),
    ("create_new_age", "create-new-age", "1.2.0"),
    ("createdieselgenerators", "create-diesel-generators", "1.3.15"),
    ("tfmg", "create-tfmg", "1.2.0"),
    ("dndesires", "create-dreams-n-desires", "2.3a-BETA"),
    ("create_sa", "create-stuff-additions", "2.0.9"),
    ("createmetalwork", "create-metalwork", "2.0.0"),
    ("createappliedkinetics", "create-applied-kinetics", "1.5.4"),
    ("aeroworks", "create-aeroworks", "1.3.0"),
    ("create_power_loader", "create-power-loader", "2.0.5"),
    ("create_dragons_plus", "create-dragons-plus", "1.11.3"),
    ("create_deep_dark", "create-deep-dark", "1.7.0"),
    ("create_ultimate_factory", "create-ultimate-factory", "1.9.0"),
    ("create_integrated_farming", "create-integrated-farming", "1.2.6")
]

for modid, mr_slug, cur_ver in addons:
    mr_res = search_modrinth_version(mr_slug)
    if mr_res:
        latest = mr_res[0]
        latest_ver = latest['version_number']
        print(f"[{modid}] Current: {cur_ver} | Latest MR: {latest_ver} ({latest['name']})")
    else:
        print(f"[{modid}] Current: {cur_ver} | No MR versions")
