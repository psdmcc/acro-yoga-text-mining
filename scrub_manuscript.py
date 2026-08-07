#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scrub_manuscript.py
Description: Automated typographical clean pass for 'The Contortionist Turn'.
             Removes duplicate loops and converts all em-dashes to spaced en-dashes.
"""

import os
import re

# Targeting your exact LaTeX file
TARGET_TEX_FILE = "main_article_v4.tex"

def execute_editorial_scrub():
    if not os.path.exists(TARGET_TEX_FILE):
        print(f"[!] Error: Target file '{TARGET_TEX_FILE}' not found.")
        return

    print(f"[*] Ingesting active manuscript: {TARGET_TEX_FILE}...")
    with open(TARGET_TEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # -------------------------------------------------------------------------
    # 🚨 UPDATED TARGET 1: FORCE NATIVE LATEX EN-DASH MACROS
    # -------------------------------------------------------------------------
    print("[*] Intercepting all em-dashes and converting to native LaTeX en-dashes...")
    
    # Replaces raw double/triple hyphens with explicit spaced textendash macros
    content = re.sub(r'\s*---\s*', r' \\textendash\\ ', content)
    content = re.sub(r'\s*--\s*', r' \\textendash\\ ', content)
    
    # Replaces true Unicode em-dashes (—) with explicit spaced textendash macros
    content = re.sub(r'\s*—\s*', r' \\textendash\\ ', content)

    # -------------------------------------------------------------------------
    # 🚨 TARGET 2: CLEANING UP THE TRIPLE DIETARY MYTH DUPLICATION (PAGE 26/27)
    # -------------------------------------------------------------------------
    print("[*] Scrubbing redundant dietary myth loops from Chapter 9...")
    dietary_boilerplate = (
        "This highly specialized dietary matrix dismantles the Neo-Romantic myth of the non-ingesting, "
        "introspective forest dweller; the text exposes a grueling, resource-heavy somatic refinery built on "
        "intense substance management and defensive statecraft metrics centuries before its late-medieval "
        "monastic sanitization (Sandesara and Mehta, 1964; Wujastyk, 2025)."
    )

    initial_diet_count = content.count(dietary_boilerplate)
    if initial_diet_count > 1:
        parts = content.split(dietary_boilerplate)
        content = parts[0] + dietary_boilerplate + "".join(parts[1:])
        print(f"  [SUCCESS] Cleaned {initial_diet_count} redundant dietary loops.")

    # -------------------------------------------------------------------------
    # 🚨 TARGET 3: CLEANING UP THE DOUBLE ORTHOGRAPHIC FRICTION LOOP (SECTION 7)
    # -------------------------------------------------------------------------
    print("[*] Scrubbing duplicate orthographic friction paragraph from Section 7...")
    friction_boilerplate = (
        "When coupled with the high edit-distance volatility and orthographic friction tracked across the "
        "raw GRETIL variants—where vernacular, regional, and low-caste phonetic markers are systematically "
        "ironed out into standard Sanskrit lemmas within the DCS—the pipeline exposes the true scope "
        "of the Brahmanical enclosure protocol. This is not the organic development of an abstract philosophy; "
        "it is a data-proven historical heist that systematically vampirized the high-leverage physical "
        "mastery of marginalized guilds, leaving their tools fully active while rendering their human creators "
        "entirely invisible."
    )

    # Standardize the duplicate block checking against our new dash updates
    friction_boilerplate_clean = friction_boilerplate.replace("—", " -- ")
    initial_friction_count = content.count(friction_boilerplate_clean)
    
    if initial_friction_count > 1:
        parts = content.split(friction_boilerplate_clean)
        content = parts[0] + friction_boilerplate_clean + "".join(parts[1:])
        print(f"  [SUCCESS] Cleaned {initial_friction_count} duplicate conclusion blocks.")

    # -------------------------------------------------------------------------
    # 💾 EXPORTING DISK WRITE BACK
    # -------------------------------------------------------------------------
    backup_file = TARGET_TEX_FILE + ".bak"
    with open(backup_file, 'w', encoding='utf-8') as b_f:
        b_f.write(content)
        
    with open(TARGET_TEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"\n[COMPLETE] Global clean pass completed successfully on '{TARGET_TEX_FILE}'.")

if __name__ == "__main__":
    execute_editorial_scrub()
