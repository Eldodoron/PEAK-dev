import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (18, 4, 6, 255),       # Darkest silhouette outline (#120406)
    'k': (35, 10, 16, 255),     # Deep blood outline (#230A10)
    
    # Blood Red Ramp
    '1': (52, 8, 16, 255),      # Deep coagulated burgundy shadow (#340810)
    '2': (88, 12, 24, 255),     # Dark blood (#580C18)
    '3': (132, 18, 36, 255),    # Rich crimson midtone (#841224)
    '4': (178, 24, 48, 255),    # Pure dragon blood (#B21830)
    '5': (224, 34, 62, 255),    # Vivid scarlet (#E0223E)
    '6': (250, 72, 98, 255),    # Fiery bright blood (#FA4862)
    '7': (255, 142, 160, 255),  # Soft pink specular (#FF8EA0)
    'W': (255, 238, 242, 255),  # Pure specular glint (#FFEEF2)
    
    # Draconic Gold / Brass
    'g': (74, 53, 16, 255),     # Dark brass (#4A3510)
    'G': (145, 108, 24, 255),   # Mid brass (#916C18)
    'Y': (218, 172, 48, 255),   # Bright dragon gold (#DAAC30)
    'y': (254, 226, 114, 255),  # Specular gold (#FEE272)
    
    # Dragon Claw / Scale / Bone
    'd': (26, 22, 28, 255),     # Pitch dragon scale (#1A161C)
    'D': (52, 46, 56, 255),     # Dark slate scale (#342E38)
    's': (86, 78, 92, 255),     # Highlight scale (#564E5C)
    
    # Glass Phial Reflections
    'c': (140, 168, 182, 210),  # Glass tint (#8CA8B6)
    'C': (205, 230, 242, 240),  # Bright glass reflection (#CDE6F2)
}

# -------------------------------------------------------------
# OPTION 1: The Dragonforge Ampoule (Ice & Fire Evolution)
# Ornate ancient glass phial with gold filigree stopper & glowing blood
# -------------------------------------------------------------
GRID_OPT1 = [
    "      KyyK      ", # 0: Gold stopper finial
    "     KgYYgK     ", # 1: Gold stopper body
    "      KgGg      ", # 2: Stopper neck
    "     KggggK     ", # 3: Brass bottle ring
    "    KCCcCcCK    ", # 4: Glass shoulder highlight
    "   KcW654321cK  ", # 5: Upper phial chamber
    "  KcCW65443211cK", # 6: Glass body with liquid
    "  KcW6543Y3211cK", # 7: Suspended golden ember 'Y'
    "  Kc6544332111cK", # 8: Deep rich blood
    "  Kc5432y21111cK", # 9: Second golden ember 'y'
    "  Kc4322111124cK", # 10: Translucent backscatter rim
    "   Kc21111123cK ", # 11: Lower base taper
    "   KcccccccccK  ", # 12: Thick glass bottle bottom
    "    KKKKKKKKK   ", # 13: Bottle base
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2: The Primordial Blood Drop (Pure Viscous Droplet)
# Organic high-detail volumetric blood tear with rich ruby shading & embers
# -------------------------------------------------------------
GRID_OPT2 = [
    "       KK       ", # 0: Droplet tip
    "      K65K      ", # 1: Apex
    "     K7651K     ", # 2: Taper
    "    KW65421K    ", # 3: Specular glint begins
    "   KW7654321K   ", # 4: Expanding curve
    "  KW765432211K  ", # 5: Core width
    "  KW6543Y22111K ", # 6: Suspended draconic ember 'Y'
    "  K75443221111K ", # 7: Deep blood volume
    "  K65432y11111K ", # 8: Draconic ember 'y'
    "  K54321111114K ", # 9: Lower curve
    "   K4321111125K ", # 10: Ambient backscatter rim '25'
    "   K321111124K  ", # 11: Base curve
    "    K2111124K   ", # 12: Bottom contour
    "     KK224KK    ", # 13: Rounded bottom
    "       KKK      ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 3: The Coagulated Draconic Heart-Gem (Faceted Crystal Tear)
# Sharp multi-faceted crystallized blood diamond
# -------------------------------------------------------------
GRID_OPT3 = [
    "       KK       ", # 0: Crystal tip
    "      KW5K      ", # 1: Facet tip
    "     KW752K     ", # 2: Upper facets
    "    KW76532K    ", # 3: Expanding facets
    "   KW7644321K   ", # 4: Mid-tier facet break
    "  KKWW654321KK  ", # 5: Facet belt
    "  K7W65443211K  ", # 6: Core facet plate
    "  K6544554211K  ", # 7: Central crystal table
    "  K5435665311K  ", # 8: Lower internal refractions
    "  K4324554211K  ", # 9: Facet boundary
    "   K32344311K   ", # 10: Lower taper
    "   K21233211K   ", # 11: Bottom pavilion
    "    K112211K    ", # 12: Base facets
    "     KK11KK     ", # 13: Culet tip
    "       KK       ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 4: The Wyrm-Talon Relic (Dragon Claws Cradling Blood)
# Stage 5 black dragon claws securely clutching the glowing blood orb
# -------------------------------------------------------------
GRID_OPT4 = [
    "      KssK      ", # 0: Talon tips
    "     KsDDsK     ", # 1: Claw arches
    "    KsDd dDsK   ", # 2: Dragon claws grasping
    "   KsDkKKkDssK  ", # 3: Gold band mounts
    "   KsdKWWKdsdK  ", # 4: Blood orb apex in talons
    "   KdKW654WdKK  ", # 5: Glowing blood orb
    "   KK7654321KK  ", # 6: Blood core
    "   K7654Y3211K  ", # 7: Suspended ember 'Y'
    "   K654322111K  ", # 8: Viscous crimson
    "   Ksd42y11dsK  ", # 9: Lower claw tips clasping
    "   KsDd1111dDsK ", # 10: Lower claw armature
    "    KsDdggdDsK  ", # 11: Brass claw ferrule
    "     KsDYYDsK   ", # 12: Golden talisman mount
    "      KKGGKK    ", # 13: Bottom ring
    "        KK      ", # 14
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
        "opt1_dragonforge_ampoule": GRID_OPT1,
        "opt2_primordial_droplet": GRID_OPT2,
        "opt3_faceted_heart_gem": GRID_OPT3,
        "opt4_wyrm_talon_relic": GRID_OPT4,
    }
    
    for key, grid in variations.items():
        assert len(grid) == 16, f"{key} row count != 16"
        for y, r in enumerate(grid):
            assert len(r) == 16, f"{key} row {y} len {len(r)} != 16: '{r}'"
        
        img = render_sprite(grid, PALETTE)
        p16 = os.path.join(out_dir, f"{key}_16.png")
        p256 = os.path.join(out_dir, f"{key}_256.png")
        img.save(p16)
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(p256)
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        print(f"Generated: {key}")

if __name__ == "__main__":
    main()
