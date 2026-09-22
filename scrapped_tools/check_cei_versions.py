import urllib.request
import json
import zipfile
import io

HEADERS = {'User-Agent': 'PEAK/1.0'}

req = urllib.request.Request("https://api.modrinth.com/v2/project/create-enchantment-industry/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D", headers=HEADERS)
versions = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

for v in versions:
    vnum = v['version_number']
    jar_file = None
    for f in v['files']:
        if f['filename'].endswith('.jar') and not 'sources' in f['filename']:
            jar_file = f
            break
    if not jar_file:
        continue
    print(f"\nChecking CEI {vnum}...")
    req_jar = urllib.request.Request(jar_file['url'], headers=HEADERS)
    with urllib.request.urlopen(req_jar) as resp:
        zf = zipfile.ZipFile(io.BytesIO(resp.read()))
        for n in zf.namelist():
            if "mods.toml" in n:
                content = zf.read(n).decode('utf-8', errors='ignore')
                for line in content.splitlines():
                    if any(k in line for k in ["sable", "apotheosis", "apothic_enchanting"]):
                        print(" ", line)
