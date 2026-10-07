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
    'C': (225, 242, 252, 250),  # Bright white/cyan specular reflection (#E1F2FC)
    'c': (168, 198, 214, 225),  # Lit glass rim (#A8C6D6)
    'm': (110, 140, 158, 210),  # Midtone glass (#6E8C9E)
    'd': (66, 86, 100, 210),    # Shaded dark glass rim (#425664)
    'D': (42, 54, 64, 220),     # Deep shadow glass (#2A3640)
}

# -------------------------------------------------------------
# FINAL OPTION 1A-1: Direct Request
# • Row 5 right glass: 'm' -> 'd' (all shadow-side glass pixels dark 'd')
# • Row 2 stopper neck: 'KgGK' from 1B reversed -> 'KGgK' (G on lit left, g on shadow right)
# -------------------------------------------------------------
GRID_1A_FINAL = [
    "      KyyK      ", # 0: Golden stopper crest
    "     KyYYyK     ", # 1: Stopper cap
    "      KGgK      ", # 2: Stopper plug: 1B detail reversed (G on left, g on right)
    "     KgYYgK     ", # 3: Golden bottle collar
    "   KCCCCCCCCK   ", # 4: Extended white glass shoulder (8px wide)
    "  KCW6543211dK  ", # 5: Right glass changed to darkest shadow 'd'!
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
# FINAL OPTION 1A-2: Fully Directional Gold Cap
# • Same as 1A-1, plus rows 0, 1, 3 also receive directional lighting
#   (bright specular 'y/Y' on left, shaded brass 'G/g' on right)
# -------------------------------------------------------------
GRID_1A_FULL_DIR = [
    "      KyYK      ", # 0: Golden stopper crest: y left, Y right
    "     KyYYgK     ", # 1: Stopper cap: y/Y left, shaded g right
    "      KGgK      ", # 2: Stopper plug: G left, g right
    "     KyYGgK     ", # 3: Collar: y/Y left, G/g right
    "   KCCCCCCCCK   ", # 4: Extended white glass shoulder
    "  KCW6543211dK  ", # 5: Darkest glass 'd'
    "  KCWW654321dK  ", # 6: Specular glare 'C', dark glass 'd'
    "  Kc76543Y21dK  ", # 7: Lit glass 'c', suspended ember 'Y', dark 'd'
    "  Kc65432211dK  ", # 8: Deep blood volume, dark 'd'
    "  Kc5432y211dK  ", # 9: Suspended ember 'y', dark 'd'
    "  Km43221112dK  ", # 10: Mid glass 'm', backscatter rim '2', dark 'd'
    "   Km321111dK   ", # 11: Base curve
    "   KccmmddDDK   ", # 12: Thick glass base
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
        "opt1a_final": (GRID_1A_FINAL, "Option 1A-Final: Exact Request (Row 5 'd' + Stopper 'KGgK')"),
        "opt1a_full_directional": (GRID_1A_FULL_DIR, "Option 1A-FullDir: Full Directional Gold & Glass"),
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
        
        # Close up of neck & upper glass
        crop_neck = img.crop((2, 0, 14, 9)).resize((256, 192), Image.Resampling.NEAREST)
        p_crop = os.path.join(out_dir, f"{key}_crop256.png")
        crop_neck.save(p_crop)
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p_crop, os.path.join(artifact_dir, f"{key}_crop256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    main()
