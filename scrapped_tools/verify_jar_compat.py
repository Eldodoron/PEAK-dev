import urllib.request
import json
import zipfile
import io

HEADERS = {'User-Agent': 'Mozilla/5.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def check_file(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
        print(f"Downloaded {len(data)} bytes from {url}")
        zf = zipfile.ZipFile(io.BytesIO(data))
        for name in zf.namelist():
            if "neoforge.mods.toml" in name or "mods.toml" in name:
                print(f"--- {name} ---")
                print(zf.read(name).decode('utf-8', errors='ignore')[:500])

print("Checking BadOptimizations...")
check_file("https://edge.forgecdn.net/files/7338/300/BadOptimizations-2.4.1-1.21.1.jar")

print("\nChecking Noisiumed...")
check_file("https://edge.forgecdn.net/files/8475/257/noisiumed-3.0.6-neoforge-1.21.1.jar")

print("\nChecking Dynamic FPS 3.7.7...")
check_file("https://edge.forgecdn.net/files/5959/826/dynamic-fps-3.7.7%2bminecraft-1.21.0-neoforge.jar")
