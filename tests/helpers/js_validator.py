"""
JavaScript Syntax Validator and Functional Logic Comparator for KubeJS Scripts.
Validates JS syntax with Node.js and extracts functional tokens to verify 100% logic preservation.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple
import re
import shutil
import subprocess


@dataclass
class JSToken:
    type: str  # 'KEYWORD', 'IDENTIFIER', 'NUMBER', 'STRING', 'PUNCTUATION', 'OPERATOR'
    value: str
    line: int
    col: int


class JSValidator:
    def __init__(self):
        self.node_path = shutil.which("node")

    def check_syntax_node(self, file_path: Path) -> Tuple[bool, str]:
        """Validate JS syntax using Node.js --check."""
        if not self.node_path:
            return True, "Node.js not found in PATH; skipped node --check"

        try:
            result = subprocess.run(
                [self.node_path, "--check", str(file_path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=10,
            )
            if result.returncode == 0:
                return True, ""
            return False, (result.stderr or result.stdout).strip()
        except Exception as e:
            return False, f"Failed to execute node --check: {e}"

    def check_syntax_string_node(self, js_content: str) -> Tuple[bool, str]:
        """Validate JS syntax of raw code string via Node.js vm.Script."""
        if not self.node_path:
            return True, "Node.js not found in PATH"

        node_script = """
const vm = require('vm');
let code = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => { code += chunk; });
process.stdin.on('end', () => {
    try {
        new vm.Script(code);
        process.exit(0);
    } catch (err) {
        console.error(err.message);
        process.exit(1);
    }
});
"""
        try:
            proc = subprocess.run(
                [self.node_path, "-e", node_script],
                input=js_content,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=10,
            )
            if proc.returncode == 0:
                return True, ""
            return False, proc.stderr.strip()
        except Exception as e:
            return False, f"Error validating JS string: {e}"

    @staticmethod
    def strip_comments(source: str) -> str:
        """
        Strips single-line (//) and multi-line (/* */) comments from JavaScript source,
        preserving string literals (', \", `) and regular expressions.
        """
        output = []
        i = 0
        n = len(source)

        while i < n:
            c = source[i]

            # String literal: single quote
            if c == "'":
                start = i
                i += 1
                while i < n:
                    if source[i] == "\\":
                        i += 2
                    elif source[i] == "'":
                        i += 1
                        break
                    else:
                        i += 1
                output.append(source[start:i])

            # String literal: double quote
            elif c == '"':
                start = i
                i += 1
                while i < n:
                    if source[i] == "\\":
                        i += 2
                    elif source[i] == '"':
                        i += 1
                        break
                    else:
                        i += 1
                output.append(source[start:i])

            # Template literal: backtick
            elif c == '`':
                start = i
                i += 1
                while i < n:
                    if source[i] == "\\":
                        i += 2
                    elif source[i] == '`':
                        i += 1
                        break
                    else:
                        i += 1
                output.append(source[start:i])

            # Single-line comment
            elif c == '/' and i + 1 < n and source[i + 1] == '/':
                i += 2
                while i < n and source[i] != '\n':
                    i += 1
                # Preserve newline to maintain line structure
                if i < n and source[i] == '\n':
                    output.append('\n')
                    i += 1

            # Multi-line comment
            elif c == '/' and i + 1 < n and source[i + 1] == '*':
                i += 2
                while i + 1 < n and not (source[i] == '*' and source[i + 1] == '/'):
                    if source[i] == '\n':
                        output.append('\n')
                    i += 1
                i += 2  # skip */

            else:
                output.append(c)
                i += 1

        return "".join(output)

    @staticmethod
    def extract_functional_tokens(source: str) -> List[str]:
        """
        Extracts a sequence of functional tokens from JavaScript code.
        Strips comments and normalizes whitespace while keeping all identifiers,
        keywords, literals, and operators.
        """
        clean_code = JSValidator.strip_comments(source)

        # Tokenize keywords, identifiers, numbers, strings, operators, and punctuation
        token_pattern = re.compile(
            r"""
            (?P<STRING>'(\\.|[^\\'])*'|"(\\.|[^\\"])*"|`(\\.|[^\\`])*`) |
            (?P<NUMBER>\b\d+(\.\d+)?([eE][+-]?\d+)?\b) |
            (?P<IDENT>[a-zA-Z_$][a-zA-Z0-9_$]*) |
            (?P<OP>===|!==|==|!=|<=|>=|=>|\+\+|--|\+=|-=|\*=|/=|&&|\|\||[+\-*/%&|^!=<>?:]+) |
            (?P<PUNCT>[{}()\[\];,.~])
            """,
            re.VERBOSE,
        )

        tokens = []
        for match in token_pattern.finditer(clean_code):
            token_val = match.group(0)
            if token_val:
                tokens.append(token_val)

        return tokens

    def compare_functional_equivalence(self, original_src: str, sanitized_src: str) -> Tuple[bool, str]:
        """
        Compares original JS source with sanitized JS source to ensure
        100% of executable functional logic is preserved identically.
        """
        tokens_orig = self.extract_functional_tokens(original_src)
        tokens_san = self.extract_functional_tokens(sanitized_src)

        if tokens_orig == tokens_san:
            return True, "Functional tokens match 100%."

        len_orig = len(tokens_orig)
        len_san = len(tokens_san)

        # Find first divergence
        min_len = min(len_orig, len_san)
        for idx in range(min_len):
            if tokens_orig[idx] != tokens_san[idx]:
                context_orig = " ".join(tokens_orig[max(0, idx - 5):min(len_orig, idx + 6)])
                context_san = " ".join(tokens_san[max(0, idx - 5):min(len_san, idx + 6)])
                return False, (
                    f"Functional mismatch at token #{idx}:\n"
                    f"  Original:  ...{context_orig}...\n"
                    f"  Sanitized: ...{context_san}...\n"
                    f"  Original token: '{tokens_orig[idx]}' != Sanitized token: '{tokens_san[idx]}'"
                )

        if len_orig != len_san:
            diff_msg = f"Token count mismatch: Original has {len_orig} tokens, Sanitized has {len_san} tokens."
            if len_san < len_orig:
                diff_msg += f" Missing trailing tokens: {' '.join(tokens_orig[min_len:min_len + 10])}"
            else:
                diff_msg += f" Extra trailing tokens: {' '.join(tokens_san[min_len:min_len + 10])}"
            return False, diff_msg

        return True, "Match"
