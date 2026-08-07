import re

# 1. Define your raw source text
latex_document = r"""
\documentclass{article}
\usepackage{graphicx}
\usepackage{amsmath}

\title{\textbf{The Contortionist Turn: Computational Text-Mining, Scholastic Capture, and the Flattening of the Indian Martial Body}}

\author{%
  \small Patrick S. D. MacCartney (Research Fellow), Anthropological Institute, Nanzan University, Japan;\\
  \small School of Culture, History and Language, Australian National University, Australia; Center for Regional Studies,\\
  \small Manipal Academy of Higher Education, India. Email: \texttt{p9856537@anu.edu.au}\\
  \small \date{August 7, 2026}
}

\begin{document}

\maketitle

\begin{abstract}
This paper outlines the ``Contortionist Turn (CT),'' a materialist framework charting the top-down scholastic capture, sanitization, and flattening of volatile subaltern physical survival practices. By deploying a high-performance parallelized text-mining pipeline across 20,529 Sanskrit text nodes, we track how raw kinetic technologies—engineered by specialized outcaste labor guilds like the \textit{Ḍombas} and \textit{Vaṃśa-nartins} for frontier defense and intelligence systems—were systematically turned inward and repackaged into the passive, quietistic metaphysical spine (\textit{merudaṇḍa}) of institutionalized yoga.
\end{abstract}

\vspace{1.5cm}

\clearpage 

\begin{figure}[p]
 \centering
 \includegraphics[width=0.75\textwidth]{kamatchiamma.jpg}
 \caption[Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances.]{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout.}
 \label{fig:kamatchi_acrobats}
\end{figure}

\clearpage

\section{Introduction: The Contortionist Turn}
At the gates of the gopura of the Sri Kacchi Kāśmīra Avaṇiyā Temple in Kanchipuram, Tamil Nadu, a vertical bamboo pole measuring exactly seventy-two spans... This paradigm shifts what we call the Contortionist Turn into active empirical tracking.

\section{Conclusion}
Ultimately, the Contortionist Turn represents a massive paradigm shift. As the Contortionist Turn settles into mainstream scholarship, we must ensure its roots are remembered.
\end{document}
"""

# 2. Separate text into Main Content and Conclusion to preserve the 1x exception rule
parts = latex_document.split(r"\section{Conclusion}")
main_body = parts[0]
conclusion_body = parts[1] if len(parts) > 1 else ""

# 3. Replace all remaining instances of the full phrase with "CT" in the main body
# We skip the very first definition block inside the abstract manually
main_body_processed = re.sub(r"(?<!the ``)Contortionist Turn(?! \(CT\))", "CT", main_body)

# 4. Handle the conclusion rules (Allow precisely 1 instance, convert the rest)
if conclusion_body:
    matches = list(re.finditer(r"Contortionist Turn", conclusion_body))
    if len(matches) > 1:
        # Keep the first match intact, switch all subsequent ones to CT
        first_match_end = matches[0].end()
        remainder = conclusion_body[first_match_end:]
        fixed_remainder = remainder.replace("Contortionist Turn", "CT")
        conclusion_body = conclusion_body[:first_match_end] + fixed_remainder

# Reconstruct the corrected LaTeX source code string
final_latex = main_body_processed + r"\section{Conclusion}" + conclusion_body

# 5. Safely write out the pristine .tex file to your workspace
with open("main_article_v10.tex", "w", encoding="utf-8") as f:
    f.write(final_latex)

print("SUCCESS: File 'main_article_v10.tex' generated with isolated figures and CT abbreviations applied safely!")
