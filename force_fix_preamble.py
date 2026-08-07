import re

with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Clean out all previously injected structural tags to reset the layout boundary
text = text.replace("\\begin{document}", "")
text = text.replace("\\maketitle", "")
text = text.replace("\\begin{abstract}", "")
text = text.replace("\\end{abstract}", "")

# 2. Re-anchor the file with absolute layout ordering: Document triggers come BEFORE the abstract
text = text.replace(
    "This paper introduces the ``Contortionist Turn,''",
    "\\begin{document}\n\\maketitle\n\\begin{abstract}\nThis paper introduces the ``Contortionist Turn,''"
)

# 3. Explicitly terminate the abstract right after the first paragraph section finishes
abstract_end_phrase = "permanently erasing the names of their subaltern creators.\n\\end{abstract}"
if "permanently erasing the names of their subaltern creators." in text:
    text = text.replace(
        "permanently erasing the names of their subaltern creators.",
        "permanently erasing the names of their subaltern creators.\n\\end{abstract}"
    )

# 4. Clean up any duplicate consecutive tag anomalies created by the patch
text = re.sub(r"\\begin\{document\}\s*\\begin\{document\}", r"\\begin{document}", text)
text = re.sub(r"\\maketitle\s*\\maketitle", r"\\maketitle", text)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("[FIX COMPLETE] Structure re-aligned.")
