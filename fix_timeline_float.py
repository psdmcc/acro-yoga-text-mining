import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Enclosing loose timeline image parameters inside a valid figure float...")

# Target the exact un-wrapped layout text block from your file
bad_layout = r"""This diachronic trend confirms a long-term civilizational transition where active, volatile physical skills were systematically turned inward and stripped of their socio-political threat to service centralized orthodoxies.
 \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
 \caption{The Contortionist Turn: Diachronic Evolution of the Acro-Yoga Complex. The network centrality curves document an acute, non-linear structural inversion between independent subaltern mobility (green) and localized somatic enclosure (purple) across three millennia.}
 \label{fig:inversion_curve}"""

good_layout = r"""This diachronic trend confirms a long-term civilizational transition where active, volatile physical skills were systematically turned inward and stripped of their socio-political threat to service centralized orthodoxies.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \caption{The Contortionist Turn: Diachronic Evolution of the Acro-Yoga Complex. The network centrality curves document an acute, non-linear structural inversion between independent subaltern mobility (green) and localized somatic enclosure (purple) across three millennia.}
    \label{fig:inversion_curve}
\end{figure}"""

# Perform literal text swap pass to clean up the structural hierarchy
if bad_layout in content:
    content = content.replace(bad_layout, good_layout)
    print("[SUCCESS] Exact block match replaced.")
else:
    # Fallback sweep matching loose variants with potential whitespace differences
    content = content.replace(
        r"\includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}",
        r"\begin{figure}[htbp]\n    \centering\n    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}"
    )
    content = content.replace(
        r"\label{fig:inversion_curve}",
        r"\label{fig:inversion_curve}\n\end{figure}"
    )
    print("[SUCCESS] Alternative environment normalization forced.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)
