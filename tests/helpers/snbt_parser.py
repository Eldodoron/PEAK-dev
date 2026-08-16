"""
FTB Quests SNBT (Stringified NBT) Parser & Validator.
Parses quest localization and structure files, ensuring validity and zero AI remnants.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import re


@dataclass
class QuestEntry:
    quest_id: str
    title: Optional[str] = None
    subtitle: Optional[str] = None
    description: Optional[List[str]] = None


class SNBTParser:
    def __init__(self):
        pass

    def parse_string(self, snbt_content: str) -> Tuple[bool, Optional[str], Dict[str, Any]]:
        """
        Parses SNBT compound key-value content into a Python dictionary.
        Handles keys without quotes, string literals with escapes, lists, and comments.
        """
        result: Dict[str, Any] = {}
        i = 0
        n = len(snbt_content)

        def skip_whitespace_and_comments():
            nonlocal i
            while i < n:
                if snbt_content[i].isspace():
                    i += 1
                elif snbt_content[i:i+2] == "//":
                    i += 2
                    while i < n and snbt_content[i] != '\n':
                        i += 1
                elif snbt_content[i:i+2] == "/*":
                    i += 2
                    while i < n and not (snbt_content[i] == '*' and snbt_content[i+1:i+2] == '/'):
                        i += 1
                    i += 2
                elif snbt_content[i] == '#':
                    i += 1
                    while i < n and snbt_content[i] != '\n':
                        i += 1
                else:
                    break

        def parse_string_literal() -> str:
            nonlocal i
            quote_char = snbt_content[i]
            i += 1  # skip opening quote
            chars = []
            while i < n:
                c = snbt_content[i]
                if c == '\\':
                    i += 1
                    if i < n:
                        next_c = snbt_content[i]
                        if next_c == 'n':
                            chars.append('\n')
                        elif next_c == 'r':
                            chars.append('\r')
                        elif next_c == 't':
                            chars.append('\t')
                        elif next_c == '"':
                            chars.append('"')
                        elif next_c == "'":
                            chars.append("'")
                        elif next_c == '\\':
                            chars.append('\\')
                        else:
                            chars.append(next_c)
                        i += 1
                elif c == quote_char:
                    i += 1  # skip closing quote
                    break
                else:
                    chars.append(c)
                    i += 1
            return "".join(chars)

        def parse_list() -> List[Any]:
            nonlocal i
            items = []
            i += 1  # skip '['
            while i < n:
                skip_whitespace_and_comments()
                if i >= n:
                    break
                if snbt_content[i] == ']':
                    i += 1
                    break
                val = parse_value()
                items.append(val)
                skip_whitespace_and_comments()
                if i < n and snbt_content[i] == ',':
                    i += 1
            return items

        def parse_key() -> str:
            nonlocal i
            skip_whitespace_and_comments()
            if i < n and (snbt_content[i] == '"' or snbt_content[i] == "'"):
                return parse_string_literal()
            start = i
            while i < n and (snbt_content[i].isalnum() or snbt_content[i] in '._-:'):
                i += 1
            return snbt_content[start:i].strip()

        def parse_value() -> Any:
            nonlocal i
            skip_whitespace_and_comments()
            if i >= n:
                return None
            c = snbt_content[i]
            if c == '"' or c == "'":
                return parse_string_literal()
            elif c == '[':
                return parse_list()
            elif c == '{':
                # Nested compound
                i += 1
                sub_dict = {}
                while i < n:
                    skip_whitespace_and_comments()
                    if i < n and snbt_content[i] == '}':
                        i += 1
                        break
                    k = parse_key()
                    skip_whitespace_and_comments()
                    if i < n and snbt_content[i] == ':':
                        i += 1
                    v = parse_value()
                    if k:
                        sub_dict[k] = v
                    skip_whitespace_and_comments()
                    if i < n and snbt_content[i] == ',':
                        i += 1
                return sub_dict
            else:
                # Bare value / number / boolean
                start = i
                while i < n and snbt_content[i] not in ',}\]\n\r\t':
                    i += 1
                val_str = snbt_content[start:i].strip()
                if val_str.lower() == 'true':
                    return True
                elif val_str.lower() == 'false':
                    return False
                return val_str

        # Top level must start with '{' or is a sequence of key-values
        skip_whitespace_and_comments()
        if i < n and snbt_content[i] == '{':
            i += 1

        try:
            while i < n:
                skip_whitespace_and_comments()
                if i >= n:
                    break
                if snbt_content[i] == '}':
                    i += 1
                    break
                k = parse_key()
                if not k:
                    i += 1
                    continue
                skip_whitespace_and_comments()
                if i < n and snbt_content[i] == ':':
                    i += 1
                v = parse_value()
                result[k] = v
                skip_whitespace_and_comments()
                if i < n and snbt_content[i] == ',':
                    i += 1
            return True, None, result
        except Exception as e:
            return False, f"SNBT parse error: {e}", result

    def parse_file(self, file_path: Path) -> Tuple[bool, Optional[str], Dict[str, Any]]:
        if not file_path.exists():
            return False, f"File not found: {file_path}", {}
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                content = file_path.read_text(encoding="utf-8-sig")
            except Exception as e:
                return False, f"Error decoding file: {e}", {}
        return self.parse_string(content)

    def extract_quests(self, data: Dict[str, Any]) -> Dict[str, QuestEntry]:
        """Extracts structured QuestEntry objects from parsed SNBT data."""
        quests: Dict[str, QuestEntry] = {}
        for key, val in data.items():
            if key.startswith("quest."):
                parts = key.split(".")
                if len(parts) >= 3:
                    quest_id = parts[1]
                    field = parts[2]
                    if quest_id not in quests:
                        quests[quest_id] = QuestEntry(quest_id=quest_id)

                    if field == "title" and isinstance(val, str):
                        quests[quest_id].title = val
                    elif field == "quest_subtitle" and isinstance(val, str):
                        quests[quest_id].subtitle = val
                    elif field == "quest_desc":
                        if isinstance(val, list):
                            quests[quest_id].description = val
                        elif isinstance(val, str):
                            quests[quest_id].description = [val]
        return quests
