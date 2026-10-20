# Handoff Report — FTB Quests Localization Survey (R3)

**Agent**: `explorer_survey_3`  
**Milestone**: Survey & Scope Mapping (R3 FTB Quests Localization Tone Polish)  
**Target File**: `minecraft/config/ftbquests/quests/lang/en_us.snbt`  
**Date**: 2026-10-19T19:27:00Z  

---

## 1. Observation

### 1.1 Scope & Architecture Overview
- **Localization File**: `minecraft/config/ftbquests/quests/lang/en_us.snbt`
  - Total Lines: 4,145
  - File Size: 259,667 bytes (~255 KB)
  - Structure: Root SNBT compound `{ ... }` mapping quest object keys to string literals or string array literals.
- **Chapter Files**: `minecraft/config/ftbquests/quests/chapters/*.snbt` (25 chapter files).
  - Search command: `grep_search` with Query `^\s*(title|subtitle|description):`
  - Result: Exactly **0** matches across all 25 chapter files. All quest titles, subtitles, and descriptions are 100% decoupled and centralized exclusively in `lang/en_us.snbt`.
- **Reward Tables**: `minecraft/config/ftbquests/quests/reward_tables/*.snbt` (14 reward tables).
  - Search command: Grep for AI buzzwords across reward tables.
  - Result: Exactly **0** AI buzzwords detected in reward tables.

### 1.2 Formatting Code Integrity & Ampersand Audit
- **Literal `& ` Violations**:
  - Command: `grep_search` with Query `&\s` across `minecraft/config/ftbquests/`.
  - Result: **0 occurrences found**.
- **Unescaped / Invalid Formatting Codes**:
  - Command: Regex audit for `&` not followed by valid Minecraft color/formatting characters `[0-9a-fk-orA-FK-OR#]`.
  - Result: **0 occurrences found**.
- **Raw Emoji Characters**:
  - Command: Unicode range scan (`0x1F300-0x1FAFF` and `0x2600-0x27BF`).
  - Result: **0 emoji glyphs** present.

### 1.3 Critical Finding: Regex Boundary Blindspots in Minecraft Text
Standard word-boundary searches (`\b<word>\b`) fail to detect words immediately following Minecraft color formatting codes (such as `&6Embark` or `&eDelving`). In regular expressions, digits (`0-9`) and hexadecimal color characters (`a-f`) are word characters (`\w`), meaning the transition between the color digit/character and the subsequent capital letter does **NOT** constitute a word boundary (`\b`).
- Example: `re.search(r'\bembark', '&6Embark')` returns `None`.
- Using a color-safe lookbehind pattern `(?<![a-zA-Z])<word>` successfully uncovered **2 additional buzzword occurrences** (`&6Embark` at line 1230 and `&eDelving` at line 3940) that were completely missed in prior audit reports.

### 1.4 Primary Target AI Buzzword Tally (Direct R3 Mandate)
A total of **22 occurrences** of the 7 core buzzwords (*surgical*, *delves*, *cornerstone*, *unleashed*, *meticulously*, *mastery*, *embark*) were identified across **20 distinct quest and task entries**:

| Category | Count | Lines in `en_us.snbt` |
| :--- | :--- | :--- |
| `surgical` | 1 | 1810 |
| `delve` / `delves` / `delving` | 4 | 1022, 2128, 2949, 3940 *(line 3940 uncovered via color-safe boundary)* |
| `cornerstone` | 2 | 1650, 1878 |
| `unleash` / `unleashed` / `unleashing` | 3 | 556, 1511, 1853 |
| `meticulous` / `meticulously` | 2 | 2506, 2907 |
| `mastery` | 7 | 863, 1716, 1794, 1873, 1943, 1955, 3993 |
| `embark` | 3 | 1230 *(uncovered via color-safe boundary)*, 3989, 4125 |
| **Total Core Buzzwords** | **22** | Across 20 distinct objects |

### 1.5 Secondary Contextual AI Buzzwords & Fluff
An additional **10 occurrences** of secondary AI filler words were cataloged for comprehensive cleanup:
- `vital` (filler: "your most vital tool"): Line 1647
- `harness` / `Harnessing`: Lines 1672, 1674, 1778
- `robust` (filler: "Distinct robust flavor"): Line 2389
- `masterpiece`: Line 2507
- `Masterfully`: Line 2908
- `comprehensive`: Line 3383
- `Synergy`: Line 3986
- `mastered` (filler: "mastered the art of practical adventure"): Line 3992

