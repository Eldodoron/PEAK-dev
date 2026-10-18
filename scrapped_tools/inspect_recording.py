import imageio.v3 as iio
from PIL import Image
import numpy as np
import os

video_path = r"C:\Users\chris\Videos\2026-10-17 16-15-03.mp4"
out_dir = r"C:\Users\chris\.gemini\antigravity\brain\f882856b-3a9d-44cd-9b42-22558e3c6d69\scratch"
os.makedirs(out_dir, exist_ok=True)

# Using imageio_ffmpeg directly

# Sample timestamps to inspect (in seconds)
# 2m00s = 120s, 2m06s = 126s, 2m16s = 136s, 2m37s = 157s, 3m00s = 180s, 3m08s = 188s
timestamps = [120, 124, 126, 127, 128, 130, 134, 136, 140, 150, 156, 158, 160, 170, 180, 185, 188, 190]

fps = 60 # Default, will detect if possible
# Let's read frames using imageio-ffmpeg
import imageio_ffmpeg
gen = imageio_ffmpeg.read_frames(video_path)
header = next(gen)
print("Video header:", header)
fps = header.get("fps", 60)
size = header.get("size", (1920, 1080))
w, h = size

target_frames = {int(round(t * fps)): t for t in timestamps}
max_frame = max(target_frames.keys())

saved_count = 0
for idx, frame_bytes in enumerate(gen):
    if idx in target_frames:
        t = target_frames[idx]
        arr = np.frombuffer(frame_bytes, dtype=np.uint8).reshape((h, w, 3))
        # Crop the center tunnel area
        # Typically tunnel is vertically centered
        img = Image.fromarray(arr)
        # Save full frame (scaled down) and crop
        preview = img.resize((960, 540), resample=Image.BILINEAR)
        preview.save(os.path.join(out_dir, f"frame_{t:03d}s.png"))
        
        # Crop center 400x200 area around tunnel
        cx, cy = w // 2, h // 2
        crop_box = (cx - 240, cy - 100, cx + 240, cy + 100)
        crop_img = img.crop(crop_box)
        crop_img.save(os.path.join(out_dir, f"crop_{t:03d}s.png"))
        print(f"Saved frame at {t}s (frame {idx})")
        saved_count += 1
    if idx > max_frame:
        break

print(f"Done! Saved {saved_count} frames.")
