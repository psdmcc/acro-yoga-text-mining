TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Wrapping the somatic matrix block inside a valid figure float...")

# Target the exact loose configuration block from your dump
bad_block = r"""    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_overlap_matrix.png}
    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Contortion. Composite density profiles aggregated across GRETIL and DCS repositories isolate severe non-linear outliers along the caravan transit, espionage, and leaping density vectors.}
    \label{fig:outliers_plot}"""

good_block = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_overlap_matrix.png}
    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Contortion. Composite density profiles aggregated across GRETIL and DCS repositories isolate severe non-linear outliers along the caravan transit, espionage, and leaping density vectors.}
    \label{fig:outliers_plot}
\end{figure}"""

content = content.replace(bad_block, good_block)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Matrix graphic successfully encapsulated.")
