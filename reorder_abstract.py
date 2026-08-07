import re

with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Strip out any stray or misplaced \begin{document} calls completely
text = text.replace("\\begin{document}", "")

# 2. Locate the abstract closing marker and insert the document body trigger right there
# This ensures that the abstract compiles as clean metadata before the body stream initiates
text = text.replace("\\end{abstract}", "\\end{abstract}\n\\begin{document}")

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Abstract ordering fixed globally.")
