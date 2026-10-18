import glob
import os
from PIL import Image

out_dir = r"C:\Users\chris\.gemini\antigravity\brain\f882856b-3a9d-44cd-9b42-22558e3c6d69\scratch\video_audit"
for t in [120, 125, 126, 127, 128, 129, 130, 132, 134, 136, 140, 188]:
    p = os.path.join(out_dir, f"audit_{t:03d}s.png")
    if os.path.exists(p):
        print(f"Frame {t}s exists: size {Image.open(p).size}")
