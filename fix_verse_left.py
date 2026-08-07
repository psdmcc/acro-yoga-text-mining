with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Target the previous flushright layout and swap it for a precise, indented block
bad_layout = r"""\begin{flushright}
\small
\textit{parvat\={a}gre\d{s}u ghore\d{s}u nad\={\i}\d{s}u ca guh\={a}su ca /} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\
\textit{\'{s}abarair barbarai\'{s} caiva pulindai\'{s} ca sup\={u}jit\={a} // (Hariva\d{m}\'{s}a Appendix 1.4)}
\end{flushright}"""

good_layout = r"""\begin{quote}
\small
\noindent\textit{parvat\={a}gre\d{s}u ghore\d{s}u nad\={\i}\d{s}u ca guh\={a}su ca /} \\
\hspace*{1.5em}\textit{\'{s}abarair barbarai\'{s} caiva pulindai\'{s} ca sup\={u}jit\={a} // (Hariva\d{m}\'{s}a Appendix 1.4)}
\end{quote}"""

text = text.replace(bad_layout, good_layout)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Verse indentation updated.")
