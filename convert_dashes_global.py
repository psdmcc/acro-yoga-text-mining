#!/usr/bin/env python3
import re
import os

TARGET_FILE = "main_article_v4.tex"

def convert_dashes_to_spaced_en():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: Target file '{TARGET_FILE}' not found.")
        return

    print(f"[*] Reading manuscript file: {TARGET_FILE}")
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create an emergency backup snapshot
    with open(TARGET_FILE + ".dashbak", 'w', encoding='utf-8') as b_f:
        b_f.write(content)
    print(f"[+] Safety snapshot archived to: {TARGET_FILE}.dashbak")

    print("[*] Executing global dash normalization rules...")

    # Rule 1: Convert literal Unicode em-dashes (—) into standard spaced en-dashes
    content = content.replace("—", " -- ")

    # Rule 2: Convert triple hyphens (---) into standard spaced en-dashes
    content = content.replace("---", " -- ")

    # Rule 3: Target double hyphens (--) that are unspaced or incorrectly spaced in paragraphs
    # This regex catches any text--text or text --text scenarios and normalizes them
    content = re.sub(r'(?<!\\)(?<!-)-{2,3}(?!-)', ' -- ', content)

    # Rule 4: Typographical cleanup to prevent accidental double-spacing artifacts (e.g., "  --  ")
    content = re.sub(r' +-- +', ' -- ', content)
    content = re.sub(r'(\s*--\s*)+', ' -- ', content)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print("[SUCCESS] All em-dashes converted globally to spaced en-dashes (--).")

if __name__ == "__main__":
    convert_dashes_to_spaced_en()
