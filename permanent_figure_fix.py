import re
import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Stripping old broken text layout and forcing absolute paragraph alignment...")

# Define the full introduction block using a regex pattern that ignores any internal carriage returns, spaces, or tabs
pattern = r"As\s+illustrated\s+in\s+Figure\s+2,\s+this\s+performance\s+is\s+not\s+mere\s+secular\s+entertainment;\s+it\s+is\s+the\s+enactment\s+of\s+an\s+ancient\s+combat\s+myth\s+wherein\s+the\s+hero\s+V\\=[\i|i]rab\\=[\={a}|a]hu\s+slew\s+Vajrab\\=[\={a}|a]hu"

# Reconstruct the entire paragraph natively with a single, perfectly structured line for the reference macro
replacement_block = r"As illustrated in Figure~\ref{fig:kamatchi_acrobats}, this performance is not mere secular entertainment; it is the enactment of an ancient combat myth wherein the hero V\={i}rab\={a}hu slew Vajrab\={a}hu"

# Execute the substitution pass
content = re.sub(pattern, replacement_block, content, flags=re.MULTILINE)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Hardcoded multi-line label successfully replaced with dynamic macro.")
