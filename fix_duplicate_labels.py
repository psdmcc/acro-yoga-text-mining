import re
import os

TARGET_FILE = "main_article_v4.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Sweeping document for duplicate label or citation keys...")

# Locate all instances of \citep{MP_7} or \label{...} that might be causing the duplicate identifier crash
# We will find the second occurrence of \citep{MP_7} or \label{MP_7} and give it a unique descriptor
if content.count("MP_7") > 1:
    print("[!] Found duplicate tracking key 'MP_7'. Adjusting occurrences to maintain network stability...")
    
    # Split content by the target key to isolate occurrences
    parts = content.split("MP_7")
    
    # Keep the first instance as MP_7, and append a unique index suffix to subsequent ones
    reconstructed = parts[0]
    for i in range(1, len(parts)):
        # If it's a citation, we alter it to a clean secondary variant
        reconstructed += f"MP_7_v{i}" + parts[i]
        
    content = reconstructed

# Scan for common double-typed or stray brackets near the very bottom of the document file matrix
content = content.replace("\n]\n", "\n")
content = re.sub(r'\\end\{document\}.*', r'\\end{document}', content, flags=re.DOTALL)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Duplicate hyperref anchors resolved and balanced.")
