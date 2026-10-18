# 05 — Raw File Formats, `.txt` Layout Schema & Storage Architecture

This reference documents the **exact on-disk serialization grammar** of FancyMenu v3 (Minecraft 1.21.1), derived directly from `Keksuccino/FancyMenu` (`PropertiesParser.java`, `Layout.java`, `ElementBuilder.java`, `AbstractElement.java`, `RequirementContainer.java`, `ExecutableBlockDeserializer.java`, and `ActionInstance.java`). Use this specification to read, debug, or procedurally generate `.txt` layout files outside the game.

---

## 1. Directory & Storage Map (`/config/fancymenu/`)

All FancyMenu configuration and user assets reside inside `<game_directory>/config/fancymenu/`:

| Path | Purpose | Ship in Modpacks? |
| :--- | :--- | :--- |
| `/config/fancymenu/assets/` | Central asset directory for images (`.png`, `.apng`, `.gif`), animations (`.fma`), shaders (`.fsh`, `.vsh`), audio (`.ogg`, `.wav`, `.mp3`), videos (`.mp4`, `.webm`), Markdown/text files (`.md`, `.txt`), JSON data, and custom window icons. | **YES** |
| `/config/fancymenu/customization/` | Serialized **Layout `.txt` files** (every enabled or disabled screen/universal layout). | **YES** |
| `/config/fancymenu/custom_gui_screens.txt` | Registry and definitions of all Custom GUIs (`custom_gui`). | **YES** |
| `/config/fancymenu/panoramas/<name>/` | Cubic panorama packs (`properties.txt` + `panorama/panorama_0.png`..`panorama_5.png` + `panorama_overlay.png`). | **YES** |
| `/config/fancymenu/slideshows/<name>/` | Slideshow packs (`properties.txt` + `images/*.png`). | **YES** |
| `/config/fancymenu/element_animations/` | Exported Element Animator presets. | **YES** (if used) |
| `/config/fancymenu/schedulers/` | Background Action Script Scheduler definitions. | **YES** (if used) |
| `/config/fancymenu/event_listeners/` | Global Event Listener Action Script definitions. | **YES** (if used) |
| `/config/fancymenu/options.txt` | Global FancyMenu mod settings (UI theme, intro animation, custom window title/icon, audio flags, etc.). | **YES** |
| `/config/fancymenu/user_variables.db` | Persistent FancyMenu Variables database (`PropertyContainerSet` format). | **OPTIONAL** (Delete before packing if you want clean initial variables for players) |
| `/config/fancymenu/fm_data.db` | Persistent `/fmdata` world/server variable storage. | **NO** (Runtime player data) |

---

## 2. `PropertiesParser` & `PropertyContainerSet` Grammar

Every `.txt` and `.db` file in FancyMenu is serialized via `PropertiesParser.serializeSetToFancyString(PropertyContainerSet)`.

### 2.1 File Structure
```ini
type = fancymenu_layout

<container_type> {
  <property_key> = <property_value>
  <property_key_2> = <property_value_2>
}

<container_type_2> {
  ...
}
```

### 2.2 Exact Parser Rules (`PropertiesParser.deserializeSetFromFancyString`)
1. **Header Line**: The first non-empty line outside a container must be `type = <set_type>` (for layouts, `type = fancymenu_layout`; legacy v2 layouts used `type = menu`).
2. **Container Opening**: Any line whose whitespace-stripped form ends with `{` opens a new `PropertyContainer` whose type is the text before `{` (e.g., `layout-meta {`, `element {`, `vanilla_button {`, `menu_background {`).
3. **Property Lines**: Inside `{ ... }`, lines containing `=` are split at the **first** `=`:
   - **Key**: Everything before the first `=`, with **all whitespace stripped** (`replaceAll("[\\p{Z}\\s]+", "")`). Keys must NEVER contain spaces.
   - **Value**: Everything after the first `=`, with **at most one leading space (`" "`) removed**. All subsequent spaces and `=` characters in the value are preserved verbatim.
4. **Container Closing**: A line starting with `}` (after whitespace stripping) closes the current `PropertyContainer`.
5. **Line Breaks & Special Characters**:
   - Properties cannot span raw newline characters inside a container.
   - Multi-line text properties (such as `TextElement` `source` or button `description` tooltips) encode newlines as `%n%`.
   - When `PropertiesParser.stringifyFancyString()` is used, `\n` becomes `$prop_line_break$`, `{` becomes `$prop_brackets_open$`, and `}` becomes `$prop_brackets_close$`.