---

## 2. Logic Chain

1. **Step 1 — Decoupling Verification**: Inspection of the 25 chapter `.snbt` files showed they contain no inline `title`, `subtitle`, or `description` tags. The quest engine resolves all strings via key references against `quests/lang/en_us.snbt`. Therefore, updating `en_us.snbt` is both necessary and sufficient, with zero risk of chapter desynchronization.
2. **Step 2 — Critical Invariant Verification**: R3 and the project Acceptance Criteria mandate that exactly 0 occurrences of "surgical" remain in `minecraft/config/ftbquests/`. Investigation confirmed line 1810 (`quest.4103000000000020.quest_subtitle: "Filter, extract, and sort with surgical precision."`) is the sole occurrence of "surgical" in the entire FTB Quests configuration.
3. **Step 3 — Color-Safe Boundary Investigation**: Because Minecraft color codes (`&6`, `&e`, `&9`, etc.) use alphanumeric characters directly adjacent to word letters, regexes relying on `\b` produce false negatives. A color-safe boundary scan revealed line 1230 (`&6Embark Upon the Boss Pantheon&r`) and line 3940 (`&eDelving into deep caves...&r`), which had escaped previous audits.
4. **Step 4 — Tone Discrimination**: Not every occurrence of target roots represents AI fluff:
   - "Vitality" (e.g. lines 615, 1035, 1975, 2065, 2542, 2935, 3375, 3813, 3976) refers to the player health / heart-scaling mechanic from Spice of Life / Minecraft health attributes. These are legitimate gameplay terms and must not be altered.
   - "Bastion" (lines 284, 3137, 3214, 3232) refers to Nether Bastion Remnants and Ars Nouveau Bastion Fruit/Bark.
   - "Labyrinth" (lines 807, 1342, 1374, 1375, 2841, etc.) refers to the Twilight Forest Minoshroom Labyrinth structure.
   - "The Master's Wand" (line 3931) is the literal item name from the *Construction Wands* mod.
   - Legitimate milestone titles (e.g., "Master of the 25 Archetypes", "Master Chef") reflect standard RPG progression tiers and can be retained or refined cleanly without compromising tone.
5. **Step 5 — Proposal Formulation**: Each flagged line was replaced with natural, grounded prose. All proposed replacements preserve Minecraft color escape sequences, maintain valid SNBT string quoting, and completely eliminate the flagged AI markers.

---

## 3. Caveats

1. **Staging Directory Synchronization**: `ServerPackStaging/config/ftbquests/quests/lang/en_us.snbt` contains a mirror of line 1810. When the worker applies changes to `minecraft/config/ftbquests/quests/lang/en_us.snbt`, the orchestrator or worker should note whether `ServerPackStaging` will be resynchronized during the final export or requires a manual mirrored edit.
2. **Game Logic Invariance**: None of the changes proposed touch quest IDs, completion criteria, item IDs, rewards, coordinates (`x`, `y`), or dependencies. The changes are 100% cosmetic and localized.
3. **SNBT Parser Sensitivity**: In SNBT files, double quotes inside double-quoted strings must be escaped (`\"`). All proposed replacements avoid internal double quotes entirely or use single quotes where needed to maintain flawless parser compliance.

---

## 4. Conclusion & Complete Replacement Table

### 4.1 Category 1: The 22 Core Mandated Replacements (R3)

