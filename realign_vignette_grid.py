TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Re-ordering visual anchors to optimize page compilation...")

# Isolate the exact figure block environment
figure_block = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
    \caption{Mid-nineteenth-century gouache on mica depicting Trichinopoly acrobat performances, showing vertical pole-balancing and suspended rope-somatic dynamics matching the historical \textit{upastambha} layout \citep{VAM2024}.}
    \label{fig:kamatchi_acrobats}
\end{figure}"""

# Purge it from its current position below the paragraph
content = content.replace(figure_block, "")

# Re-inject the figure environment right after \maketitle so it compiles at the top of page 1
target_entry = "\\maketitle"
if target_entry in content:
    content = content.replace(target_entry, "\\maketitle\n\n" + figure_block)
    print("[SUCCESS] Figure successfully hoisted to chapter headline anchor.")
else:
    print("[!] Warning: Preamble marker not found.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)
