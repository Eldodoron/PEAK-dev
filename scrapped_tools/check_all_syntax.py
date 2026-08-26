import os
import subprocess

scripts_dir = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs\server_scripts"

for root, dirs, files in os.walk(scripts_dir):
    for f in files:
        if f.endswith(".js"):
            path = os.path.join(root, f)
            res = subprocess.run(["node", "-c", path], capture_output=True, text=True)
            if res.returncode != 0:
                print(f"SYNTAX ERROR in {f}:\n{res.stderr}")
            else:
                pass
print("Server scripts syntax check completed!")
