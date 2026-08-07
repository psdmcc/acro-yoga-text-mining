#!/usr/bin/env python3
import re
import os

filename = "main_article_new.tex"

if not os.path.exists(filename):
    print(f"[!] Error: {filename} not found in current directory.")
    exit(1)

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Successfully read main_article_new.tex. Commencing structural remediation...")

# 1. Correct the typo 'Esopnage' -> 'Espionage' in the keyword string
text = re.sub(r'Esopnage', 'Espionage', text)

# 2. Safely extract and isolate the major structural sections using regex blocks
# We split by top-level sections to reorganize the hierarchy cleanly
parts = re.split(r'(\\section\{.*?\})', text)

# Let's rebuild the document sections into a clean array
new_parts = []
intro_subsections = []
methodology_subsections = []

# Keep the document preamble intact
preamble = parts[0]
new_parts.append(preamble)

current_section = ""

for i in range(1, len(parts), 2):
    sec_header = parts[i]
    sec_body = parts[i+1] if (i+1) < len(parts) else ""
    
    if "Introduction" in sec_header:
        # Extract all unique subsections within the introduction, discarding duplicates
        subs = re.split(r'(\\subsection\{.*?\})', sec_body)
        seen_subs = set()
        intro_body_cleaned = subs[0]
        
        for j in range(1, len(subs), 2):
            sub_header = subs[j]
            sub_body = subs[j+1] if (j+1) < len(subs) else ""
            if sub_header not in seen_subs:
                seen_subs.add(sub_header)
                intro_body_cleaned += sub_header + sub_body
        
        # Save this to be appended later with the relocated blocks
        intro_parts = (sec_header, intro_body_cleaned)
        
    elif "Methodology" in sec_header:
        # Pull out the misplaced historical blocks from methodology
        subs = re.split(r'(\\subsection\{.*?\})', sec_body)
        method_body_cleaned = subs[0]
        
        for j in range(1, len(subs), 2):
            sub_header = subs[j]
            sub_body = subs[j+1] if (j+1) < len(subs) else ""
            
            # Check if this subsection belongs to historical statecraft or algorithm work
            if any(k in sub_header for k in ["Panoptic Pillar", "Intelligence Nexus", "Geopolitical Formula"]):
                intro_subsections.append(sub_header + sub_body)
            else:
                method_body_cleaned += sub_header + sub_body
                
        methodology_parts = (sec_header, method_body_cleaned)
    else:
        # Keep all subsequent chapters (3 through Conclusion) completely untouched
        new_parts.append(sec_header + sec_body)

# Reconstruct the corrected Introduction with its relocated subsections appended to the end
final_intro = intro_parts[0] + intro_parts[1]
for sub in intro_subsections:
    final_intro += "\n" + sub

# Insert the cleaned chapters sequentially back into the document string
final_methodology = methodology_parts[0] + methodology_parts[1]
new_parts.insert(1, final_intro)
new_parts.insert(2, final_methodology)

# Write the pristine structure back out to disk
final_text = "".join(new_parts)
with open(filename, "w", encoding="utf-8") as f:
    f.write(final_text)

print("[+] Remediation complete! Duplicates purged and sections reordered successfully.")
