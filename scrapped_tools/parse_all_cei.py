import urllib.request
import json
import zipfile
import io

HEADERS = {'User-Agent': 'PEAK/1.0'}
req = urllib.request.Request('https://api.modrinth.com/v2/project/create-enchantment-industry/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D', headers=HEADERS)
versions = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

for v in versions:
    vnum = v['version_number']
    url = v['files'][0]['url']
    req_jar = urllib.request.Request(url, headers=HEADERS)
    zf = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(req_jar).read()))
    for n in zf.namelist():
        if "mods.toml" in n:
            content = zf.read(n).decode('utf-8', errors='ignore')
            sable_range = ""
            apoth_range = ""
            for line in content.splitlines():
                if "versionRange" in line:
                    last_range = line.split("=")[-1].strip()
                if 'modId="sable"' in line:
                    pass
            # Let's parse sections
            in_sable = False
            in_apoth = False
            sr = None
            ar = None
            for line in content.splitlines():
                if 'modId="sable"' in line:
                    in_sable = True
                elif in_sable and 'versionRange' in line:
                    sr = line.strip()
                    in_sable = False
                elif 'modId="apotheosis"' in line:
                    in_apoth = True
                elif in_apoth and 'versionRange' in line:
                    ar = line.strip()
                    in_apoth = False
            print(f"CEI {vnum:10} -> Sable: {sr} | Apotheosis: {ar}")
