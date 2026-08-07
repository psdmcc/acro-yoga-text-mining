import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Re-sealing structural boundaries below the Jaccard equation...")

# Define the exact scrambled block from your diagnostic dump
bad_scrambled_chunk = """J_{\\text{slide}}(T_i, S_j) = \\frac{|f_W(T_i) \\cap f_W(S_j)|}{|f_W(T_i) \\cup f_W(S_j)|}
\\end{equation}

\\begin{figure}[t]
    \\centering
    \\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}

\\begin{figure}[t]
    \\centering
    \\label{fig:somatic_chronology}
\\end{figure}
    \\caption{Where $f_W(x)$ defines the localized frequency profile of token $x$ isolated inside the active window envelope. By isolating these contextual envelopes, the pipeline flushes out 82 high-density text files containing valid, cross-category subaltern semantic intersections, ready for granular philological decryption}"""

# Reconstruct a completely valid, un-nested layout stream
good_pristine_chunk = """J_{\\text{slide}}(T_i, S_j) = \\frac{|f_W(T_i) \\cap f_W(S_j)|}{|f_W(T_i) \\cup f_W(S_j)|}
\\end{equation}

\\begin{figure}[htbp]
    \\centering
    \\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}
    \\label{fig:somatic_chronology}
\\end{figure}

Where $f_W(x)$ defines the localized frequency profile of token $x$ isolated inside the active window envelope. By isolating these contextual envelopes, the pipeline flushes out 82 high-density text files containing valid, cross-category subaltern semantic intersections, ready for granular philological decryption."""

if bad_scrambled_chunk in content:
    content = content.replace(bad_scrambled_chunk, good_pristine_chunk)
    print("[SUCCESS] Scrambled figure wrappers completely scrubbed and re-aligned.")
else:
    # Secondary aggressive cleanup check if file whitespace varies slightly
    print("[*] Exact string split match failed. Forcing a surgical block rebuild...")
    anchor = r"J_{\text{slide}}(T_i, S_j) = \frac{|f_W(T_i) \cap f_W(S_j)|}{|f_W(T_i) \cup f_W(S_j)|}"
    if anchor in content:
        parts = content.split(anchor, 1)
        # Cut off the broken macro loop down to the subsection heading anchor
        remainder_parts = parts[1].split(r"\subsection{High-Performance", 1)
        content = parts[0] + anchor + "\n\\end{equation}\n\n" + """\\begin{figure}[htbp]
    \\centering
    \\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}
    \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}
    \\label{fig:somatic_chronology}
\\end{figure}

Where $f_W(x)$ defines the localized frequency profile of token $x$ isolated inside the active window envelope. By isolating these contextual envelopes, the pipeline flushes out 82 high-density text files containing valid, cross-category subaltern semantic intersections, ready for granular philological decryption.

\\subsection{High-Performance""" + remainder_parts[1]
        print("[SUCCESS] Fallback sweep successfully forced structure normalization.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)
