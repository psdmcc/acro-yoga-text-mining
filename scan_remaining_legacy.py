import re

def scan_only_legacy_fragments():
    file_path = "main_article_v5.tex"
    print(f"[*] Auditing {file_path} for remaining legacy formatting fragments...")
    print("=" * 60)
    print(f"{'Line':<8} | {'Legacy Fragment Found'}")
    print("=" * 60)

    # Comprehensive regex targeting all legacy variations with or without braces
    legacy_regex = re.compile(
        r'\\d\{[a-zA-Z]\}|\\=\{[a-zA-Z]\}|\\\'\{[a-zA-Z]\}|\\\~\{[a-zA-Z]\}|\\\'[sS]|\\=[a-zA-Z]|\\d\{.*?\}|\\=\d|\\={\\i}'
    )

    count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line_content in enumerate(f, 1):
            matches = legacy_regex.findall(line_content)
            if matches:
                # Remove duplicate matches found on the exact same line for clean output
                unique_matches = sorted(list(set(matches)))
                for match in unique_matches:
                    print(f"{line_num:<8} | {match}")
                    count += 1

    print("=" * 60)
    print(f"[✓] SCAN COMPLETE: Isolated {count} remaining legacy fragments.")

if __name__ == "__main__":
    scan_only_legacy_fragments()
