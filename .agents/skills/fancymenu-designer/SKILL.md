---
name: fancymenu-designer
description: Master reference, architecture guide, and code generator for FancyMenu v3 (Minecraft 1.20.1 / 1.21.1 NeoForge, Forge, Fabric). Use whenever designing, generating, editing, or troubleshooting FancyMenu layouts (.txt), custom GUIs, menu animations (.hma / .fma), GLSL fragment shaders (.fsh), cubic panoramas, 9-slice textures, placeholders, variables, loading requirements, executable action blocks, event listeners, or preparing Title Screen / menu integrations with Drippy Loading Screen.
---

# FancyMenu v3 Master Designer Skill (`fancymenu-designer`)

This skill equips you with 100% mastery of **FancyMenu v3** (official documentation + source-verified 1.21.1 `.txt` serialization engine from `Keksuccino/FancyMenu`). You can both **generate ready-to-load `.txt` layout files, GLSL shaders, `.fma` animations, and pixel-art assets directly on disk** and **guide the user step-by-step through the in-game Layout Editor**.

---

## 1. Directory & Reference Map

Always consult the specialized reference files in `references/` when building or debugging specific subsystems:

| Reference File | Contents |
|---|---|
| [`references/01-elements-and-positioning.md`](references/01-elements-and-positioning.md) | Core architecture, Menu Identifiers (`title_screen`, `pause_screen`, etc.), 12 Anchor Points (`top-left`, `mid-centered`, `element`, etc.), 5 Sizing Modes (`normal`, `stretch`, `percentage`, `aspect_ratio`), all 9 Element Types (`image`, `text_v2`, `button`, `custom_button`, `splash_text`, `player_entity`, `ticker`, `shape`, `progress_bar`), Vanilla Widget (`vanilla_button`) overrides, Layering (`order`), and Universal Layout Settings (`forced_scale`, `auto_scaling`). |
| [`references/02-visuals-animations-shaders-audio.md`](references/02-visuals-animations-shaders-audio.md) | Menu Background types (`image`, `slideshow`, `animation`, `panorama`, `shader`, `solid_color`, `menu_background`), `.fma` Pack Format (`main.properties` + `intro/` + `loop/`), Cubic Panorama 6-face format (`panorama_0.png`..`panorama_5.png`), GLSL Fragment Shaders (`#version 150` / `#version 330`, `uniform float u_time; uniform vec2 u_resolution;`), Nine-Slice 9-patch `.nine_slice.json` sidecars, Audio Controllers (`music:` / `sound:`), and World Background Vignette/Blur. |
| [`references/03-actions-listeners-schedulers.md`](references/03-actions-listeners-schedulers.md) | All 30 Executable Action Types (`open_link`, `join_server`, `send_message`, `run_cmd`, `set_variable`, `reload_fancy_menu`, `play_sound`, `if-else` blocks, etc.), Event Listeners (Mouse/Keyboard/Tick/Screen lifecycle), Scheduled Tasks, Custom GUIs (`/opengui`, `allow_esc`), and Screen Overrides (`/closescreen`). |
| [`references/04-placeholders-variables-conditions.md`](references/04-placeholders-variables-conditions.md) | All 70+ Placeholders (`{"placeholder":"...","values":{...}}`) across Text, Client/Player, World/Server, System/Time, Math, Web/JSON (`json` + Jayway JsonPath + `html`), Nested Placeholders, FM Variables, and all 40+ Loading Requirements (AND/OR groups, `is_Variable_value`, `is_mod_loaded`, `is_hovered`, `is_realtime_day`, etc.). |
| [`references/05-raw-file-formats-and-storage.md`](references/05-raw-file-formats-and-storage.md) | Source-verified `PropertiesParser` grammar (`type = fancymenu_layout`), `[source:local]/config/fancymenu/assets/...` resource syntax, inline `RequirementContainer` serialization (`[loading_requirement_container_meta:...]`), inline `GenericExecutableBlock` serialization (`[executable_block:...]`), and every exact property key for every element, background, and vanilla widget. |
| [`references/06-troubleshooting-and-compat.md`](references/06-troubleshooting-and-compat.md) | Diagnosis playbook for invisible elements, deep element collisions (`deep:title_screen:forge_top`), anchor chains, `forced_scale` vs `auto_scaling`, Resource Reload hangs (`disable_resource_reload = true`), and **Drippy Loading Screen** visual handoff rules. |
| [`references/fancymenu_docs_full.txt`](references/fancymenu_docs_full.txt) | Complete, verbatim 83-page official FancyMenu v3 documentation (`docs.txt`, 10,668 lines) for full-text search or edge-case verification. |

