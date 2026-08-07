import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Running broad regex pattern matching for damaged headings...")

# 1. Fix variations of subsubsections
text = re.sub(r'\\?ububection\{', r'\\subsubsection{', text)
text = re.sub(r'\\?ubsubection\{', r'\\subsubsection{', text)

# 2. Fix variations of subsections (e.g., \ubsection, ubsection, \ubection, ubection)
text = re.sub(r'\\?ubsection\{', r'\\subsection{', text)
text = re.sub(r'\\?ubection\{', r'\\subsection{', text)

# 3. Fix variations of sections (e.g., \ection, ection)
text = re.sub(r'\\?ection\{', r'\\section{', text)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Comprehensive section heading sweep complete.")
