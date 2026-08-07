import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Repairing split subsection commands...")

# Replace any instance where subsection was broken into \subs \section
text = re.sub(r'\\subs\s*\\section\{', r'\\subsection{', text)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Split subsection commands repaired.")
