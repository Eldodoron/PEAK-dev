import urllib.request
import json

headers = {'User-Agent': 'PEAK-Modpack-Agent/1.0'}

def query_modrinth(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data:
                print(f"=== Found {slug} on Modrinth ===")
                latest = data[0]
                print(f"Version: {latest['version_number']}, Name: {latest['name']}")
                for f in latest['files']:
                    print(f"  File: {f['filename']} -> {f['url']}")
                return latest['files'][0]
    except Exception as e:
        print(f"Error querying {slug}: {e}")
    return None

print("Checking BadOptimizations...")
query_modrinth("badoptimizations")

print("\nChecking Noisium...")
query_modrinth("noisium")

print("\nChecking Noisiumed...")
query_modrinth("noisiumed")

print("\nChecking NoisiumForked...")
query_modrinth("noisiumforked")
