# 04 — Placeholders, Variables, Calculator, JSONPath, NBT & Conditions

This reference provides the complete catalog of **Placeholders**, **Calculator (`calc`) expressions**, **JSONPath queries**, **NBT data queries**, **Variables**, and **Loading Requirements (Conditions)** in FancyMenu v3 (Minecraft 1.21.1).

---

## 1. Placeholder Syntax & Nesting Rules

Placeholders use JSON-like syntax and can be inserted into almost any text, path, number, color, or advanced positioning/sizing field in FancyMenu.

### 1.1 Basic Syntax
- **Without parameters**:
  ```json
  {"placeholder":"fps"}
  ```
- **With parameters (`values`)**:
  ```json
  {"placeholder":"elementposx","values":{"id":"some_identifier"}}
  ```

### 1.2 Nesting Placeholders
Placeholders can be nested to arbitrary depth inside the `values` of outer placeholders:
```json
{"placeholder":"calc","values":{"decimal":"false","expression":"{"placeholder":"guiwidth"} / 2 - 100"}}
```
> [!IMPORTANT]
> In FancyMenu's parser, nested placeholders inside `"values":{...}` do **not** require escaping their outer quotes in the in-game UI editor, though literal syntax characters inside string values can be escaped with `\` (`\{`, `\}`, `\"`) or via the `stringify` placeholder.

---

## 2. Complete Placeholder Catalog

### 2.1 GUI, Screen & Window Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `guiwidth` | None | `1920` | Current GUI scaled width. |
| `guiheight` | None | `1080` | Current GUI scaled height. |
| `guiscale` | None | `2.0` | Current Minecraft GUI scale factor. |
| `screenwidth` | None | `1920` | Game window pixel width. |
| `screenheight` | None | `1080` | Game window pixel height. |
| `screenid` | None | `net.minecraft.client.gui.screens.TitleScreen` | Identifier of the currently open screen. |
| `aspect_ratio` | `char` (separator, e.g. `:`) | `16:9` | Current game window aspect ratio. |

### 2.2 Mouse, Cursor & Hovered Widget Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `mouseposx` | None | `960` | Current mouse X coordinate in GUI space. |
| `mouseposy` | None | `540` | Current mouse Y coordinate in GUI space. |
| `LastClickedButtonX` | None | `400` | X position of the last clicked button. |
| `LastClickedButtonY` | None | `300` | Y position of the last clicked button. |
| `LastClickedButtonWidth` | None | `200` | Width of the last clicked button. |
| `LastClickedButtonHeight` | None | `20` | Height of the last clicked button. |
| `hovered_element_id` | None | `vanillabtn:button_compatibility_id:mc_titlescreen_singleplayer_button` | Widget Locator (`vanillabtn:<id>` or `element:<id>`) of the currently hovered widget/element. |
| `focused_element_id` | None | `element:my_custom_button` | Widget Locator of the currently focused widget/element. |

### 2.3 Element & Vanilla Widget Geometry Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `elementposx` | `id` (element or vanilla button ID) | `100` | X position of target element/widget. |
| `elementposy` | `id` | `200` | Y position of target element/widget. |
| `elementwidth` | `id` | `150` | Width of target element/widget. |
| `elementheight` | `id` | `40` | Height of target element/widget. |
| `vanillabuttonlabel` | `locator` (e.g. `vanillabtn:504394`) | `Options...` | Current text label of a vanilla button. |
| `gui_slider_value` | `id`, `display_value` (`true`/`false`) | `50%` or `0.5` | Value of a FancyMenu v2 slider element (`display_value:"true"` returns label text; `"false"` returns raw `0.0`–`1.0`). |
| `edit_box_content` | `element_id` (Widget Locator) | `User input` | Current text inside an EditBox widget. |

