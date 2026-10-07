import os
import base64
from PIL import Image

# -------------------------------------------------------------
# Palette: Mowzie's Mobs Ice Crystal Authenticity
# -------------------------------------------------------------
PALETTE = {
    ' ': (0, 0, 0, 0),          # Transparent
    'K': (7, 40, 56, 255),       # Deep glacial shadow outline (#072838)
    'D': (27, 114, 137, 255),    # Dark glacial cyan (#1B7289)
    'M': (71, 189, 218, 255),    # Crystal facet midtone (#47BDDA)
    'B': (57, 199, 236, 255),    # Vibrant electric cyan (#39C7EC)
    'G': (105, 255, 255, 255),   # Glowing frost highlight (#69FFFF)
    'W': (255, 255, 255, 255),   # Specular white reflection (#FFFFFF)
}

# -------------------------------------------------------------
# CANDIDATE 1: Glacial Heart Gem (Faceted Prismatic Cut)
# Perfectly symmetrical silhouette, diamond facet seams, top-left specular glint.
# -------------------------------------------------------------
GRID_1 = [
    "                ",
    "   KK      KK   ",
    "  KWWK    KGDK  ",
    " KWWGBKK  KBBDK ",
    " KWGGBBMKKGBBDK ",
    " KWGBBBMDMBMDDK ",
    " KGBBBMMDDBMDDK ",
    "  KBBMMDDDMDDK  ",
    "  KBBMMDDDMDDK  ",
    "   KBMMDDDDDDK  ",
    "   KBMMDDDDDDK  ",
    "    KMDDDDDDK   ",
    "     KDDDDDDK   ",
    "      KDDDDK    ",
    "       KDDK     ",
    "        KK      "
]

# -------------------------------------------------------------
# CANDIDATE 2: Frostfang Beast Core (Frostmaw Horns & Jagged Spikes)
# Distinctive frozen horns / tusks flanking the lobes with jagged ice rime.
# -------------------------------------------------------------
GRID_2 = [
    "  KK      KK    ",
    " KWWK    KGDK   ",
    " KWBGK  KGMDDK  ",
    "  KWGGKKGMBBDK  ",
    "  KWBGBBGBBMDK  ",
    " KDWBGBBMMBMDDK ",
    " KDMBBBMMMMDDDK ",
    "  KDBMMMMMDDDK  ",
    "  KDDMBMMMDDK   ",
    "   KDDMMMDDK    ",
    "   KDDMMDDDK    ",
    "    KDDMDDDK    ",
    "     KDMDDK     ",
    "      KDMDDK    ",
    "       KDDK     ",
    "        KK      "
]

# -------------------------------------------------------------
# CANDIDATE 3: Anatomical Glacial Organ (Living Ice Heart with Crystal Tubes)
# Asymmetric organic ice heart with crystal aorta & branching pulmonary veins.
# -------------------------------------------------------------
GRID_3 = [
    "   KK   KK      ",
    "  KWWK  KGGK    ",
    " KWWGBKKGMDDK   ",
    " KWGBBGKKGBBBDK ",
    " KWBGGBBMDBBBDDK",
    "  KGBBBBMDBMDDK ",
    "  KBBMGBMDMDDDDK",
    "  KBBMGBMDDDDKK ",
    "   KBMGMDDDDDK  ",
    "   KBMGMDDDDK   ",
    "    KBMMDDDDK   ",
    "    KMDDDDDK    ",
    "     KDDDDDK    ",
    "      KDDDK     ",
    "       KDDK     ",
    "        KK      "
]

# -------------------------------------------------------------
# CANDIDATE 4: Stalactite Crystal Matrix (Triple Icicle Fluting)
# Vertical crystalline fluting ending in triple dangling icicle needles.
# -------------------------------------------------------------
GRID_4 = [
    "                ",
    "  KKK    KKK    ",
    " KWWGK  KGWWK   ",
    " KWWGBKKGBWBDK  ",
    " KWGBBGMGGBBBDK ",
    " KWGBBGMGGBBBDK ",
    "  KGBBGMGGBBDK  ",
    "  KBBMMMMMBBDK  ",
    "  KBBMDMDMBBDK  ",
    "   KBMDMDMBDK   ",
    "   KBMDMDMDDK   ",
    "    KDMDMDDK    ",
    "    KD KMDDK    ",
    "    K   KMDK    ",
    "         KDK    ",
    "          K     "
]

def make_image(grid):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        row = grid[y]
        assert len(row) == 16, f"Row {y} len is {len(row)}"
        for x in range(16):
            ch = row[x]
            img.putpixel((x, y), PALETTE.get(ch, (0, 0, 0, 0)))
    return img

def render_preview():
    out_dir = r"scrapped_tools\preview_frozen_heart"
    os.makedirs(out_dir, exist_ok=True)
    
    candidates = {
        "candidate_1_faceted_gem": GRID_1,
        "candidate_2_frostfang_core": GRID_2,
        "candidate_3_anatomical_ice": GRID_3,
        "candidate_4_stalactite_matrix": GRID_4,
    }
    
    for name, grid in candidates.items():
        img = make_image(grid)
        img.save(os.path.join(out_dir, f"{name}_16.png"))
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(os.path.join(out_dir, f"{name}_256.png"))
        print(f"Generated {name}")

if __name__ == '__main__':
    render_preview()
