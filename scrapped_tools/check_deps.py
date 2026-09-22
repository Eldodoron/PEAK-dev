import zipfile
import io
import urllib.request

HEADERS = {'User-Agent': 'Mozilla/5.0'}

urls = [
    ("BadOptimizations", "https://edge.forgecdn.net/files/7338/300/BadOptimizations-2.4.1-1.21.1.jar"),
    ("Noisiumed", "https://edge.forgecdn.net/files/8475/257/noisiumed-3.0.6-neoforge-1.21.1.jar"),
    ("Dynamic FPS", "https://edge.forgecdn.net/files/5959/826/dynamic-fps-3.7.7%2bminecraft-1.21.0-neoforge.jar")
]

for name, url in urls:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
        zf = zipfile.ZipFile(io.BytesIO(data))
        for item in zf.namelist():
            if "neoforge.mods.toml" in item:
                print(f"=== {name} deps ===")
                content = zf.read(item).decode('utf-8', errors='ignore')
                for line in content.splitlines():
                    if "modId" in line or "versionRange" in line or "mandatory" in line:
                        print(line)
