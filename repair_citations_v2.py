#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repair_citations_v2.py
Description: Advanced structural citation repair engine for 'The Contortionist Turn'.
             Maps plain-text strings into correct native \citet or \citep formatting blocks.
"""

import os
import re

TARGET_FILE = "main_article_v4.tex"

def clean_and_repair_citations():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: Target file '{TARGET_FILE}' not found in active workspace.")
        return

    print(f"[*] Ingesting current text state: {TARGET_FILE}...")
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    # Create a fallback recovery snapshot before performing raw character swaps
    with open(TARGET_FILE + ".v2bak", 'w', encoding='utf-8') as b_f:
        b_f.write(text)
    print(f"[+] Fallback snapshot safely archived to: {TARGET_FILE}.v2bak")

    # Master list of citation tracking keys
    citation_keys = [
        "Birch2024", "Mallinson2007", "Wujastyk2025", "Sandesara1964", "Olivelle2011",
        "Khasgivale1929", "Buhler1875", "KauśP", "Baudhāyana", "Vasiṣṭha", "Berger2023",
        "Shastri1991", "McCartney2021", "McCartney2026", "Wujastyk2020", "Mallinson2017",
        "Birch2020", "Suka21", "HC3", "PB13.12", "BhP3.1", "Kir12", "DKC", "KSS", "MU"
    ]

    print("[*] Striking out scrambled syntax remnants from the previous run...")
    # First, undo the broken "Author \citeyearpar{Author2007}" or raw text duplicates
    for key in citation_keys:
        match = re.match(r"([A-Za-z\u00C0-\u017F]+)(\d{4})", key)
        if match:
            author_name = match.group(1)
            # Scrub out strings where the author name was repeated right before a macro tag
            text = re.sub(rf"{author_name}\s*\\citeyearpar\{{{key}\}}", key, text)
            text = re.sub(rf"{author_name}\s*\\citet\{{{key}\}}", key, text)
            text = re.sub(rf"{author_name}\s*\\citep\{{{key}\}}", key, text)

    print("[*] Programmatically mapping native textual and parenthetical citation tracks...")
    
    # -------------------------------------------------------------------------
    # LAYER 1: TEXTUAL NARRATIVE PASS (\citet)
    # -------------------------------------------------------------------------
    # If a key sits immediately before active verbs of writing or tracking, 
    # it must look like a natural text noun/subject -> \citet{Key}
    textual_verbs = ["tracks", "outlines", "argues", "demonstrates", "codifies", "shows", "claims", "states", "unmasks"]
    for verb in textual_verbs:
        for key in citation_keys:
            # Match author name combinations sitting directly in front of an execution verb
            pattern_textual = rf"\b{re.escape(key)}\s+{verb}\b"
            text = re.sub(pattern_textual, f"\\citet{{{key}}} {verb}", text)

    # -------------------------------------------------------------------------
    # LAYER 2: PARENTHETICAL CLOSURE PASS (\citep)
    # -------------------------------------------------------------------------
    # Any remaining raw citation strings that are not part of an active sentence 
    # action are wrapped into standard reference brackets -> \citep{Key}
    for key in citation_keys:
        pattern_standalone = rf"(?<!\\citet\{{)(?<!\\citep\{{)\b{re.escape(key)}\b"
        text = re.sub(pattern_standalone, f"\\citep{{{key}}}", text)

    # -------------------------------------------------------------------------
    # LAYER 3: CLEANUP POST-PROCESSING RE-REGULATION
    # -------------------------------------------------------------------------
    # Clean up double-bracket anomalies like "( \citep{Key} )" or "( \citet{Key} )"
    text = re.sub(r'\(\s*\\citep\{([^}]+)\}\s*\)', r'\\citep{\1}', text)
    text = re.sub(r'\(\s*\\citet\{([^}]+)\}\s*\)', r'\\citet{\1}', text)
    
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"\n[COMPLETE] Global structural citation tracking completed successfully.")
    print("[*] Recompile your layout: pdflatex main_article_v4.tex")

if __name__ == "__main__":
    clean_and_repair_citations()
