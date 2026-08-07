with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Locate the temporary quote block and swap it for your exact layout structure
bad_layout = r"""\begin{quote}
\small
\textit{parvat\={a}gre\d{s}u ghore\d{s}u nad\={\i}\d{s}u ca guh\={a}su ca | \\
\'{s}abarair barbarais caiva pulindai\'{s} ca sup\={u}jit\={a} ||} \\
\hfill \small (Hariva\d{m}\'{s}a Appendix 1.4)
\end{quote}"""

good_layout = r"""\begin{flushright}
\small
\textit{parvat\={a}gre\d{s}u ghore\d{s}u nad\={\i}\d{s}u ca guh\={a}su ca /} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\
\textit{\'{s}abarair barbarai\'{s} caiva pulindai\'{s} ca sup\={u}jit\={a} // (Hariva\d{m}\'{s}a Appendix 1.4)}
\end{flushright}"""

text = text.replace(bad_layout, good_layout)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Verse layout re-mapped.")
