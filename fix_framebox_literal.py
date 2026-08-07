import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Performing direct literal clean-up of unclosed framebox fragments...")

# 1. Broadly clean out any loose minipage or framebox remnants around the figure area
content = content.replace(r"\framebox{\begin{minipage}[c][0.4\textheight][c]{0.85\textwidth}\centering", "")
content = content.replace(r"\end{minipage}}", "")

# 2. Target the exact text-to-figure transition and inject a clean layout split
bad_transition = r"This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"

good_transition = r"""This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"""

content = content.replace(bad_transition, good_transition)

# Fallback check: if the graphic tag has spaces or line breaks around it
fallback_bad = r"support'' of subaltern kinetic technology.\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"
fallback_good = r"""support'' of subaltern kinetic technology.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"""

content = content.replace(fallback_bad, fallback_good)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Manuscript file text blocks successfully decoupled.")
