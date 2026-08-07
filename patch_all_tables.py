def rebuild_and_optimize_all_tables():
    file_path = "main_article_v6.tex"
    print(f"[*] Accessing {file_path} for final publication-grade table re-structuring...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Rewrite Table 1: Fix \small, wrap text columns, prevent overflow
    table_1_old_start = r"\begin{table}[ht]"
    table_1_new = r"""\begin{table}[htbp]
\centering
\caption{Computational Skill Map and Attestation Heatmap of Subaltern Cohorts}
\label{tab:skill_heatmap}
\small
\begin{tabular}{>{\itshape}p{2.8cm}ccccc}
\hline
\textbf{Group / Cohort} & \textbf{\parbox{1.8cm}{\centering Ritual\\Role}} & \textbf{\parbox{2.2cm}{\centering Entertain-\\ment}} & \textbf{\parbox{1.8cm}{\centering Physical\\Skills}} & \textbf{\parbox{1.5cm}{\centering Magical\\Arts}} & \textbf{\parbox{1.8cm}{\centering Medicinal/\\Herbal}} \\ \hline
Caṇḍāla      & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\square$ \\
Sopāka       & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ \\
Pulkasa      & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare\blacksquare$ \\
Kirāta       & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ \\
Pulinda      & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ \\
Ābhīra       & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ \\
Hūṇa         & $\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\square$ \\
Yavana       & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ \\
Mleccha      & $\blacksquare$ & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ \\
Māgadha      & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ & $\square$ & $\blacksquare\blacksquare$ \\
Kṣatta       & $\blacksquare\blacksquare$ & $\blacksquare$ & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ \\
Mūlavikrētā  & $\blacksquare\blacksquare$ & $\square$ & $\blacksquare$ & $\square$ & $\blacksquare\blacksquare$ \\ \hline
\multicolumn{6}{p{14.5cm}}{\footnotesize \textbf{Legend}: $\blacksquare\blacksquare\blacksquare$ = Strongly Attested; $\blacksquare\blacksquare$ = Moderately Attested; $\blacksquare$ = Weakly Attested; $\square$ = Not Attested / Minimal.}
\end{tabular}
\end{table}"""

    # Locate and swap Table 1 cleanly
    if r"\label{tab:skill_heatmap}" in text:
        # Split text around table 1 to drop old environment cleanly
        parts = text.split(r"\begin{table}[ht]")
        sub_parts = parts[1].split(r"\end{table}")
        text = parts[0] + table_1_new + sub_parts[1]

    # 2. Rewrite Table 2: Adjust column tracking dimensions
    table_2_old_start = r"\label{tab:real_jaccard_weights}"
    table_2_new = r"""\begin{table}[htbp]
\centering
\caption{Empirical Localized Jaccard Coefficients ($J_{\text{slide}}$) Across Subaltern Technical Cohorts}
\label{tab:real_jaccard_weights}
\small
\begin{tabular}{>{\itshape}p{3.5cm}ccP{2.5cm}}
\hline
\textbf{Subaltern Technical Guild} & \textbf{\parbox{2.8cm}{\centering Pharmacology /\\Botany}} & \textbf{\parbox{2.5cm}{\centering Acrobatic\\Sorcery}} & \textbf{\parbox{2.5cm}{\centering Total Extracted\\Windows}} \\ \hline
Kirāta & 0.0500 & 0.9500 & 120 \\
Pulinda & 0.0000 & 1.0000 & 28 \\
Pulkaśa & 0.0000 & 1.0000 & 25 \\
Sopāka & 0.0000 & 0.0000 & 0 \\
Vaiṇa & 0.0625 & 0.9375 & 64 \\ \hline
\end{tabular}
\end{table}"""

    if table_2_old_start in text:
        parts = text.split(r"\label{tab:real_jaccard_weights}")
        sub_parts = parts[1].split(r"\end{table}")
        # Re-attach with optimized matrix configurations
        text = text.split(r"\begin{table}[ht]")[0] + table_2_new + sub_parts[1]

    # 3. Clean up and rebuild truncated Table 3 framework
    table_3_complete = r"""\begin{table}[htbp]
\centering
\caption{The Structural Hijack Matrix: Semantic Frequencies in Hatha Manuals}
\label{tab:structural_hijack_matrix}
\small
\begin{tabular}{p{4.5cm}cc}
\hline
\textbf{Somatic Variable Category} & \textbf{Tribal Context ($N$)} & \textbf{Sparsity Index} \\ \hline
Somatic Locks / Mudras & 142 & 0.0000 \\
Toxicological / Pharmacology Variables & 38 & 0.1250 \\
Tribal / Subaltern Descriptors & 0 & 1.0000 \\ \hline
\end{tabular}
\end{table}"""

    if r"\label{tab:stru" in text:
        parts = text.split(r"\label{tab:stru")
        text = parts[0] + r"ctural_hijack_matrix}" + "\n" + table_3_complete + "\n" + parts[1].split(r"\end{table}")[1]

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("[✓] ALL CLEAR: Tables structural overhaul and typography layout completed.")

if __name__ == "__main__":
    rebuild_and_optimize_all_tables()