### 2.4 Minecraft, Mod Loader & Mod Version Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `mcversion` | None | `1.21.1` | Current Minecraft version. |
| `modversion` | `modid` (e.g. `fancymenu`) | `3.2.1` | Version of a specific loaded mod. |
| `loaderver` | None | `0.15.7` | Mod loader version (Forge / Fabric / NeoForge). |
| `loadername` | None | `Fabric` | Mod loader name. |
| `totalmods` | None | `42` | Total count of loaded mods (includes sub-mods/APIs on Fabric). |
| `loadedmods` | None | `35` | Count of active mods. |
| `forgemods` | None | `35/42` | Formatted active/total mods string. |
| `splashtext` | None | `Awesome!` | Current Minecraft title screen splash text. |
| `drippy_gl_percent` | None | `75` | Current game loading progress percentage (0–100, Drippy Loading Screen integration). |
| `mc_option_value` | `name` (key from `options.txt`) | `70.0` | Current value of a setting in `options.txt` (e.g. `fov`, `gamma`). |
| `current_language` | None | `en_us` | Currently selected Minecraft language code. |

### 2.5 Player Identity & Vital Statistics Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `playername` | None | `Steve` | Current player's username (`user.getName()`). |
| `player_display_name` | `as_json` (`true`/`false`) | `Steve` | In-world player display name (plain or JSON component). |
| `playeruuid` | None | `8667ba71-...` | Current player's UUID. |
| `current_player_health` | None | `20.0` | Current player health points. |
| `max_player_health` | None | `20.0` | Maximum player health points. |
| `current_player_health_percent` | None | `100` | Player health as integer percentage (0–100). |
| `current_player_absorption` | None | `4` | Current absorption hearts/points. |
| `current_player_armor` | None | `15` | Current armor defense points. |
| `max_player_armor` | None | `20` | Maximum armor points. |
| `current_player_armor_percent` | None | `75` | Armor points as percentage. |
| `current_player_food` | None | `18` | Current hunger bar level (0–20). |
| `current_player_food_percent` | None | `90` | Hunger level as percentage. |
| `current_player_saturation` | None | `5.0` | Current food saturation level. |
| `current_player_saturation_percent` | None | `25` | Food saturation as percentage. |
| `current_player_air` | None | `300` | Remaining breath air ticks (underwater). |
| `max_player_air` | None | `300` | Maximum breath air ticks. |
| `current_player_air_percent` | None | `100` | Remaining air as percentage. |
| `current_player_exp` | None | `75` | Current progress toward next XP level as percentage (0–100). |
| `current_player_level` | None | `30` | Current experience level. |
| `total_player_exp` | None | `1395` | Total accumulated experience points. |
| `player_frozen_ticks` | None | `100` | Current powdered snow freezing ticks. |
| `player_max_frozen_ticks` | None | `140` | Ticks required to become fully frozen. |
| `player_frozen_percent` | None | `71` | Freezing progress as percentage. |
| `player_gamemode` | None | `survival` | Player gamemode (`survival`, `creative`, `adventure`, `spectator`). |
| `player_view_direction` | None | `north` | Cardinal direction the player is facing. |
| `player_x_coordinate` | None | `125` | Player X position in world. |
| `player_y_coordinate` | None | `64` | Player Y position in world. |
| `player_z_coordinate` | None | `-250` | Player Z position in world. |
| `lastdeathmessage` | `as_json_component` (`true`/`false`) | `Steve was slain by Zombie` | Last recorded death message of the client player. |

### 2.6 Mounts, Bosses, Potion Effects & Inventory Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `current_mount_health` | None | `30.0` | Current health of ridden entity. |
| `max_mount_health` | None | `30.0` | Max health of ridden entity. |
| `current_mount_health_percent` | None | `100` | Mount health as percentage. |
| `current_mount_jump_meter` | None | `75` | Mount jump meter percentage. |
| `current_boss_health` | `boss_index` (0-based) | `75` | Selected boss health percentage (0–100). |
| `boss_name` | `boss_index`, `as_json` (`true`/`false`) | `Ender Dragon` | Selected boss name. |
| `boss_count` | None | `1` | Number of active boss bars. |
| `effects_count` | None | `3` | Number of active status effects on player. |
| `active_effect` | `effect_index` (0-based) | `minecraft:speed` | Registry ID of active status effect at `effect_index`. |
| `active_hotbar_slot` | None | `4` | Selected hotbar slot index (`0`–`8`). |
| `slot_item` | `slot` | `minecraft:diamond_sword` | Item registry ID in inventory `slot`. |
| `slot_item_count` | `slot` | `64` | Stack count in inventory `slot`. |
| `slot_item_durability` | `slot`, `format` (`current`/`remaining`/`max`/`damage`/`percentage`/`percent`) | `87` | Item durability in `slot`. |
| `slot_item_display_name_fm` | `slot`, `ignore_spectator` (`true`/`false`) | `{"text":"Diamond Sword","color":"aqua"}` | JSON text component display name of item in `slot`. |
| `inventory_item_count` | `item` (e.g. `minecraft:diamond`, or empty for all) | `12` | Total matching items across player inventory. |
| `inventory_slot_food_point_restore_amount` | `slot` | `4.0` | Hunger points restored by food item in `slot`. |
| `hovered_inventory_item` | None | `minecraft:apple` | Registry key of currently hovered item in an inventory screen. |
| `item_category` | `item`, `as_key` (`true`/`false`) | `Combat` | Creative tab category of an item. |

