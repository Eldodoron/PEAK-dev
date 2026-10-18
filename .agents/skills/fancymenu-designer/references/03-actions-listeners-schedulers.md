# FancyMenu Reference 03: Action Scripts, Listeners, Schedulers, Commands & FM Data

## 1. Action Script Architecture (`action-scripts.md`)

Action scripts execute sequences of tasks from top to bottom when triggered by:
- **Buttons** (on click)
- **Sliders** (on value change — supplies `$$value`)
- **Checkboxes** (on toggle)
- **Tickers** (every tick interval inside an active layout)
- **Screen Open / Close Events** (configured on layouts)
- **Listeners** (global event hooks — supply event-specific `$$` variables)
- **Schedulers** (global background timers)

### Control Statements & Execution Blocks
| Construct | Type | Behavior |
| :--- | :--- | :--- |
| **`If`** | Statement | Runs nested actions only when its attached Loading Requirements are met. |
| **`Else-If`** | Statement | Evaluated if the preceding `If` / `Else-If` did not run; checks its own Loading Requirements. |
| **`Else`** | Statement | Runs when none of the preceding `If` / `Else-If` branches in the chain matched. |
| **`While`** | Statement | Loops nested actions while its Loading Requirements remain true (**auto-terminates after 3 seconds** to prevent infinite freezes; never use `While` as a timer!). |
| **`Delay`** | Block | Starts a non-blocking countdown (`ms`) for its nested actions without pausing the rest of the script. Reinitializing the screen resets the countdown; does not stack if reached again while counting down. |
| **`Execute Later`** | Block | Schedules a fresh independent delayed execution (`ms`) of its nested actions **every time** the block is reached. |
| **`Comment`** | Block | Visual documentation note inside the script; no runtime effect. |
| **`Folder`** | Block | Collapsible visual container for organizing actions. |

### Delimiters & Value Rules
- Actions use exact field delimiters (`:`, `||`, or `|||`). There is **no escape syntax** for delimiters inside a field, except that **`set_variable` splits only on the FIRST colon `:`** (so `my_var:http://example.com:8080` stores `http://example.com:8080`).
- Placeholders (`{"placeholder":"..."}` and `$$` script variables) are resolved **before** the action value string is split by its delimiter.
- Async actions (`download_file_to_game_dir`, `extract_zip_file_in_game_dir`, `send_http_request`) run in the background; subsequent actions do NOT wait for them to finish. Use their completion **Listeners** (`file_downloaded_via_action`, `zip_extracted_via_action`) to react when done.

### Action Script Editor Shortcuts
`A` = Open Action Chooser | `Enter` = Edit selected entry | `Double-click value` = Inline edit | `Del` = Delete | `Ctrl+C` / `Ctrl+V` = Copy/Paste action | `Ctrl+Z` / `Ctrl+Y` = Undo/Redo | `Shift + Up/Down` = Reorder entry | `Ctrl+S` = Save & Close.

---

## 2. Complete Catalog of Built-in Actions

### Audio & Video Actions
| Action ID | Value Format | Description |
| :--- | :--- | :--- |
| `audio_next_track` | `audio_element_id` | Skips to the next track in an `Audio` element. |
| `audio_previous_track` | `audio_element_id` | Returns to the previous track in an `Audio` element. |
| `set_audio_element_volume` | `audio_element_id:volume` | Sets `Audio` element volume (`0.0` to `1.0`). |
| `audio_toggle_play` | `audio_element_id` | Toggles play/pause on an `Audio` element. |
| `play_audio` | `{"audioSource":"[source:local]/config/fancymenu/assets/sfx.ogg","soundChannel":"master","baseVolume":1.0}` | Plays a one-shot audio resource (cannot run from an async Ticker). |
| `stop_all_action_audios` | *(none)* | Stops all tracks started by `play_audio`. |
| `set_video_element_volume` | `video_element_id:volume` | Sets `Video` element volume (`0.0` to `1.0`). |
| `set_video_element_play_time` | `video_element_id:timestamp_ms` | Seeks a `Video` element to `timestamp_ms`. |
| `toggle_video_element_pause_state` | `video_element_id` | Toggles pause/play on a `Video` element. |
| `set_video_menu_background_volume` | `background_id:volume` | Sets `Video` menu background volume (`0.0` to `1.0`). Copy ID via right-click editor BG -> *Copy Background Identifier*. |
| `set_video_menu_background_play_time` | `background_id:timestamp_ms` | Seeks a `Video` menu background to `timestamp_ms`. |
| `toggle_video_menu_background_pause_state` | `background_id` | Toggles pause/play on a `Video` menu background. |