### Examples & Helper CLI
- [`examples/annotated_title_screen_layout.txt`](examples/annotated_title_screen_layout.txt) — Complete, valid `title_screen` layout `.txt` demonstrating GLSL shader background, open/close fade animations, audio controller, hidden vanilla buttons, custom anchored buttons with `if-else` executable blocks, 3D `player_entity`, markdown `text_v2`, and `loading_requirement` blocks.
- [`examples/glsl_menu_shader_example.fsh`](examples/glsl_menu_shader_example.fsh) — Ready-to-use `#version 150` GLSL fragment shader background using `u_time` and `u_resolution`.
- [`scripts/fancymenu_helper.py`](scripts/fancymenu_helper.py) — Python CLI utility for deterministic UUID generation, layout `.txt` structural validation, `.nine_slice.json` sidecar generation, `.fma` animation `main.properties` scaffolding, and cubic panorama verification.

---

## 2. Core Workflows

### Workflow A: Generating or Editing FancyMenu Files Directly on Disk
When building or modifying a menu programmatically in a Minecraft instance (`<instance>/config/fancymenu/`):

1. **Locate or Create the Instance Directories**:
   - Layouts: `<instance>/config/fancymenu/layouts/<layout_name>.txt`
   - Assets: `<instance>/config/fancymenu/assets/` (never hardcode absolute OS paths; always reference via `[source:local]/config/fancymenu/assets/<subpath>`)
   - Custom GUIs: `<instance>/config/fancymenu/custom_gui_screens.txt`
   - Legacy `.fma` Animations: `<instance>/config/fancymenu/animation_packs/<anim_name>.fma/`
   - Variables: `<instance>/config/fancymenu/variables. immediately` (`variables.txt`)

2. **Follow Strict `.txt` Layout Serialization Rules** (see [`05-raw-file-formats-and-storage.md`](references/05-raw-file-formats-and-storage.md)):
   - **Line 1 MUST be** `type = fancymenu_layout`.
   - Top-level settings live inside `layout-meta { ... }`.
   - Every `element { ... }`, `vanilla_button { ... }`, `[loading_requirement_container_meta:...]`, `[executable_block:...]`, and `[executable_action_instance:...]` **MUST have a unique lowercase UUIDv4**.
   - **Never** put whitespace inside property keys (left of `=`), because `PropertiesParser` strips all whitespace from keys upon load.
   - Multi-line strings (such as `text_v2` content) use `%n%` for newlines inside the value.
   - Escape literal `{` as `\{` and `}` as `\}` if they appear inside raw property values where they could be confused with container braces (though standard JSON placeholders `{"placeholder":"..."}` are balanced and parse cleanly).
   - Always include the inline `[loading_requirement_container_meta:<uuid>] = [groups:][instances:] { ... }` block inside every `element`, `vanilla_button`, and `custom_element` block.

3. **Validate Before Reloading**:
   Run the helper script on any generated `.txt` layout file:
   ```powershell
   python "<skill_dir>/scripts/fancymenu_helper.py" validate-layout "<path/to/layout.txt>"
   ```
   Then instruct the user to press the **Reload** button in the top-left customization bar (or trigger the `reload_fancy_menu` action).

---

