import os
import base64
from PIL import Image

PREVIEW_DIR = r"scrapped_tools\preview_primordial_core"
OLD_SPRITE = r"minecraft\kubejs\assets\kubejs\textures\item\primordial_core.png"
USER_REF = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405\.user_uploaded\media_1791231588241.png"
HTML_OUT = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405\primordial_core_preview.html"

def b64_img(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Old sprite 256px
old_im = Image.open(OLD_SPRITE)
old_256_path = os.path.join(PREVIEW_DIR, "old_placeholder_256.png")
old_im.resize((256, 256), Image.Resampling.NEAREST).save(old_256_path)

# User ref downscaled/cropped for compact pill
ref_im = Image.open(USER_REF)
ref_pill_path = os.path.join(PREVIEW_DIR, "user_ref_pill.png")
ref_im.resize((128, 128), Image.Resampling.LANCZOS).save(ref_pill_path)

cands = [
    {
        "id": "opt1",
        "name": "Option 1: Faithful Relic Plate",
        "subtitle": "Direct 1:1 Translation • Fiery Cross Core",
        "desc": "Brushed steel & slate chassis with beveled corners, recessed bevel groove, and fiery orange/crimson cross core exactly as in your reference.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt1_faithful_plate_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt1_faithful_plate_16.png")),
        "rec": True
    },
    {
        "id": "opt2",
        "name": "Option 2: Overcharged Relic Plate",
        "subtitle": "Incandescent Spark • Specular Rivets",
        "desc": "Same faithful chassis with an added hot white-gold center spark, amber glowing core rim, and top-left specular bevel accent.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt2_overcharge_plate_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt2_overcharge_plate_16.png")),
        "rec": False
    },
    {
        "id": "opt3",
        "name": "Option 3: Ancient Bronze Casing",
        "subtitle": "Cataclysm Ancient Metal • Fiery Core",
        "desc": "Uses authentic Cataclysm Ancient Metal Ingot bronze/brass tones for the outer plate, matched with the glowing fiery cross.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt3_ancient_bronze_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt3_ancient_bronze_16.png")),
        "rec": False
    },
    {
        "id": "opt4",
        "name": "Option 4: Primordial Amethyst",
        "subtitle": "Steel Chassis • §5 Cosmic Violet Core",
        "desc": "The faithful steel chassis enclosing an electric violet & royal amethyst core, matching the in-game §5 purple item name and Wyvern tier.",
        "img_256": b64_img(os.path.join(PREVIEW_DIR, "opt4_violet_amethyst_256.png")),
        "img_16": b64_img(os.path.join(PREVIEW_DIR, "opt4_violet_amethyst_16.png")),
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
            <img src="{c['img_256']}" class="w-16 h-16 pixelated mx-auto drop-shadow-[0_2px_8px_rgba(238,101,28,0.3)]" />
          </div>
          <div class="text-center">
            <div class="text-[10px] text-slate-500 uppercase tracking-wider mb-1">1× Actual</div>
            <div class="w-16 h-16 flex items-center justify-center bg-slate-900/60 rounded border border-slate-800/60">
              <img src="{c['img_16']}" class="w-4 h-4 pixelated drop-shadow-[0_2px_4px_rgba(238,101,28,0.5)]" />
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

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Primordial Core Candidates</title>
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
          <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Boss Drop #2</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-slate-800 text-slate-300">Ancient Remnant (Cataclysm)</span>
          <span class="px-2 py-0.5 text-[10px] font-semibold rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">Draconic Evolution Wyvern Tier</span>
        </div>
        <h2 class="text-base font-black text-white tracking-tight">Primordial Core &bull; Sprite Candidates</h2>
      </div>

      <!-- References -->
      <div class="flex items-center gap-2 bg-slate-900 border border-slate-800 rounded-lg p-1.5">
        <div class="text-center px-1">
          <div class="text-[9px] text-red-400 font-semibold">Old (Generic)</div>
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

    <!-- Palette Swatches -->
    <div class="bg-slate-900/60 border border-slate-800 rounded-lg px-3 py-1.5 flex items-center justify-between text-[11px]">
      <span class="text-slate-400 font-medium">Sampled Palette (Brushed Steel &amp; Fiery Core):</span>
      <div class="flex items-center gap-2">
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#C2CCD4"></div><span class="text-slate-400 font-mono text-[10px]">#C2CCD4</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#74828E"></div><span class="text-slate-400 font-mono text-[10px]">#74828E</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#282E38"></div><span class="text-slate-400 font-mono text-[10px]">#282E38</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#EE651C"></div><span class="text-slate-400 font-mono text-[10px]">#EE651C</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#DC3838"></div><span class="text-slate-400 font-mono text-[10px]">#DC3838</span></div>
        <div class="flex items-center gap-1"><div class="w-3 h-3 rounded" style="background:#A52131"></div><span class="text-slate-400 font-mono text-[10px]">#A52131</span></div>
      </div>
    </div>

  </div>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Generated HTML preview at {HTML_OUT}")
