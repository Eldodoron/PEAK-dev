import urllib.request
import zipfile
import io

HEADERS = {'User-Agent': 'Mozilla/5.0'}

urls = [
    ("SB 3.26.3", "https://edge.forgecdn.net/files/8845/926/sophisticatedbackpacks-1.21.1-3.26.3.2158.jar"),
    ("SC 1.5.1", "https://edge.forgecdn.net/files/8838/842/sophisticatedcore-1.21.1-1.5.1.2341.jar")
]

for name, url in urls:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    zf = zipfile.ZipFile(io.BytesIO(data))
    print(f"=== {name} ({len(data)} bytes) ===")
    for n in zf.namelist():
        if "StackUpgradeItem" in n or "MaxUgradesPerStorageConfig" in n:
            print(" ", n)