### Workflow B: Guiding the User in the In-Game Layout Editor
When the user prefers to build or tweak elements interactively in-game:
1. Ensure the **Customization Controls** bar is visible at the top of the screen (toggle with `CTRL + ALT + C`).
2. Verify the target screen identifier via **Current Screen -> Screen Info** (`title_screen`, `pause_screen`, `receiving_level_screen`, etc.).
3. Open **Layout -> New Layout** (or **Manage Layouts -> Edit**).
4. Provide exact **Right-Click Context Menu paths**, **Anchor Point names**, **Offset X/Y coordinates**, **Placeholder syntax**, and **Action Script chains** step-by-step.

---

## 3. Master Design Playbook: Building an "Animated, Everything-In-It" Title Screen

To create a flagship, AAA-grade animated Minecraft Title Screen, layer the following 7 systems together:

### Layer 1: Dynamic Animated Background + Screen Transitions
Choose one of the 4 animated background engines inside `menu_background`:
- **GLSL Fragment Shader (`background_type = shader`)**: Zero-VRAM procedural animation running at native FPS (`#version 150`, `uniform float u_time; uniform vec2 u_resolution;`). Ideal for arcane portals, starfields, nebula waves, or retro CRT grids.
- **Animation Controller (`background_type = animation`)**: Frame-perfect intro + loop video sequences (`.hma` via HeyMrAnimator or `.fma` folder in `config/fancymenu/animation_packs/`).
- **Cubic Panorama (`background_type = panorama`)**: 360-degree rotating skybox (`panorama_0.png` through `panorama_5.png` + optional `overlay.png`) with custom `rotation_speed`, `fov`, and `angle`.
- **Slideshow (`background_type = slideshow`)**: Cross-fading curated high-res screenshots with customizable `fade_speed` and `display_duration`.
- **Open/Close Screen Fade (`layout-meta`)**: Enable `enable_open_animation = true` (`fade_in`, `fade_in_speed = 1.5`) so the menu smoothly fades in after the loading screen finishes.

### Layer 2: Responsive Sidebar or Centered Navigation Dock
1. **Hide Cluttered Vanilla Buttons**: Set `is_hidden = true` on unused vanilla buttons (`mc_titlescreen_realms_button`, `mc_titlescreen_accessibility_button`, `mc_titlescreen_language_button`, `mc_titlescreen_copyright_button`) or reskin/re-anchor them cleanly.
2. **Create a Semi-Transparent Backdrop Dock**: Add a `shape` (`rectangle`, `#12121A99`) or 9-slice `image` anchored to `mid-left` (for a modern sidebar menu) or `mid-centered` (for a classic hero menu).
3. **Anchor-Chain the Buttons**:
   - Anchor the **Primary Button** (e.g., Singleplayer or "Play on Official Server") to `mid-left` (or `mid-centered`).
   - Anchor every subsequent button (`Multiplayer`, `Mods`, `Options`, `Quit`) to `anchor_point = element` with `anchor_point_element = <previous-button-uuid>`, placing it cleanly below (`y = 26`) so moving the first button moves the entire stack automatically!
4. **Custom Button Styling & Polish**:
   - Supply 3-state textures (`background_texture_normal`, `background_texture_hover`, `background_texture_inactive`) with `.nine_slice.json` sidecars for crisp pixel-art borders at any width.
   - Add custom hover sounds (`hover_sound = [source:local]/config/fancymenu/assets/audio/hover.ogg`) and click sounds (`click_sound`).
   - Use `hover_label` to animate the label on hover (e.g., `▸ Singleplayer ◂` or `{"placeholder":"recolor","values":{"text":"Singleplayer","color_hex":"#FFD700"}}`).

### Layer 3: Animated Logo & Custom Splash Text
- Hide the vanilla logo (`vanilla_button` with `element_type = title_screen_logo`, `is_hidden = true`) and replace it with a high-res `image` or `animation` element (`custom_logo`) anchored to `top-left` or `top-centered` with `sizing_mode = aspect_ratio`.
- Customize or replace `splash_text` (`custom_splash` or vanilla `mc_titlescreen_splash_button`) anchored to `element` (`custom_logo`), pulling lines from `[source:local]/config/fancymenu/assets/splashes.txt` with `bouncing = true`.

