import re
import os

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Sweeping bibliography hooks for structural alignment...")

# Rule 1: Fix common unclosed brackets or mismatched braces in recent additions
text = text.replace(r"\bibitem[Srinivas, 2012]{Srinivas2012}", r"\bibitem[Srinivas(2012)]{Srinivas2012}")
text = text.replace(r"\bibitem[Thomas, 2025]{Thomas2025}", r"\bibitem[Thomas(2025)]{Thomas2025}")

# Rule 2: Ensure any loose bracket trailing before \end{document} is cleanly neutralized
text = re.sub(r'\n\]\n', '\n', text)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Reference markers balanced.")