### 2.7 World, Environment, HUD & Camera Delta Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `game_time` | None | `18000` | Total world game time ticks. |
| `world_daytime` | None | `13000` | Current world day time ticks. |
| `world_daytime_hour` | `twelve_hour_format` (`true`/`false`) | `12` | Hour component of world time. |
| `world_daytime_minute` | None | `30` | Minute component of world time (`00`–`59`). |
| `world_difficulty` | None | `normal` | Current world difficulty. |
| `current_world_seed` | None | `123456789` | Seed of current singleplayer world (empty if unavailable). |
| `current_biome` | `as_key` (`true`/`false`) | `minecraft:plains` | Player's current biome (registry key or translated name). |
| `current_dimension` | `as_key` (`true`/`false`) | `minecraft:overworld` | Player's current dimension (registry key or translated name). |
| `gamerule_value` | `name` (e.g. `doDaylightCycle`) | `true` | Gamerule value (requires FancyMenu on server for multiplayer). |
| `current_title` | `is_subtitle` (`true`/`false`), `as_json` (`true`/`false`) | `Game Over!` | Currently displayed HUD title or subtitle. |
| `action_bar_message_fm` | None | `{"text":"..."}` | Current vanilla action bar message as JSON component. |
| `action_bar_message_time_fm` | None | `42` | Remaining ticks for current action bar message. |
| `highlighted_item_time_fm` | None | `30` | Remaining ticks for highlighted hotbar item tooltip. |
| `player_item_use_progress_fm` | None | `0.65` | Current item-use progress (`0.0` to `1.0`). |
| `camera_rotation_x_fm` | None | `12.5` | Camera pitch in degrees. |
| `camera_rotation_y_fm` | None | `-90.0` | Camera yaw in degrees. |
| `camera_rotation_delta_x_fm` | None | `0.4` | Per-tick change in camera pitch (great for dynamic HUD sway!). |
| `camera_rotation_delta_y_fm` | None | `-1.2` | Per-tick change in camera yaw (great for dynamic HUD sway!). |
| `player_position_delta_x_fm` | None | `0.0` | Per-tick change in player X position. |
| `player_position_delta_y_fm` | None | `-0.08` | Per-tick change in player Y position. |
| `player_position_delta_z_fm` | None | `0.12` | Per-tick change in player Z position. |
| `level_save_names` | `separator` (e.g. `, `) | `World 1, World 2` | List of local world save names. |
| `level_save_data` | `level_name` | `{"name":"..."}` | Serialized JSON level data for a local save. |

### 2.8 Server & Multiplayer Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `current_server_ip` | None | `mc.hypixel.net` | IP address of currently connected server. |
| `world_players_list` | `separator` (e.g. `, `) | `Steve, Alex` | List of players currently in the world. |
| `servermotd` | `ip`, `line` (`1` or `2`) | `Welcome!` | Server MOTD line. |
| `serverping` | `ip` | `54` | Server ping in ms. |
| `serverplayercount` | `ip` | `25000/30000` | Server player count (`online/max`). |
| `serverstatus` | `ip` | `§aOnline` / `§cOffline` | Server online status. |
| `serverversion` | `ip` | `1.21.1` | Server Minecraft version string. |

### 2.9 Realtime, Hardware & System Placeholders

