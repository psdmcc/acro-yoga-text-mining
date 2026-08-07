TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("[*] Enclosing timeline block inside a pristine figure float...")

clean_lines = []
for index, line in enumerate(lines):
    line_num = index + 1
    
    # Target exactly line 202 where the graphic file is called
    if line_num == 202 or ("somatic_chronology_timeline.png" in line and "\\begin{figure}" not in lines[max(0, index-2)]):
        line = "\\begin{figure}[t]\n    \\centering\n    " + line.lstrip()
        
    # Target exactly line 204 or the label right below it to seal the environment
    if "label{fig:somatic_chronology}" in line:
        line = line + "\\end{figure}\n"
        
    clean_lines.append(line)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write("".join(clean_lines))

print("[SUCCESS] Timeline environment successfully closed and sealed.")
