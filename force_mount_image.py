import re

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Sweeping figure environment to restore native image layout...")

# Target the figure environment and strip whatever layout wrapper is currently inside it
pattern = r"\\begin\{figure\}\[htbp\].*?\\caption"

replacement = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
    \caption"""

# Perform the regex substitution pass
modified_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(modified_content)

print("[SUCCESS] Image code successfully updated in v5 source.")
