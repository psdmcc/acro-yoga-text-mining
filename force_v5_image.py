import re

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Locating image placeholder token...")

# 1. Target the literal placeholder token and clear out its specific frame wrappers
pattern = r"\\framebox\{\\begin\{minipage\}[^}]+?\[IMAGE PLACEHOLDER: kamatchiamma\.jpg\]\\end\{minipage\}\}"
text = re.sub(pattern, r"\\includegraphics[width=0.85\\textwidth]{kamatchiamma.jpg}", text, flags=re.DOTALL)

# 2. Secondary fallback sweep: target just the text token loose inside the figure environment
text = text.replace("[IMAGE PLACEHOLDER: kamatchiamma.jpg]", r"\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}")

# 3. Clean up any accidental double-nested graphics codes if both rules hit
text = text.replace(r"\includegraphics[width=0.85\textwidth]{\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}}", r"\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] v5 source code updated with native image markers.")
