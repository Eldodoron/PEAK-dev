import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (18, 4, 6, 255),       # Darkest silhouette outline (#120406)
    
    # Blood Red Ramp
    '1': (48, 7, 14, 255),      # Deep coagulated burgundy (#30070E)
    '2': (82, 11, 22, 255),     # Dark blood (#520B16)
    '3': (126, 16, 34, 255),    # Rich crimson midtone (#7E1022)
    '4': (176, 22, 48, 255),    # Pure dragon blood (#B01630)
    '5': (224, 32, 60, 255),    # Vivid scarlet (#E0203C)
    '6': (250, 68, 94, 255),    # Fiery bright blood (#FA445E)
    '7': (255, 138, 156, 255),  # Soft pink specular (#FF8A9C)
    'W': (255, 238, 242, 255),  # Pure white specular glint (#FFEEF2)
    
    # Draconic Gold / Brass Ramp
    'g': (74, 53, 16, 255),     # Dark brass (#4A3510)
    'G': (145, 108, 24, 255),   # Mid brass (#916C18)
    'Y': (218, 172, 48, 255),   # Bright dragon gold (#DAAC30)
    'y': (254, 226, 114, 255),  # Specular gold (#FEE272)
    
    # Dynamic Glass Lighting Ramps
    # High-lit glass (top-left)
    'C': (225, 242, 252, 250),  # Bright white/cyan specular reflection (#E1F2FC)
    'c': (168, 198, 214, 225),  # Lit glass rim (#A8C6D6)
    'm': (110, 140, 158, 210),  # Midtone glass (#6E8C9E)
    'd': (66, 86, 100, 210),    # Shaded glass rim (#425664)
    'D': (42, 54, 64, 220),     # Deep shadow glass (#2A3640)
    
    # Blood-tinted dark glass (optional for warm variation)
    'b': (78, 26, 38, 220),     # Glass refracting deep blood (#4E1A26)
    'B': (108, 38, 54, 220),    # Mid blood-refracting glass (#6C2636)
}

