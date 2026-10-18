import imageio_ffmpeg
import numpy as np
from PIL import Image
import os

video_path = r"C:\Users\chris\Videos\2026-10-17 16-15-03.mp4"
out_dir = r"C:\Users\chris\.gemini\antigravity\brain\f882856b-3a9d-44cd-9b42-22558e3c6d69\scratch\video_audit"
os.makedirs(out_dir, exist_ok=True)

gen = imageio_ffmpeg.read_frames(video_path)
header = next(gen)
fps = header.get("fps", 60)
w, h = header.get("size", (1920, 1080))
print(f"FPS: {fps}, Size: {w}x{h}")

# We want to check key moments:
# 0s, 30s, 60s, 90s, 115s, 120s, 124s, 125s, 126s (2m06s), 127s, 128s, 129s, 130s, 132s, 134s, 136s, 140s, 150s, 160s, 170s, 180s, 185s, 188s, 190s
sample_times = [0, 30, 60, 90, 115, 120, 124, 125, 126, 127, 128, 129, 130, 132, 134, 136, 140, 150, 160, 170, 180, 185, 188, 190]
target_frames = {int(round(t * fps)): t for t in sample_times}
max_frame = max(target_frames.keys())

for idx, frame_bytes in enumerate(gen):
    if idx in target_frames:
        t = target_frames[idx]
        arr = np.frombuffer(frame_bytes, dtype=np.uint8).reshape((h, w, 3))
        img = Image.fromarray(arr)
        # Crop center 600x300
        cx, cy = w // 2, h // 2
        crop = img.crop((cx - 300, cy - 120, cx + 300, cy + 120))
        crop.save(os.path.join(out_dir, f"audit_{t:03d}s.png"))
        print(f"Saved audit frame at {t}s (frame {idx})")
    if idx > max_frame:
        break

print("Audit complete.")
