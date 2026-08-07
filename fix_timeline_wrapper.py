import re

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Re-centering timeline graphic anchors outside equation scopes...")

# 1. Broadly purge any broken table/figure remnants causing the line 217 hang
content = re.sub(r"\\begin\{table\}\[htbp\].*?somatic\_chronology\_timeline\.png.*?\\end\{table\}", "", content, flags=re.DOTALL)
content = re.sub(r"\\begin\{figure\}\[htbp\].*?somatic\_chronology\_timeline\.png.*?\\end\{figure\}", "", content, flags=re.DOTALL)

# 2. Target the exact text area right after the Jaccard equation and inject a pristine figure block
bad_transition = r"""\begin{equation}
J_{\text{slide}}(T_i, S_j) = \frac{|f_W(T_i) \cap f_W(S_j)|}{|f_W(T_i) \cup f_W(S_j)|}
\end{equation}
    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}
    \label{fig:somatic_chronology}
    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}"""

good_transition = r"""\begin{equation}
J_{\text{slide}}(T_i, S_j) = \frac{|f_W(T_i) \cap f_W(S_j)|}{|f_W(T_i) \cup f_W(S_j)|}
\end{equation}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}
    \label{fig:somatic_chronology}
\end{figure}"""

# Apply literal string clean sweep
if bad_transition in content:
    content = content.replace(bad_transition, good_transition)
else:
    # Aggressive fallback sweep matching just the equation closure and caption string
    anchor = r"\end{equation}"
    parts = content.split(anchor, 1)
    if len(parts) > 1:
        # Strip out loose loose caption remnants sitting below the equation split
        remainder = re.sub(r"^\s*\\caption\{.*?\}.*?outputs/visualizations/somatic_chronology_timeline\.png\}", "", parts[1], flags=re.DOTALL)
        content = parts[0] + anchor + "\n\n" + """\\begin{figure}[htbp]
    \\centering
    \\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}
    \\label{fig:somatic_chronology}
\\end{figure}""" + remainder

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Timeline graphics block cleanly wrapped and sealed.")