### Layout, Animator, Screen & Widget Actions
| Action ID | Value Format | Description |
| :--- | :--- | :--- |
| `toggle_layout` | `layout_name` | Toggles enabled state of `config/fancymenu/customization/<layout_name>.txt` (omit `.txt`). |
| `enable_layout` | `layout_name` | Enables and saves `<layout_name>.txt`. |
| `disable_layout` | `layout_name` | Disables and saves `<layout_name>.txt`. |
| `toggle_element_animator` | `animator_id` | Toggles playback state and resets active timeline of an `Element Animator`. |
| `enable_element_animator` | `animator_id` | Enables playback of an `Element Animator` (resets if previously disabled). |
| `disable_element_animator` | `animator_id` | Disables playback and resets active timeline of an `Element Animator`. |
| `reset_element_animator` | `animator_id` | Resets timeline of an `Element Animator` to `0ms` without changing enabled state. |
| `opengui` | `screen_identifier` | Opens a Vanilla screen, mod screen, or Custom GUI by exact identifier. |
| `closegui` | *(none)* | Closes the active screen. |
| `update_screen` | *(none)* | Reinitializes/refreshes the current screen. |
| `back_to_last_screen` | *(none)* | Returns to Custom GUI parent or most recently closed screen instance. |
| `mimicbutton` | `widget_locator` | Invokes the click action of a Vanilla/mod button (e.g. `title_screen:505280`; copy locator via `CTRL+ALT+D` right-click or in layout editor). |
| `mimic_keybind` | `keybind_id\|\|\|keep_pressed_bool\|\|\|duration_ms` | Triggers or holds a Minecraft keybind (e.g. `key.jump\|\|\|true\|\|\|1000`). |
| `set_text_input_field_value` | `element_id\|\|\|new_value\|\|\|force_set_when_inactive` | Sets the text inside a `Text Input Field` (`true`/`false` for inactive override). |

### World, Server, Chat & Game State Actions
| Action ID | Value Format | Description |
| :--- | :--- | :--- |
| `joinserver` | `server_ip` or `server_ip:port` | Connects to a multiplayer server (only when not already in a world/server). |
| `loadworld` | `world_folder_name` | Loads a singleplayer world by save folder name. |
| `join_last_world` | *(none)* | Rejoins the last played singleplayer world or multiplayer server. |
| `disconnect_server_or_world` | `screen_identifier` | Disconnects from current world/server and opens `screen_identifier` (falls back to `title_screen`). |
| `quitgame` | *(none)* | Closes Minecraft immediately. |
| `sendmessage` | `message_or_command` | Sends a chat message (supports `&` codes) or executes `/command`. |
| `execute_command_as_integrated_server` | `/command` | Force-runs a server command in Singleplayer (ignores cheats/OP settings; disabled if opened to LAN). |
| `paste_to_chat` | `append_bool:Text` | Opens chat and appends (`true:Text`) or replaces (`false:Text`) chat input box text. |
| `display_in_chat_client_side` | `plain_text_or_json_component` | Prints a client-only chat message when in a world. |
| `show_toast` | `{"width":200,"durationMs":5000,"title":"...","message":"...","iconSource":"...","backgroundSource":"..."}` | Displays a customizable popup toast (`width` `120–320`, `durationMs` `1000–600000`). |