### Layer 4: Interactive 3D Player Avatar (`player_entity`)
- Place a `player_entity` element on the right or left side of the screen:
  - `auto_skin = true` & `auto_cape = true` (automatically fetches the logged-in player's skin and cape!).
  - `copy_client_player = true` (displays the player's actual equipped armor/items when in-world).
  - `head_follows_mouse = true` & `body_follows_mouse = true` so the 3D character tracks the user's cursor across the menu.
  - `is_baby = false`, `crouching = false`, or dynamically toggle `crouching` / `elytra_flying` via variables!

### Layer 5: Live Server Status & News Feed (`text_v2` + `ticker` + Web Placeholders)
- **Live Server Status Badge**: Use `{"placeholder":"server_status","values":{"ip":"play.example.com"}}`, `{"placeholder":"server_ping","values":{"ip":"play.example.com"}}`, and `{"placeholder":"server_playercount","values":{"ip":"play.example.com"}}` inside a `text_v2` or button tooltip to display real-time player counts and ping.
- **Remote Changelog / News Panel**: Use a Markdown-enabled `text_v2` element (`enable_markdown = true`, `enable_scrolling = true`) populated via `{"placeholder":"web_text","values":{"url":"https://.../changelog.md","update_interval":"300000"}}` or `{"placeholder":"json","values":{"url":"https://api.github.com/repos/.../releases/latest","json_path":"$.body"}}`.
- **News Ticker**: Add a `ticker` element along the bottom bar (`bottom-centered`) that scrolls tips or announcements on hover or continuously.

### Layer 6: Ambient Soundtrack & Sound Toggle (`audio` + Variables)
- Add an `audio` element (`loop = true`, `play_mode = normal`) with one or more `.ogg` tracks (`[source:local]/config/fancymenu/assets/audio/theme.ogg`).
- Pair it with a top-right **Mute/Unmute Custom Button** that toggles a persistent variable (`music_muted` = `true`/`false` via `set_variable`), and attach an inverted `is_Variable_value` loading requirement (`[loading_requirement:fancymenu_visibility_requirement_is_variable_value][requirement_mode:if_not]`) to the `audio` element so players can toggle menu music with one click!

### Layer 7: Seamless Handoff with Drippy Loading Screen
- Set identical `forced_scale` and `auto_scaling` rules between your `drippy_loading_overlay` layout and your `title_screen` layout.
- Match the final background color/image of the loading screen to the opening frame of `title_screen`, and enable `enable_open_animation = true` (`fade_in`) on `title_screen` for a butter-smooth transition when resources finish loading.

---

## 4. Using the Helper Script (`fancymenu_helper.py`)

Run `scripts/fancymenu_helper.py` via `run_command` whenever generating or inspecting FancyMenu files:

```powershell
# 1. Validate a layout .txt file (checks header, balanced braces, UUID collisions, required fields)
python "<skill_dir>/scripts/fancymenu_helper.py" validate-layout "<path/to/layout.txt>"

# 2. Generate N fresh UUIDv4 strings for elements, blocks, and requirement instances
python "<skill_dir>/scripts/fancymenu_helper.py" uuid 10

# 3. Create a Nine-Slice (.nine_slice.json) sidecar for a button or panel texture
python "<skill_dir>/scripts/fancymenu_helper.py" make-nine-slice "<path/to/button.png>" --top 4 --bottom 4 --left 4 --right 4

# 4. Generate a .fma animation pack main.properties file
python "<skill_dir>/scripts/fancymenu_helper.py" make-fma-props "<path/to/pack.fma/main.properties>" --fps 24 --loop true

# 5. Verify a 6-face cubic panorama folder (panorama_0.png .. panorama_5.png)
python "<skill_dir>/scripts/fancymenu_helper.py" check-panorama "<path/to/panorama_dir>"
```
