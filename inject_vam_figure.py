import os

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Locate the precise end of the second vignette paragraph to anchor the image block
bad_anchor = r"This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology."

good_anchor = r"""This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
    \caption{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout \citep{VAM2024}.}
    \label{fig:kamatchi_acrobats}
\end{figure}"""

if bad_anchor in text:
    text = text.replace(bad_anchor, good_anchor)
    print("[SUCCESS] V&A mica painting figure block injected into opening vignette.")
else:
    print("[!] Error: Vignette target anchor paragraph not found.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)
