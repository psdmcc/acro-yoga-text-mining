import re
import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Slicing out unclosed framebox macro remnants...")

# 1. Target any malformed framebox layout blocks that were left open or broken near line 55
pattern = r"\\framebox\{\\begin\{minipage\}[^}]+?\[IMAGE PLACEHOLDER.*?\\end\{minipage\}\}*"
content = re.sub(pattern, "", content, flags=re.DOTALL)

# 2. Direct surgical string replacement for any loose fragments left near line 55
content = content.replace(r"\framebox{\begin{minipage}[c][0.4\textheight][c]{0.85\textwidth}\centering", "")
content = content.replace(r"\end{minipage}}", "")

# 3. Clean up the standalone figure structure to make sure it is pristine and isolated
bad_figure_area = r"This ritual pole represents the \\textit\{upastambha\}\\gdash the raw, visceral, materialist ``support'' of subaltern kinetic technology\..*?\\includegraphics\[width=0\.85\\textwidth\]\{kamatchiamma\.jpg\}"

good_figure_area = r"""This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``support'' of subaltern kinetic technology.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"""

content = re.sub(bad_figure_area, good_figure_area, content, flags=re.DOTALL)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Fragmented framebox elements completely removed from source.")
