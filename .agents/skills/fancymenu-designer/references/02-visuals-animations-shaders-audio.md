# FancyMenu Reference 02: Visuals, Animations, Shaders, Backgrounds & Audio

## 1. Element Animator (Keyframe Timeline System)

The **Element Animator** (`element_animator`) animates the **position, size, and anchor point** of one or multiple target elements over time using keyframes.
- **Limitation**: Element Animator ONLY animates position, size, and anchor point. To animate **opacity**, **rotation**, **tilt**, or **player entity pose**, either use built-in element **Fading**, or drive those properties' text fields using **Placeholders + Variables + a Ticker** (or feed variables directly into a **GLSL Shader**).
- **Crucial Setup Rule**: For elements that slide in from off-screen, right-click the target element and disable **Stay On Screen**!

### Keyframe Editor Workflow & Shortcuts
Open via right-click on the Animator element -> **Edit Keyframes** (or **Manage Keyframes**), then attach elements via **Manage Targets -> Add Target**.

| Key / Action | Function in Keyframe Editor |
| :--- | :--- |
| `R` | Start / Stop recording mode (preview box changes color when active) |
| `T` | Pause / Resume recording |
| `K` | Insert keyframe at current timeline position (captures X, Y, Width, Height, Anchor) |
| `P` | Play / Pause animation preview (Note: looping does NOT play in editor preview; only on final target elements) |
| `Left` / `Right Arrow` | Shift selected keyframe(s) `-100ms` / `+100ms` |
| `Ctrl + Click` / `Ctrl + A` | Multi-select keyframes / Select all keyframes |
| `Distance Smoothing` button | Evenly spaces all selected keyframes by a specified millisecond interval |
| `Delete` | Remove selected keyframe(s) |
| `Ctrl + Z` / `Ctrl + Y` | Undo / Redo |

### Advanced Animator Settings
- **Offset Mode**: Applies keyframe coordinates as relative offsets (`ΔX, ΔY`) from each target element's own base position (preview is centered on a crosshair). Essential when animating a group of buttons (e.g., staggered slide-in) that live at different Y positions!
- **Timing Offsets**: Configure fixed per-target or randomized start-time offsets so multiple targets linked to a single Animator cascade smoothly instead of moving in lockstep.
- **Ignore Size / Ignore Position**: Toggle off either channel if the animator should only move elements without resizing them (or vice versa).
- **Loop Animation**: Restarts the timeline after the final keyframe on target elements.
- **Action Script Control**: Control animators dynamically with `enable_element_animator`, `disable_element_animator`, `toggle_element_animator`, and `reset_element_animator`.

---

## 2. Animated Textures: AFMA, Classic `.fma`, APNG & FFmpeg

FancyMenu accepts animated textures anywhere an **Image** input is accepted (Image elements, Image backgrounds, button textures, etc.). Store files in `<game-directory>/config/fancymenu/assets/`.

### Format Comparison
1. **AFMA (`.afma` — Recommended)**:
   - Binary, streaming, non-ZIP format with low RAM usage and high performance. Does not suffer from the 200-frame / 1000-total-frame RAM limits of legacy formats.
   - **Creation**: Cannot be packed manually; create in-game via **Menu Bar -> Tools -> AFMA Creator**.
2. **Classic FMA (`.fma` — Script-Generatable ZIP Archive)**:
   - A standard `.zip` file renamed to `.fma` where `metadata.json`, `frames/`, and optional `intro_frames/` sit **directly at the root of the ZIP** (NOT nested inside a subfolder!).
   - **Frame Naming**: Sequential zero-indexed PNGs: `frames/0.png`, `frames/1.png`, `frames/2.png`, ... (and optionally `intro_frames/0.png`, `1.png`, ... which play once before looping `frames/`).
   - **`metadata.json` Schema**:
     ```json
     {
       "loop_count": 0,
       "frame_time": 41,
       "frame_time_intro": 41,
       "custom_frame_times": {
         "0": 5000,
         "1": 5000
       },
       "custom_frame_times_intro": {}
     }
     ```
     - `loop_count`: `0` = infinite loop; `>0` = play `N` times then hold last frame.
     - `frame_time` / `frame_time_intro`: Default frame duration in milliseconds (`41` ms ≈ 24 fps, `33` ms ≈ 30 fps, `16` ms ≈ 60 fps).
     - `custom_frame_times`: Map of `"frame_index": duration_ms` overrides.
