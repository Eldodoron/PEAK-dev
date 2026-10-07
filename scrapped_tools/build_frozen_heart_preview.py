import os
import base64
from PIL import Image

PREVIEW_DIR = r"scrapped_tools\preview_frozen_heart"
HTML_OUT = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405\frozen_heart_preview.html"

def b64_img(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Images
crooked_old = b64_img(os.path.join(PREVIEW_DIR, "candidate_1_faceted_gem_256.png"))
ref_mowzie = b64_img(os.path.join(PREVIEW_DIR, "mowzie_icecrystal_256.png"))

cands = [
    {
        "id": "a1",
        "name": "Revision A1: Balanced Gem Cut",
        "subtitle": "100% Symmetrical • Dual Specular Glint",
        "desc": "Perfect bilateral silhouette. Primary glint on left lobe, secondary specular shine on right lobe to keep visual weight upright and balanced.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_balanced_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_balanced_16.png")),
        "rec": True
    },
    {
        "id": "a2",
        "name": "Revision A2: Directional Gem Cut",
        "subtitle": "100% Symmetrical • Top-Left Light",
        "desc": "Bilateral silhouette with traditional isometric top-left lighting and darker right-hand shadow facet.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_directional_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_directional_16.png")),
        "rec": False
    },
    {
        "id": "a3",
        "name": "Revision A3: Luminous Star Core",
        "subtitle": "100% Symmetrical • Glowing Chamber",
        "desc": "Features a radiant white & electric cyan star gem at the center of the heart, framed by crystalline facet walls.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_luminous_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_luminous_16.png")),
        "rec": False
    },
    {
        "id": "a4",
        "name": "Revision A4: Slender Icicle Apex",
        "subtitle": "100% Symmetrical • Needle Tip",
        "desc": "Balanced lighting with a 1-pixel extended vertical drop at the bottom tip for an icicle drip aesthetic.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_needle_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt_a_fixed_needle_16.png")),
        "rec": False
    }
]

cards_html = ""
for c in cands:
    badge = '<span class="px-1.5 py-0.5 text-[10px] font-bold rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Recommended</span>' if c['rec'] else ''
    cards_html += f"""
    <div class="bg-slate-900/90 border border-slate-800 hover:border-cyan-400/60 rounded-xl p-3 flex flex-col justify-between transition-all">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-bold text-slate-100 text-xs">{c['name']}</span>
          {badge}
        </div>
        <p class="text-[11px] text-cyan-400 font-medium mb-2">{c['subtitle']}</p>
        
        <!-- Sprite Previews -->
        <div class="bg-slate-950/80 rounded-lg p-2 border border-slate-800/80 flex items-center justify-around mb-2">
          <div class="text-center">
            <div class="text-[10px] text-slate-500 uppercase tracking-wider mb-1">16× Zoom</div>
            <img src="{c['img_256']}" class="w-16 h-16 pixelated mx-auto drop-shadow-[0_2px_8px_rgba(57,199,236,0.3)]" />
          </div>
          <div class="text-center">
            <div class="text-[10px] text-slate-500 uppercase tracking-wider mb-1">1× Actual</div>
            <div class="w-16 h-16 flex items-center justify-center bg-slate-900/60 rounded border border-slate-800/60">
              <img src="{c['img_16']}" class="w-4 h-4 pixelated drop-shadow-[0_2px_4px_rgba(57,199,236,0.5)]" />
            </div>
          </div>
        </div>

        <p class="text-[11px] text-slate-400 leading-snug">{c['desc']}</p>
      </div>
      <div class="mt-2.5 pt-2 border-t border-slate-800/60 flex items-center justify-between text-[10px] text-slate-400">
        <span class="text-emerald-400 font-mono font-semibold">Bilateral Sym: OK</span>
        <span class="text-slate-500">Mowzie 6-Color</span>
      </div>
    </div>
    """

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Frozen Heart Core — Symmetrical Fix</title>
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
          <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Option A Symmetry Fix</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-slate-800 text-slate-300">Frostmaw (Mowzie's Mobs)</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Fixed Axis Alignment</span>
        </div>
        <h2 class="text-base font-black text-white tracking-tight">Option A &bull; Straightened & Symmetrical Variations</h2>
      </div>

      <!-- Before & After Comparison -->
      <div class="flex items-center gap-2 bg-slate-900 border border-slate-800 rounded-lg p-1.5">
        <div class="text-center px-1">
          <div class="text-[9px] text-red-400 font-semibold">Crooked Draft</div>
          <img src="{crooked_old}" class="w-8 h-8 pixelated mx-auto opacity-70" />
        </div>
        <div class="h-6 w-px bg-slate-800"></div>
        <div class="text-center px-1">
          <div class="text-[9px] text-cyan-400 font-semibold">Mowzie Ref</div>
          <img src="{ref_mowzie}" class="w-8 h-8 pixelated mx-auto" />
        </div>
      </div>
    </div>

    <!-- Candidate Cards Grid -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5">
      {cards_html}
    </div>

    <!-- Symmetry Note -->
    <div class="bg-slate-900/60 border border-slate-800 rounded-lg px-3 py-1.5 flex items-center justify-between text-[11px]">
      <span class="text-slate-400">
        <strong class="text-emerald-400 font-semibold">Fix Applied:</strong> Symmetrical outline mask (mirror axis between x=7 and x=8). Bottom tip centered precisely at (x=7, x=8).
      </span>
      <span class="text-cyan-400 font-mono text-[10px]">16&times;16 RGBA</span>
    </div>

  </div>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated HTML preview at {HTML_OUT}")
