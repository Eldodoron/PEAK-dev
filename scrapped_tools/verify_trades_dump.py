# Script to verify villager trades dump files
import os

files = [
    r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\scrapped_tools\villager_trades_dump.txt",
    r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.continue\villager_trades_dump.txt"
]

for f in files:
    if os.path.exists(f):
        print(f"File {f} exists, size: {os.path.getsize(f) / (1024*1024):.2f} MB")
