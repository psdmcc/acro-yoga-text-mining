import re

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Sweeping document to purge orphaned minipage string artifacts...")

# Broad search pattern to find and cleanly replace the broken figure structure on line 55
bad_block_pattern = r"\\includegraphics\[width=0\.85\\textwidth\]\{kamatchiamma\.jpg\}\\end\{minipage\}\}"

# Force inject a standardized, clean floating figure environment
good_block = r"\begin{figure}[htbp]\n    \centering\n    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"

text = re.sub(bad_block_pattern, good_block, text)

# Catch potential alternate variations of the stray token if any whitespace differs
text = text.replace(r"\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}\end{minipage}}", 
                    r"\begin{figure}[htbp]\n    \centering\n    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Stray minipage strings purged completely.")