| ID | Line | Quest Key | Flagged Buzzword | Current Exact String | Proposed Replacement String |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C1-01** | 556 | `quest.2002000000000029.quest_desc` | `unleashed` | `"\t\t\"&9The ocean's fury unleashed upon the surface.\""` | `"\t\t\"&9Strikes landbound foes with the crushing weight of the open sea.\""` |
| **C1-02** | 863 | `quest.2004000000000000.quest_desc` | `mastery` | `"\t\t\"&5The Cosmos recognizes your supreme mastery.&r\""` | `"\t\t\"&5The Cosmos yields before your boundless conquest.&r\""` |
| **C1-03** | 1022 | `quest.2006000000000002.quest_desc` | `delves` | `"\t\t\"&7Exceptional base durability for sustained dungeon delves.\""` | `"\t\t\"&7Exceptional base durability for prolonged dungeon raids.\""` |
| **C1-04** | 1230 | `quest.3100000000000005.title` | `Embark` | `"\tquest.3100000000000005.title: \"&6Embark Upon the Boss Pantheon&r\""` | `"\tquest.3100000000000005.title: \"&6Enter the Boss Pantheon&r\""` |
| **C1-05** | 1511 | `quest.3105000000000032.quest_desc` | `unleashing` | `"\tquest.3105000000000032.quest_desc: [\"&aThe radioactive leviathan unleashing devastating atomic breath rays.&r\"]"` | `"\tquest.3105000000000032.quest_desc: [\"&aA radioactive apex titan that fires concentrated beams of atomic energy.&r\"]"` |
| **C1-06** | 1650 | `quest.4101000000000010.quest_subtitle` | `cornerstone` | `"\tquest.4101000000000010.quest_subtitle: \"The cornerstone of all kinetic mechanics.\""` | `"\tquest.4101000000000010.quest_subtitle: \"The essential tool for configuring and dismantling machinery.\""` |
| **C1-07** | 1716 | `quest.4101000000000110.quest_subtitle` | `Mastery` | `"\tquest.4101000000000110.quest_subtitle: \"Mastery of rotational motion.\""` | `"\tquest.4101000000000110.quest_subtitle: \"Regulate and stabilize high-stress rotational networks.\""` |
| **C1-08** | 1794 | `quest.4102000000000120.quest_desc` | `mastery` | `"\t\t\"&6Precision Mechanisms represent true engineering mastery.&r\""` | `"\t\t\"&6Precision Mechanisms bridge basic kinetics and advanced automated systems.&r\""` |
| **C1-09** | 1810 | `quest.4103000000000020.quest_subtitle` | `surgical` | `"\tquest.4103000000000020.quest_subtitle: \"Filter, extract, and sort with surgical precision.\""` | `"\tquest.4103000000000020.quest_subtitle: \"Filter, extract, and sort item streams with exact stack limits.\""` |
| **C1-10** | 1853 | `quest.4103000000000090.quest_subtitle` | `Unleashing` | `"\tquest.4103000000000090.quest_subtitle: \"Unleashing the power of pressurized steam.\""` | `"\tquest.4103000000000090.quest_subtitle: \"Generate immense rotational stress using pressurized steam.\""` |
| **C1-11** | 1873 | `quest.4103000000000120.quest_subtitle` | `Mastery` | `"\tquest.4103000000000120.quest_subtitle: \"Mastery of factory logistics and transit.\""` | `"\tquest.4103000000000120.quest_subtitle: \"Monitor train schedules, storage vaults, and factory throughput.\""` |
| **C1-12** | 1878 | `quest.4104000000000010.quest_desc` | `cornerstone` | `"\t\t\"Steel is the cornerstone of industrial casings, diesel combustion, and aerospace rocketry.\""` | `"\t\t\"Steel forms the structural backbone for industrial casings, diesel combustion, and aerospace rocketry.\""` |
| **C1-13** | 1943 | `quest.4104000000000110.quest_desc` | `mastery` | `"\t\t\"With steel foundries, diesel power, physics airships, and Martian bases under your command, your industrial mastery over PEAK is absolute.\""` | `"\t\t\"With steel foundries, diesel power, physics airships, and Martian bases under your command, your industrial network across PEAK is complete.\""` |
| **C1-14** | 1955 | `quest.47ACECB62DA96AD6.quest_subtitle` | `mastery` | `"\tquest.47ACECB62DA96AD6.quest_subtitle: \"Combat mastery and weapons\""` | `"\tquest.47ACECB62DA96AD6.quest_subtitle: \"Weapon archetypes, combat stances, and runic blades\""` |
| **C1-15** | 2128 | `quest.5100000000000048.quest_desc` | `delve` | `"\tquest.5100000000000048.quest_desc: [\"&e* Classic lunchbox sandwich ready for any mining delve.\"]"` | `"\tquest.5100000000000048.quest_desc: [\"&e* Classic lunchbox sandwich packed for deep mining runs.\"]"` |
| **C1-16** | 2506 | `quest.5101000000000067.quest_desc` | `Meticulously` | `"\tquest.5101000000000067.quest_desc: [\"&c* Meticulously arranged baked summer vegetable layers.\"]"` | `"\tquest.5101000000000067.quest_desc: [\"&c* Thinly sliced summer squash and tomatoes baked with garden herbs.\"]"` |
| **C1-17** | 2907 | `quest.5102000000000066.quest_desc` | `meticulously` | `"\tquest.5102000000000066.quest_desc: [\"&e* Toxins meticulously removed. Spicy and thrilling.\"]"` | `"\tquest.5102000000000066.quest_desc: [\"&e* Carefully trimmed pufferfish cured with sea salt and chili flakes.\"]"` |
| **C1-18** | 2949 | `quest.5102000000000080.quest_desc` | `delves` | `"\tquest.5102000000000080.quest_desc: [\"&6* Slow-cooked until tender. The staple food of underworld delves.\"]"` | `"\tquest.5102000000000080.quest_desc: [\"&6* Slow-cooked until tender. A hearty staple during deep Undergarden exploration.\"]"` |
| **C1-19** | 3940 | `quest.7000000000000080.quest_desc` | `Delving` | `"\t\t\"&eDelving into deep caves and perilous dungeons can quickly turn deadly.&r\""` | `"\t\t\"&eExploring deep caves and perilous dungeons can quickly turn deadly.&r\""` |
| **C1-20** | 3989 | `quest.7000000000000150.quest_desc` | `embark` *(and `master`)* | `"\t\t\"You are now equipped to master the kinetic factories of Create, conquer the 12 Boss Eyes, and embark on the voyage to Mars and Venus.\""` | `"\t\t\"You are now equipped to construct the kinetic factories of Create, conquer the 12 Boss Eyes, and launch your voyage to Mars and Venus.\""` |
| **C1-21** | 3993 | `quest.7000000000000150.title` | `Mastery` | `"\tquest.7000000000000150.title: \"&6The PEAK Pioneer - Summit Mastery&r\""` | `"\tquest.7000000000000150.title: \"&6The PEAK Pioneer - The Summit Reached&r\""` |
| **C1-22** | 4125 | `task.5400000000004001.title` | `Embark` | `"\ttask.5400000000004001.title: \"Embark on the Safari\""` | `"\ttask.5400000000004001.title: \"Begin the Safari\""` |

