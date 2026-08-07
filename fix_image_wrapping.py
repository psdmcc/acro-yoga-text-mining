import re

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Separating text blocks from the figure environment grid...")

# Target the entire text block around the image area
bad_layout = r"""This performance is not mere secular entertainment; it is the enactment of an ancient combat myth wherein the hero V\={\i}rab\={a}hu slew Vajrab\={a}hu, physically transforming the victim's spinal column into a vertical performance pole, his bones into structural fasteners, his connective tissues into stabilizing guidelines, and his skull into a clanging victory bell (\textit{jaya-ma\d{n}i}) hoisted at the temple threshold \citep{ThurstonRangachari1909}. This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
\caption{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout \citep{VAM2024}.}
\label{fig:kamatchi_acrobats}
\end{figure}"""

# Reconstruct with explicit paragraph spacing and a clean figure block
good_layout = r"""This performance is not mere secular entertainment; it is the enactment of an ancient combat myth wherein the hero V\={\i}rab\={a}hu slew Vajrab\={a}hu, physically transforming the victim's spinal column into a vertical performance pole, his bones into structural fasteners, his connective tissues into stabilizing guidelines, and his skull into a clanging victory bell (\textit{jaya-ma\d{n}i}) hoisted at the temple threshold \citep{ThurstonRangachari1909}. This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
    \caption{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout \citep{VAM2024}.}
    \label{fig:kamatchi_acrobats}
\end{figure}"""

# Replace text if an exact match is found
if bad_layout in text:
    text = text.replace(bad_layout, good_layout)
else:
    # Aggressive fallback: locate just the graphic tag and isolate it completely
    text = text.replace(r"\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}", r"""

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}""")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Image and paragraph text blocks cleanly decoupled.")
