TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the direct image inclusion with a structural draft bounding box layout
bad_figure = r"\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"
good_figure = r"\framebox{\begin{minipage}[c][0.4\textheight][c]{0.85\textwidth}\centering [IMAGE PLACEHOLDER: kamatchiamma.jpg]\end{minipage}}"

text = text.replace(bad_figure, good_figure)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Figure layout shifted to safe bounding box matrix.")
