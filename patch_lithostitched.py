import os
import zipfile
import shutil

jar_path = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\mods\lithostitched-1.7.9-neoforge-21.1.jar"
temp_jar_path = jar_path + ".tmp"

new_mcmeta = b"""{
  "pack": {
    "description": "Lithostitched",
    "pack_format": 48,
    "supported_formats": [48, 99]
  }
}"""

with zipfile.ZipFile(jar_path, 'r') as zin:
    with zipfile.ZipFile(temp_jar_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == 'pack.mcmeta':
                continue
            if item.filename.startswith('META-INF/') and item.filename.endswith(('.SF', '.DSA', '.RSA')):
                continue
            
            # Read and copy other files
            buffer = zin.read(item.filename)
            zout.writestr(item, buffer)
        
        # Write the new clean pack.mcmeta
        zout.writestr('pack.mcmeta', new_mcmeta)

# Replace original with the patched one
shutil.move(temp_jar_path, jar_path)
print("Jar successfully patched.")