3. **APNG (`.apng`) & GIF (`.gif`)**:
   - APNG files **must** end with `.apng`, be **uncompressed**, and **non-interlaced** (in ScreenToGif: disable *Detect Unchanged Pixels*).
   - **Memory Limits for Classic FMA / APNG / GIF**: Keep each animation `<= 200 frames`, resolution `<= 1080p`, and combined frames across all loaded legacy animations `<= 1000 frames`.
4. **Extracting Video Frames with FFmpeg**:
   ```bash
   ffmpeg -i input.mp4 -vf "fps=24,scale=1280:720" frames/%d.png
   ```
   *(Note: Use `-start_number 0` with `frames/%d.png` so FFmpeg outputs `0.png, 1.png, ...` directly for `.fma` packaging!)*

---

## 3. Opacity, Fading, Rotation, Tilting & Parallax

- **Opacity & Built-in Fading (`element-opacity.md`)**:
  - Right-click element -> **Opacity -> Set** (`0.0` to `1.0`). Supports **Placeholders** for dynamic variable-driven opacity.
  - **Built-in Fade-In / Fade-Out**: Enable **Fading** in the element's right-click menu and set **Fading Speed**. The element automatically fades in on screen load or when its Loading Requirements become true, and fades out when its Loading Requirements become false!
- **2D Rotation (`rotating-elements.md`)**:
  - Drag the circular rotation grabber in the editor, or right-click -> set rotation angle via text input (supports **Placeholders** for continuous spinning/wobble via Ticker/calc!).
  - *Note*: Interactive elements (Buttons/Sliders) rotate visually only; their clickable hitbox remains in the original unrotated bounding box.
- **3D Vertical & Horizontal Tilting (`tilting-elements.md`)**:
  - Drag vertical/horizontal tilt grabbers or right-click to input tilt angles (supports **Placeholders**!).
  - *Note*: Visual-only for interactive hitboxes.
- **Mouse Parallax Effect (`parallax.md`)**:
  - Available on **Image Menu Backgrounds** and **Elements**.
  - Configure **Parallax Intensity X** (`0.0` to `1.0`), **Parallax Intensity Y** (`0.0` to `1.0`), and optional **Invert Parallax Movement**.
  - **Multi-Layer Depth Recipe**: Stack 3–4 full-screen or oversized transparent Image layers with increasing intensity (e.g., Sky/BG `0.05`, Midground hills `0.15`, Foreground particles/foliage `0.35` inverted) for a 3D parallax scene.
  - *Conflict Warning*: On Image Menu Backgrounds, disable **Slide Wide Images From Left To Right** when using Parallax.

---

## 4. GLSL Shader API (`glsl-shader-api.md`)

FancyMenu runs an internal `#version 150` OpenGL shader pipeline across **GLSL Menu Backgrounds**, **GLSL Elements**, and **GLSL Decoration Overlays**.
- **Preprocessing**: Automatically strips `#version` and `precision` lines, injects `#version 150`, `in vec2 fmUv_FancyMenu` (`[0,1]`, bottom-left origin), `#define iGlobalTime iTime`, `#define texture2D texture`, and `#define textureCube texture`.
- **Compile Modes**:
  1. `Shadertoy`: Entry point `void mainImage(out vec4 fragColor, in vec2 fragCoord)` — coordinates are automatically area-local (`gl_FragCoord.xy - fmAreaOffset`) and output alpha is automatically multiplied by `fmOpacity`.
  2. `Direct Fragment`: Entry point `void main()` — use `gl_FragCoord.xy - fmAreaOffset` and multiply alpha by `fmOpacity` manually.
  3. `Auto`: Tries compatible variants automatically.
- **5-Pass Multipass Pipeline**:
  - Optional `Buffer A`, `Buffer B`, `Buffer C`, `Buffer D` (offscreen `GL_RGBA16F` floating-point ping-pong textures, linear filtering, clamp-to-edge) + required `Image` pass.
  - Each pass can route `iChannel0..3` to `None`, `Resource 0..3` (2D textures), or `Buffer A..D` (including self-routing for previous-frame feedback!).

