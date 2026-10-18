import os
import zipfile
from io import BytesIO
from PIL import Image, ImageDraw
import numpy as np
import imageio.v2 as imageio

ASSETS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\config\fancymenu\assets\loading_tunnel"
BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\f882856b-3a9d-44cd-9b42-22558e3c6d69"
MULTIMEDIA_DIR = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA"

fma_path = os.path.join(ASSETS_DIR, "tunnel_scene.fma")
bg_path = os.path.join(ASSETS_DIR, "tunnel_bg.png")

print("Reading assets...")
tunnel_bg = Image.open(bg_path).convert("RGBA")
# tunnel_bg is 960x640

with zipfile.ZipFile(fma_path, "r") as zf:
    intro_frames = [Image.open(BytesIO(zf.read(f"intro_frames/{i}.png"))).convert("RGBA") for i in range(190)]
    loop_frames = [Image.open(BytesIO(zf.read(f"frames/{i}.png"))).convert("RGBA") for i in range(8)]

# Total frames: 190 intro + 32 loop (4 cycles) = 222 frames (~11.1s @ 20fps)
total_frames = len(intro_frames) + len(loop_frames) * 4
fps = 20

# =========================================================================
# 1. Full-Screen In-Game 16:9 Master (1920x1080 @ 60fps / 20fps master)
# In Minecraft GUI coordinates (960x540 base @ 16:9):
# Center is (480, 270)
# Scene anchor: mid-centered -> x = -128, y = -16 -> top-left = (480-128, 270-16) = (352, 254)
# Bar anchor: mid-centered -> x = -82, y = 67 -> top-left = (480-82, 270+67) = (398, 337)
# Bar size: 164x10
# =========================================================================

# We will create native 960x540 canvases, then upscale 2x nearest-neighbor to 1920x1080 for pristine 1080p quality!
mp4_1080p_path = os.path.join(MULTIMEDIA_DIR, "Loading_Screen_16x9_1080p.mp4")
mp4_brain_path = os.path.join(BRAIN_DIR, "Loading_Screen_16x9_1080p.mp4")

# Also Focused 16:9 (Cinematic close-up on mining action):
# Focus box centered on scene and bar:
# Scene is 224x96 at (352, 254), Bar is 164x10 at (398, 337).
# Total action bounding box: x: 330..580, y: 240..360.
# A 16:9 crop of 320x180 centered at (464, 298) scaled 4x gives 1280x720!
mp4_focused_path = os.path.join(MULTIMEDIA_DIR, "Loading_Screen_Focused_16x9_720p.mp4")
gif_focused_path = os.path.join(MULTIMEDIA_DIR, "Loading_Screen_Focused_16x9.gif")
gif_brain_path = os.path.join(BRAIN_DIR, "Loading_Screen_Focused_16x9.gif")
gif_cf_path = os.path.join(MULTIMEDIA_DIR, "Loading_Screen_16x9_CurseForge.gif")

# Setup writers
writer_1080p = imageio.get_writer(mp4_1080p_path, fps=fps, codec='libx264', quality=9, pixelformat='yuv420p', macro_block_size=1)
writer_focused = imageio.get_writer(mp4_focused_path, fps=fps, codec='libx264', quality=9, pixelformat='yuv420p', macro_block_size=1)

focused_gif_frames = []
cf_gif_frames = []

# Base background: crop 960x640 to 960x540 (crop 50px top and 50px bottom so center is preserved at 270)
bg_16_9 = tunnel_bg.crop((0, 50, 960, 590))  # 960x540

print("Generating 16:9 frames...")
for f_idx in range(total_frames):
    canvas = bg_16_9.copy()
    
    if f_idx < len(intro_frames):
        scene = intro_frames[f_idx]
        progress = f_idx / 189.0
    else:
        loop_idx = (f_idx - len(intro_frames)) % len(loop_frames)
        scene = loop_frames[loop_idx]
        progress = 1.0
        
    # Composite scene at (352, 254)
    canvas.alpha_composite(scene, (352, 254))
    
    # Draw native Mojang Loading Bar at (398, 337), w=164, h=10
    draw = ImageDraw.Draw(canvas)
    bx, by, bw, bh = 398, 337, 164, 10
    # 1px border
    draw.rectangle([bx, by, bx + bw - 1, by + bh - 1], outline=(255, 255, 255, 240), width=1)
    # Inner progress fill
    fill_w = int(round((bw - 4) * progress))
    if fill_w > 0:
        draw.rectangle([bx + 2, by + 2, bx + 2 + fill_w - 1, by + bh - 3], fill=(255, 255, 255, 245))
        
    # 1. Full 1080p Frame (upscaled 2x nearest-neighbor)
    frame_1080p = canvas.resize((1920, 1080), Image.Resampling.NEAREST).convert("RGB")
    writer_1080p.append_data(np.array(frame_1080p))
    
    # 2. Focused 16:9 Frame:
    # 320x180 crop centered around tunnel and bar:
    # x from (480 - 160) = 320 to (480 + 160) = 640
    # y from (298 - 90) = 208 to (298 + 90) = 388
    focused_crop = canvas.crop((320, 208, 640, 388))
    # 720p focused (1280x720) 4x nearest
    focused_720p = focused_crop.resize((1280, 720), Image.Resampling.NEAREST).convert("RGB")
    writer_focused.append_data(np.array(focused_720p))
    
    # Sample every 2nd frame for lightweight GIF previews
    if f_idx % 2 == 0:
        # 480x270 focused gif
        f_gif_im = focused_crop.resize((480, 270), Image.Resampling.NEAREST)
        focused_gif_frames.append(f_gif_im)
        
        # 480x270 full screen gif
        cf_im = canvas.resize((480, 270), Image.Resampling.BILINEAR)
        cf_gif_frames.append(cf_im)

writer_1080p.close()
writer_focused.close()

# Copy 1080p mp4 to brain dir as well
import shutil
shutil.copy2(mp4_1080p_path, mp4_brain_path)

print("Saving GIFs...")
# Save focused GIF
focused_gif_frames[0].save(
    gif_focused_path,
    save_all=True,
    append_images=focused_gif_frames[1:],
    duration=100,
    loop=0,
    optimize=True
)
shutil.copy2(gif_focused_path, gif_brain_path)

# Save full 16:9 CurseForge GIF
cf_gif_frames[0].save(
    gif_cf_path,
    save_all=True,
    append_images=cf_gif_frames[1:],
    duration=100,
    loop=0,
    optimize=True
)

print(f"All 16:9 assets rendered and saved successfully to:\n{MULTIMEDIA_DIR}")
