import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Cleaning up stray \\s commands before headings...")

# Remove any stray \s commands followed by a sectioning macro
text = re.sub(r'\\s\s*\\subsection\{', r'\\subsection{', text)
text = re.sub(r'\\s\s*\\section\{', r'\\section{', text)
text = re.sub(r'\\s\s*\\subsubsection\{', r'\\subsubsection{', text)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Stray \\s patterns scrubbed.")
