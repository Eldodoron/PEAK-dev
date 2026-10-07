import os
import base64
from PIL import Image

PREVIEW_DIR = r"scrapped_tools\preview_void_resonator"
OLD_SPRITE = r"minecraft\kubejs\assets\kubejs\textures\item\void_resonator.png"
USER_REF = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405\.user_uploaded\media_1791231893698.png"
HTML_OUT = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405\void_resonator_preview.html"

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
        "id": "opt1",
        "name": "Option 1: Faithful Resonant Plaque",
        "subtitle": "Direct 1:1 Translation • Concentric Violet Field",
        "desc": "Deep purple frame encasing concentric stepped indigo, periwinkle, and pale lavender layers with the glowing white tuning glyph.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt1_faithful_plaque_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt1_faithful_plaque_16.png")),
        "rec": True
    },
    {
        "id": "opt2",
        "name": "Option 2: Void Rift Matrix",
        "subtitle": "Cyan Corner Sparks • Dimensional Nodes",
        "desc": "The faithful purple plaque upgraded with luminous cyan energy emitters in the 4 corners, capturing the turquoise void rift from your background.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt2_cyan_rift_matrix_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt2_cyan_rift_matrix_16.png")),
        "rec": False
    },
    {
        "id": "opt3",
        "name": "Option 3: Directional Shaded Relic",
        "subtitle": "Brushed Top-Left Bevel • Deep Shadow",
        "desc": "Subtle isometric lighting across the purple frame with a lighter periwinkle bevel on the top-left and deep shadow on the bottom-right.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt3_directional_relic_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt3_directional_relic_16.png")),
        "rec": False
    },
    {
        "id": "opt4",
        "name": "Option 4: Frequency Tine Core",
        "subtitle": "Waisted Core • Specular Tine Tips",
        "desc": "Pronounced hourglass waist on the central resonant bridge, featuring specular highlights on the 4 vertical tuning tines.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt4_tine_frequency_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt4_tine_frequency_16.png")),
        "rec": False
    }
]

ref_user_b64 = b64_img(ref_pill_path)
ref_old_b64 = b64_img(old_256_path)

cards_html = ""
for c in cands:
    badge = '<span class="px-1.5 py-0.5 text-[10px] font-bold rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">Recommended</span>' if c['rec'] else ''
    cards_html += f"""
    <div class="bg-slate-900/90 border border-slate-800 hover:border-purple-400/60 rounded-xl p-3 flex flex-col justify-between transition-all">
      <div>
        <div class="flex items-center justify-between mb-1">
          <span class="font-bold text-slate-100 text-xs">{c['name']}</span>
          {badge}
        </div>
        <p class="text-[11px] text-purple-400 font-medium mb-2">{c['subtitle']}</p>
        
        <!-- Sprite Previews -->
        <div class="bg-slate-950/80 rounded-lg p-2 border border-slate-800/80 flex items-center justify-around mb-2">
          <div class="text-center">
            <div class="text-[10px] text-slate-500 uppercase tracking-wider mb-1">16× Zoom</div>
            <img src="{c['img_256']}" class="w-16 h-16 pixelated mx-auto drop-shadow-[0_2px_8px_rgba(128,96,240,0.35)]" />
          </div>
          <div class="text-center">
            <div class="text-[10px] text-slate-500 uppercase tracking-wider mb-1">1× Actual</div>
            <div class="w-16 h-16 flex items-center justify-center bg-slate-900/60 rounded border border-slate-800/60">
              <img src="{c['img_16']}" class="w-4 h-4 pixelated drop-shadow-[0_2px_4px_rgba(128,96,240,0.5)]" />
            </div>
          </div>
        </div>

        <p class="text-[11px] text-slate-400 leading-snug">{c['desc']}</p>
      </div>
      <div class="mt-2.5 pt-2 border-t border-slate-800/60 flex items-center justify-between text-[10px] text-slate-400">
        <span class="text-purple-400 font-mono">16×16 RGBA</span>
        <span class="text-emerald-400 font-semibold">Bilateral Sym: OK</span>
      </div>
    </div>
    """

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Void Resonator Candidates</title>
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
          <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">Boss Drop #3</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-slate-800 text-slate-300">Ender Guardian &bull; Void Worm</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">AE2 ME Controller Crafting</span>
        </div>
        <h2 class="text-base font-black text-white tracking-tight">Void Resonator &bull; Sprite Candidates</h2>
      </div>

      <!-- References -->
      <div class="flex items-center gap-2 bg-slate-900 border border-slate-800 rounded-lg p-1.5">
        <div class="text-center px-1">
          <div class="text-[9px] text-red-400 font-semibold">Old Placeholder</div>
          <img src="{ref_old_b64}" class="w-8 h-8 pixelated mx-auto opacity-70" />
        </div>
        <div class="h-6 w-px bg-slate-800"></div>
        <div class="text-center px-1">
          <div class="text-[9px] text-purple-400 font-semibold">Your Reference</div>
          <img src="{ref_user_b64}" class="w-8 h-8 rounded mx-auto object-cover" />
        </div>
      </div>
    </div>

    <!-- Candidate Cards Grid -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5">
      {cards_html}
    </div>

    <!-- Palette Swatches -->
    <div class="bg-slate-900/60 border border-slate-800 rounded-lg px-3 py-1.5 flex items-center justify-between text-[11px]">
      <span class="text-slate-400 font-medium">Sampled Palette (Void Violet &amp; Resonant White):</span>
      <div class="flex items-center gap-2">
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#5040B0"></div><span class="text-slate-400 font-mono text-[10px]">#5040B0</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#6060D0"></div><span class="text-slate-400 font-mono text-[10px]">#6060D0</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#90A8F8"></div><span class="text-slate-400 font-mono text-[10px]">#90A8F8</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#D0D6FA"></div><span class="text-slate-400 font-mono text-[10px]">#D0D6FA</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#FFFFFF"></div><span class="text-slate-400 font-mono text-[10px]">#FFFFFF</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#20F8F8"></div><span class="text-slate-400 font-mono text-[10px]">#20F8F8</span></div>
      </div>
    </div>

  </div>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Generated HTML preview at {HTML_OUT}")