# -------------------------------------------------------------
# OPTION 1A: Directional Cool-Glass Shading (Recommended)
# • Lid neck row 2 fixed: 'KggK' (symmetrical black outline).
# • Top glass row 4 extended: 8 white pixels 'CCCCCCCC'.
# • Glass rim shaded from bright specular 'C/c' on left to dark shadow 'd/D' on right.
# • Thick glass bottom graded 'ccmmddDD'.
# -------------------------------------------------------------
GRID_1A = [
    "      KyyK      ", # 0: Golden stopper crest
    "     KyYYyK     ", # 1: Stopper cap
    "      KggK      ", # 2: Stopper plug with black outline on BOTH sides!
    "     KgYYgK     ", # 3: Golden bottle collar
    "   KCCCCCCCCK   ", # 4: Top glass reaches sides (8 white pixels)
    "  KCW6543211mK  ", # 5: Upper phial: lit 'C' left, shaded 'm' right
    "  KCWW654321dK  ", # 6: Specular glare 'C', dark glass 'd' on right
    "  Kc76543Y21dK  ", # 7: Lit glass 'c', suspended ember 'Y', dark 'd'
    "  Kc65432211dK  ", # 8: Deep blood volume, dark 'd'
    "  Kc5432y211dK  ", # 9: Suspended ember 'y', dark 'd'
    "  Km43221112dK  ", # 10: Mid glass 'm', backscatter rim '2', dark 'd'
    "   Km321111dK   ", # 11: Base curve: mid 'm' left, dark 'd' right
    "   KccmmddDDK   ", # 12: Thick glass base graded from lit to shadow
    "    KKKKKKKK    ", # 13: Bottle base rim
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 1B: High-Contrast Prismatic Glass
# • Brighter specular glints on the left glass wall.
# • Bottom base catches a crisp counter-reflection.
# -------------------------------------------------------------
GRID_1B = [
    "      KyyK      ", # 0: Golden stopper crest
    "     KyYYyK     ", # 1: Stopper cap
    "      KgGK      ", # 2: Stopper plug with highlight and black outlines
    "     KgYYgK     ", # 3: Golden bottle collar
    "   KCCCCCCCCK   ", # 4: Top glass reaches sides
    "  KCW6543211dK  ", # 5: Upper phial
    "  KCWW654321dK  ", # 6: Pure specular 'C'
    "  KC76543Y21DK  ", # 7: Deep shadow 'D' on right
    "  Kc65432211DK  ", # 8: Deep shadow 'D' on right
    "  Kc5432y211dK  ", # 9: Shadow glass 'd'
    "  Km43221112dK  ", # 10: Translucent backscatter rim
    "   Km321111DK   ", # 11: Base curve
    "   KCCmmddccK   ", # 12: Prismatic base reflection on bottom right
    "    KKKKKKKK    ", # 13: Bottle base rim
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 1C: Translucent Blood-Refracting Glass
# • Shadow side of glass absorbs deep blood tones ('b', 'B')
# • Feels like thick, magical alchemical glass
# -------------------------------------------------------------
GRID_1C = [
    "      KyyK      ", # 0: Golden stopper crest
    "     KyYYyK     ", # 1: Stopper cap
    "      KggK      ", # 2: Stopper plug
    "     KgYYgK     ", # 3: Golden bottle collar
    "   KCCCCCCCCK   ", # 4: Top glass reaches sides
    "  KCW6543211bK  ", # 5: Blood-tinted shadow glass 'b'
    "  KCWW654321bK  ", # 6: Specular glare 'C', blood glass 'b'
    "  Kc76543Y21bK  ", # 7: Suspended ember 'Y', blood glass 'b'
    "  Kc65432211bK  ", # 8: Deep blood volume, blood glass 'b'
    "  Kc5432y211bK  ", # 9: Suspended ember 'y', blood glass 'b'
    "  Km43221112bK  ", # 10: Blood glass 'b'
    "   Km321111bK   ", # 11: Base curve
    "   KccmmbbbbK   ", # 12: Base transitions into blood-tinted glass
    "    KKKKKKKK    ", # 13: Bottle base rim
    "                ", # 14
    "                "  # 15
]

def render_sprite(grid, palette):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        row = grid[y]
        assert len(row) == 16, f"Row {y} len={len(row)}: '{row}'"
        for x in range(16):
            ch = row[x]
            img.putpixel((x, y), palette.get(ch, (0, 0, 0, 0)))
    return img

def main():
    out_dir = r"scrapped_tools\preview_dragon_blood"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt1a_directional_glass": (GRID_1A, "Option 1A: Directional Cool-Glass Shading"),
        "opt1b_prismatic_glass": (GRID_1B, "Option 1B: High-Contrast Prismatic Glass"),
        "opt1c_blood_refraction": (GRID_1C, "Option 1C: Translucent Blood-Refracting Glass"),
    }
    
    for key, (grid, title) in variations.items():
        assert len(grid) == 16, f"{key} row count != 16"
        for y, r in enumerate(grid):
            assert len(r) == 16, f"{key} row {y} len {len(r)} != 16: '{r}'"
            stripped = r.strip()
            if stripped:
                lead_sp = len(r) - len(r.lstrip())
                trail_sp = len(r) - len(r.rstrip())
                assert lead_sp == trail_sp, f"{key} row {y} not centered: lead={lead_sp}, trail={trail_sp}: '{r}'"
        
        img = render_sprite(grid, PALETTE)
        p16 = os.path.join(out_dir, f"{key}_16.png")
        p256 = os.path.join(out_dir, f"{key}_256.png")
        img.save(p16)
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(p256)
        
        # Also create a zoom crop of the neck and shoulder area
        crop_neck = img.crop((3, 0, 13, 8)).resize((256, 204), Image.Resampling.NEAREST)
        p_crop = os.path.join(out_dir, f"{key}_neck_crop256.png")
        crop_neck.save(p_crop)
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p_crop, os.path.join(artifact_dir, f"{key}_neck_crop256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    main()
