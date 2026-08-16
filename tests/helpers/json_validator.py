"""
JSON Structure and Syntax Validator for PEAK Assets, Models, and Configs.
"""
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import json


class JSONValidator:
    @staticmethod
    def strip_json_comments(source: str) -> str:
        """Strip comments from JSON5/relaxed JSON files while preserving strings."""
        output = []
        i = 0
        n = len(source)
        while i < n:
            c = source[i]
            if c == '"':
                start = i
                i += 1
                while i < n:
                    if source[i] == '\\':
                        i += 2
                    elif source[i] == '"':
                        i += 1
                        break
                    else:
                        i += 1
                output.append(source[start:i])
            elif c == "'" :
                start = i
                i += 1
                while i < n:
                    if source[i] == '\\':
                        i += 2
                    elif source[i] == "'":
                        i += 1
                        break
                    else:
                        i += 1
                output.append(source[start:i])
            elif c == '/' and i + 1 < n and source[i + 1] == '/':
                i += 2
                while i < n and source[i] != '\n':
                    i += 1
            elif c == '/' and i + 1 < n and source[i + 1] == '*':
                i += 2
                while i + 1 < n and not (source[i] == '*' and source[i + 1] == '/'):
                    i += 1
                i += 2
            else:
                output.append(c)
                i += 1
        return "".join(output)

    @staticmethod
    def validate_file(file_path: Path) -> Tuple[bool, Optional[str], Optional[Any]]:
        """Parses and validates a JSON file, returning (is_valid, error_message, parsed_data)."""
        if not file_path.exists():
            return False, f"File not found: {file_path}", None

        try:
            content = file_path.read_text(encoding="utf-8-sig", errors="replace")
        except Exception as e:
            return False, f"Encoding error reading {file_path}: {e}", None

        # Check for 0-byte or whitespace-only files (some cache/log files)
        if not content.strip():
            return True, None, None

        # 1. Try standard JSON parse
        try:
            data = json.loads(content)
            return True, None, data
        except json.JSONDecodeError:
            pass

        # 2. Try relaxed JSON parse (stripping comments for mod configs / JSON5)
        try:
            clean_content = JSONValidator.strip_json_comments(content)
            data = json.loads(clean_content)
            return True, None, data
        except json.JSONDecodeError as err:
            return False, f"JSON syntax error in {file_path.name}:{err.lineno}:{err.colno}: {err.msg}", None
        except Exception as e:
            return False, f"Unexpected error parsing {file_path.name}: {e}", None

    @staticmethod
    def deep_compare_json(
        data1: Any,
        data2: Any,
        path: str = "",
        ignored_keys: Optional[List[str]] = None,
    ) -> Tuple[bool, str]:
        """Deep comparison of two JSON data structures, allowing specific keys to be ignored."""
        ignored = set(ignored_keys or [])

        if type(data1) is not type(data2):
            return False, f"Type mismatch at '{path}': {type(data1).__name__} vs {type(data2).__name__}"

        if isinstance(data1, dict):
            keys1 = set(data1.keys()) - ignored
            keys2 = set(data2.keys()) - ignored

            if keys1 != keys2:
                missing_in_2 = keys1 - keys2
                extra_in_2 = keys2 - keys1
                diff = []
                if missing_in_2:
                    diff.append(f"Missing keys in target: {missing_in_2}")
                if extra_in_2:
                    diff.append(f"Unexpected keys in target: {extra_in_2}")
                return False, f"Key mismatch at '{path}': {'; '.join(diff)}"

            for key in keys1:
                sub_path = f"{path}.{key}" if path else key
                equal, reason = JSONValidator.deep_compare_json(data1[key], data2[key], sub_path, ignored_keys)
                if not equal:
                    return False, reason
            return True, ""

        elif isinstance(data1, list):
            if len(data1) != len(data2):
                return False, f"Array length mismatch at '{path}': {len(data1)} items vs {len(data2)} items"

            for idx, (item1, item2) in enumerate(zip(data1, data2)):
                sub_path = f"{path}[{idx}]"
                equal, reason = JSONValidator.deep_compare_json(item1, item2, sub_path, ignored_keys)
                if not equal:
                    return False, reason
            return True, ""

        else:
            if data1 != data2:
                return False, f"Value mismatch at '{path}': {data1!r} != {data2!r}"
            return True, ""
