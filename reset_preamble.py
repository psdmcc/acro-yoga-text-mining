import re

with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Clean out all structural tags around the top of the file to prepare a blank canvas
text = text.replace("\\begin{document}", "")
text = text.replace("\\maketitle", "")
text = text.replace("\\begin{abstract}", "")

# 2. Extract everything from the opening word of your abstract down to the end of the file
abstract_start_phrase = "This paper introduces the ``Contortionist Turn,''"
if abstract_start_phrase in text:
    body_content = text.split(abstract_start_phrase, 1)[1]
else:
    # Fallback to prevent data loss if the phrase was modified by previous regex passes
    body_content = text

# 3. Construct a standard, minimized academic preamble header block
new_preamble = """\\documentclass[11pt,twoside,letterpaper]{article}

% -- Core System Layout Packages --
\\usepackage{geometry}
\\geometry{letterpaper, margin=1in, bindingoffset=0in}
\\usepackage{amsmath, amssymb}
\\usepackage{microtype}
\\usepackage{graphicx}
\\usepackage[dvipsnames,table]{xcolor}
\\usepackage{url}

% -- Unified Citation and Routing Systems --
\\usepackage[round,authoryear]{natbib}
\\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}

% -- Custom Spaced En-Dash Shorthand Definitions --
\\renewcommand{\\textemdash}{\\, -- \\,}
\\newcommand{\\gdash}{\\,--\\,}

% -- Manuscript Metadata Fields --
\\title{\\textbf{The Contortionist Turn:\\\\Computational Text-Mining, Scholastic Capture, and the Flattening of the Indian Martial Body}}
\\author{\\textbf{Patrick S. D. McCartney}\\\\
\\textit{Research Affiliate, Anthropological Institute, Nanzan University, Japan}\\\\
\\textit{School of Culture, History and Language, Australian National University, Australia}\\\\
\\textit{Centre for Religious Studies, Manipal Academy of Higher Education, India}\\\\
\\texttt{u4556787@anu.edu.au}}
\\date{July 31, 2026}

% =====================================================================
% MAIN TEXT BODY INITIALIZATION
% =====================================================================
\\begin{document}
\\maketitle

\\begin{abstract}
This paper introduces the ``Contortionist Turn,'' """

# 4. Synthesize the new header cleanly with your running text body content
final_manuscript = new_preamble + body_content

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(final_manuscript)

print("[SUCCESS] New academic preamble successfully compiled onto disk.")
