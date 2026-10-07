import os
import shutil
from PIL import Image

# -------------------------------------------------------------------------
# PALETTE DEFINITION
# Combining Cataclysm Leviathan Purple + Sunken Slate + Deep Trench Algae
# -------------------------------------------------------------------------
PALETTE = {
    ' ': (0, 0, 0, 0),
    # Outline & Deep Void
    'k': (12, 8, 16, 255),        # Deepest void trench outline (#0C0810)
    'K': (21, 14, 27, 255),       # Obsidian abyssal carapace outline (#150E1B)
    
    # Leviathan Abyssal Violet Flesh & Muscle
    'W': (229, 230, 242, 255),    # White-lavender core glint / spark (#E5E6F2)
    'Y': (179, 130, 255, 255),    # Luminous radiant violet (#B382FF)
    'P': (138, 62, 255, 255),     # Vibrant abyssal purple (#8A3EFF)
    'V': (101, 0, 255, 255),      # Electric deep violet (#6500FF)
    'v': (95, 18, 211, 255),      # Midtone abyssal purple (#5F12D3)
    'D': (70, 19, 147, 255),      # Deep violet shadow (#461393)
    'd': (52, 14, 111, 255),      # Abyssal trench shadow (#340E6F)
    'B': (33, 22, 43, 255),       # Dark violet carapace tissue (#21162B)
    
    # Sunken Slate / Chitin Bone Plates (like Warden Heart rib plates)
    's': (173, 175, 203, 255),    # Pale sunken slate glint (#ADAFCB)
    'S': (122, 125, 161, 255),    # Sunken slate midtone (#7A7DA1)
    'Z': (67, 45, 86, 255),       # Dark slate/carapace shadow (#432D56)
    
    # Deep Ocean Trench Algae & Sea Moss
    'l': (150, 237, 181, 255),    # Bright bioluminescent algae spore (#96EDB5)
    'L': (98, 201, 135, 255),     # Lush abyssal algae highlight (#62C987)
    'A': (61, 148, 93, 255),      # Deep trench sea-moss green (#3D945D)
    'G': (39, 99, 65, 255),       # Dark kelp midtone (#276341)
    'g': (22, 59, 41, 255),       # Deep trench kelp shadow (#163B29)
}

# -------------------------------------------------------------------------
# VARIATION 1: Sunken Leviathan Heart (Balanced Algae Creep)
# Faithful Warden heart anatomy with Leviathan purple muscle, sunken slate
# bone ribs, white-violet core, and natural algae creeping on apex & cleft
# -------------------------------------------------------------------------
GRID_1_SUNKEN = [
    "                ", # 0
    "     KKK   KK   ", # 1: Dual upper lobes with deep cleft
    "   KKdPdK KdPdK ", # 2: Lobe peaks
    "  KKdVPVdKKvPVdK", # 3: Ventricles flare out
    "  KdVVPPdKKSsPZK", # 4: Upper muscle chambers + right slate plate start
    "  KdZssSZKKSSsZK", # 5: Left slate bone plate + right slate plate
    "  KkZSsSdKSssSZK", # 6: Chitin rib plates curving over heart
    "  KKdZZdKdSsSZk ", # 7: Central muscle septum
    "  KdZddkWdZddk  ", # 8: White-lavender core spark (W) at center!
    "   KdPdKKKdPdK  ", # 9: Lower chambers + cleft
    "   KdZZdKKGAdK  ", # 10: Slate on left, algae sprout (GA) on right
    "    KdvdKGLAdK  ", # 11: Lush algae frond (GLA) growing on right edge
    "    KdZSsKKgK   ", # 12: Slate plate + dark kelp root
    "     KkZdGLK    ", # 13: Algae draping across bottom apex (GL)
    "      KkgK      ", # 14: Kelp tendril tip at apex
    "       KK       "  # 15: Heart tip
]

# -------------------------------------------------------------------------
# VARIATION 2: Abyssal Kelp-Wrapped Heart (Rich Ocean Algae Growth)
# More prominent trench algae vines wrapping around the purple heart chambers
# -------------------------------------------------------------------------
GRID_2_KELP_WRAPPED = [
    "                ", # 0
    "     KKK   KK   ", # 1: Lobe peaks
    "   KKdPdK KdPdK ", # 2: Upper lobes
    "  KKdVPVdKKvPVdK", # 3: Ventricle shoulders
    "  KdVVPPdKGAsPZK", # 4: Algae creeping on right cleft (GA)
    "  KdZssSZKGLsSZK", # 5: Algae vine (GL) wrapping over right plate
    "  KkZSsSdKGAsSZK", # 6: Kelp root line
    "  KKdZZdKdSZddk ", # 7: Central septum
    "  KdZddkWdZddk  ", # 8: White-lavender pulsating core
    "   KdPdKKKdPdK  ", # 9: Lower chambers
    "   KGLAdKKGAdK  ", # 10: Algae fronds on both left (GLA) & right (GA)
    "    KLlAKKGLAdK ", # 11: Vibrant bioluminescent algae sprout (LlA)
    "    KGAsKKgLK   ", # 12: Kelp band wrapping lower left
    "     KkZGALK    ", # 13: Kelp cluster at apex (GAL)
    "      KgLK      ", # 14: Dangling kelp leaf
    "       KK       "  # 15: Tip
]

