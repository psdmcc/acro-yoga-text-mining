with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_preamble = [
    "\\documentclass[11pt,twoside,letterpaper]{article}\n",
    "\\usepackage[letterpaper, margin=1in, bindingoffset=0in]{geometry}\n",
    "\\usepackage{amsmath, amssymb}\n",
    "\\usepackage{microtype}\n",
    "\\usepackage{graphicx}\n",
    "\\usepackage[dvipsnames,table]{xcolor}\n",
    "\\usepackage{url}\n",
    "\\usepackage[round,authoryear]{natbib}\n",
    "\\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}\n",
    "\\renewcommand{\\textemdash}{\\, -- \\,}\n",
    "\\newcommand{\\gdash}{\\, -- \\,}\n",
    "\\title{\\textbf{The Contortionist Turn:\\\\Computational Text-Mining, Scholastic Capture, and the Flattening of the Indian Martial Body}}\n"
]

# Find where the author block begins (line 20 in your snippet, index 19)
author_index = None
for i, line in enumerate(lines):
    if "\\author{" in line:
        author_index = i
        break

if author_index is not None:
    final_output = "".join(clean_preamble) + "".join(lines[author_index:])
    with open("main_article_v4.tex", "w", encoding="utf-8") as f:
        f.write(final_output)
    print("[SUCCESS] Core packages and title un-commented.")
else:
    print("[!] Error: Could not parse author baseline.")
