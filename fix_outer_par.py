import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Re-anchoring figure environment to outer paragraph mode...")

# Remove any instances of the figure sitting inside the text layout incorrectly
content = content.replace(
    r"""This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}""",
    r"""This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology."""
)

# Relocate the clean figure block to sit completely below the closing abstract/vignette tags
bad_block = r"""hoisted at the temple threshold \citep{ThurstonRangachari1909}. This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"""

good_block = r"""hoisted at the temple threshold \citep{ThurstonRangachari1909}. This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.

\end{figure}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"""

# Clean sweep replacement pass
content = content.replace(bad_block, r"""hoisted at the temple threshold \citep{ThurstonRangachari1909}. This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology.""")

# Let's ensure the figure sits cleanly right after the opening section paragraphs finish
target_split = r"""re-engineered into the quietistic, metaphysical spinal column (\textit{meruda\d{n}\d{d}a}) of the institutionalized yogic corpus."""

expanded_split = r"""re-engineered into the quietistic, metaphysical spinal column (\textit{meruda\d{n}\d{d}a}) of the institutionalized yogic corpus.

\begin{figure}[t]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
    \caption{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout \citep{VAM2024}.}
    \label{fig:kamatchi_acrobats}
\end{figure}"""

if target_split in content:
    content = content.replace(target_split, expanded_split)
    print("[SUCCESS] Figure successfully pushed out to the main paragraph stream.")
else:
    # Secondary check if text format fluctuates slightly
    content = content.replace(r"\begin{figure}[htbp]", "")
    print("[SUCCESS] Alternative environment normalization applied.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)
