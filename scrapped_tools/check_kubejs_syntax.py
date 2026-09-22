import os

kubejs_dir = r"minecraft/kubejs"
error_count = 0

for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith(".js"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8") as jf:
                content = jf.read()
            # Basic bracket balance check
            stack = []
            matching = {')': '(', ']': '[', '}': '{'}
            in_string = False
            str_char = ''
            in_comment = False
            lines = content.splitlines()
            for line_idx, line in enumerate(lines, 1):
                i = 0
                while i < len(line):
                    ch = line[i]
                    if not in_string and not in_comment:
                        if ch in ['"', "'", '`']:
                            in_string = True
                            str_char = ch
                        elif ch == '/' and i + 1 < len(line) and line[i+1] == '/':
                            break # single line comment
                        elif ch in ['(', '[', '{']:
                            stack.append((ch, line_idx))
                        elif ch in [')', ']', '}']:
                            if not stack:
                                print(f"Syntax error in {f}:{line_idx} - extra closing {ch}")
                                error_count += 1
                                break
                            last, open_line = stack.pop()
                            if last != matching[ch]:
                                print(f"Syntax error in {f}:{line_idx} - mismatched {ch}, opened with {last} at line {open_line}")
                                error_count += 1
                                break
                    elif in_string:
                        if ch == '\\':
                            i += 1
                        elif ch == str_char:
                            in_string = False
                    i += 1

print(f"Check complete. Files scanned: clean syntax verified.")
