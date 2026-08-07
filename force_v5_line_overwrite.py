TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("[*] Forcing line-by-line normalization on cross-reference splits...")

clean_lines = []
for index, line in enumerate(lines):
    # Locate any row text block containing the broken cross-reference sequence
    if "As illustrated in Figure" in line:
        print(f"[!] Target found on row {index + 1}. Overwriting reference anchor...")
        # Replace the entire line fragment up to the comma with clean, dynamic macro calls
        line = " As illustrated in Figure~\\ref{fig:kamatchi_acrobats}, this performance is not mere secular entertainment; it is the enactment of\n"
    
    # Catch any loose leftover row remnants that got orphaned right below it
    elif "2," in line and index > 0 and "As illustrated in" in lines[index-1]:
        print(f"[!] Cleaning orphaned row marker on row {index + 1}...")
        line = ""
        
    clean_lines.append(line)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write("".join(clean_lines))

print("[SUCCESS] Manuscript code lines successfully synchronized.")
