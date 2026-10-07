import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (18, 4, 6, 255),       # Darkest silhouette outline (#120406)
    'k': (35, 10, 16, 255),     # Deep blood outline (#230A10)
    
    # Blood Red Ramp
    '1': (48, 7, 14, 255),      # Deep coagulated burgundy (#30070E)
    '2': (82, 11, 22, 255),     # Dark blood (#520B16)
    '3': (126, 16, 34, 255),    # Rich crimson midtone (#7E1022)
    '4': (176, 22, 48, 255),    # Pure dragon blood (#B01630)
    '5': (224, 32, 60, 255),    # Vivid scarlet (#E0203C)
    '6': (250, 68, 94, 255),    # Fiery bright blood (#FA445E)
    '7': (255, 138, 156, 255),  # Soft pink specular (#FF8A9C)
    'W': (255, 238, 242, 255),  # Pure white specular glint (#FFEEF2)
    
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
# Symmetrical ornate glass phial with gold stopper & boiling blood
# -------------------------------------------------------------
GRID_OPT1 = [
    "      KyyK      ", # 0: Golden stopper crest (width 4, 6sp)
    "     KyYYyK     ", # 1: Stopper cap (width 6, 5sp)
    "      KgGg      ", # 2: Stopper plug (width 4, 6sp)
    "     KgYYgK     ", # 3: Golden bottle collar (width 6, 5sp)
    "   KKCCCCCCKK   ", # 4: Glass shoulder (width 10, 3sp)
    "  KcW6543211cK  ", # 5: Upper phial (width 12, 2sp)
    "  KcWW654321cK  ", # 6: Specular glare + rich blood (width 12, 2sp)
    "  Kc76543Y21cK  ", # 7: Suspended ember 'Y' (width 12, 2sp)
    "  Kc65432211cK  ", # 8: Deep blood volume (width 12, 2sp)
    "  Kc5432y211cK  ", # 9: Suspended ember 'y' (width 12, 2sp)
    "  Kc43221112cK  ", # 10: Translucent backscatter rim (width 12, 2sp)
    "   Kc321111cK   ", # 11: Base curve (width 10, 3sp)
    "   KccccccccK   ", # 12: Thick glass base (width 10, 3sp)
    "    KKKKKKKK    ", # 13: Bottle base rim (width 8, 4sp)
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2: The Primordial Blood Drop (Pure Volumetric Teardrop)
# Clean organic teardrop with rich ruby shading & draconic embers
# -------------------------------------------------------------
GRID_OPT2 = [
    "       KK       ", # 0: Droplet tip (width 2, 7sp)
    "      K65K      ", # 1: Apex (width 4, 6sp)
    "     K7651K     ", # 2: Taper (width 6, 5sp)
    "    KW65421K    ", # 3: Specular glint begins (width 8, 4sp)
    "   KW7654321K   ", # 4: Expanding curve (width 10, 3sp)
    "  KW765432211K  ", # 5: Core width (width 12, 2sp)
    "  KW6543Y2211K  ", # 6: Suspended draconic ember 'Y' (width 12, 2sp)
    "  K7544322111K  ", # 7: Deep blood volume (width 12, 2sp)
    "  K65432y1111K  ", # 8: Draconic ember 'y' (width 12, 2sp)
    "  K5432111114K  ", # 9: Lower curve (width 12, 2sp)
    "   K43211112K   ", # 10: Ambient backscatter rim (width 10, 3sp)
    "   K32111124K   ", # 11: Base curve (width 10, 3sp)
    "    K211124K    ", # 12: Bottom contour (width 8, 4sp)
    "     KK24KK     ", # 13: Rounded bottom (width 6, 5sp)
    "       KK       ", # 14: Bottom tip (width 2, 7sp)
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 3: The Coagulated Draconic Heart-Gem (Faceted Blood Diamond)
# Geometric multi-faceted crystal tear / ruby jewel
# -------------------------------------------------------------
GRID_OPT3 = [
    "       KK       ", # 0: Crystal tip (width 2, 7sp)
    "      KW5K      ", # 1: Facet tip (width 4, 6sp)
    "     KW752K     ", # 2: Upper facets (width 6, 5sp)
    "    KW76532K    ", # 3: Expanding facets (width 8, 4sp)
    "   KW7644321K   ", # 4: Mid-tier facet break (width 10, 3sp)
    "  KKWW654321KK  ", # 5: Facet belt (width 12, 2sp)
    "  K7W65443211K  ", # 6: Core facet plate (width 12, 2sp)
    "  K6544554211K  ", # 7: Central crystal table (width 12, 2sp)
    "  K5435665311K  ", # 8: Lower internal refractions (width 12, 2sp)
    "  K4324554211K  ", # 9: Facet boundary (width 12, 2sp)
    "   K32344311K   ", # 10: Lower taper (width 10, 3sp)
    "   K21233211K   ", # 11: Bottom pavilion (width 10, 3sp)
    "    K112211K    ", # 12: Base facets (width 8, 4sp)
    "     KK11KK     ", # 13: Culet tip (width 6, 5sp)
    "       KK       ", # 14: Culet point (width 2, 7sp)
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 4: The Wyrm-Talon Relic (Dragon Claws Cradling Blood)
# Stage 5 black dragon claws securely clutching the glowing blood orb
# -------------------------------------------------------------
GRID_OPT4 = [
    "      KssK      ", # 0: Talon tips (width 4, 6sp)
    "     KsDDsK     ", # 1: Claw arches (width 6, 5sp)
    "    KsD  DsK    ", # 2: Dragon claws grasping (width 8, 4sp)
    "   KsDkKKkDsK   ", # 3: Gold band mounts (width 10, 3sp)
    "   KsdKWWKdsK   ", # 4: Blood orb apex in talons (width 10, 3sp)
    "  KdKW6544WdKK  ", # 5: Glowing blood orb (width 12, 2sp)
    "  KK76543211KK  ", # 6: Blood core (width 12, 2sp)
    "  K7654Y32111K  ", # 7: Suspended ember 'Y' (width 12, 2sp)
    "  K6543221111K  ", # 8: Viscous crimson (width 12, 2sp)
    "  Ksd42y111dsK  ", # 9: Lower claw tips clasping (width 12, 2sp)
    "   KsD1111DsK   ", # 10: Lower claw armature (width 10, 3sp)
    "    KsDggDsK    ", # 11: Brass claw ferrule (width 8, 4sp)
    "     KsYYsK     ", # 12: Golden talisman mount (width 6, 5sp)
    "      KKKK      ", # 13: Bottom ring (width 4, 6sp)
    "       KK       ", # 14: Base finial (width 2, 7sp)
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

def verify_and_generate():
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
            # Verify silhouette centering: leading spaces must equal trailing spaces if not empty
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
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    verify_and_generate()