### Variables, Schedulers, Options & Resource Packs
| Action ID | Value Format | Description |
| :--- | :--- | :--- |
| `set_variable` | `variable_name:variable_value` | Sets a FancyMenu variable (splits at first `:` only; saved immediately to `user_variables.db`). |
| `clear_variables` | *(none)* | Clears all stored FancyMenu variables. |
| `start_scheduler` | `scheduler_id` | Starts a background Scheduler by ID. |
| `stop_scheduler` | `scheduler_id` | Stops a background Scheduler by ID. |
| `edit_minecraft_option` | `option_name:set_to_value` | Sets a Minecraft `options.txt` setting (e.g. `soundCategory_music:0.5`, `fov:0.0`, `renderDistance:16`). |
| `manage_resource_pack` | `pack_name_or_id\|\|\|MODE\|\|\|reload_bool` | Enables, disables, or toggles a resource pack with optional reload. |
| `reload_resource_packs` | *(none)* | Reloads Minecraft resource packs (5-second anti-spam cooldown). |
| `reloadmenu` | *(none)* | Reloads FancyMenu layouts, Custom GUIs, panoramas, slideshows, and caches (do not call from a fast Ticker!). |

### File System, Clipboard, Logging & Network Actions
| Action ID | Value Format | Description |
| :--- | :--- | :--- |
| `openlink` | `https://example.com` | Opens URL in OS browser without confirmation prompt. |
| `copytoclipboard` | `text_to_copy` | Copies string to OS clipboard. |
| `print_to_log` | `text_to_log` | Logs message to `latest.log`. |
| `create_file_in_game_dir` | `relative_file_path` | Creates empty file + parent dirs inside `<game-directory>` (or `.minecraft/` prefix). |
| `write_file_in_game_dir` | `path\|\|\|content\|\|\|append_bool` | Writes/appends text to file (`\n` inserts newline). |
| `delete_file_in_game_dir` | `target_path` | Deletes file, folder recursively, or `folder/*` (direct child files only). |
| `copy_file_in_game_dir` | `source\|\|destination` | Copies file/folder (or `source/*` direct files); refuses overwrite. |
| `move_file_in_game_dir` | `source\|\|destination` | Moves file/folder (or `source/*` direct files); refuses overwrite. |
| `rename_file_in_game_dir` | `path\|\|new_name` | Renames file/folder in place; refuses overwrite. |
| `open_file_folder_in_game_dir` | `target_path` | Opens file/folder inside `<game-directory>` with OS default handler. |
| `select_file_to_game_dir` | `target_path\|\|\|filter_desc\|\|\|ext1;ext2\|\|\|overwrite_bool` | Opens native file picker and copies chosen file to `target_path`. Triggers `file_selected_via_action`. |
| `download_file_to_game_dir` | `url\|\|target_folder` | Async file download into `target_folder` (overwrites existing). Triggers `file_downloaded_via_action`. |
| `extract_zip_file_in_game_dir` | `source_zip_path\|\|target_folder_path` | Async ZIP extraction (overwrites matching files). Triggers `zip_extracted_via_action`. |
| `send_http_request` | *(JSON config via editor)* | Async HTTP `GET`/`POST`/`PUT`/`DELETE`/`PATCH`/`HEAD`/`OPTIONS` with headers, auth, body, and response variable storage. |
| `send_fm_data_to_server` | `data_identifier\|\|data` | Sends an FM Data packet to the connected Minecraft server (requires FancyMenu on server). |
| `connect_to_remote_server` | `wss://example.com/ws` | Opens/reuses client-initiated WebSocket connection (retries every 10s on crash). |
| `send_data_to_remote_server` | `remote_server_url\|\|data` | Sends text/JSON payload over WebSocket (queues unsent messages up to 30s). |
| `close_remote_server_connection` | `request_id` | Closes WebSocket connection by `$$request_id`. |
| `close_all_remote_server_connections` | *(none)* | Closes all active WebSocket connections. |

---

## 3. Complete Catalog of Global Event Listeners (`listeners.md`)

Stored in `<game-directory>/config/fancymenu/listener_instances.txt` and managed via **Customization -> Manage Listeners**. Listeners run globally (even when no menu is open) and inject read-only `$$` variables into their Action Script and Loading Requirements.

