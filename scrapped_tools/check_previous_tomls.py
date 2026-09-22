import urllib.request
import json
import zipfile
import io

HEADERS = {'User-Agent': 'PEAK/1.0'}

def check_version_toml(slug, ver_str):
    url = f"https://api.modrinth.com/v2/project/{slug}/version"
    req = urllib.request.Request(url, headers=HEADERS)
    data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    for v in data:
        if ver_str in v['version_number']:
            furl = v['files'][0]['url']
            print(f"Downloading {slug} {v['version_number']}...")
            req_f = urllib.request.Request(furl, headers=HEADERS)
            zf = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(req_f).read()))
            for n in zf.namelist():
                if "mods.toml" in n:
                    print(f"=== {v['version_number']} toml ===")
                    for line in zf.read(n).decode('utf-8', errors='ignore').splitlines():
                        if any(k in line for k in ["sable", "apotheosis", "apothic", "supplementaries"]):
                            print(" ", line)
            return

print("Checking CEI 2.5.0-preview-alpha1:")
check_version_toml("create-enchantment-industry", "preview-alpha1")

print("\nChecking Integrated Farming 1.2.6:")
check_version_toml("create-integrated-farming", "1.2.6")
