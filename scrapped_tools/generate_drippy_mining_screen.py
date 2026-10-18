import os
import glob
import json
import math
import re
import time
import uuid
import zipfile
from io import BytesIO
import numpy as np
from PIL import Image, ImageDraw

INSTANCE_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft"
PRISM_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher"
ASSETS_DIR = os.path.join(INSTANCE_DIR, "config", "fancymenu", "assets", "loading_tunnel")
LAYOUT_DIR = os.path.join(INSTANCE_DIR, "config", "fancymenu", "customization")
DRIPPY_OPTS_PATH = os.path.join(INSTANCE_DIR, "config", "drippyloadingscreen", "options.txt")
FM_OPTS_PATH = os.path.join(INSTANCE_DIR, "config", "fancymenu", "options.txt")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(LAYOUT_DIR, exist_ok=True)

whim_zips = glob.glob(os.path.join(INSTANCE_DIR, "config", "paxi", "resourcepacks", "Whimscape_1*.zip"))
if not whim_zips:
    raise FileNotFoundError("Could not find Whimscape resourcepack zip")

with zipfile.ZipFile(whim_zips[0], "r") as zf:
    names = zf.namelist()
    def load_tex(subpath):
        target = f"assets/minecraft/textures/{subpath}"
        if target in names:
            return Image.open(BytesIO(zf.read(target))).convert("RGBA")
        matches = [n for n in names if n.endswith(subpath)]
        if matches:
            return Image.open(BytesIO(zf.read(matches[0]))).convert("RGBA")
        return None

    stone_16 = load_tex("block/stone.png")
    destroy_stages = [load_tex(f"block/destroy_stage_{i}.png") for i in range(10)]
    iron_pick_16 = load_tex("item/iron_pickaxe.png")

steve_skin = None
mc_jars = glob.glob(os.path.join(PRISM_DIR, "libraries", "**", "*client*.jar"), recursive=True) + \
          glob.glob(os.path.join(PRISM_DIR, "libraries", "net", "minecraft", "**", "*.jar"), recursive=True)
for jar in mc_jars:
    try:
        with zipfile.ZipFile(jar, "r") as zf:
            for cand in [
                "assets/minecraft/textures/entity/player/wide/steve.png",
                "assets/minecraft/textures/entity/steve.png"
            ]:
                if cand in zf.namelist():
                    steve_skin = Image.open(BytesIO(zf.read(cand))).convert("RGBA")
                    break
        if steve_skin:
            break
    except Exception:
        pass

if steve_skin is None:
    raise RuntimeError("Could not load vanilla Steve skin")


def tint_image(img, factor):
    r, g, b, a = img.split()
    r = r.point(lambda p: max(0, min(255, int(p * factor))))
    g = g.point(lambda p: max(0, min(255, int(p * factor))))
    b = b.point(lambda p: max(0, min(255, int(p * factor))))
    return Image.merge("RGBA", (r, g, b, a))


def rot_x(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]], dtype=np.float32)

def rot_y(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]], dtype=np.float32)

def rot_z(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], dtype=np.float32)