---

## 3. Resource Source Prefixes (`ResourceSourceType`)

Whenever a property references a texture, audio track, video, or text resource via `ResourceSupplier.getSourceWithPrefix()`, it is prefixed with its `ResourceSourceType`:

| Source Type | Serialized Prefix | Example Value |
| :--- | :--- | :--- |
| **Local File** (`/config/fancymenu/assets/...`) | `[source:local]` | `[source:local]/config/fancymenu/assets/bg.png` |
| **ResourceLocation** (Vanilla or Modded) | `[source:location]` | `[source:location]minecraft:textures/gui/title/minecraft.png` |
| **Web URL** (`http://` or `https://`) | `[source:web]` | `[source:web]https://example.com/banner.png` |

---

## 4. Complete Layout `.txt` File Schema (`type = fancymenu_layout`)

A FancyMenu v3 layout file (`Layout.java`) contains the following container types in order:

### 4.1 `layout-meta` Container
Stores screen target, activation status, random group settings, universal layout filters, and layout-wide loading requirements:
```ini
layout-meta {
  identifier = title_screen
  render_custom_elements_behind_vanilla = false
  last_edited_time = 1729180000000
  is_enabled = true
  randommode = false
  randomgroup = 1
  randomonlyfirsttime = false
  layout_index = 0
  custom_menu_title = My Custom Title
  universal_layout_whitelist = title_screen;join_multiplayer_screen;
  universal_layout_blacklist = 
  [loading_requirement_container_meta:a1b2c3d4-...] = [groups:][instances:]
}
```
- For **Universal Layouts**, `identifier = %fancymenu:universal_layout%`.

### 4.2 `customization` Containers (Layout-Level Options)
Optional containers for forced GUI scale, auto-scaling, open/close audio, and background aspect ratio:
```ini
customization {
  action = setscale
  scale = 2
}

customization {
  action = autoscale
  basewidth = 1920
  baseheight = 1080
}

customization {
  action = setopenaudio
  path = [source:local]/config/fancymenu/assets/menu_open.ogg
}

customization {
  action = setcloseaudio
  path = [source:local]/config/fancymenu/assets/menu_close.ogg
}

customization {
  action = backgroundoptions
  keepaspectratio = true
}
```

### 4.3 `menu_background` Container
Configures the active menu background (`MenuBackgroundBuilder.java`). Registered `background_type` values (`MenuBackgrounds.java`):
- `color` (Solid/gradient hex color)
- `panorama` (Cubic panorama pack)
- `image` (Static/animated image with optional slide/repeat/parallax)
- `slideshow` (Slideshow pack)
- `video_mcef` / `video_rinku` (Video background)
- `browser` (Web page background)
- `glsl` (GLSL shader background)

Example (`image` background with parallax):
```ini
menu_background {
  instance_identifier = 8f7e6d5c-1111-2222-3333-444455556666
  background_type = image
  image_path = [source:local]/config/fancymenu/assets/main_bg.png
  fallback_path = 
  slide = false
  repeat_texture = false
  parallax = true
  parallax_intensity_x = 0.03
  parallax_intensity_y = 0.03
  invert_parallax = false
  restart_animated_on_menu_load = false
}
```

Example (`glsl` shader background):
```ini
menu_background {
  instance_identifier = 9a8b7c6d-1111-2222-3333-444455556666
  background_type = glsl
  inline_shader_source = [source:local]/config/fancymenu/assets/shaders/nebula.fsh
  buffer_a_inline_source = 
  buffer_b_inline_source = 
  buffer_c_inline_source = 
  buffer_d_inline_source = 
  image_ichannel0_input = none
  image_ichannel1_input = none
  image_ichannel2_input = none
  image_ichannel3_input = none
  compile_mode = auto
  force_shadertoy_compatibility = true
  freeze_time = false
  time_scale = 1.0
  enable_blending = true
  use_input = true
  mouse_position_requires_hold = false
  opacity_multiplier = 1.0
  show_compile_errors = true
}
```

