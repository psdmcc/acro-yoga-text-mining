import re
import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Sweeping document layout lines for loose figure strings...")

# Regex pattern that matches "As illustrated in Figure 2" regardless of internal spaces or line breaks
pattern = r"As\s+illustrated\s+in\s+Figure\s+2"

# Replace with the standard dynamic LaTeX reference macro tag
content = re.sub(pattern, r"As illustrated in Figure~\\ref{fig:kamatchi_acrobats}", content)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Hardcoded layout labels converted to dynamic cross-references.")
