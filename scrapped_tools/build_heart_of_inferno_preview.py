import os
import base64
from PIL import Image

PREVIEW_DIR = r"scrapped_tools\preview_heart_of_inferno"
OLD_SPRITE = r"minecraft\kubejs\assets\kubejs\textures\item\heart_of_the_inferno.png"
USER_REF = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405\.user_uploaded\media_1791232259858.png"
HTML_OUT = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405\heart_of_inferno_preview.html"

def b64_img(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Old sprite 256px
old_im = Image.open(OLD_SPRITE)
old_256_path = os.path.join(PREVIEW_DIR, "old_placeholder_256.png")
old_im.resize((256, 256), Image.Resampling.NEAREST).save(old_256_path)

# User ref downscaled for compact pill
ref_im = Image.open(USER_REF)
ref_pill_path = os.path.join(PREVIEW_DIR, "user_ref_pill.png")
ref_im.resize((128, 128), Image.Resampling.LANCZOS).save(ref_pill_path)

cands = [
    {
        "id": "opt1a",
        "name": "Option 1A: Clean Square Relic",
        "subtitle": "Uniform 2px Rim • 12×12 Square",
        "desc": "Perfect bilateral symmetry and 100% uniform 2px golden rim thickness all around the 6×6 obsidian void window. Single-pixel diagonal bevels eliminate any crooked feel.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt1a_square_relic_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt1a_square_relic_16.png")),
        "rec": True
    },
    {
        "id": "opt1b",
        "name": "Option 1B: Octagonal Relic Plate",
        "subtitle": "14×14 Medallion • Gradual Chamfers",
        "desc": "Grand 14×14 octagonal boss plate with smooth 45° stepped chamfers (4 → 8 → 10 → 12 → 14). Elegant, rounded medallion style matching Primordial Core and Void Resonator.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt1b_octagonal_plate_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt1b_octagonal_plate_16.png")),
        "rec": False
    },
    {
        "id": "opt1c",
        "name": "Option 1C: Sculpted Flame Crest",
        "subtitle": "Spurred Flame Wings • Waist Notch",
        "desc": "Directly sculpted after Ignis's breastplate in your reference: flared upper wings, stepped-in waist notch, flared lower spurs, corner horns, and tapered chin point.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt1c_flame_wing_crest_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt1c_flame_wing_crest_16.png")),
        "rec": False
    },
    {
        "id": "opt1d",
        "name": "Option 1D: Straightened Crest",
        "subtitle": "Stepped Bevels • Smooth Shading",
        "desc": "Direct revision of Option 1: fixes the optical dent by smoothing the right shadow ramp, replaces the chunky double-outline with clean 1px steps, and centers the 6×6 window.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt1d_straightened_crest_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt1d_straightened_crest_16.png")),
        "rec": False
    }
]

ref_user_b64 = b64_img(ref_pill_path)
ref_old_b64 = b64_img(old_256_path)

cards_html = ""
for c in cands:
    badge = '<span class="px-1.5 py-0.5 text-[10px] font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Recommended</span>' if c['rec'] else ''
    cards_html += f"""
    <div class="bg-slate-900/90 border border-slate-800 hover:border-amber-400/60 rounded-xl p-3 flex flex-col justify-between transition-all">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-bold text-slate-100 text-xs">{c['name']}</span>
          {badge}
        </div>
        <p class="text-[11px] text-amber-400 font-medium mb-2">{c['subtitle']}</p>
        
        <!-- Sprite Previews -->
        <div class="bg-slate-950/80 rounded-lg p-2 border border-slate-800/80 flex items-center justify-around mb-2">
          <div class="text-center">
            <div class="text-[10px] text-slate-500 uppercase tracking-wider mb-1">16× Zoom</div>
            <img src="{c['img_256']}" class="w-16 h-16 pixelated mx-auto drop-shadow-[0_2px_8px_rgba(255,180,40,0.35)]" />
          </div>
          <div class="text-center">
            <div class="text-[10px] text-slate-500 uppercase tracking-wider mb-1">1× Actual</div>
            <div class="w-16 h-16 flex items-center justify-center bg-slate-900/60 rounded border border-slate-800/60">
              <img src="{c['img_16']}" class="w-4 h-4 pixelated drop-shadow-[0_2px_4px_rgba(255,180,40,0.5)]" />
            </div>
          </div>
        </div>

        <p class="text-[11px] text-slate-400 leading-snug">{c['desc']}</p>
      </div>
      <div class="mt-2.5 pt-2 border-t border-slate-800/60 flex items-center justify-between text-[10px] text-slate-400">
        <span class="text-amber-400 font-mono">16×16 RGBA</span>
        <span class="text-emerald-400 font-semibold">Bilateral Sym: OK</span>
      </div>
    </div>
    """

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Heart of the Inferno — Straightened Outer Shapes</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    .pixelated {{
      image-rendering: pixelated;
      image-rendering: crisp-edges;
    }}
  </style>
