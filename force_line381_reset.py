TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("[*] Re-sealing line 381 layout boundaries...")

clean_lines = []
for index, line in enumerate(lines):
    line_num = index + 1
    
    # Isolate the exact crashing row holding the timeline image asset
    if line_num == 381 or "somatic_chronology_timeline.png" in line:
        print(f"[+] Re-writing corrupt brace layout on line {line_num}")
        # Force a perfectly clean, single-brace text string call
        line = "    \\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_chronology_timeline.png}\n"
        
    clean_lines.append(line)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write("".join(clean_lines))

print("[SUCCESS] Line 381 parameters successfully balanced.")
