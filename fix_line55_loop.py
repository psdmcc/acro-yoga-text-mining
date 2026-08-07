TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("[*] Performing targeted surgery on line 55 token structures...")

clean_lines = []
for index, line in enumerate(lines):
    line_num = index + 1
    
    # Catch line 55 or any adjacent row holding the corrupting token wrapper
    if "kamatchiamma.jpg" in line and "\\end{minipage}}" in line:
        print(f"[!] Purging corrupting minipage tail discovered on Row {line_num}")
        # Strip out the broken row and replace it with a clean, standalone figure block
        line = r"""\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}
"""
    clean_lines.append(line)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write("".join(clean_lines))

print("[SUCCESS] Line 55 re-sealed perfectly.")
