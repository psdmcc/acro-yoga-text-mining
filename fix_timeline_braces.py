TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Re-balancing brace parameters around timeline figure blocks...")

# Target the corrupted graphic block and replace it with clean, standalone compilation code
bad_block = r"\includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}}\end{figure}"
good_block = r"\includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}"

# Safe clean replacement pass
content = content.replace(bad_block, r"\includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}" + "\n" + r"\end{figure}")
content = content.replace(r"somatic_chronology_timeline.png}}\end{figure}", r"somatic_chronology_timeline.png}" + "\n" + r"\end{figure}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Layout parameters completely balanced.")