### 4.4 `scroll_list_customization` Container
Controls scroll list headers/footers and vanilla 1.21+ menu background blur:
```ini
scroll_list_customization {
  preserve_scroll_list_header_footer_aspect_ratio = true
  scroll_list_header_texture = [source:local]/config/fancymenu/assets/header.png
  scroll_list_footer_texture = [source:local]/config/fancymenu/assets/footer.png
  render_scroll_list_header_shadow = true
  render_scroll_list_footer_shadow = true
  show_scroll_list_header_footer_preview_in_editor = false
  repeat_scroll_list_header_texture = false
  repeat_scroll_list_footer_texture = false
  show_screen_background_overlay_on_custom_background = true
  apply_vanilla_background_blur = false
}
```

### 4.5 `layout_action_executable_blocks` Container
Holds Action Scripts that execute when the screen opens or closes:
```ini
layout_action_executable_blocks {
  open_screen_executable_block_identifier = block_open_uuid
  [executable_block:block_open_uuid][type:generic] = [executables:act_1;]
  [executable_action_instance:act_1][action_type:set_variable] = menu_visits:1
  close_screen_executable_block_identifier = block_close_uuid
  [executable_block:block_close_uuid][type:generic] = [executables:]
}
```

### 4.6 `layer_group` Containers
Groups elements in the editor's layer panel:
```ini
layer_group {
  group_name = Header Elements
  collapsed = false
  element_ids = elem_uuid_1;elem_uuid_2;
}
```

---

## 5. `element` & `vanilla_button` Containers

Every custom element is serialized as an `element { ... }` container, and every customized vanilla widget is serialized as a `vanilla_button { ... }` container.
- **Layering Order**: Elements are rendered in the **exact order** their `element { ... }` blocks appear in the `.txt` file (top of file = back/bottom layer; bottom of file = front/top layer).

### 5.1 Registered `element_type` Identifiers (`Elements.java`)

| Element Type | `element_type` Value |
| :--- | :--- |
| Vanilla Widget | `vanilla_button` (inside `vanilla_button { ... }` container) |
| Custom Button | `custom_button` |
| Input Field | `input_field` |
| Slider (v2) | `slider_v2` |
| Checkbox | `checkbox` |
| Text (Markdown v2) | `text_v2` |
| Tooltip | `tooltip` |
| Action Script Ticker | `ticker` |
| Player Entity (v2 / FER) | `player_entity_v2` (or legacy `fancymenu_customization_player_entity`) |
| Image | `image` |
| GLSL Shader | `glsl_shader` |
| JSON Model | `json_model` |
| Splash Text | `splash_text` |
| Slideshow | `slideshow` |
| Rectangle Shape | `shape` (via `RectangleShapeElementBuilder`) |
| Circle Shape | `circle_shape` |
| Custom Cursor | `cursor` |
| Progress Bar | `progress_bar` |
| Audio Player (v2) | `audio_v2` |
| Music Controller | `music_controller` |
| Window Dragger | `dragger` |
| Web Browser | `browser` |
| Item Display | `item` |
| Animation Controller | `animation_controller` |
| Video Player | `video_mcef` / `video_rinku` |

### 5.2 Universal Base Element Properties (`ElementBuilder.java` & `AbstractElement.java`)
Every `element { ... }` and `vanilla_button { ... }` container shares these base properties:

```ini
element {
  element_type = image
  instance_identifier = 12345678-aaaa-bbbb-cccc-1234567890ab
  custom_element_layer_name = Logo Graphic
  anchor_point = top-centered
  anchor_point_element = parent_element_uuid_if_anchor_is_element
  x = 0
  y = 24
  width = 200
  height = 60
  stretch_x = false
  stretch_y = false
  stay_on_screen = true
  auto_sizing = false
  auto_sizing_base_screen_width = 0
  auto_sizing_base_screen_height = 0
  auto_sizing_base_gui_scale = 0.0
  auto_sizing_base_gui_width = 0
  auto_sizing_base_gui_height = 0
  sticky_anchor = false
  advanced_posx = {"placeholder":"calc","values":{"decimal":"false","expression":"{"placeholder":"guiwidth"} / 4"}}
  advanced_posy = 
  advanced_width = 
  advanced_height = 
  appearance_delay = no_delay
  appearance_delay_seconds = 1.0
  disappearance_delay = no_delay
  disappearance_delay_seconds = 1.0
  fade_in_v2 = no_fading
  fade_in_speed = 1.0
  fade_out = no_fading
  fade_out_speed = 1.0
  base_opacity = 1.0
  enable_parallax = false
  parallax_intensity_x = 0.5
  parallax_intensity_y = 0.5
  invert_parallax = false
  animated_offset_x = 0
  animated_offset_y = 0
  load_once_per_session = false
  in_editor_color = #FFC800FF
  layer_hidden_in_editor = false
  should_be_affected_by_decoration_overlays = false
  rotation_degrees = 0.0
  advanced_rotation_mode = false
  advanced_rotation_degrees = 0.0
  vertical_tilt_degrees = 0.0
  advanced_vertical_tilt_mode = false
  advanced_vertical_tilt_degrees = 0.0
  horizontal_tilt_degrees = 0.0
  advanced_horizontal_tilt_mode = false
  advanced_horizontal_tilt_degrees = 0.0
  element_loading_requirement_container_identifier = req_container_uuid
  [loading_requirement_container_meta:req_container_uuid] = [groups:][instances:]
}
```
- **Valid `anchor_point` values**: `top-left`, `top-centered`, `top-right`, `mid-left`, `mid-centered`, `mid-right`, `bottom-left`, `bottom-centered`, `bottom-right`, `element`, `vanilla` (only for `vanilla_button`).
- **Valid `appearance_delay` / `disappearance_delay` values**: `no_delay`, `first_time`, `every_time`.
- **Valid `fade_in_v2` / `fade_out` values**: `no_fading`, `first_time`, `every_time`.
- **Note on `advanced_posx`, `advanced_posy`, `advanced_width`, `advanced_height`**: When unused, omit them or leave them out so they default to `Integer.MIN_VALUE`; when set to a placeholder/math string, `ManualInputProperty` stores the raw placeholder string directly.

### 5.3 Element-Specific Properties (Most Common Elements)

#### A. `image` (`ImageElement.java`)
```ini
  source = [source:local]/config/fancymenu/assets/logo.png
  repeat_texture = false
  nine_slice_texture = false
  nine_slice_texture_border_x = 5
  nine_slice_texture_border_y = 5
  image_tint = #FFFFFF
  restart_animated_on_menu_load = false
  rounding_radius_top_left = 0.0
  rounding_radius_top_right = 0.0
  rounding_radius_bottom_right = 0.0
  rounding_radius_bottom_left = 0.0
```

#### B. `custom_button` & `vanilla_button` (`ButtonElement.java`, `VanillaWidgetElementBuilder.java`)
For `vanilla_button`, the container header is `vanilla_button {`, `element_type = vanilla_button`, `instance_identifier` is the button compatibility ID or hash (without `vanillabtn:`, e.g. `button_compatibility_id:mc_titlescreen_singleplayer_button` or `minecraft_logo_widget`), and `is_hidden = true|false` controls whether the vanilla widget is hidden.
```ini
  label = Play Now
  hoverlabel = &e> Play Now <
  label_base_color = #FFFFFF
  label_hover_color = #FFFF55
  label_scale = 1.0
  label_shadow = true
  description = Click to enter%n%Second tooltip line
  backgroundnormal = [source:local]/config/fancymenu/assets/btn_normal.png
  backgroundhovered = [source:local]/config/fancymenu/assets/btn_hover.png
  background_texture_inactive = [source:local]/config/fancymenu/assets/btn_disabled.png
  iconnormal = 
  iconhovered = 
  icon_texture_inactive = 
  hoversound = [source:local]/config/fancymenu/assets/hover.ogg
  clicksound = [source:local]/config/fancymenu/assets/click.ogg
  unhover_audio = 
  underline_label_on_hover = false
  transparent_background = false
  restartbackgroundanimations = true
  nine_slice_custom_background = true
  nine_slice_border_x = 5
  nine_slice_border_y = 5
  navigatable = true
  is_template = false
  template_apply_width = false
  template_apply_height = false
  template_apply_posx = false
  template_apply_posy = false
  template_apply_opacity = false
  template_apply_visibility = false
  template_apply_label = false
  template_share_with = buttons
  button_element_executable_block_identifier = btn_exec_uuid
  [executable_block:btn_exec_uuid][type:generic] = [executables:act_uuid_1;]
  [executable_action_instance:act_uuid_1][action_type:opengui] = join_multiplayer_screen
  widget_active_state_requirement_container_identifier = active_req_uuid
  [loading_requirement_container_meta:active_req_uuid] = [groups:][instances:]
```