### UI, Input, Screen & Media Listeners
| Listener ID | Trigger | Supplied `$$` Variables |
| :--- | :--- | :--- |
| `screen_open` | Right after any screen opens | `$$screen_identifier` |
| `screen_close` | Immediately after a screen closes | `$$screen_identifier` |
| `quit_minecraft` | Client begins shutting down | `$$timestamp_millis`, `$$timestamp_iso` |
| `keyboard_key_pressed` | Key pressed/repeated (menus & in-game) | `$$key_name`, `$$key_keycode`, `$$key_scancode`, `$$key_modifiers` |
| `keyboard_key_released` | Key released (menus & in-game) | `$$key_name`, `$$key_keycode`, `$$key_scancode`, `$$key_modifiers` |
| `keyboard_char_typed` | Character typed while a screen is open | `$$char` |
| `mouse_moved` | Mouse moved while a screen is open | `$$mouse_pos_x`, `$$mouse_pos_y`, `$$mouse_move_delta_x`, `$$mouse_move_delta_y` |
| `mouse_button_clicked` | Mouse button pressed (menus & in-game) | `$$button` (`left`/`right`/`middle`), `$$mouse_pos_x`, `$$mouse_pos_y` |
| `mouse_button_released` | Mouse button released (menus & in-game) | `$$button`, `$$mouse_pos_x`, `$$mouse_pos_y` |
| `mouse_scrolled` | Mouse wheel scrolled in a screen | `$$scroll_delta_y` |
| `text_clicked` | Markdown `[text](click:id)` clicked | `$$text_event_id` |
| `text_hovered` | Markdown `[text](hover:id)` hovered | `$$text_event_id` |
| `fm_variable_updated` | Any FancyMenu variable changes | `$$var_name`, `$$old_value`, `$$new_value` |
| `element_spawned_via_action` | Dynamic element spawned | `$$element_type`, `$$element_identifier`, `$$target_screen` |
| `animated_texture_started_playing` | `.afma`/`.fma`/`.apng` starts | `$$texture_source`, `$$texture_source_type`, `$$texture_will_restart` |
| `animated_texture_finished_playing` | Animated texture finishes | `$$texture_source`, `$$texture_source_type`, `$$texture_will_restart` |
| `video_playback_status_changed` | Video changes status | `$$video_source`, `$$video_source_type`, `$$is_looping`, `$$new_status` (`PLAYING`/`STOPPED`/`PAUSED`/`FINISHED`) |
| `music_track_started` | Music track begins | `$$track_resource_location`, `$$track_display_name`, `$$track_artist`, `$$track_duration_ms` |
| `music_track_stopped` | Music track ends/replaced | `$$track_resource_location`, `$$track_display_name`, `$$track_artist`, `$$track_duration_ms` |
| `world_sound_triggered` | Positional sound plays near player | `$$sound_resource_location`, `$$sound_display_name`, `$$sound_origin_pos_x/y/z`, `$$sound_origin_distance_to_player`, `$$sound_origin_direction_from_player` (`0–360`) |

### File, Network & Chat Listeners
| Listener ID | Trigger | Supplied `$$` Variables |
| :--- | :--- | :--- |
| `file_downloaded_via_action` | `download_file_to_game_dir` completes | `$$download_url`, `$$target_file_path`, `$$download_succeeded` |
| `zip_extracted_via_action` | `extract_zip_file_in_game_dir` completes | `$$source_zip_path`, `$$target_folder_path`, `$$extract_succeeded`, `$$failure_reason` |
| `file_selected_via_action` | `select_file_to_game_dir` completes | `$$selected_file_path`, `$$target_file_path`, `$$selection_succeeded`, `$$selection_cancelled`, `$$failure_reason` |
| `fm_data_received` | Server sends `/fmdata send` | `$$data_identifier`, `$$data`, `$$sent_by` (server IP or `integrated_server`) |
| `remote_server_connected` | WebSocket connects | `$$request_id`, `$$remote_server_url` |
| `remote_server_data_received` | WebSocket receives text | `$$request_id`, `$$remote_server_url`, `$$data` |
| `remote_server_connection_closed` | WebSocket closes | `$$request_id`, `$$remote_server_url`, `$$intentionally_closed`, `$$crashed`, `$$unknown_close_reason` |
| `chat_message_received` | Player chat message received | `$$chat_message_string`, `$$chat_message_component`, `$$sender_uuid`, `$$sender_name` |
| `chat_message_sent` | Local player sends chat message | `$$chat_message_string`, `$$chat_message_component` |
| `system_message_received_in_chat` | System/command feedback chat received | `$$system_message_string`, `$$system_message_component` |