All `realtime*` placeholders (except `unix_time`) optionally accept `"timezone":"UTC"` (or `"system"` / any Java timezone ID like `"America/New_York"`).

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `realtimeyear` | `timezone` (opt) | `2026` | Current year. |
| `realtimemonth` | `timezone` (opt) | `10` | Current month (`01`–`12`). |
| `realtimeday` | `timezone` (opt) | `17` | Current day of month (`01`–`31`). |
| `realtimehour` | `twelve_hour_format` (`true`/`false`), `timezone` | `14` | Current hour (`00`–`23` or `01`–`12`). |
| `realtimeminute` | `timezone` (opt) | `30` | Current minute (`00`–`59`). |
| `realtimesecond` | `timezone` (opt) | `45` | Current second (`00`–`59`). |
| `unix_time` | None | `1716552478123` | Current Unix timestamp in milliseconds. |
| `uptime_duration` | `output_as_millis` (`true`/`false`) | `742` | Time since FancyMenu loaded (seconds or ms). |
| `fps` | None | `120` | Current frames per second. |
| `usedram` | None | `4096` | Currently used RAM in MB. |
| `maxram` | None | `8192` | Maximum allocated RAM in MB. |
| `percentram` | None | `50` | Percentage of allocated RAM in use. |
| `cpuinfo` | None | `Intel(R) Core(TM)...` | CPU model string. |
| `jvmcpu` | None | `25.5` | JVM CPU usage percentage. |
| `oscpu` | None | `42.8` | Total OS CPU usage percentage. |
| `gpuinfo` | None | `NVIDIA GeForce...` | Active rendering GPU device name. |
| `javaver` | None | `21.0.3` | Java runtime version. |
| `jvmname` | None | `OpenJDK 64-Bit...` | JVM implementation name. |
| `glver` | None | `4.6.0 NVIDIA...` | OpenGL / driver version string. |
| `osname` | None | `Windows 10` | Operating system name. |

### 2.10 Audio & Video Element / Background Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `audio_element_vol` | `element_identifier` | `0.5` | Volume of target Audio element (`0.0`–`1.0`). |
| `audio_element_current_track` | `element_identifier`, `display_name_mappings` (`a.ogg=>Track A%:%b.ogg=>Track B`) | `Track A` | Current track name of Audio element. |
| `audio_duration` | `element_identifier` | `03:45` | Duration of Audio element's current track (`MM:SS`). |
| `audio_playtime` | `element_identifier`, `show_percentage` (`true`/`false`) | `01:30` or `45` | Current playback progress of Audio element. |
| `audio_playing_state` | `element_identifier` | `true` | Whether Audio element is currently playing. |
| `video_element_vol` | `element_identifier` | `0.5` | Volume of Video element (`0.0`–`1.0`). |
| `video_element_duration` | `element_identifier`, `output_as_timestamp` (`true`/`false`) | `02:00` or `120000` | Total duration of Video element (`MM:SS` or ms). |
| `video_element_playtime` | `element_identifier`, `show_percentage`, `output_as_timestamp` | `00:45` / `38` / `45200` | Current playback progress of Video element. |
| `video_element_paused_state` | `element_identifier` | `false` | Whether Video element is paused. |
| `video_background_vol` | `background_identifier` | `0.7` | Volume of Video menu background. |
| `video_background_duration` | `background_identifier`, `output_as_timestamp` | `03:00` | Duration of Video menu background. |
| `video_background_playtime` | `background_identifier`, `show_percentage`, `output_as_timestamp` | `01:00` | Current playback progress of Video menu background. |
| `video_background_paused_state` | `background_identifier` | `true` | Whether Video menu background is paused. |

