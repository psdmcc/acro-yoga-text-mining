import re

with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Clean out any previous duplicate or malformed structural tags around the abstract
text = text.replace("\\begin{document}", "")
text = text.replace("\\begin{abstract}", "")

# 2. Insert the document initialization block precisely right before the abstract opens
text = text.replace(r"This paper introduces the ``Contortionist Turn,''", 
                    "\\begin{document}\n\\maketitle\n\\begin{abstract}\nThis paper introduces the ``Contortionist Turn,''")

# 3. Clean up title duplication tags to make sure \maketitle doesn't fire twice
text = re.sub(r"\\maketitle\s*\\maketitle", r"\\maketitle", text)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] LaTeX structural sequence fully calibrated.")
