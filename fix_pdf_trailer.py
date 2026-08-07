import re

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Locate the true end of the document block
if "\\end{document}" in content:
    # Split the file at the true document closing tag
    clean_parts = content.split("\\end{document}", 1)
    # Reconstruct the file, throwing away any trailing junk, stray brackets, or artifact lines
    sanitized_content = clean_parts[0] + "\\end{document}\n"
    
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(sanitized_content)
    print("[SUCCESS] PDF trailer sanitized. All trailing junk characters removed.")
else:
    print("[!] Warning: Could not locate standard \\end{document} tag.")
