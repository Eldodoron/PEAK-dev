import os
import sys
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8")

VANILLA_SHEET = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\preview_frames\vanilla\assets\minecraft\textures\font\ascii.png"
FRAME_0 = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\preview_frames\frame_0.png"
OUT_DIR = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\preview_frames"

def extract_glyphs(sheet_path):
    sheet = Image.open(sheet_path).convert("RGBA")
    glyphs = {}
    for code in range(256):
        row = code // 16
        col = code % 16
        cell = sheet.crop((col * 8, row * 8, (col + 1) * 8, (row + 1) * 8))
        bbox = cell.getbbox()
        if bbox is None:
            glyphs[chr(code)] = (Image.new("RGBA", (4, 8), (0, 0, 0, 0)), 4)
        else:
            w = min(8, bbox[2] + 1)
            glyph = cell.crop((0, 0, w, 8))
            glyphs[chr(code)] = (glyph, w)
    return glyphs

def colorize_glyph(glyph, rgb_color):
    r, g, b = rgb_color
    data = list(glyph.getdata())
    new_data = []
    for pixel in data:
        if pixel[3] > 20:
            new_data.append((r, g, b, pixel[3]))
        else:
            new_data.append((0, 0, 0, 0))
    colored = Image.new("RGBA", glyph.size)
    colored.putdata(new_data)
    return colored

def render_mc_text(text, glyphs, color=(255, 255, 255), shadow_color=(63, 63, 63), scale=3, has_shadow=True, has_plate=False, plate_alpha=110):
    total_w = 0
    chars = []
    for ch in text:
        if ch in glyphs:
            g, w = glyphs[ch]
            chars.append((g, w))
            total_w += w
        else:
            chars.append((Image.new("RGBA", (4, 8), (0, 0, 0, 0)), 4))
            total_w += 4
    
    base_w = total_w + (1 if has_shadow else 0)
    base_h = 8 + (1 if has_shadow else 0)
    
    txt_img = Image.new("RGBA", (base_w, base_h), (0, 0, 0, 0))
    
    if has_shadow and shadow_color:
        curr_x = 1
        for g, w in chars:
            colored_shadow = colorize_glyph(g, shadow_color)
            txt_img.paste(colored_shadow, (curr_x, 1), colored_shadow)
            curr_x += w
            
    curr_x = 0
    for g, w in chars:
        colored_main = colorize_glyph(g, color)
        txt_img.paste(colored_main, (curr_x, 0), colored_main)
        curr_x += w

    scaled_txt = txt_img.resize((base_w * scale, base_h * scale), Image.NEAREST)
    
    if not has_plate:
        return scaled_txt
    
    # Minecraft nametag plate padding: 2px horizontal, 1px vertical (scaled)
    pad_x = 2 * scale
    pad_y = 1 * scale
    plate_w = scaled_txt.width + pad_x * 2
    plate_h = scaled_txt.height + pad_y * 2
    
    plate_img = Image.new("RGBA", (plate_w, plate_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(plate_img)
    draw.rectangle([0, 0, plate_w, plate_h], fill=(0, 0, 0, plate_alpha))
    plate_img.paste(scaled_txt, (pad_x, pad_y), scaled_txt)
    return plate_img

def main():
    glyphs = extract_glyphs(VANILLA_SHEET)
    base_frame = Image.open(FRAME_0).convert("RGBA")
    
    # Player head center X = 297, Top Y = 81
    player_center_x = 297
    player_head_top_y = 81
    
    # Ideal offset above player head: 14 pixels
    head_gap = 14
    
    variations = [
        {
            "id": "variant_a_nametag_white",
            "label": "Option A: Classic Minecraft Nametag (Semi-Transparent Box + White)",
            "color": (255, 255, 255),
            "shadow": (63, 63, 63),
            "scale": 3,
            "plate": True,
            "plate_alpha": 115,
            "desc": "Traditional Minecraft in-game nametag look with subtle semi-transparent black backing."
        },
        {
            "id": "variant_b_nametag_gold",
            "label": "Option B: PEAK Gold Nametag (Semi-Transparent Box + Gold)",
            "color": (255, 170, 0),
            "shadow": (63, 42, 0),
            "scale": 3,
            "plate": True,
            "plate_alpha": 120,
            "desc": "Branded gold nametag (#FFAA00) matching the PEAK title palette."
        },
        {
            "id": "variant_c_nametag_emerald",
            "label": "Option C: PEAK Emerald Nametag (Semi-Transparent Box + Green)",
            "color": (85, 255, 85),
            "shadow": (21, 63, 21),
            "scale": 3,
            "plate": True,
            "plate_alpha": 120,
            "desc": "Vibrant emerald green nametag (#55FF55) matching the player's chest emblem."
        },
        {
            "id": "variant_d_floating_gold",
            "label": "Option D: Floating Gold Title (Drop Shadow, No Box)",
            "color": (255, 170, 0),
            "shadow": (63, 42, 0),
            "scale": 3,
            "plate": False,
            "plate_alpha": 0,
            "desc": "Clean floating text with native Minecraft shadow, gold styling."
        },
        {
            "id": "variant_e_floating_yellow",
            "label": "Option E: Floating Classic Yellow (Drop Shadow, No Box)",
            "color": (255, 255, 85),
            "shadow": (63, 63, 21),
            "scale": 3,
            "plate": False,
            "plate_alpha": 0,
            "desc": "Minecraft splash-text yellow (#FFFF55) with dark shadow."
        },
        {
            "id": "variant_f_floating_white",
            "label": "Option F: Floating Clean White (Drop Shadow, No Box)",
            "color": (255, 255, 255),
            "shadow": (63, 63, 63),
            "scale": 3,
            "plate": False,
            "plate_alpha": 0,
            "desc": "Minimalist white text floating seamlessly in the open sky."
        }
    ]
    
    for v in variations:
        sprite = render_mc_text(
            "Lite",
            glyphs,
            color=v["color"],
            shadow_color=v["shadow"],
            scale=v["scale"],
            has_shadow=True,
            has_plate=v["plate"],
            plate_alpha=v["plate_alpha"]
        )
        
        pos_x = player_center_x - (sprite.width // 2)
        pos_y = player_head_top_y - head_gap - sprite.height
        
        frame = base_frame.copy()
        frame.paste(sprite, (pos_x, pos_y), sprite)
        
        out_path = os.path.join(OUT_DIR, f"{v['id']}.png")
        frame.save(out_path)
        print(f"Generated {v['id']}: Pos=({pos_x}, {pos_y}), Sprite={sprite.size} -> {out_path}")

if __name__ == "__main__":
    main()
