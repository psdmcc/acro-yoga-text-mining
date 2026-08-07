with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Target any lingering paragraph layout configurations from the previous passes
bad_layouts = [
r"""\begin{quote}
\small
\noindent\textit{parvat\={a}gre\d{s}u ghore\d{s}u nad\={\i}\d{s}u ca guh\={a}su ca /} \\
\hspace*{1.5em}\textit{\'{s}abarair barbarai\'{s} caiva pulindai\'{s} ca sup\={u}jit\={a} // (Hariva\d{m}\'{s}a Appendix 1.4)}
\end{quote}""",
r"""\begin{flushright}
\small
\textit{parvat\={a}gre\d{s}u ghore\d{s}u nad\={\i}\d{s}u ca guh\={a}su ca /} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\
\textit{\'{s}abarair barbarai\'{s} caiva pulindai\'{s} ca sup\={u}jit\={a} // (Hariva\d{m}\'{s}a Appendix 1.4)}
\end{flushright}"""
]

# Force-inject the absolute left-aligned, stacked two-line block
good_layout = r"""\begin{quote}
\small
\noindent\textit{parvat\={a}gre\d{s}u ghore\d{s}u nad\={\i}\d{s}u ca guh\={a}su ca /} \\
\noindent\textit{\'{s}abarair barbarai\'{s} caiva pulindai\'{s} ca sup\={u}jit\={a} // (Hariva\d{m}\'{s}a Appendix 1.4)}
\end{quote}"""

for layout in bad_layouts:
    text = text.replace(layout, good_layout)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Verse lines stacked perfectly straight.")