class Software3DRenderer:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.color_buf = np.zeros((height, width, 4), dtype=np.uint8)
        self.depth_buf = np.full((height, width), -1e9, dtype=np.float32)

    def draw_textured_quad(self, p0, p1, p2, p3, tex_patch, shade=1.0):
        v1 = p1 - p0
        v2 = p3 - p0
        cross_z = v1[0] * v2[1] - v1[1] * v2[0]
        if cross_z <= 0:
            return

        tw, th = tex_patch.size
        tex_np = np.array(tex_patch, dtype=np.float32)

        len_u = max(np.linalg.norm(p1[:2] - p0[:2]), np.linalg.norm(p2[:2] - p3[:2]))
        len_v = max(np.linalg.norm(p3[:2] - p0[:2]), np.linalg.norm(p2[:2] - p1[:2]))
        steps_u = max(int(math.ceil(len_u * 2.0)), tw * 2, 6)
        steps_v = max(int(math.ceil(len_v * 2.0)), th * 2, 6)

        u = np.linspace(0.0, 0.9999, steps_u, dtype=np.float32)[:, None, None]
        v = np.linspace(0.0, 0.9999, steps_v, dtype=np.float32)[None, :, None]

        pts = (1 - u) * (1 - v) * p0[None, None, :] + \
              u * (1 - v) * p1[None, None, :] + \
              u * v * p2[None, None, :] + \
              (1 - u) * v * p3[None, None, :]

        xs = np.round(pts[:, :, 0]).astype(np.int32)
        ys = np.round(pts[:, :, 1]).astype(np.int32)
        zs = pts[:, :, 2]

        tx = (u[:, :, 0] * tw).astype(np.int32)
        ty = (v[:, :, 0] * th).astype(np.int32)
        colors = tex_np[ty, tx]

        valid = (xs >= 0) & (xs < self.w) & (ys >= 0) & (ys < self.h) & (colors[:, :, 3] > 128)
        xs_v = xs[valid]
        ys_v = ys[valid]
        zs_v = zs[valid]
        cols_v = colors[valid].copy()
        cols_v[:, :3] = np.clip(cols_v[:, :3] * shade, 0, 255)
        cols_v = cols_v.astype(np.uint8)

        order = np.argsort(zs_v)
        xs_v = xs_v[order]
        ys_v = ys_v[order]
        zs_v = zs_v[order]
        cols_v = cols_v[order]

        mask = zs_v >= self.depth_buf[ys_v, xs_v]
        self.depth_buf[ys_v[mask], xs_v[mask]] = zs_v[mask]
        self.color_buf[ys_v[mask], xs_v[mask]] = cols_v[mask]

    def draw_mc_box(self, skin_img, uv_origin, size_xyz, pivot_xyz, pos_xyz, rot_mat, global_rot, global_pos, scale):
        dx, dy, dz = size_xyz
        u0, v0 = uv_origin
        px, py, pz = pivot_xyz

        x0, x1 = -dx / 2.0 - px, dx / 2.0 - px
        y0, y1 = 0.0 - py, dy - py
        z0, z1 = -dz / 2.0 - pz, dz / 2.0 - pz

        verts = np.array([
            [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1],
            [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
        ], dtype=np.float32)

        verts = (verts @ rot_mat.T) + np.array(pos_xyz, dtype=np.float32)
        verts = (verts @ global_rot.T) * scale + np.array(global_pos, dtype=np.float32)

        tex_right = skin_img.crop((u0, v0 + dz, u0 + dz, v0 + dz + dy))
        tex_front = skin_img.crop((u0 + dz, v0 + dz, u0 + dz + dx, v0 + dz + dy))
        tex_left  = skin_img.crop((u0 + dz + dx, v0 + dz, u0 + 2 * dz + dx, v0 + dz + dy))
        tex_back  = skin_img.crop((u0 + 2 * dz + dx, v0 + dz, u0 + 2 * dz + 2 * dx, v0 + dz + dy))
        tex_top   = skin_img.crop((u0 + dz, v0, u0 + dz + dx, v0 + dz))
        tex_bot   = skin_img.crop((u0 + dz + dx, v0, u0 + dz + 2 * dx, v0 + dz))

        self.draw_textured_quad(verts[0], verts[1], verts[2], verts[3], tex_front, shade=0.96)
        self.draw_textured_quad(verts[4], verts[0], verts[3], verts[7], tex_right, shade=0.84)
        self.draw_textured_quad(verts[1], verts[5], verts[6], verts[2], tex_left, shade=0.88)
        self.draw_textured_quad(verts[5], verts[4], verts[7], verts[6], tex_back, shade=0.72)
        self.draw_textured_quad(verts[4], verts[5], verts[1], verts[0], tex_top, shade=1.0)
        self.draw_textured_quad(verts[3], verts[2], verts[6], verts[7], tex_bot, shade=0.65)

    def draw_extruded_item(self, item_img, arm_rot_mat, arm_pos_xyz, global_rot, global_pos, scale, tool_tilt_deg=-80):
        iw, ih = item_img.size
        item_np = np.array(item_img)
        tool_tilt = rot_x(math.radians(tool_tilt_deg))
        vox_size = 0.82
        thickness = 1.0

        for py in range(ih):
            for px in range(iw):
                r, g, b, a = item_np[py, px]
                if a < 128:
                    continue
                single_px = Image.new("RGBA", (1, 1), (int(r), int(g), int(b), 255))
                lx = 0.0
                ly = (py - 12) * vox_size
                lz = (px - 3) * vox_size

                x0, x1 = lx - thickness / 2, lx + thickness / 2
                y0, y1 = ly, ly + vox_size
                z0, z1 = lz, lz + vox_size

                v = np.array([
                    [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1],
                    [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
                ], dtype=np.float32)

                v = (v @ tool_tilt.T) + np.array([0.0, 9.5, 2.0], dtype=np.float32)
                v = (v @ arm_rot_mat.T) + np.array(arm_pos_xyz, dtype=np.float32)
                v = (v @ global_rot.T) * scale + np.array(global_pos, dtype=np.float32)

                self.draw_textured_quad(v[4], v[0], v[3], v[7], single_px, shade=0.98)
                self.draw_textured_quad(v[1], v[5], v[6], v[2], single_px, shade=0.98)
                self.draw_textured_quad(v[0], v[1], v[2], v[3], single_px, shade=0.80)
                self.draw_textured_quad(v[5], v[4], v[7], v[6], single_px, shade=0.75)
                self.draw_textured_quad(v[4], v[5], v[1], v[0], single_px, shade=1.05)
                self.draw_textured_quad(v[3], v[2], v[6], v[7], single_px, shade=0.68)


BLOCK_PX = 32
SPRITE_PX = BLOCK_PX * 2  # 64x64 GUI units

CORE_COLS, CORE_ROWS = 12, 7
CORE_W, CORE_H = CORE_COLS * BLOCK_PX, CORE_ROWS * BLOCK_PX  # 384 x 224 GUI units
CORE_CENTER_X, CORE_CENTER_Y = CORE_W // 2, CORE_H // 2      # 192, 112 GUI units

PAD_COLS_LEFT = 9
PAD_COLS_RIGHT = 9
PAD_ROWS_TOP = 7
PAD_ROWS_BOT = 6

BG_COLS = CORE_COLS + PAD_COLS_LEFT + PAD_COLS_RIGHT  # 30 columns = 960 GUI units
BG_ROWS = CORE_ROWS + PAD_ROWS_TOP + PAD_ROWS_BOT    # 20 rows = 640 GUI units
BG_W, BG_H = BG_COLS * BLOCK_PX, BG_ROWS * BLOCK_PX  # 960 x 640 GUI units

# Clean Mojang-style loading bar geometry in native GUI units (centered below the tunnel floor):
BAR_FRAME_MC_X = -82
BAR_FRAME_MC_Y = 67
BAR_FRAME_W = 164
BAR_FRAME_H = 10

BAR_FILL_MC_X = -80
BAR_FILL_MC_Y = 69
BAR_FILL_W = 160
BAR_FILL_H = 6

# Active animated scene bounding box in mid-centered GUI units:
# Spans core_gx = 2..8 (mc_x = -128..+96 -> width = 224) and core_gy = 3..5 (mc_y = -16..+80 -> height = 96)
SCENE_MC_X = -128
SCENE_MC_Y = -16
SCENE_W = 224
SCENE_H = 96


def core_to_mid_centered(core_x, core_y):
    return core_x - CORE_CENTER_X, core_y - CORE_CENTER_Y


def render_miner_swing_frame(target_mode, frame_idx, num_frames=10, block_px=BLOCK_PX):
    sprite_w, sprite_h = block_px * 2, block_px * 2
    scale = (1.8 * block_px) / 32.0
    ratio = block_px / 96.0
    renderer = Software3DRenderer(sprite_w, sprite_h)

    t = frame_idx / float(num_frames)
    swing = math.sin(t * 2.0 * math.pi - math.pi / 2.0) * 0.5 + 0.5
    strike = swing ** 0.75

    global_rot = rot_y(math.radians(68))
    bob_y = math.sin(t * 2.0 * math.pi) * (1.5 * ratio)
    neck_x = (96 - 64 + strike * 3.0) * ratio
    neck_y = sprite_h - 24 * scale + abs(bob_y)

    if target_mode == "top":
        head_pitch = 12.0 - strike * 6.0
        torso_lean = -4.0 - strike * 5.0
        arm_pitch = 112.0 - strike * 46.0
        tool_tilt_deg = -78.0
    else:
        head_pitch = -16.0 - strike * 6.0
        torso_lean = -12.0 - strike * 6.0
        arm_pitch = 64.0 - strike * 42.0
        tool_tilt_deg = -92.0

    global_pos = [neck_x, neck_y + ((3.0 * ratio) if target_mode == "bottom" else 0.0), 0.0]

    head_rot = rot_x(math.radians(head_pitch)) @ rot_y(math.radians(-8))
    torso_rot = rot_x(math.radians(torso_lean))
    r_arm_rot = rot_x(math.radians(arm_pitch)) @ rot_y(math.radians(8))
    l_arm_rot = rot_x(math.radians(-24 + strike * 10.0))
    r_leg_rot = rot_x(math.radians(22))
    l_leg_rot = rot_x(math.radians(-22))

    renderer.draw_mc_box(steve_skin, (16, 48), (4, 12, 4), (0, 0, 0), (+2, 12, 0), l_leg_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (32, 48), (4, 12, 4), (0, 2, 0), (+6, 2, 0), l_arm_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (16, 16), (8, 12, 4), (0, 0, 0), (0, 0, 0), torso_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (0, 16), (4, 12, 4), (0, 0, 0), (-2, 12, 0), r_leg_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (0, 0), (8, 8, 8), (0, 8, 0), (0, 0, 0), head_rot, global_rot, global_pos, scale)
    renderer.draw_extruded_item(iron_pick_16, r_arm_rot, (-6, 2, 0), global_rot, global_pos, scale, tool_tilt_deg=tool_tilt_deg)
    renderer.draw_mc_box(steve_skin, (40, 16), (4, 12, 4), (0, 2, 0), (-6, 2, 0), r_arm_rot, global_rot, global_pos, scale)

    img = Image.fromarray(renderer.color_buf, mode="RGBA")

    if strike > 0.72:
        draw = ImageDraw.Draw(img)
        impact_y = int((46 if target_mode == "top" else 132) * ratio)
        phase = int((frame_idx % 4) * max(1, int(round(3 * ratio))))
        chips = [
            (int(92 * ratio) - phase, impact_y - max(2, int(8 * ratio)) + phase),
            (int(88 * ratio) - phase * 2, impact_y + max(1, int(4 * ratio)) + phase),
            (int(93 * ratio) - phase, impact_y + max(3, int(14 * ratio)) + phase * 2),
        ]
        chip_sz = max(1, int(round(3 * ratio)))
        for cx, cy in chips:
            draw.rectangle([cx, cy, cx + chip_sz, cy + chip_sz], fill=(135, 135, 135, 255))
            draw.rectangle([cx, cy, cx + max(0, chip_sz - 1), cy + max(0, chip_sz - 1)], fill=(175, 175, 175, 255))

    return img


def render_miner_walk_frame(step_idx, num_steps=6, block_px=BLOCK_PX):
    """Render Steve taking a smooth 3D walking stride forward with legs and arms swinging."""
    sprite_w, sprite_h = block_px * 2, block_px * 2
    scale = (1.8 * block_px) / 32.0
    ratio = block_px / 96.0
    renderer = Software3DRenderer(sprite_w, sprite_h)

    t = (step_idx + 0.5) / float(num_steps)
    stride = math.sin(t * math.pi * 2.0)
    bob = abs(math.cos(t * math.pi * 2.0)) * (1.8 * ratio)

    global_rot = rot_y(math.radians(68))
    neck_x = 32.0 * ratio
    neck_y = sprite_h - 24 * scale - bob

    global_pos = [neck_x, neck_y, 0.0]

    head_rot = rot_x(math.radians(2.0)) @ rot_y(math.radians(-6))
    torso_rot = rot_x(math.radians(-3.0))
    r_arm_rot = rot_x(math.radians(48.0 + stride * 18.0)) @ rot_y(math.radians(6))
    l_arm_rot = rot_x(math.radians(-stride * 24.0))
    r_leg_rot = rot_x(math.radians(-stride * 30.0))
    l_leg_rot = rot_x(math.radians(+stride * 30.0))

    renderer.draw_mc_box(steve_skin, (16, 48), (4, 12, 4), (0, 0, 0), (+2, 12, 0), l_leg_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (32, 48), (4, 12, 4), (0, 2, 0), (+6, 2, 0), l_arm_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (16, 16), (8, 12, 4), (0, 0, 0), (0, 0, 0), torso_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (0, 16), (4, 12, 4), (0, 0, 0), (-2, 12, 0), r_leg_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (0, 0), (8, 8, 8), (0, 8, 0), (0, 0, 0), head_rot, global_rot, global_pos, scale)
    renderer.draw_extruded_item(iron_pick_16, r_arm_rot, (-6, 2, 0), global_rot, global_pos, scale, tool_tilt_deg=-75.0)
    renderer.draw_mc_box(steve_skin, (40, 16), (4, 12, 4), (0, 2, 0), (-6, 2, 0), r_arm_rot, global_rot, global_pos, scale)

    return Image.fromarray(renderer.color_buf, mode="RGBA")


def render_miner_idle_frame(frame_idx, num_frames=8, block_px=BLOCK_PX):
    """Render Steve standing proudly at the cave entrance in an idle breathing pose."""
    sprite_w, sprite_h = block_px * 2, block_px * 2
    scale = (1.8 * block_px) / 32.0
    ratio = block_px / 96.0
    renderer = Software3DRenderer(sprite_w, sprite_h)

    t = frame_idx / float(num_frames)
    breath = math.sin(t * math.pi * 2.0) * 0.5 + 0.5

    global_rot = rot_y(math.radians(68))
    neck_x = 32.0 * ratio
    neck_y = sprite_h - 24 * scale - (breath * 1.0 * ratio)

    global_pos = [neck_x, neck_y, 0.0]

    head_rot = rot_x(math.radians(-2.0)) @ rot_y(math.radians(-4))
    torso_rot = rot_x(math.radians(0.0))
    r_arm_rot = rot_x(math.radians(20.0 - breath * 3.0)) @ rot_y(math.radians(4))
    l_arm_rot = rot_x(math.radians(-8.0 + breath * 2.0))
    r_leg_rot = rot_x(math.radians(0.0))
    l_leg_rot = rot_x(math.radians(0.0))

    renderer.draw_mc_box(steve_skin, (16, 48), (4, 12, 4), (0, 0, 0), (+2, 12, 0), l_leg_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (32, 48), (4, 12, 4), (0, 2, 0), (+6, 2, 0), l_arm_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (16, 16), (8, 12, 4), (0, 0, 0), (0, 0, 0), torso_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (0, 16), (4, 12, 4), (0, 0, 0), (-2, 12, 0), r_leg_rot, global_rot, global_pos, scale)
    renderer.draw_mc_box(steve_skin, (0, 0), (8, 8, 8), (0, 8, 0), (0, 0, 0), head_rot, global_rot, global_pos, scale)
    renderer.draw_extruded_item(iron_pick_16, r_arm_rot, (-6, 2, 0), global_rot, global_pos, scale, tool_tilt_deg=-35.0)
    renderer.draw_mc_box(steve_skin, (40, 16), (4, 12, 4), (0, 2, 0), (-6, 2, 0), r_arm_rot, global_rot, global_pos, scale)

    return Image.fromarray(renderer.color_buf, mode="RGBA")


def write_fma_with_intro(fma_path, intro_frames, loop_frames, frame_time_ms=50):
    metadata = {
        "loop_count": 0,
        "frame_time": frame_time_ms,
        "frame_time_intro": frame_time_ms,
        "custom_frame_times": {},
        "custom_frame_times_intro": {}
    }
    with zipfile.ZipFile(fma_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("metadata.json", json.dumps(metadata, indent=2))
        for idx, frame_img in enumerate(intro_frames):
            buf = BytesIO()
            frame_img.save(buf, format="PNG")
            zf.writestr(f"intro_frames/{idx}.png", buf.getvalue())
        for idx, frame_img in enumerate(loop_frames):
            buf = BytesIO()
            frame_img.save(buf, format="PNG")
            zf.writestr(f"frames/{idx}.png", buf.getvalue())


def make_vanilla_bar_element(mc_x, mc_y, w, h, color="#FFFFFF"):
    elem_id = str(uuid.uuid4())
    req_cont_id = str(uuid.uuid4())
    return f"""element {{
  color = {color}
  element_type = drippy_vanilla_bar
  instance_identifier = {elem_id}
  custom_element_layer_name = Native Mojang Loading Bar
  anchor_point = mid-centered
  x = {mc_x}
  y = {mc_y}
  width = {w}
  height = {h}
  stretch_x = false
  stretch_y = false
  stay_on_screen = false
  auto_sizing = false
  auto_sizing_base_screen_width = 0
  auto_sizing_base_screen_height = 0
  auto_sizing_base_gui_scale = 0.0
  auto_sizing_base_gui_width = 0
  auto_sizing_base_gui_height = 0
  element_loading_requirement_container_identifier = {req_cont_id}
  [loading_requirement_container_meta:{req_cont_id}] = [groups:][instances:]
  is_hidden = false
  automated_button_clicks = 0
}}"""


def make_image_element(layer_name, source_rel, mc_x, mc_y, w, h, req_entries):
    elem_id = str(uuid.uuid4())
    req_cont_id = str(uuid.uuid4())

    req_instances = []
    req_lines = []
    for mode_str, comp_val in req_entries:
        r_id = str(uuid.uuid4())
        req_instances.append(r_id)
        req_lines.append(
            f'  [loading_requirement:fancymenu_visibility_requirement_is_number][requirement_mode:if][req_id:{r_id}] = ["mode":"{mode_str}","number":"{{"placeholder":"drippy_gl_percent"}}","compare_with":"{comp_val}"]$'
        )

    inst_str = ";".join(req_instances) + (";" if req_instances else "")
    lines = [
        "element {",
        f"  source = [source:local]{source_rel}",
        "  repeat_texture = true",
        "  nine_slice_texture = false",
        "  nine_slice_texture_border_x = 5",
        "  nine_slice_texture_border_y = 5",
        "  image_tint = #FFFFFF",
        "  restart_animated_on_menu_load = true",
        "  element_type = image",
        f"  instance_identifier = {elem_id}",
        f"  custom_element_layer_name = {layer_name}",
        "  anchor_point = mid-centered",
        f"  x = {mc_x}",
        f"  y = {mc_y}",
        f"  width = {w}",
        f"  height = {h}",
        "  stretch_x = false",
        "  stretch_y = false",
        "  stay_on_screen = false",
        "  auto_sizing = false",
        "  auto_sizing_base_screen_width = 0",
        "  auto_sizing_base_screen_height = 0",
        "  auto_sizing_base_gui_scale = 0.0",
        "  auto_sizing_base_gui_width = 0",
        "  auto_sizing_base_gui_height = 0",
        f"  element_loading_requirement_container_identifier = {req_cont_id}",
        f"  [loading_requirement_container_meta:{req_cont_id}] = [groups:][instances:{inst_str}]",
    ] + req_lines + [
        "  is_hidden = false",
        "  automated_button_clicks = 0",
        "}"
    ]
    return "\n".join(lines)


def generate_drippy_layout():
    layout_req_id = str(uuid.uuid4())
    open_block_id = str(uuid.uuid4())
    close_block_id = str(uuid.uuid4())
    bg_inst_id = str(uuid.uuid4())

    sections = []
    sections.append("type = fancymenu_layout")
    sections.append(f"""layout-meta {{
  identifier = de.keksuccino.drippyloadingscreen.customization.DrippyOverlayScreen
  render_custom_elements_behind_vanilla = true
  last_edited_time = {int(time.time() * 1000)}
  is_enabled = true
  randommode = false
  randomgroup = 1
  randomonlyfirsttime = false
  layout_index = 0
  [loading_requirement_container_meta:{layout_req_id}] = [groups:][instances:]
}}""")

    sections.append(f"""menu_background {{
  color = #05060A
  instance_identifier = {bg_inst_id}
  background_type = color_fancymenu
}}

customization {{
  action = backgroundoptions
  keepaspectratio = true
}}""")

    sections.append("""scroll_list_customization {
  preserve_scroll_list_header_footer_aspect_ratio = true
  render_scroll_list_header_shadow = true
  render_scroll_list_footer_shadow = true
  show_scroll_list_header_footer_preview_in_editor = false
  repeat_scroll_list_header_texture = false
  repeat_scroll_list_footer_texture = false
  show_screen_background_overlay_on_custom_background = false
  apply_vanilla_background_blur = false
}""")

    sections.append(f"""layout_action_executable_blocks {{
  open_screen_executable_block_identifier = {open_block_id}
  [executable_block:{open_block_id}][type:generic] = [executables:]
  close_screen_executable_block_identifier = {close_block_id}
  [executable_block:{close_block_id}][type:generic] = [executables:]
}}""")

    # Layer 1: Oversized 960x640 Tunnel Base Background (with vignette & dark bar slot baked in)
    bg_mc_x, bg_mc_y = core_to_mid_centered(-PAD_COLS_LEFT * BLOCK_PX, -PAD_ROWS_TOP * BLOCK_PX)
    sections.append(make_image_element(
        "Tunnel Base Background",
        "/config/fancymenu/assets/loading_tunnel/tunnel_bg.png",
        bg_mc_x, bg_mc_y, BG_W, BG_H,
        []
    ))

    # Layer 2: Tunnel Mining Sequence (smooth 9.5-second sequence that reaches the cavern threshold)
    sections.append(make_image_element(
        "Tunnel Mining Sequence",
        "/config/fancymenu/assets/loading_tunnel/tunnel_scene.fma",
        SCENE_MC_X, SCENE_MC_Y, SCENE_W, SCENE_H,
        []
    ))

    # Layer 3: Native Mojang Loading Bar (hooks into real resource reload progress)
    sections.append(make_vanilla_bar_element(
        BAR_FRAME_MC_X, BAR_FRAME_MC_Y, BAR_FRAME_W, BAR_FRAME_H,
        color="#FFFFFF"
    ))

    # Vanilla Widgets on DrippyOverlayScreen (both hidden since we render our clean Mojang-style bar above):
    logo_req_id = str(uuid.uuid4())
    logo_exec_id = str(uuid.uuid4())
    logo_act_req_id = str(uuid.uuid4())
    sections.append(f"""vanilla_button {{
  button_element_executable_block_identifier = {logo_exec_id}
  [executable_block:{logo_exec_id}][type:generic] = [executables:]
  restartbackgroundanimations = true
  nine_slice_custom_background = false
  nine_slice_border_x = 5
  nine_slice_border_y = 5
  navigatable = true
  widget_active_state_requirement_container_identifier = {logo_act_req_id}
  [loading_requirement_container_meta:{logo_act_req_id}] = [groups:][instances:]
  is_template = false
  template_apply_width = false
  template_apply_height = false
  template_apply_posx = false
  template_apply_posy = false
  template_apply_opacity = false
  template_apply_visibility = false
  template_apply_label = false
  template_share_with = buttons
  nine_slice_slider_handle = false
  nine_slice_slider_handle_border_x = 5
  nine_slice_slider_handle_border_y = 5
  element_type = vanilla_button
  instance_identifier = mojang_logo
  is_hidden = true
  automated_button_clicks = 0
  element_loading_requirement_container_identifier = {logo_req_id}
  [loading_requirement_container_meta:{logo_req_id}] = [groups:][instances:]
}}""")

    bar_req_id = str(uuid.uuid4())
    bar_exec_id = str(uuid.uuid4())
    bar_act_req_id = str(uuid.uuid4())
    sections.append(f"""vanilla_button {{
  button_element_executable_block_identifier = {bar_exec_id}
  [executable_block:{bar_exec_id}][type:generic] = [executables:]
  restartbackgroundanimations = true
  nine_slice_custom_background = false
  nine_slice_border_x = 5
  nine_slice_border_y = 5
  navigatable = true
  widget_active_state_requirement_container_identifier = {bar_act_req_id}
  [loading_requirement_container_meta:{bar_act_req_id}] = [groups:][instances:]
  is_template = false
  template_apply_width = false
  template_apply_height = false
  template_apply_posx = false
  template_apply_posy = false
  template_apply_opacity = false
  template_apply_visibility = false
  template_apply_label = false
  template_share_with = buttons
  nine_slice_slider_handle = false
  nine_slice_slider_handle_border_x = 5
  nine_slice_slider_handle_border_y = 5
  element_type = vanilla_button
  instance_identifier = progress_bar
  is_hidden = true
  automated_button_clicks = 0
  element_loading_requirement_container_identifier = {bar_req_id}
  [loading_requirement_container_meta:{bar_req_id}] = [groups:][instances:]
}}""")

    layout_path = os.path.join(LAYOUT_DIR, "drippy_mining_loading.txt")
    with open(layout_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n\n".join(sections) + "\n")
    print("Saved layout to:", layout_path)


def update_options_files():
    if os.path.exists(DRIPPY_OPTS_PATH):
        with open(DRIPPY_OPTS_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace(
            "B:early_loading_background_preserve_aspect_ratio = 'false';",
            "B:early_loading_background_preserve_aspect_ratio = 'true';"
        )
        content = content.replace(
            "B:early_loading_hide_bar = 'false';",
            "B:early_loading_hide_bar = 'true';"
        )
        with open(DRIPPY_OPTS_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print("Updated:", DRIPPY_OPTS_PATH)

    if os.path.exists(FM_OPTS_PATH):
        with open(FM_OPTS_PATH, "r", encoding="utf-8") as f:
            fm_content = f.read()
        fm_content = re.sub(
            r"S:preload_resources\s*=\s*'[^']*';",
            "S:preload_resources = '';",
            fm_content
        )
        with open(FM_OPTS_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(fm_content)
        print("Cleared preload_resources in:", FM_OPTS_PATH)


def draw_break_particles(canvas, blk_x, blk_y, burst_frame):
    """Draw pixel-art stone break fragments flying outward when a block shatters."""
    draw = ImageDraw.Draw(canvas)
    offsets = [
        (4, 5, -3, -2), (14, 4, 0, -3), (24, 6, +3, -2),
        (6, 15, -4, 0), (16, 16, +1, +1), (25, 14, +4, 0),
        (5, 25, -3, +3), (15, 24, 0, +4), (23, 26, +3, +3),
    ]
    t = burst_frame + 1
    for ox, oy, vx, vy in offsets:
        px = blk_x + ox + vx * t
        py = blk_y + oy + vy * t + (t * t)
        draw.rectangle([px, py, px + 3, py + 3], fill=(95, 95, 95, 255))
        draw.rectangle([px, py, px + 1, py + 1], fill=(150, 150, 150, 255))


def build_all_assets_and_layout():
    stone_block = stone_16.resize((BLOCK_PX, BLOCK_PX), resample=Image.NEAREST)
    lighter_bg_stone = tint_image(stone_block, 1.08)
    darker_fg_stone = tint_image(stone_block, 0.56)

    darker_fg_stone.save(os.path.join(ASSETS_DIR, "stone_fg.png"))

    crack_stage_imgs = []
    for d_idx in range(10):
        blk = darker_fg_stone.copy()
        crack = destroy_stages[d_idx].resize((BLOCK_PX, BLOCK_PX), resample=Image.NEAREST)
        blk.alpha_composite(crack)
        crack_stage_imgs.append(blk)

    # Clean Mojang-style loading bar dark backing slot (164 x 10 GUI units)
    bar_slot = Image.new("RGBA", (BAR_FRAME_W, BAR_FRAME_H), (0, 0, 0, 0))
    bsd = ImageDraw.Draw(bar_slot)
    bsd.rectangle([0, 0, BAR_FRAME_W - 1, BAR_FRAME_H - 1], fill=(15, 16, 20, 220))
    bar_slot.save(os.path.join(ASSETS_DIR, "bar_frame.png"))

    # Oversized 960x640 tunnel_bg.png in native GUI units:
    tunnel_bg = Image.new("RGBA", (BG_W, BG_H), (0, 0, 0, 255))
    shadow_h = max(2, BLOCK_PX // 10)
    shadow_strip = Image.new("RGBA", (BLOCK_PX, shadow_h), (0, 0, 0, 60))
    for bg_gx in range(BG_COLS):
        for bg_gy in range(BG_ROWS):
            core_gx = bg_gx - PAD_COLS_LEFT
            core_gy = bg_gy - PAD_ROWS_TOP
            if core_gy in [3, 4] and core_gx <= 7:
                tunnel_bg.paste(lighter_bg_stone, (bg_gx * BLOCK_PX, bg_gy * BLOCK_PX))
                if core_gy == 3:
                    tunnel_bg.alpha_composite(shadow_strip, (bg_gx * BLOCK_PX, bg_gy * BLOCK_PX))
                else:
                    tunnel_bg.alpha_composite(shadow_strip, (bg_gx * BLOCK_PX, (bg_gy + 1) * BLOCK_PX - shadow_h))
            else:
                tunnel_bg.paste(darker_fg_stone, (bg_gx * BLOCK_PX, bg_gy * BLOCK_PX))

    # Cave depth vignette baked directly onto tunnel_bg.png
    yy, xx = np.mgrid[0:BG_H, 0:BG_W]
    center_px_x = (PAD_COLS_LEFT + 5.5) * BLOCK_PX
    center_px_y = (PAD_ROWS_TOP + 4.0) * BLOCK_PX
    dx = (xx - center_px_x) / (CORE_W * 0.68)
    dy = (yy - center_px_y) / (CORE_H * 0.55)
    dist = np.sqrt(dx * dx * 0.4 + dy * dy * 1.2)
    alpha = np.clip((dist - 0.35) * 235, 0, 225).astype(np.uint8)
    vig_np = np.zeros((BG_H, BG_W, 4), dtype=np.uint8)
    vig_np[:, :, 0] = 5
    vig_np[:, :, 1] = 6
    vig_np[:, :, 2] = 10
    vig_np[:, :, 3] = alpha
    cave_vignette = Image.fromarray(vig_np, mode="RGBA")
    cave_vignette.save(os.path.join(ASSETS_DIR, "cave_vignette.png"))

    tunnel_bg.alpha_composite(cave_vignette)

    bg_center_x = PAD_COLS_LEFT * BLOCK_PX + CORE_CENTER_X
    bg_center_y = PAD_ROWS_TOP * BLOCK_PX + CORE_CENTER_Y
    tunnel_bg.alpha_composite(bar_slot, (bg_center_x + BAR_FRAME_MC_X, bg_center_y + BAR_FRAME_MC_Y))
    tunnel_bg.save(os.path.join(ASSETS_DIR, "tunnel_bg.png"))

    # Base crop of the 224x96 active scene region from tunnel_bg.png
    scene_x0 = bg_center_x + SCENE_MC_X
    scene_y0 = bg_center_y + SCENE_MC_Y
    scene_base = tunnel_bg.crop((scene_x0, scene_y0, scene_x0 + SCENE_W, scene_y0 + SCENE_H))

    # Pre-render 8-frame swing loops, 6-frame walk cycle, and 8-frame idle breathing cycle
    SWING_FRAMES = 8
    WALK_FRAMES = 6
    IDLE_FRAMES = 8
    top_swing_sprites = [render_miner_swing_frame("top", i, SWING_FRAMES, block_px=BLOCK_PX) for i in range(SWING_FRAMES)]
    bot_swing_sprites = [render_miner_swing_frame("bottom", i, SWING_FRAMES, block_px=BLOCK_PX) for i in range(SWING_FRAMES)]
    walk_sprites = [render_miner_walk_frame(i, WALK_FRAMES, block_px=BLOCK_PX) for i in range(WALK_FRAMES)]
    idle_sprites = [render_miner_idle_frame(i, IDLE_FRAMES, block_px=BLOCK_PX) for i in range(IDLE_FRAMES)]

    # 16-frame crack progression across 2 swings per block (800ms per block):
    block_crack_schedule = [0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 9]

    def compose_scene_frame(miner_sprite, miner_px_x, broken_set, cracking_target, crack_stage, burst_target, burst_idx):
        """
        Compose one 224x96 frame of tunnel_scene.fma:
        - Base tunnel
        - 3D sideways Steve sprite (behind foreground stone so pickaxe tip sinks into the stone!)
        - Remaining intact foreground blocks + active cracking block + block break particle burst
        """
        frame = scene_base.copy()
        frame.alpha_composite(miner_sprite, (miner_px_x, 0))

        for c_idx in range(5):
            bx = (1 + c_idx) * BLOCK_PX
            for is_bot in [False, True]:
                by = BLOCK_PX if is_bot else 0
                b_key = (c_idx, is_bot)
                if b_key in broken_set:
                    if burst_target == b_key:
                        draw_break_particles(frame, bx, by, burst_idx)
                    continue
                if cracking_target == b_key and crack_stage is not None:
                    frame.alpha_composite(crack_stage_imgs[crack_stage], (bx, by))
                else:
                    frame.paste(darker_fg_stone, (bx, by))

        return frame

    # Build the complete sequence of intro_frames (mining Columns 1..5 across 9.5 seconds)
    # and loop_frames (Steve standing proudly at cavern threshold in idle breathing pose).
    intro_frames = []
    loop_frames = []
    broken_blocks = set()

    for col_idx in range(5):
        miner_x = col_idx * BLOCK_PX

        # 1. Mine Top Block of col_idx (16 frames = 2 swings)
        top_key = (col_idx, False)
        for f_i, c_stage in enumerate(block_crack_schedule):
            burst_t = (col_idx - 1, True) if (col_idx > 0 and f_i < 3) else None
            intro_frames.append(compose_scene_frame(
                top_swing_sprites[f_i % SWING_FRAMES],
                miner_x,
                broken_blocks,
                top_key,
                c_stage,
                burst_t,
                f_i
            ))
        broken_blocks.add(top_key)

        # 2. Mine Bottom Block of col_idx (16 frames = 2 swings)
        bot_key = (col_idx, True)
        for f_i, c_stage in enumerate(block_crack_schedule):
            burst_t = top_key if f_i < 3 else None
            intro_frames.append(compose_scene_frame(
                bot_swing_sprites[f_i % SWING_FRAMES],
                miner_x,
                broken_blocks,
                bot_key,
                c_stage,
                burst_t,
                f_i
            ))
        broken_blocks.add(bot_key)

        # 3. Smoothly walk 1 block forward over 6 frames
        # For columns 0..3: walk from col_idx to col_idx + 1
        # For column 4: walk past the excavated stone into the illuminated cavern entrance!
        for w_i in range(WALK_FRAMES):
            walk_x = int(round(miner_x + ((w_i + 1) / float(WALK_FRAMES)) * BLOCK_PX))
            burst_t = bot_key if w_i < 3 else None
            intro_frames.append(compose_scene_frame(
                walk_sprites[w_i],
                walk_x,
                broken_blocks,
                None,
                None,
                burst_t,
                w_i
            ))

    # Loop frames: Steve standing at cavern threshold in idle breathing pose!
    final_miner_x = 5 * BLOCK_PX
    for l_i in range(IDLE_FRAMES):
        loop_frames.append(compose_scene_frame(
            idle_sprites[l_i],
            final_miner_x,
            broken_blocks,
            None,
            None,
            None,
            0
        ))

    # Save initial frame (tunnel_scene_initial.png) and full sequence (tunnel_scene.fma)
    intro_frames[0].save(os.path.join(ASSETS_DIR, "tunnel_scene_initial.png"))
    write_fma_with_intro(os.path.join(ASSETS_DIR, "tunnel_scene.fma"), intro_frames, loop_frames, frame_time_ms=50)

    # Also build an 800x800 (2x of 400x400 GUI grid around mid-centered) early_window_bg.png
    # so the early GLFW window (800x800) matches DrippyOverlayScreen 1:1 with zero left/right cropping!
    full_initial = tunnel_bg.copy()
    full_initial.alpha_composite(intro_frames[0], (scene_x0, scene_y0))
    early_400 = full_initial.crop((
        bg_center_x - 200,
        bg_center_y - 200,
        bg_center_x + 200,
        bg_center_y + 200
    ))
    early_800 = early_400.resize((800, 800), resample=Image.NEAREST)
    early_800.save(os.path.join(ASSETS_DIR, "early_window_bg.png"))

    generate_drippy_layout()
    update_options_files()
    print(f"Generated tunnel_scene.fma ({len(intro_frames)} intro frames + {len(loop_frames)} loop frames) and 800x800 early_window_bg.png!")


if __name__ == "__main__":
    build_all_assets_and_layout()
