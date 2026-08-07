import re
import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Sweeping paragraph text for stray macro artifacts...")

# Broad regex pattern matching that targets the ghost string 'quote>' 
# regardless of spacing or adjacent paragraph characters
cleaned_content = re.sub(r'quote\s*>', '', content)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(cleaned_content)

print("[SUCCESS] Manuscript code lines successfully sanitized.")
