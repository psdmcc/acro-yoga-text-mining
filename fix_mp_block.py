import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Precise structural regex signature pattern for the target verse layout
regex_pattern = r"\\begin\{quote\}\s*mall\s*\\textit\{tatr.*?MP 3\.13.*?\}\s*\\end\{quote\}"

clean_stacked_block = r"""\begin{quote}
\small
\noindent\textit{mall tatr\={a}dau tavad ucyante lak\d{s}a\d{n}\={a}ni jye\d{s}\d{t}hamall\={a}n\={a}\d{m} gu\d{n}\={a}\d{h} |} \\
\noindent\textit{sa\d{m}sk\d{r}taprak\d{r}t\={a}bhy\={a}\d{m} ca tato bh\={a}\d{s}\={a}laukik\={a}bhi\d{h} || MP 3.12 ||} \\
\\
\noindent\textit{apabhra\d{m}\'s\={a}cca vak\d{s}y\={a}mi ye yatrokt\={a}s tathaiva t\={a}n |} \\
\noindent\textit{kula\d{m} \'s\={i}la\d{m} ca nayo vinaya\'sca tathaiva ca || MP 3.13 ||}
\end{quote}"""

modified_content = re.sub(regex_pattern, clean_stacked_block, content, flags=re.DOTALL)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(modified_content)

print("[SUCCESS] Verse 3.12-3.13 block scrubbed and reformatted.")
