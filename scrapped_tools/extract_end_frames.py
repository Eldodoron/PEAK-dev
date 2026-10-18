import imageio_ffmpeg
import numpy as np
from PIL import Image
import os

video_path = r"C:\Users\chris\Videos\2026-10-17 16-15-03.mp4"
out_dir = r"C:\Users\chris\.gemini\antigravity\brain\f882856b-3a9d-44cd-9b42-22558e3c6d69\scratch\video_audit\end_frames"
os.makedirs(out_dir, exist_ok=True)

gen = imageio_ffmpeg.read_frames(video_path)
header = next(gen)
fps = header.get("fps", 30)
w, h = header.get("size", (1024, 576))

times = [187.0, 188.0, 188.5, 189.0, 189.5, 190.0, 190.5, 191.0, 191.5, 192.0]
target_frames = {int(round(t * fps)): t for t in times}
max_frame = max(target_frames.keys())

for idx, frame_bytes in enumerate(gen):
    if idx in target_frames:
        t = target_frames[idx]
        arr = np.frombuffer(frame_bytes, dtype=np.uint8).reshape((h, w, 3))
        img = Image.fromarray(arr)
        cx, cy = w // 2, h // 2
        crop = img.crop((cx - 300, cy - 120, cx + 300, cy + 120))
        crop.save(os.path.join(out_dir, f"end_{t:05.1f}s.png"))
        print(f"Saved end frame at {t}s (frame {idx})")
    if idx > max_frame:
        break

print("Done end frames.")