---

### 4.2 Category 2: The 10 Secondary Contextual Replacements

| ID | Line | Quest Key | Flagged Buzzword | Current Exact String | Proposed Replacement String |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C2-01** | 1647 | `quest.4101000000000010.quest_desc` | `most vital` | `"\t\t\"The Wrench is your most vital tool. Right-click any kinetic component to rotate it, configure its axis, or sneak-right-click to instantly dismantle machinery safely into your inventory.\""` | `"\t\t\"The Wrench is an essential engineering tool. Right-click any kinetic component to rotate it, configure its axis, or sneak-right-click to instantly dismantle machinery safely into your inventory.\""` |
| **C2-02** | 1672 | `quest.4101000000000040.title` | `Harnessing` | `"\tquest.4101000000000040.title: \"&6Harnessing the River - Water Wheels&r\""` | `"\tquest.4101000000000040.title: \"&6Hydroelectric Power - Water Wheels&r\""` |
| **C2-03** | 1674 | `quest.4101000000000050.quest_desc` | `harness` | `"\t\t\"&eWindmill Bearings harness the breeze to generate massive kinetic power.&r\""` | `"\t\t\"&eWindmill Bearings convert wind currents into massive kinetic power.&r\""` |
| **C2-04** | 1778 | `quest.4102000000000100.quest_desc` | `Harness` | `"\t\t\"&eHarness all airflow processing mediums with your Encased Fan:&r\""` | `"\t\t\"&eDirect Encased Fan airflow through five processing mediums:&r\""` |
| **C2-05** | 2389 | `quest.5101000000000031.quest_desc` | `robust` | `"\tquest.5101000000000031.quest_desc: [\"&c* Distinct robust flavor that craves rosemary and garlic.\"]"` | `"\tquest.5101000000000031.quest_desc: [\"&c* Rich, hearty flavor seasoned with rosemary and garlic.\"]"` |
| **C2-06** | 2507 | `quest.5101000000000067.quest_subtitle` | `masterpiece` | `"\tquest.5101000000000067.quest_subtitle: \"Layered squash and tomato masterpiece.\""` | `"\tquest.5101000000000067.quest_subtitle: \"Baked summer squash and tomato gratin.\""` |
| **C2-07** | 2908 | `quest.5102000000000066.quest_subtitle` | `Masterfully` | `"\tquest.5102000000000066.quest_subtitle: \"Masterfully cured pufferfish.\""` | `"\tquest.5102000000000066.quest_subtitle: \"Salt-cured and thinly sliced pufferfish.\""` |
| **C2-08** | 3383 | `quest.5104000000000000.quest_desc` | `comprehensive` | `"\t\t\"Featuring the comprehensive aquatic catches of &bAquaculture 2&r.\""` | `"\t\t\"Featuring all marine and freshwater catches from &bAquaculture 2&r.\""` |
| **C2-09** | 3986 | `quest.7000000000000140.title` | `Synergy` | `"\tquest.7000000000000140.title: \"&eCurios Synergy - Trinket Optimization&r\""` | `"\tquest.7000000000000140.title: \"&eCurios Loadouts - Trinket Combinations&r\""` |
| **C2-10** | 3992 | `quest.7000000000000150.quest_subtitle` | `mastered` | `"\tquest.7000000000000150.quest_subtitle: \"You have mastered the art of practical adventure.\""` | `"\tquest.7000000000000150.quest_subtitle: \"Essential tools acquired. The wider world awaits.\""` |