### Player, World, Entity, Block & Item Listeners
| Listener ID | Trigger | Supplied `$$` Variables |
| :--- | :--- | :--- |
| `server_joined` / `server_left` | Multiplayer join / disconnect | `$$server_ip` |
| `world_entered` | Singleplayer world loaded | `$$world_name`, `$$world_save_path`, `$$world_difficulty`, `$$world_cheats_allowed`, `$$world_icon_path`, `$$world_is_first_join` |
| `world_left` | Singleplayer world closed | `$$world_name`, `$$world_save_path`, `$$world_difficulty`, `$$world_cheats_allowed`, `$$world_icon_path` |
| `other_player_joined_world` / `other_player_left_world` | Another player joins/leaves | `$$player_name`, `$$player_uuid` |
| `other_player_died` | Another player dies | `$$player_name`, `$$player_uuid`, `$$death_pos_x`, `$$death_pos_y`, `$$death_pos_z` |
| `player_death` | Local player death screen opens | `$$days_survived`, `$$death_reason_string`, `$$death_reason_component`, `$$death_pos_x/y/z` |
| `damage_taken` | Local player takes damage | `$$damage_amount`, `$$damage_type`, `$$is_fatal_damage`, `$$damage_source` |
| `experience_changed` | Local player XP changes | `$$new_experience_amount`, `$$old_experience_amount`, `$$is_level_up` |
| `effect_gained` / `effect_lost` | Status effect gained / lost | `$$effect_key`, `$$effect_type`, `$$effect_duration` (on gained) |
| `position_changed` | Player block pos changes | `$$old_pos_x/y/z`, `$$new_pos_x/y/z` |
| `enter_biome` / `leave_biome` | Player enters / leaves biome | `$$biome_key` |
| `enter_dimension` | Player enters dimension | `$$dimension_key` |
| `enter_structure` / `leave_structure` | Coarse structure enter/leave *(Server FM req)* | `$$structure_key` |
| `enter_structure_high_precision` / `leave_structure_high_precision` | Exact structure bounds *(Server FM req)* | `$$structure_key` |
| `weather_changed` | Weather state changes | `$$weather_type` (`clear`/`rain`/`thunder`), `$$weather_can_snow`, `$$weather_can_rain` |
| `start_swimming` / `stop_swimming` | Swimming state changes | `$$fluid_type` |
| `start_touching_fluid` / `stop_touching_fluid` | Fluid contact changes | `$$fluid_type` |
| `started_freezing` | Player starts freezing | `$$freezing_intensity` (`0.0–1.0`) |
| `stopped_freezing` / `fully_frozen` / `started_burning` / `stopped_burning` / `started_drowning` / `started_running` / `stopped_running` / `jump` | Player state transitions | *(no variables)* |
| `start_looking_at_block` / `stop_looking_at_block` | Crosshair block raycast (<=20m) | `$$block_key`, `$$block_pos_x/y/z`, `$$distance_to_player` |
| `start_looking_at_entity` / `stop_looking_at_entity` | Crosshair entity raycast (<=20m) | `$$entity_key`, `$$distance_to_player`, `$$entity_pos_x/y/z`, `$$entity_uuid` |
| `entity_starts_being_in_sight` / `entity_stops_being_in_sight` | Entity enters/leaves view (<=200m) | `$$entity_key`, `$$distance_to_player`, `$$entity_pos_x/y/z`, `$$entity_uuid` |
| `entity_interacted` / `entity_mounted` / `entity_unmounted` | Player interacts/mounts/unmounts entity | `$$entity_key`, `$$entity_pos_x/y/z`, `$$entity_uuid` |
| `entity_spawned` | Entity spawns *(Server FM req)* | `$$entity_key`, `$$distance_to_player`, `$$entity_pos_x/y/z`, `$$entity_uuid`, `$$dimension_key`, `$$is_same_dimension_as_player` |
| `entity_died` | Entity dies *(Server FM req)* | `$$entity_key`, `$$distance_to_player`, `$$death_pos_x/y/z`, `$$entity_uuid`, `$$dimension_key`, `$$damage_type`, `$$is_same_dimension_as_player`, `$$entity_killed_by_name/key/uuid` |
| `block_broke` | Player breaks block | `$$block_key`, `$$broke_with_item_key`, `$$block_pos_x/y/z` |
| `block_placed` / `interacted_with_block` / `stepping_on_block` | Block placed / interacted / stepped on | `$$block_key`, `$$block_pos_x/y/z` |
| `item_picked_up` / `item_dropped` / `item_consumed` | Item pickup / drop / consume | `$$item_key` |
| `item_hovered_in_inventory` | Item hovered in GUI slot | `$$item_key`, `$$item_display_name_string`, `$$item_display_name_json` |
| `item_used` | Item used | `$$item_key`, `$$used_on_type` (`block`/`entity`/`self`/`none`), `$$used_on_entity_key`, `$$used_on_block_key`, `$$target_pos_x/y/z` |
| `item_broke` | Inventory item breaks | `$$item_key`, `$$item_type` (`tool`/`armor`/`other`) |