### Built-in Uniforms
- **Shadertoy Uniforms**:
  - `uniform vec3 iResolution;` (`widthPx, heightPx, 1.0`)
  - `uniform float iTime;`, `uniform float iTimeDelta;`, `uniform float iFrameRate;`, `uniform int iFrame;`
  - `uniform vec4 iMouse;` (`xy` = current local pixel pos; `zw` = click origin, positive while LMB held)
  - `uniform vec4 iDate;` (`year, month, day, secondsOfDay`)
  - `uniform float iSampleRate;` (`44100.0`), `uniform float iChannelTime[4];`
  - `uniform vec3 iChannelResolution[4];` (`width, height, validFlag` where `z=0.0` if unbound)
  - `uniform sampler2D iChannel0..3;`
- **FancyMenu Uniforms**:
  - Geometry/Screen: `fmAreaOffset` (`vec2`), `fmAreaSize` (`vec2`), `fmAreaPosition` (`vec2`), `fmAreaTopLeft` (`vec2`), `fmScreenSize` (`vec2`), `fmGuiScale` (`float`), `fmOpacity` (`float`).
  - Mouse/Input: `fmMouse` (`vec4(localPxX, localPxYBottom, normX, normY)`), `fmMouseDelta` (`vec2`), `fmMouseButtons` (`ivec4`), `fmMouseClickCount` (`ivec4`), `fmMouseReleaseCount` (`ivec4`), `fmMouseScroll` (`vec2`), `fmMouseScrollTotal` (`vec2`), `fmKeyEvent` (`ivec4(key, scan, mods, action)`), `fmKeyEventCount` (`int`), `fmCharEvent` (`ivec4`), `fmCharEventCount` (`int`).
  - Time/State: `fmDateParts` (`ivec4`), `fmTimeParts` (`ivec4`), `fmDayOfYear` (`int`), `fmWeekOfYear` (`int`), `fmUnixTimeSeconds` (`int`), `fmUnixTimeMilliseconds` (`int`), `fmPartialTick` (`float`), `fmGameDeltaTicks` (`float`), `fmRealtimeDeltaTicks` (`float`), `fmInWorld` (`int`), `fmIsPaused` (`int`), `fmVariableCount` (`int`).
- **Live FancyMenu Variable Uniforms (Zero-Recompile Reactivity!)**:
  - Any FancyMenu variable `<name>` (sanitized to `[A-Za-z0-9_]`, leading digit prefixed with `_`) can be declared manually in your shader as:
    - `uniform float fmVarFloat_<name>;`
    - `uniform int fmVarInt_<name>;`
    - `uniform int fmVarBool_<name>;`
    - `uniform vec2 fmVarVec2_<name>;` / `vec3 fmVarVec3_<name>;` / `vec4 fmVarVec4_<name>;` (parses space/comma/semicolon/pipe-separated numbers)
    - `uniform int fmVarExists_<name>;` (`1` if exists, `0` if removed)

---

## 5. Menu Backgrounds, Panoramas, Slideshows & Decoration Overlays

### Menu Backgrounds (`menu-backgrounds.md`)
- Types: `Vanilla`, `Image` (supports `.png`, `.jpg`, `.afma`, `.fma`, `.apng`, `.gif` + Parallax), `Slideshow`, `Cubic Panorama`, `Color (HEX)`, `Browser` (fullscreen auto-focused), `Video` (Watermedia V3 + OpenGL), and `GLSL Shader`.
- **Stacking Rule**: Multiple background types can be enabled simultaneously in one layout (and across stacked layouts by `layout_index`). FancyMenu draws a solid **black backing layer** behind the bottom-most custom background, so put an opaque background at the bottom and stack translucent shader/image/parallax layers on top.

### Cubic Panoramas (`panoramas.md`)
- Directory structure:
  ```text
  <game-directory>/config/fancymenu/panoramas/<folder_name>/
  ├── properties.txt
  ├── overlay.png          # optional vignette/overlay
  └── panorama/
      ├── panorama_0.png ... panorama_5.png   # 6 square PNGs of identical dimensions
  ```
- `properties.txt`:
  ```ini
  type = panorama

  panorama-meta {
    name = unique_panorama_id
    speed = 1.0
    fov = 85.0
    angle = 25.0
    start_rotation = 0
  }
  ```

