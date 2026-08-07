with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Reconstruct a clean, non-commented, bounded preamble layout block
clean_header = [
    "\\documentclass[11pt,twoside,letterpaper]{article}\n",
    "\\usepackage{geometry}\n",
    "\\geometry{letterpaper, margin=1in, bindingoffset=0in}\n",
    "\\usepackage{amsmath, amssymb}\n",
    "\\usepackage{listings}\n",
    "\\usepackage{microtype}\n",
    "\\usepackage{graphicx}\n",
    "\\usepackage[dvipsnames,table]{xcolor}\n",
    "\\usepackage[round,authoryear]{natbib}\n",
    "\\usepackage{url}\n",
    "\\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}\n",
    "\\makeatletter\n",
    "\\makeatother\n",
    "\\renewcommand{\\textemdash}{\\, -- \\,}\n"
]

# Locate where the abstract or body starts (usually around line 28 in your snippet)
body_index = 0
for i, line in enumerate(lines):
    if "\\begin{abstract}" in line or "\\begin{document}" in line:
        body_index = i
        break

if body_index > 0:
    final_content = "".join(clean_header) + "".join(lines[body_index:])
    with open("main_article_v4.tex", "w", encoding="utf-8") as f:
        f.write(final_content)
    print("[SUCCESS] Preamble package lines restored.")
else:
    print("[!] Error: Could not locate body start index.")
