#!/usr/bin/env python3
import os

TARGET_FILE = "main_article_v4.tex"

# Comprehensive dictionary mapping raw Unicode Sanskrit characters to native LaTeX macros
DIACRITIC_MAP = {
    # Long Vowels
    'ā': r'\={a}', 'ā'.upper(): r'\={A}',
    'ī': r'\={i}', 'ī'.upper(): r'\={I}',
    'ū': r'\={u}', 'ū'.upper(): r'\={U}',
    
    # Retroflexes / Subdots
    'ṭ': r'\d{t}', 'ṭ'.upper(): r'\d{T}',
    'ḍ': r'\d{d}', 'ḍ'.upper(): r'\d{D}',
    'ṇ': r'\d{n}', 'ṇ'.upper(): r'\d{N}',
    'ṣ': r'\d{s}', 'ṣ'.upper(): r'\d{S}',
    'ḷ': r'\d{l}', 'ḷ'.upper(): r'\d{L}',
    'ṛ': r'\d{r}', 'ṛ'.upper(): r'\d{R}',
    'ṝ': r'\d{\={r}}', 'ṝ'.upper(): r'\d{\={R}}',
    
    # Nasals / Anusvara / Visarga
    'ṃ': r'\d{m}', 'ṃ'.upper(): r'\d{M}',
    'ṅ': r'\dot{n}', 'ṅ'.upper(): r'\dot{N}',
    'ñ': r'\~{n}', 'ñ'.upper(): r'\~{N}',
    'ḥ': r'\d{h}', 'ḥ'.upper(): r'\d{H}',
    
    # Palatal Sibilant (Fixing the previous \s typo with proper standard acute accent macro)
    'ś': r"\'{s}", 'ś'.upper(): r"\'{S}"
}

def clean_manuscript_unicode():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: Target file '{TARGET_FILE}' not found.")
        return

    print(f"[*] Reading manuscript file: {TARGET_FILE}")
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create an emergency backup just in case
    with open(TARGET_FILE + ".unicodetbak", 'w', encoding='utf-8') as b_f:
        b_f.write(content)
        
    print("[*] Executing global character conversion rules...")
    
    # Clean up the previous broken typo attempts first
    content = content.replace(r"\s{s}", r"\'{s}")
    content = content.replace(r"\s", r"")
    
    # Globally swap every Unicode key for its LaTeX macro counterpart
    for unicode_char, latex_macro in DIACRITIC_MAP.items():
        content = content.replace(unicode_char, latex_macro)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print("[SUCCESS] All raw Sanskrit diacritics converted to native LaTeX macros.")

if __name__ == "__main__":
    clean_manuscript_unicode()