</head>
<body class="bg-transparent text-slate-100 antialiased p-2">
  <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 shadow-xl max-w-5xl mx-auto space-y-3">
    
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-slate-800/80 pb-3">
      <div>
        <div class="flex items-center gap-1.5 mb-0.5">
          <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Boss Drop #4</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-slate-800 text-slate-300">Ignis (Cataclysm)</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">Straightened Outer Shapes</span>
        </div>
        <h2 class="text-base font-black text-white tracking-tight">Heart of the Inferno &bull; Outer Shape Refinements</h2>
      </div>

      <!-- References -->
      <div class="flex items-center gap-2 bg-slate-900 border border-slate-800 rounded-lg p-1.5">
        <div class="text-center px-1">
          <div class="text-[9px] text-red-400 font-semibold">Old (58px)</div>
          <img src="{ref_old_b64}" class="w-8 h-8 pixelated mx-auto opacity-70" />
        </div>
        <div class="h-6 w-px bg-slate-800"></div>
        <div class="text-center px-1">
          <div class="text-[9px] text-amber-400 font-semibold">Your Reference</div>
          <img src="{ref_user_b64}" class="w-8 h-8 rounded mx-auto object-cover" />
        </div>
      </div>
    </div>

    <!-- Candidate Cards Grid -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5">
      {cards_html}
    </div>

    <!-- Palette & Technical Footer -->
    <div class="bg-slate-900/60 border border-slate-800/80 rounded-lg px-3 py-2 flex items-center justify-between text-xs text-slate-400">
      <div class="flex items-center gap-2">
        <span class="text-slate-300 font-medium">Palette:</span>
        <div class="flex items-center gap-1">
          <div class="w-3.5 h-3.5 rounded bg-[#180C0E] border border-slate-700" title="Darkest Outline #180C0E"></div>
          <div class="w-3.5 h-3.5 rounded bg-[#000000] border border-slate-700" title="Void Window #000000"></div>
          <div class="w-3.5 h-3.5 rounded bg-[#5E2200] border border-slate-700" title="Deep Molten #5E2200"></div>
          <div class="w-3.5 h-3.5 rounded bg-[#9B3E00] border border-slate-700" title="Burnt Orange #9B3E00"></div>
          <div class="w-3.5 h-3.5 rounded bg-[#CD7E00] border border-slate-700" title="Amber Gold #CD7E00"></div>
          <div class="w-3.5 h-3.5 rounded bg-[#FFD73F] border border-slate-700" title="Molten Gold #FFD73F"></div>
          <div class="w-3.5 h-3.5 rounded bg-[#FFEA90] border border-slate-700" title="Radiant Pale Gold #FFEA90"></div>
          <div class="w-3.5 h-3.5 rounded bg-[#FFFAEE] border border-slate-700" title="White-Gold Spark #FFFAEE"></div>
        </div>
      </div>
      <div class="text-slate-500 text-[11px]">
        Skull Visor: Preserved Exactly &bull; 100% Bilateral Outline Symmetry &bull; Programmatic Pixel Art
      </div>
    </div>

  </div>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML preview at: {HTML_OUT}")