### 2.11 Math & Calculator Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `calc` | `decimal` (`true`/`false`), `expression` | `42` or `42.5` | Evaluates math expressions (`+`, `-`, `*`, `/`, `^`, `( )`, `sqrt()`, `sin()`, `cos()`, `tan()`, `abs()`, `log()`, `ln()`, `pi`, `e`). |
| `random_number` | `min`, `max` | `42` | Random integer between `min` and `max`. |
| `maxnum` | `first`, `second` | `20` | Larger of two numbers. |
| `minnum` | `first`, `second` | `10` | Smaller of two numbers. |
| `absnum` | `num` | `10.5` | Absolute value. |
| `negnum` | `num` | `-10.5` | Makes positive numbers negative (leaves `<= 0` unchanged). |
| `math_pi` | None | `3.141592653589793` | Constant $\pi$. |
| `math_sin` / `math_cos` / `math_tan` | `angle` (in radians) | `1.0` | Trigonometric functions (radians). |
| `math_sinh` / `math_cosh` / `math_tanh` | `num` | `1.1752...` | Hyperbolic functions. |
| `math_floor` / `math_ceil` | `num` | `3.0` / `4.0` | Floor / ceiling with `.0` suffix. |
| `math_round` | `num`, `decimals` (optional, default integer) | `3.14` or `3` | Rounds to nearest integer or `decimals` places. |
| `math_sign` | `num` | `1`, `-1`, `0` | Sign of number. |
| `number_base_convert` | `input`, `from_base`, `to_base` (`2`–`36`) | `43.8` | Converts integer/fractional numbers between bases. |

### 2.12 Text, File, Web, JSON, Variables & NBT Placeholders

| Placeholder ID | Parameters (`values`) | Output Example | Description |
| :--- | :--- | :--- | :--- |
| `getvariable` | `name` | `42` | Retrieves value of a stored FancyMenu variable. |
| `local` | `key` (e.g. `menu.singleplayer`) | `Singleplayer` | Translates a Minecraft localization key. |
| `switch_case` | `value`, `cases` (`1:first,2:second`), `default` | `first` | Switch-case mapping on `value`. |
| `replace_text` | `text`, `search`, `replacement`, `use_regex` (`true`/`false`), `replace_all` (`true`/`false`) | `Hello FancyMenu!` | Literal or regex string replacement. |
| `split_text` | `input`, `regex`, `max_parts`, `split_index` | `world` | Splits string by regex and returns element at `split_index`. |
| `trim_text` | `text` | `hello world` | Trims leading/trailing whitespace. |
| `crop_text` | `text`, `remove_from_start`, `remove_from_end` | `ello worl` | Strips $N$ characters from start/end. |
| `stringify` | `text` | `\{escaped\}` | Escapes FancyMenu syntax characters. |
| `text_character_count` | `text` | `12` | Character length of string. |
| `text_width` | `text` | `66` | Rendered pixel width of string in Minecraft font. |
| `uppercase_text` / `lowercase_text` | `text` | `HELLO` / `hello` | Case conversion. |
| `title_case_text` / `sentence_case_text` | `text` | `Hello World` | Title or sentence case conversion. |
| `snake_case_text` / `kebab_case_text` | `text` | `hello_world` / `hello-world` | Identifier case conversion. |
| `alternating_case_text` / `toggle_case_text` | `text` | `aLtErNaTiNg` | Stylized case conversion. |
| `base64_encode` / `base64_decode` | `text` | `SGVsbG8=` | Base64 encoding/decoding. |
| `clipboard_content` | None | `Clipboard text` | Current system clipboard string. |
| `webtext` | `link` (URL) | `Server notice` | Fetches plain text from a URL. |
| `randomtext` | `source` (file path `/config/...`, URL, or inline `Line 1\nLine 2`), `interval` (seconds) | `Random quote` | Picks a random line every `interval` seconds. |
| `file_text` | `path_or_url`, `mode` (`all`/`last`), `separator` (`\n`), `last_lines` (`1`) | `File content` | Reads all or last $N$ lines from a file/URL. |
| `json` | `source` (file path, URL, or raw JSON), `json_path` (`$.path`) | `Extracted value` | Evaluates a Jayway JSONPath expression against JSON data. |
| `absolute_path` | `short_path` | `C:/.../file.txt` | Resolves a relative game directory path to an absolute OS path. |
| `file_size` | `path` (`/config/fancymenu/...`) | `1284` | Size of local file in bytes. |
| `file_md5` | `path` (`/config/fancymenu/...`) | `d41d8cd9...` | Lowercase hex MD5 hash of local file. |
| `nbt_data_get` | `source_type` (`entity`/`block`), `entity_selector` (`@s`), `block_pos`, `nbt_path`, `scale`, `return_type` (`value`/`string`/`snbt`/`json`) | `20` | Client-side NBT query (like `/data get`). |
| `nbt_data_get_server` | `source_type` (`entity`/`block`/`storage`), `entity_selector`, `block_pos`, `storage_id`, `nbt_path`, `scale`, `return_type` | `minecraft:diamond_sword` | Server-side authoritative NBT query (requires FancyMenu on server). |

