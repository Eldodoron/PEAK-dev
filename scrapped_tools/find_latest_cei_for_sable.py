import urllib.request
import json
import zipfile
import io

HEADERS = {'User-Agent': 'PEAK/1.0'}
url = "https://api.modrinth.com/v2/project/create-enchantment-industry/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
req = urllib.request.Request(url, headers=HEADERS)
versions = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

print(f"Total CEI 1.21.1 versions: {len(versions)}", flush=True)

for v in versions[:6]:
    vnum = v['version_number']
    jar_file = None
    for f in v['files']:
        if f['filename'].endswith('.jar') and 'sources' not in f['filename']:
            jar_file = f
            break
    if not jar_file:
        continue
    
    furl = jar_file['url']
    req_f = urllib.request.Request(furl, headers=HEADERS)
    try:
        print(f"Checking {vnum}...", flush=True)
        with urllib.request.urlopen(req_f) as resp:
            data = resp.read()
        zf = zipfile.ZipFile(io.BytesIO(data))
        for name in zf.namelist():
            if "mods.toml" in name:
                content = zf.read(name).decode('utf-8', errors='ignore')
                sable_range = None
                apoth_range = None
                in_sable = False
                in_apoth = False
                for line in content.splitlines():
                    if 'modId="sable"' in line:
                        in_sable = True
                    elif in_sable and 'versionRange' in line:
                        sable_range = line.split("=")[-1].strip().strip('"')
                        in_sable = False
                    elif 'modId="apotheosis"' in line:
                        in_apoth = True
                    elif in_apoth and 'versionRange' in line:
                        apoth_range = line.split("=")[-1].strip().strip('"')
                        in_apoth = False
                print(f"Version: {vnum:22} | Sable: {sable_range} | Apotheosis: {apoth_range}", flush=True)
    except Exception as e:
        print(f"Error {vnum}: {e}", flush=True)
