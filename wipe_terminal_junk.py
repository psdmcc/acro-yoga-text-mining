import re

TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Locate the true end of the document block and strip everything after it
if "\\end{document}" in content:
    parts = content.split("\\end{document}", 1)
    sanitized_content = parts[0] + "\\end{document}\n"
    
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(sanitized_content)
    print("[SUCCESS] Terminal junk strings completely removed from file footer.")
else:
    print("[!] Warning: Could not locate standard \\end{document} tag.")