---

## 3. JSONPath (`json`) & NBT (`nbt_data_get`) Deep Dive

### 3.1 JSONPath Expressions (`json` Placeholder)
FancyMenu uses **Jayway JsonPath**.
- `$` = root element, `@` = current element in filter predicates.
- Child navigation: `$.store.book[0].title` or `$['store']['book'][0]['title']`.
- Deep scan: `$..author` (all `author` fields at any depth).
- Array slices: `$[0,1]`, `$[-1:]` (last element), `$[:2]` (first two).
- Filter expressions: `$.store.book[?(@.price < 10 && @.category == 'fiction')]`
- Functions (at end of path): `.min()`, `.max()`, `.avg()`, `.stddev()`, `.length()`, `.sum()`, `.keys()`, `.concat(X)`, `.append(X)`, `.first()`, `.last()`, `.index(X)`.

### 3.2 NBT Path Navigation (`nbt_data_get` & `nbt_data_get_server`)
Follows vanilla `/data get` NBT path syntax:
- Root & child tags: `foodLevel`, `Inventory[0].id`, `SelectedItem.components."minecraft:custom_name"`.
- Compound matching in lists: `Inventory[{Slot:0b}].id` or `Inventory[{id:"minecraft:diamond"}].count`.
- **Return Types**:
  - `value`: Numeric values (multiplied by `scale`), string contents, list element counts, or compound key counts.
  - `string`: Raw `.toString()` of the NBT tag.
  - `snbt`: Pretty-printed Stringified NBT.
  - `json`: Serialized JSON text component representation.

---

## 4. Variables System

Variables store dynamic string/numeric values manipulated by Action Scripts and read by Placeholders, Conditions, and GLSL Shaders.

### 4.1 Naming Rules
- Allowed characters: `a-z`, `A-Z`, `0-9`, `_`, `-` (no spaces or special characters).

### 4.2 Persistence vs. Session Variables
- **Default**: Variables persist across game restarts in `/config/fancymenu/user_variables.db`.
- **Session-only (`clear_on_launch`)**: When setting a variable via the `set_variable` action, set `clear_on_launch:true` (or toggle it in the Variable Manager UI) so the variable resets every time Minecraft launches.

### 4.3 Live Binding to GLSL Shaders
Any FancyMenu variable can be read directly inside a custom GLSL shader (`.fsh`) at 60+ FPS without string parsing by declaring a uniform prefixed with its type:
- `uniform float fmVarF_<var_name>;`
- `uniform int fmVarI_<var_name>;`
- `uniform vec2 fmVarVec2_<var_name>;` (comma-separated variable value, e.g. `"120.5, -45.0"`)
- `uniform vec3 fmVarVec3_<var_name>;`
- `uniform vec4 fmVarVec4_<var_name>;`

---

## 5. Loading Requirements (Conditions)

Loading Requirements control when **Layouts**, **Elements**, **Element Appearances** (e.g. texture/text swaps), and **Action Script `IF` / `ELSE IF` blocks** are active.

### 5.1 Group Logic & Inversion
Every Loading Requirement container supports:
1. **Group Requirement Mode (`requirement_mode`)**:
   - `AND` (`all`): Every requirement inside the group must pass.
   - `OR` (`any`): At least one requirement inside the group must pass.
   - `SOME` (`some`): At least $N$ requirements inside the group must pass.
2. **Invert Whole Group**: Turns `AND` into `NAND` ("not all") and `OR` into `NOR` ("none").
3. **Invert Individual Requirement**: Negates a single requirement instance (`!`).

### 5.2 Complete Catalog of Loading Requirement IDs

