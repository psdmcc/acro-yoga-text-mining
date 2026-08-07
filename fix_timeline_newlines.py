import os

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Stripping literal escape character strings from the timeline block...")

# Replace the broken string block containing the literal \n characters
bad_block = r"\begin{figure}[htbp]\n    \centering\n    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}"

good_block = """\\begin{figure}[htbp]
    \\centering
    \\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}"""

content = content.replace(bad_block, good_block)

# Clean up the trailing environment closure if it has identical formatting artifacts
content = content.replace(r"\label{fig:inversion_curve}\n\end{figure}", "\\label{fig:inversion_curve}\n\\end{figure}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Timeline float parameters sanitized.")
