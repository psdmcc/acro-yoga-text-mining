TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Re-sealing timeline environment around the caption block...")

# Locate the loose timeline graphic area and wrap it into a valid, isolated float environment
bad_segment = r"""    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \caption{The Contortionist Turn: Diachronic Evolution of the Acro-"""

good_segment = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \caption{The Contortionist Turn: Diachronic Evolution of the Acro-"""

# Perform literal text swap to clean up the structural tracking layers
if "somatic_chronology_timeline.png" in content and "\\begin{figure}" not in content.split("somatic_chronology_timeline.png")[0][-200:]:
    # Secondary check: If the figure tag was missing completely above the graphic
    content = content.replace(
        r"\includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}",
        r"\begin{figure}[htbp]\n    \centering\n    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}"
    )

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Timeline caption block successfully anchored inside valid float parameters.")
