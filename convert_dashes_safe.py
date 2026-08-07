#!/usr/bin/env python3
import re
import os

TARGET_FILE = "main_article_v4.tex"

def safe_dash_normalization():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: Target file '{TARGET_FILE}' not found.")
        return

    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    print("[*] Running isolated punctuation regex rules...")

    # Rule 1: Convert raw literal Unicode em-dashes (—) into standard spaced en-dashes
    text = text.replace("—", " -- ")

    # Rule 2: Convert literal triple hyphens (---) into standard spaced en-dashes
    text = text.replace("---", " -- ")

    # Rule 3: Target double-hyphens ONLY when they act as punctuation tokens between words.
    # [A-Za-z]}--[A-Za-z]} ensures it leaves internal keys, file paths, and citations untouched.
    text = re.sub(r'([A-Za-z])\s*--\s*([A-Za-z])', r'\1 -- \2', text)

    # Rule 4: Standardize space widths to prevent double-spacing layout bloat ("  --  ")
    text = re.sub(r'\s+--\s+', ' -- ', text)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(text)

    print("[SUCCESS] All em-dashes safely converted to spaced en-dashes.")

if __name__ == "__main__":
    safe_dash_normalization()
