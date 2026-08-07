import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Locate the exact author block down to the email line
bad_block = r"""\author{\textbf{Patrick S. D. McCartney}\\
\textit{Research Affiliate, Anthropological Institute, Nanzan University, Japan}\\
\textit{School of Culture, History and Language, Australian National University, Australia}\\
\textit{Centre for Religious Studies, Manipal Academy of Higher Education, India}\\
\texttt{u4556787@anu.edu.au}}"""

# Re-inject it explicitly ensuring the final macro brace closes perfectly
good_block = r"""\author{\textbf{Patrick S. D. McCartney}\\
\textit{Research Affiliate, Anthropological Institute, Nanzan University, Japan}\\
\textit{School of Culture, History and Language, Australian National University, Australia}\\
\textit{Centre for Religious Studies, Manipal Academy of Higher Education, India}\\
\texttt{u4556787@anu.edu.au}}"""

# If the exact match fails due to minor spacing variations from previous scripts, 
# let's find the email anchor and force-terminate the author macro there
if "u4556787@anu.edu.au" in text:
    text = re.sub(r"\\texttt\{u4556787@anu\.edu\.au\}\s*\}*", r"\\texttt{u4556787@anu.edu.au}}", text)
    print("[SUCCESS] Author macro brace forced closed via regex matching.")
else:
    print("[!] Warning: Author email anchor not found.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)
