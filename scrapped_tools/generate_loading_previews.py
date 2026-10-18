import os
import zipfile
from io import BytesIO
from PIL import Image, ImageDraw

ASSETS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\config\fancymenu\assets\loading_tunnel"
BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\f882856b-3a9d-44cd-9b42-22558e3c6d69"

fma_path = os.path.join(ASSETS_DIR, "tunnel_scene.fma")
bg_path = os.path.join(ASSETS_DIR, "tunnel_bg.png")

with zipfile.ZipFile(fma_path, "r") as zf:
    # Read frame 0 (start), frame 95 (halfway), frame 180 (final break), and loop frame 0 (idle at cavern)
    frame_0 = Image.open(BytesIO(zf.read("intro_frames/0.png"))).convert("RGBA")
    frame_95 = Image.open(BytesIO(zf.read("intro_frames/95.png"))).convert("RGBA")
    frame_180 = Image.open(BytesIO(zf.read("intro_frames/180.png"))).convert("RGBA")
    frame_idle = Image.open(BytesIO(zf.read("frames/0.png"))).convert("RGBA")

tunnel_bg = Image.open(bg_path).convert("RGBA")

# Coordinates of scene on tunnel_bg:
# tunnel_bg is 960x640. Center is (480, 336).
# SCENE_MC_X = -128, SCENE_MC_Y = -16, SCENE_W = 224, SCENE_H = 96
# In native pixels:
# Center of tunnel_bg in GUI coords: cx = 480, cy = 336
# scene top-left = (480 - 128, 336 - 16) = (352, 320)
# bar pos = (480 - 82, 336 + 67) = (398, 403), w = 164, h = 10

def compose_preview(scene_frame, bar_progress=0.0):
    canvas = tunnel_bg.copy()
    canvas.alpha_composite(scene_frame, (352, 320))

    # Simulate native Mojang bar drawn by VanillaBarElement:
    bx, by, bw, bh = 398, 403, 164, 10
    draw = ImageDraw.Draw(canvas)
    # White 1px outline
    draw.rectangle([bx, by, bx + bw - 1, by + bh - 1], outline=(255, 255, 255, 240), width=1)
    # White fill
    fill_w = max(2, min(bw - 4, int(round((bw - 4) * bar_progress))))
    if bar_progress > 0:
        draw.rectangle([bx + 2, by + 2, bx + 2 + fill_w - 1, by + bh - 3], fill=(255, 255, 255, 245))

    # Crop a clean 480x280 window centered on the tunnel and bar
    crop_box = (480 - 200, 336 - 90, 480 + 200, 336 + 90)
    cropped = canvas.crop(crop_box)
    return cropped

# 1. Preview 1: Early Window / Frame 0 (0% progress)
p1 = compose_preview(frame_0, 0.05)
p1.save(os.path.join(BRAIN_DIR, "preview_stage_01_entrance.png"))

# 2. Preview 2: Active Mining (Col 2, 45% progress)
p2 = compose_preview(frame_95, 0.45)
p2.save(os.path.join(BRAIN_DIR, "preview_stage_02_mining.png"))

# 3. Preview 3: Final Wall Breakthrough (90% progress)
p3 = compose_preview(frame_180, 0.88)
p3.save(os.path.join(BRAIN_DIR, "preview_stage_03_breakthrough.png"))

# 4. Preview 4: Cavern Threshold Idle (100% / Shader Freeze Hold)
p4 = compose_preview(frame_idle, 0.98)
p4.save(os.path.join(BRAIN_DIR, "preview_stage_04_cavern_hold.png"))

print("Generated 4 stage previews in BRAIN_DIR!")