#### C. `text_v2` (`TextElementBuilder.java`)
```ini
  interactable = true
  source = ### Welcome, {"placeholder":"playername"}!%n%Modpack v1.0
  source_mode = direct
  shadow = true
  case_mode = normal
  scale = 1.0
  base_color = #FFFFFFFF
  text_border = 2
  line_spacing = 2
  enable_scrolling = true
  auto_line_wrapping = true
  remove_html_breaks = true
  parse_markdown = true
  code_block_single_color = #737373FF
  code_block_multi_color = #565656FF
  headline_line_color = #A6A6A6FF
  separation_line_color = #A6A6A6FF
  hyperlink_color = #0078FFFF
  quote_color = #A6A6A6FF
  quote_italic = true
  bullet_list_dot_color = #A6A6A6FF
```

---

## 6. Inline Serialization of `RequirementContainer` (Loading Requirements)

Whenever a container (such as `layout-meta`, `element`, `vanilla_button`, or an `if`/`else-if`/`while` block) embeds a `RequirementContainer`, its properties are flattened into the parent container (`RequirementContainer.java`, `RequirementGroup.java`, `RequirementInstance.java`):

```ini
  element_loading_requirement_container_identifier = req_cont_01
  [loading_requirement_container_meta:req_cont_01] = [groups:grp_01;][instances:inst_root_01;]
  [loading_requirement_group:grp_01] = [group_mode:or]
  [loading_requirement:fancymenu_loading_requirement_is_element_hovered][requirement_mode:if][group:grp_01][req_id:inst_grp_01] = vanillabtn:button_compatibility_id:mc_titlescreen_singleplayer_button
  [loading_requirement:fancymenu_loading_requirement_is_variable_value][requirement_mode:if_not][req_id:inst_root_01] = hide_ui:true
```
- **`requirement_mode`**: `if` (normal) or `if_not` (inverted `!`).
- **`group_mode`**: `and` or `or`.

---

## 7. Inline Serialization of `AbstractExecutableBlock` (Action Scripts)

Action Scripts on buttons, tickers, sliders, or screen open/close hooks are flattened into the owning container (`AbstractExecutableBlock.java`, `ExecutableBlockDeserializer.java`, `ActionInstance.java`):

```ini
  button_element_executable_block_identifier = root_block_01
  [executable_block:root_block_01][type:generic] = [executables:if_block_01;delay_block_01;]
  
  [executable_block:if_block_01][type:if] = [executables:act_01;][appended:else_block_01]
  [if_executable_block_body:if_block_01] = cond_cont_01
  [if_executable_block_collapsed:if_block_01] = false
  [loading_requirement_container_meta:cond_cont_01] = [groups:][instances:req_01;]
  [loading_requirement:fancymenu_loading_requirement_is_mod_loaded][requirement_mode:if][req_id:req_01] = relics
  
  [executable_block:else_block_01][type:else] = [executables:act_02;]
  
  [executable_block:delay_block_01][type:delay] = [executables:act_03;]
  [delay_executable_block_value:delay_block_01] = 1000
  [delay_executable_block_collapsed:delay_block_01] = false
  
  [executable_action_instance:act_01][action_type:send_message] = Relics is loaded!
  [executable_action_instance:act_02][action_type:send_message] = Relics is missing!
  [executable_action_instance:act_03][action_type:reloadmenu] = 
```

### Block Type Reference (`ExecutableBlockDeserializer.java`)
- `generic`: Top-level root container block.
- `if`: Conditional `IF` block; links to its `RequirementContainer` via `[if_executable_block_body:<id>] = <cond_id>` and optional `else-if`/`else` chain via `[appended:<next_block_id>]`.
- `else-if`: Conditional `ELSE IF` block; links to `[else_if_executable_block_body:<id>] = <cond_id>` and optional `[appended:<next_block_id>]`.
- `else`: Unconditional `ELSE` fallback block.
- `while`: Loop block (3000ms safety timeout); links to `[while_executable_block_body:<id>] = <cond_id>`.
- `delay`: One-time cooldown gate; uses `[delay_executable_block_value:<id>] = <ms>`.
- `execute-later`: Asynchronous timer block; uses `[execute_later_executable_block_value:<id>] = <ms>`.
- `folder`: Organizational folder block in the Action Script editor.
- `comment`: Non-executing editor comment block.