# -------------------------------------------------------------------------
# VARIATION 3: Bioluminescent Abyssal Heart (Deep Obsidian + Spore Algae)
# Darker obsidian carapace texture with glowing electric violet veins and
# neon bioluminescent algae spores (L, l)
# -------------------------------------------------------------------------
GRID_3_BIOLUMINESCENT = [
    "                ", # 0
    "     KKK   KK   ", # 1
    "   KKdPdK KdPdK ", # 2
    "  KKdVPVdKKvPVdK", # 3
    "  KkBVVVbKKbVVBK", # 4: Dark obsidian carapace chambers with violet rifts
    "  KkVsSYVKKYsSVk", # 5: Glowing slate veins inside carapace
    "  KkVsSYVKKYsSVk", # 6: Glowing rift chambers
    "  KKbVVbKKbVVbK ", # 7: Septum
    "  KkVVdkWkVVdk  ", # 8: Central radiant core
    "   KkPPbKKbPPk  ", # 9: Lower chambers
    "   KkdZbKKGAdk  ", # 10: Algae colony starting on right
    "    KkdKKGLAdK  ", # 11: Glowing spore frond (GLA)
    "    KkSsKGllAK  ", # 12: Bioluminescent spore cluster (GllA)
    "     KkZdGLk    ", # 13: Apex algae
    "      KkgK      ", # 14: Tip tendril
    "       KK       "  # 15
]

# -------------------------------------------------------------------------
# VARIATION 4: Pristine Trench Core Heart (Subtle Creeping Algae)
# Maximum focus on the Warden heart's iconic bone plates and rich purple
# anatomy, with subtle, natural algae accents in the bottom seams
# -------------------------------------------------------------------------
GRID_4_PRISTINE = [
    "                ", # 0
    "     KKK   KK   ", # 1: Dual upper lobes
    "   KKdPdK KdPdK ", # 2: Lobe peaks
    "  KKdVPVdKKvPVdK", # 3: Shoulders
    "  KdVVPPdKKSsPZK", # 4: Upper muscle chambers
    "  KdZssSZKKSSsZK", # 5: Left bone plate + right bone plate
    "  KkZSsSdKSssSZK", # 6: Curving chitin rib plates
    "  KKdZZdKdSsSZk ", # 7: Center septum
    "  KdZddkWdZddk  ", # 8: Pulsing abyssal core (W)
    "   KdPdKKKdPdK  ", # 9: Lower ventricles
    "   KdZZdKKdZZdK ", # 10: Lower bone plates
    "    KdvdKKGLAdK ", # 11: Subtle algae creeping into right seam (GLA)
    "    KdZSsKKgAK  ", # 12: Algae in lower crevice (gA)
    "     KkZgGLK    ", # 13: Algae tuft at apex (gGL)
    "      KkGk      ", # 14: Dark kelp apex tip
    "       KK       "  # 15: Tip
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
    out_dir = r"scrapped_tools\preview_abyssal_catalyst"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt1_sunken_leviathan_heart": (GRID_1_SUNKEN, "Option 1: Sunken Leviathan Heart (Balanced Algae)"),
        "opt2_kelp_wrapped_heart": (GRID_2_KELP_WRAPPED, "Option 2: Abyssal Kelp-Wrapped Heart (Rich Algae Growth)"),
        "opt3_bioluminescent_heart": (GRID_3_BIOLUMINESCENT, "Option 3: Bioluminescent Abyssal Heart (Neon Spores)"),
        "opt4_pristine_trench_heart": (GRID_4_PRISTINE, "Option 4: Pristine Trench Heart (Subtle Creeping Algae)")
    }
    
    for key, (grid, title) in variations.items():
        assert len(grid) == 16, f"{key} row count != 16"
        for y, r in enumerate(grid):
            assert len(r) == 16, f"{key} row {y} len {len(r)} != 16: '{r}'"
        
        img = render_sprite(grid, PALETTE)
        p16 = os.path.join(out_dir, f"{key}_16.png")
        p256 = os.path.join(out_dir, f"{key}_256.png")
        img.save(p16)
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(p256)
        
        # Copy to artifact dir for markdown embedding
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        print(f"Verified & generated: {key}")

if __name__ == '__main__':
    verify_and_generate()
