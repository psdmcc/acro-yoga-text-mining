import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Restoring stripped structural commands...")

# Restore nested subsubsections, subsections, and base sections in exact cascading order
text = text.replace(r"\ububection", r"\subsubsection")
text = text.replace(r"\ubsection", r"\subsection")
text = text.replace(r"\ection", r"\section")

# Fix common text-size macro corruptions (like \small becoming \mall or plain mall in blocks)
text = text.replace(r"\mall", r"\small")
text = re.sub(r"\\begin\{quote\}\s*mall", r"\\begin{quote}\n\\small", text)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] All structural section anchors successfully restored.")