---

## 4. Schedulers, Commands, FM Data & Localization

### Global Schedulers (`schedulers.md`)
- Stored in `<game-directory>/config/fancymenu/scheduler_instances.txt`; managed via **Customization -> Manage Schedulers**.
- Settings: `Scheduler ID` (`[a-z0-9._-]`), `Start Delay (ms)`, `Tick Delay (ms)` (`0` = every game tick), `Ticks to Run` (`0` = infinite), `Start on Launch` (`true`/`false`).
- Control via `start_scheduler` / `stop_scheduler` actions and check state with the `Scheduler Is Running` condition.

### In-Game Commands (`commands.md` & `fm-data.md`)
- `/openguiscreen <screen_identifier> [<target_players>]` (target arg requires OP 2)
- `/closeguiscreen [<target_players>]` (target arg requires OP 2)
- `/fmlayout <layout_name> <true|false> [<target_players>]` (target arg requires OP 3)
- `/fmvariable get <variable_name>`
- `/fmvariable set <variable_name> <send_chat_feedback_bool> <set_to_value>`
- `/fmdata send <target_players> <data_identifier> <string_data>` (OP 2)
- `/fmdata listener add|edit <name> <match_id_mode> <match_data_mode> <ignore_case_id> <ignore_case_data> <fire_for_player> <listen_id> <listen_data> "<cmd1|||cmd2>"` (supports `%fm_sender%` and `%fm_data%`; persisted in `config/fancymenu/fmdata_server_listeners.json`).
- `/fmdata welcome_data add|edit <name> <target_player> <data_identifier> <string_data>` (persisted in `config/fancymenu/fmdata_welcome_data.json`).

### Localization (`localization.md`)
- Use `{"placeholder":"local","values":{"key":"modpack.menu.play"}}`.
- Custom static dictionary files go inside a **subdirectory** of `<game-directory>/config/fancymenu/custom_locals/<pack_name>/` (`.json`, `.lang`, or `.properties` — files directly in the root of `custom_locals/` are ignored!).
- For dynamic language switching based on Minecraft's language setting, provide `assets/<namespace>/lang/<lang_code>.json` via a resource pack or gate elements with the `fancymenu_loading_requirement_is_language` condition.