---

## 5. Verification Method

### 5.1 Verification Commands for Downstream Worker & Auditor
1. **Zero "Surgical" Verification**:
   ```powershell
   python -c "
   with open('minecraft/config/ftbquests/quests/lang/en_us.snbt', 'r', encoding='utf-8') as f:
       text = f.read()
   import re
   matches = re.findall(r'surgic\w*', text, re.IGNORECASE)
   print('Surgical occurrences:', len(matches))
   assert len(matches) == 0, 'Surgical still present!'
   "
   ```
2. **Zero Core Buzzwords Verification**:
   ```powershell
   python -c "
   with open('minecraft/config/ftbquests/quests/lang/en_us.snbt', 'r', encoding='utf-8') as f:
       text = f.read()
   import re
   pat = re.compile(r'(?<![a-zA-Z])(surgical|cornerstone|unleash\w*|meticulous\w*|mastery|delv\w*|embark\w*)', re.IGNORECASE)
   matches = pat.findall(text)
   print('Core buzzwords remaining:', len(matches), matches)
   "
   ```
3. **Zero Literal Ampersand Violation Check**:
   ```powershell
   python -c "
   with open('minecraft/config/ftbquests/quests/lang/en_us.snbt', 'r', encoding='utf-8') as f:
       lines = f.readlines()
   violations = [(i, l.strip()) for i, l in enumerate(lines, 1) if '& ' in l]
   print('Literal & violations:', len(violations))
   assert len(violations) == 0, 'Found literal & violations!'
   "
   ```
4. **Valid SNBT Bracket and Quotation Integrity**:
   ```powershell
   python -c "
   with open('minecraft/config/ftbquests/quests/lang/en_us.snbt', 'r', encoding='utf-8') as f:
       content = f.read()
   assert content.startswith('{') and content.rstrip().endswith('}'), 'Invalid root compound!'
   print('Root SNBT compound is intact.')
   "
   ```

### 5.2 Invalidation Conditions
- Any occurrence of `"surgical"` or `"surgically"` found in `minecraft/config/ftbquests/quests/lang/en_us.snbt`.
- Any presence of `& ` (ampersand followed by a space) which corrupts Minecraft's text formatting renderer into printing `"Invalid formatting code"`.
- Any syntax corruption resulting in unbalanced brackets (`{ }` or `[ ]`) or unescaped interior double-quotes in `en_us.snbt`.
- Any desynchronization caused by introducing text into `chapters/*.snbt`.
