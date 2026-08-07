import re
import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Sweeping document to erase every trace of the old figure block...")

# 1. Broadly strip out any existing figure environments containing kamatchiamma.jpg
# This pattern catches the environment regardless of any hidden, broken formatting wrappers
pattern_purge = r"\\begin\{figure\}.*?kamatchiamma\.jpg.*?\\end\{figure\}"
content = re.sub(pattern_purge, "", content, flags=re.DOTALL)

# 2. Direct literal cleanup for any loose, fragmented tags left behind by previous passes
content = content.replace(r"\begin{figure}[htbp]", "")
content = content.replace(r"\begin{figure}[t]", "")
content = content.replace(r"\end{figure}", "")
content = content.replace(r"\centering", "")
content = content.replace(r"\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}", "")
content = content.replace(r"\caption{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout \citep{VAM2024}.", "")
content = content.replace(r"\label{fig:kamatchi_acrobats}", "")

print("[*] Re-injecting pristine figure block into outer paragraph mode...")

# Define the exact text marker where the introductory opening text ends
target_anchor = r"re-engineered into the quietistic, metaphysical spinal column (\textit{meruda\d{n}\d{d}a}) of the institutionalized yogic corpus."

# Define the perfectly structured, standalone floating figure environment
pristine_figure_block = r"""re-engineered into the quietistic, metaphysical spinal column (\textit{meruda\d{n}\d{d}a}) of the institutionalized yogic corpus.

\begin{figure}[t]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
    \caption{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout \citep{VAM2024}.}
    \label{fig:kamatchi_acrobats}
\end{figure}"""

if target_anchor in content:
    content = content.replace(target_anchor, pristine_figure_block)
    print("[SUCCESS] Manuscript source successfully sterilized and re-added.")
else:
    print("[!] Error: Could not locate introduction target anchor text inside the file.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)