| Requirement ID | Parameters | Description |
| :--- | :--- | :--- |
| `fancymenu_loading_requirement_is_number` | `Value`, `Comparison Mode` (`equals`, `bigger-than`, `smaller-than`, `bigger-than-or-equals`, `smaller-than-or-equals`), `Compare With` | Numeric comparison (supports placeholders/variables). |
| `fancymenu_loading_requirement_is_text` | `Value`, `Comparison Mode` (`equals`, `contains`, `starts-with`, `ends-with`), `Compare With` | String comparison (supports placeholders/variables). |
| `fancymenu_loading_requirement_is_variable_value` | `Variable Name`, `Expected Value` | Checks if a FancyMenu variable equals a specific string. |
| `fancymenu_loading_requirement_is_element_hovered` | `Element ID` (`vanillabtn:...` or `element:...`) | True when the target widget/element is hovered. |
| `fancymenu_loading_requirement_is_element_focused` | `Element ID` | True when the target widget/element is focused. |
| `fancymenu_loading_requirement_is_button_clicked` | `Button ID`, `Detect All Click Types` (`true`/`false`) | True on the frame/tick a button is clicked. |
| `fancymenu_visibility_requirement_is_key_down` | `Key Code` (GLFW integer keycode, e.g. `340` = Left Shift) | True while the keyboard key is held down. |
| `fancymenu_loading_requirement_is_mouse_button_clicked` | `Mouse Button` (`left`, `right`, `middle`) | True while the mouse button is pressed. |
| `fancymenu_loading_requirement_is_mod_loaded` | `Mod ID` | True if the mod with `Mod ID` is loaded. |
| `fancymenu_loading_requirement_is_in_world` | None | True when the player is in any world (SP or MP). |
| `fancymenu_loading_requirement_is_singleplayer` | None | True when in a singleplayer world. |
| `fancymenu_loading_requirement_is_multiplayer` | None | True when connected to a multiplayer server. |
| `fancymenu_loading_requirement_is_connected_to_server` | `Server IP` (optional) | True when connected to any server (or a specific IP). |
| `fancymenu_loading_requirement_is_server_online` | `Server IP` | True if the remote server responds as online. |
| `fancymenu_loading_requirement_is_world_loaded` | `World Name` (optional) | True when a specific singleplayer world is loaded. |
| `fancymenu_loading_requirement_is_realtime_Ack` | `Type` (`year`, `month`, `day`, `hour`, `minute`, `second`), `Values` (comma-separated, e.g. `12,1,2`) | True when real-world date/time matches any listed value. |
| `fancymenu_loading_requirement_is_holiday` | `Check System Date` (`true`/`false`), `Custom Date`, `Holidays` (`christmas`, `new_year`, `halloween`, `valentines_day`, `st_patricks_day`, `april_fools`, `thanksgiving`, `easter`) | True on selected holidays. |
| `fancymenu_loading_requirement_is_os` | `OS` (`windows`, `macos`, `linux`, `other`) | True when running on the specified OS. |
| `fancymenu_loading_requirement_is_window_maximized` | None | True when the game window is maximized. |
| `fancymenu_loading_requirement_is_fullscreen` | None | True when the game is in fullscreen mode. |
| `fancymenu_loading_requirement_is_language` | `Language Code` (e.g. `en_us`, `de_de`) | True when Minecraft's active language matches. |
| `fancymenu_loading_requirement_is_layout_enabled` | `Layout Name` | True when the specified layout is currently enabled. |
| `fancymenu_loading_requirement_is_file_Check` | `File Path`, `Check Mode` (`exists`, `is_file`, `is_directory`) | True if the local file/folder exists or matches type. |
| `fancymenu_loading_requirement_random_chance` | `Chance` (`0`–`100`), `Interval` (seconds) | Evaluates a random roll every `Interval` seconds. |
| `fancymenu_loading_requirement_has_Advancement` | `Advancement ID`, `Player` (opt) | True if player has completed the advancement. |
| `fancymenu_loading_requirement_is_gamemode` | `Gamemode` (`survival`, `creative`, `adventure`, `spectator`) | True when player is in the specified gamemode. |
| `fancymenu_loading_requirement_is_dimension` | `Dimension ID` (e.g. `minecraft:overworld`) | True when player is in the specified dimension. |
| `fancymenu_loading_requirement_is_biome` | `Biome ID` (e.g. `minecraft:plains`) | True when player is in the specified biome. |
| `fancymenu_loading_requirement_is_weather` | `Weather` (`clear`, `rain`, `thunder`) | True when current world weather matches. |
| `fancymenu_loading_requirement_is_difficulty` | `Difficulty` (`peaceful`, `easy`, `normal`, `hard`) | True when world difficulty matches. |
| `fancymenu_loading_requirement_is_hardcore` | None | True when world is in Hardcore mode. |
| `fancymenu_loading_requirement_is_daytime` | None | True during in-game daytime (invert for nighttime). |
| `fancymenu_loading_requirement_is_player_swimming` | None | True when player is swimming. |
| `fancymenu_loading_requirement_is_player_crawling` | None | True when player is crawling. |
| `fancymenu_loading_requirement_is_player_climbing` | None | True when player is climbing a ladder/vine. |
| `fancymenu_loading_requirement_is_player_sneaking` | None | True when player is sneaking/crouching. |
| `fancymenu_loading_requirement_is_player_sprinting` | None | True when player is sprinting. |
| `fancymenu_loading_requirement_is_player_flying` | None | True when player is creative/spectator flying. |
| `fancymenu_loading_requirement_is_player_elytra_flying` | None | True when player is gliding with an Elytra. |
| `fancymenu_loading_requirement_is_player_riding` | `Entity ID` (optional) | True when riding any mount or a specific entity ID. |
| `fancymenu_loading_requirement_is_player_underwater` | None | True when player's eyes are underwater. |
| `fancymenu_loading_requirement_is_player_in_lava` | None | True when player is in lava. |
| `fancymenu_loading_requirement_is_player_burning` | None | True when player is on fire. |
| `fancymenu_loading_requirement_is_player_freezing` | None | True when player is freezing in powdered snow. |
| `fancymenu_loading_requirement_is_player_sleeping` | None | True when player is sleeping in a bed. |
| `fancymenu_loading_requirement_is_player_blocking` | None | True when player is blocking with a shield. |
| `fancymenu_loading_requirement_is_player_using_item` | `Item ID` (optional) | True when player is actively using an item (eating, drawing bow, etc.). |
| `fancymenu_loading_requirement_is_player_having_effect` | `Effect ID` (e.g. `minecraft:speed`), `Min Amplifier` (opt) | True when player has the specified potion effect. |
| `fancymenu_loading_requirement_is_player_having_item` | `Item ID`, `Min Count` (opt), `Slot` (opt: `mainhand`, `offhand`, `head`, `chest`, `legs`, `feet`, `any`) | True when player has the item in inventory or specific slot. |
| `fancymenu_loading_requirement_is_player_looking_at_block` | `Block ID` (e.g. `minecraft:chest`) | True when player's crosshair targets the block. |
| `fancymenu_loading_requirement_is_player_looking_at_entity` | `Entity ID` (e.g. `minecraft:villager`) | True when player's crosshair targets the entity. |
| `fancymenu_loading_requirement_is_player_standing_on_block` | `Block ID` | True when the block directly beneath the player matches. |
| `fancymenu_loading_requirement_is_hud_visible` | None | True when the vanilla HUD is visible (`F1` not pressed). |
| `fancymenu_loading_requirement_is_debug_screen_visible` | None | True when the `F3` debug overlay is open. |
| `fancymenu_loading_requirement_is_tab_list_visible` | None | True when the multiplayer player list (`Tab`) is held. |
| `fancymenu_loading_requirement_is_boss_bar_visible` | `Boss Name` (optional) | True when a boss bar is currently displayed. |
| `fancymenu_loading_requirement_is_gui_scale` | `GUI Scale` (integer) | True when Minecraft's GUI scale matches. |
| `fancymenu_loading_requirement_is_audio_playing` | `Element ID` | True when the specified Audio element is playing. |
| `fancymenu_loading_requirement_is_video_paused` | `Element/Background ID`, `Is Background` (`true`/`false`) | True when the Video element or background is paused. |
