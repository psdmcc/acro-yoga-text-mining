import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Locate the author block and strip any internal blank rows or malformed paragraph splits
bad_author_pattern = r"\\author\{\\textbf\{Patrick S\. D\. McCartney\}\\\\\\s*\n\s*\n"
text = re.sub(bad_author_pattern, r"\\author{\\textbf{Patrick S. D. McCartney}\\\\\n", text)

# Explicitly ensure the entire metadata block is unified without single blank lines
text = text.replace(
    r"\author{\textbf{Patrick S. D. McCartney}\\",
    r"\author{\textbf{Patrick S. D. McCartney}\\"
)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Author metadata rows consolidated.")