### Slideshows (`slideshows.md`)
- Directory structure:
  ```text
  <game-directory>/config/fancymenu/slideshows/<folder_name>/
  ├── properties.txt
  ├── overlay.png          # optional
  └── images/
      ├── image_01.png     # only .png and .jpg supported (.jpeg is ignored!)
      └── image_02.png
  ```
- `properties.txt`:
  ```ini
  type = slideshow

  slideshow-meta {
    name = unique_slideshow_id
    width = 1920
    height = 1080
    x = 0
    y = 0
    duration = 5.0
    fadespeed = 12.0
    randomize = false
  }
  ```

### Decoration Overlays (`decoration-overlays.md`)
Fullscreen atmospheric layers rendered **in front of** menu elements (right-click editor background -> **Decoration Overlays**). Multiple overlays can be enabled per layout:
- **Snowfall** (with optional snow accumulation on top of buttons/surfaces!)
- **Rainfall** (with optional puddles, drips, and thunder flashes)
- **Fireflies** (configurable group count, density, size, color)
- **String Lights** (wind/flicker behavior, custom/holiday colors)
- **Leaves** (falling leaves with custom colors, wind, speed, scale, density)
- **Fireworks** (amount, explosion size, scale)
- **Confetti** (rain or mouse-click burst mode)
- **Buddy** (Tamagotchi-style virtual pet with Hunger/Happiness/Energy/Fun, ball physics, leveling 1–30, achievements, custom sprite atlas; saved in `fancymenu_data/buddy/`)
- **Browser** (interactive or passive visual overlay via `Process`/`Consume` toggles)
- **GLSL Shader** (fullscreen post/foreground shader overlay)

---

## 6. Nine-Slicing, Tiling, Templates, Global Customizations & Audio

- **Nine-Slicing & Tiling (`nine-slicing-and-tiling.md`)**:
  - **Nine-Slicing**: Keeps corners and border thicknesses fixed while stretching the center. Supported on Buttons, Sliders, Image elements, Progress Bars, Tooltips, and Global Button/Slider visuals.
  - **Tiling (`Repeat Texture`)**: Repeats seamless textures without stretching. Supported on Image elements, Image backgrounds, and Scroll-list headers/footers.
- **Button & Slider Templates (`button-slider-templates.md`)**:
  - Add a custom Button -> right-click -> **Template Settings -> Is Template: ON**, choose **Share With: Buttons** or **Sliders** (you can have 1 active Button template + 1 active Slider template per layout; invisible in-game).
  - Custom textures set on the template are **always** shared; Width, Height, X, Y, Opacity, Visibility, and Label sharing can be toggled individually.
- **Global Customizations (`global-customizations.md`)**:
  - Accessed outside the editor via **Customization -> Global Customizations**.
  - Configures **Game Intro** (video/animation before Title screen), **Seamless World Loading** (uses recent world screenshot for loading screen), **Custom Window Icon** (16x16 PNG, 32x32 PNG, macOS ICNS — **MUST contain at least 1 fully transparent pixel** to avoid the LWJGL/MC icon glitch!), **Custom Window Title**, **Default GUI Scale**, **Force Fullscreen on Launch**, Global Button/Slider textures & nine-slicing, and **Global Custom Menu Music Tracks**.
- **Audio & Music Best Practices (`background-music.md`, `fix-audio.md`, `vanilla-sounds.md`)**:
  - Global Custom Menu Music only plays when **no world is loaded** (starts after ~5s, random 1–30s delay between tracks). For in-world menus or instant playback, use an **Audio** element (place in a Universal Layout to persist across screens) + a **Music Controller** element to mute Vanilla menu/world music.
  - Vanilla sounds can be referenced via resource location, e.g., `minecraft:sounds/music/game/bromeliad.ogg`.
  - If a custom `.ogg` or `.wav` fails to play, re-encode with FFmpeg to standard Vorbis `.ogg` or **48 kHz, 16-bit PCM `.wav`**.
- **Hiding Title Screen Emerald/Diamond Glyphs (`title-screen-glyph.md`)**:
  - NeoForge/Forge update emerald on Mods button: set `versionCheck = false` in `<game-directory>/config/fml.toml` (or hide the Mods button and replace it with a custom Button using `mimicbutton`).
  - Vanilla Realms notification icon: delete the dedicated Realms icon element in a screen-specific `title_screen` layout.
