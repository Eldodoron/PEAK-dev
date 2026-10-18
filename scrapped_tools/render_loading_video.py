import os
import zipfile
from io import BytesIO
from PIL import Image, ImageDraw
import numpy as np
import imageio.v2 as imageio

ASSETS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\config\fancymenu\assets\loading_tunnel"
BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\f882856b-3a9d-44cd-9b42-22558e3c6d69"

fma_path = os.path.join(ASSETS_DIR, "tunnel_scene.fma")
bg_path = os.path.join(ASSETS_DIR, "tunnel_bg.png")

output_mp4 = os.path.join(BRAIN_DIR, "loading_screen_animation.mp4")

print("Loading assets...")
tunnel_bg = Image.open(bg_path).convert("RGBA")
bg_w, bg_h = tunnel_bg.size  # 960x640

# In 16:9 HD framing (960x540):
# Center is (480, 320)
# tunnel_bg is 960x640, so crop 50px top and bottom to make it crisp 960x540 (16:9)
crop_y_top = 50
crop_y_bottom = 590

scene_x = 480 - 128  # 352
scene_y = 336 - 16   # 320

bar_x = 480 - 82     # 398
bar_y = 336 + 67     # 403
bar_w = 164
bar_h = 10

with zipfile.ZipFile(fma_path, "r") as zf:
    intro_frames = []
    for i in range(190):
        img = Image.open(BytesIO(zf.read(f"intro_frames/{i}.png"))).convert("RGBA")
        intro_frames.append(img)
    
    loop_frames = []
    for i in range(8):
        img = Image.open(BytesIO(zf.read(f"frames/{i}.png"))).convert("RGBA")
        loop_frames.append(img)

print(f"Loaded {len(intro_frames)} intro frames and {len(loop_frames)} loop frames.")

# Total frames: 190 intro + 4 loops of 8 frames (32 frames) = 222 frames (~11.1s at 20 fps)
total_frames = len(intro_frames) + len(loop_frames) * 4

fps = 20
writer = imageio.get_writer(output_mp4, fps=fps, codec='libx264', quality=8, pixelformat='yuv420p')

print("Rendering video frames...")
for f_idx in range(total_frames):
    canvas = tunnel_bg.copy()
    
    # Pick scene frame
    if f_idx < len(intro_frames):
        scene = intro_frames[f_idx]
        progress = f_idx / 189.0
    else:
        loop_idx = (f_idx - len(intro_frames)) % len(loop_frames)
        scene = loop_frames[loop_idx]
        progress = 1.0
        
    canvas.alpha_composite(scene, (scene_x, scene_y))
    
    # Draw native Mojang Loading Bar
    draw = ImageDraw.Draw(canvas)
    # White 1px outer border
    draw.rectangle([bar_x, bar_y, bar_x + bar_w - 1, bar_y + bar_h - 1], outline=(255, 255, 255, 240), width=1)
    
    # Progress fill
    fill_inner_max = bar_w - 4
    current_fill = int(round(fill_inner_max * progress))
    if current_fill > 0:
        draw.rectangle([bar_x + 2, bar_y + 2, bar_x + 2 + current_fill - 1, bar_y + bar_h - 3], fill=(255, 255, 255, 245))
        
    # Crop to standard 16:9 (960x540)
    frame_16_9 = canvas.crop((0, crop_y_top, bg_w, crop_y_bottom))
    
    # Convert RGBA -> RGB for MP4
    frame_rgb = frame_16_9.convert("RGB")
    writer.append_data(np.array(frame_rgb))

writer.close()
print(f"Video saved successfully to: {output_mp4}")
