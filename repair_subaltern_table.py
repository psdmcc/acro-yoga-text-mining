import re

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Locate the corrupted block fragment and replace it with pristine, compiling LaTeX code
bad_table_content = r"""\caption{Computational Skill Map and Attestation Heatmap of Subaltern Cohorts}
\label{tab:skill_heatmap}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lccccc}
\hline
\textbf{Group / Cohort} & \textbf{Ritual Role} & \textbf{Entertainment} & \textbf{Physical Skills} & \textbf{Magical Arts} & \textbf{Medicinal/Herbal} \\ \hline
\textit{Ca\d{n}\d{d}\={a}la}      & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $quare$ \\
\textit{Sop\={a}ka}       & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ \\
\textit{Pulkasa}      & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $quare$ & $\blacksquare\blacksquare$ \\
\textit{Kir\={a}ta}       & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ \\
\textit{Pulinda}      & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ \\
\textit{\={A}bh\={i}ra}       & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $quare$ & $\blacksquare$ \\
\textit{H\={u}\d{n}a}         & $\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $quare$ \\
\textit{Yavana}       & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $quare$ \\
\textit{Mleccha}      & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $quare$ \\
\textit{M\={a}gadha}      & $\blacksquare\blacksquare$ & $quare$ & $\blacksquare$ & $quare$ & $\blacksquare\blacksquare$ \\
\textit{K\d{s}atta}       & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $quare$ & $\blacksquare$ \\
\textit{M\={u}lavikrēt\={a}}  & $\blacksquare\blacksquare$ & $quare$ & $\blacksquare$ & $quare$ & $\blacksquare\blacksquare$ \\ \hline"""

good_table_content = r"""\caption{Computational Skill Map and Attestation Heatmap of Subaltern Cohorts}
\label{tab:skill_heatmap}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lccccc}
\hline
\textbf{Group / Cohort} & \textbf{Ritual Role} & \textbf{Entertainment} & \textbf{Physical Skills} & \textbf{Magical Arts} & \textbf{Medicinal/Herbal} \\ \hline
\textit{Ca\d{n}\d{d}\={a}la}      & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\square$ \\
\textit{Sop\={a}ka}       & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ \\
\textit{Pulkasa}      & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare\blacksquare$ \\
\textit{Kir\={a}ta}       & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ \\
\textit{Pulinda}      & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ \\
\textit{\={A}bh\={i}ra}       & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ \\
\textit{H\={u}\d{n}a}         & $\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\square$ \\
\textit{Yavana}       & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ \\
\textit{Mleccha}      & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ \\
\textit{M\={a}gadha}      & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ & $\square$ & $\blacksquare\blacksquare$ \\
\textit{K\d{s}atta}       & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ \\
\textit{M\={u}lavikrēt\={a}}  & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ & $\square$ & $\blacksquare\blacksquare$ \\ \hline"""

# Replace the broken string block entirely
text = text.replace(bad_table_content, good_table_content)

# Fallback clean replacement to scrub any lingering lone square errors inside tabular fields
text = text.replace("$quare$", r"$\square$")
text = text.replace(" & \n", " & ")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Subaltern attestation table matrix fully repaired.")
