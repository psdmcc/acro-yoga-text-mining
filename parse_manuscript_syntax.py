import os

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("[*] Sweeping document layout lines for unbalanced structural tags...")

for index, line in enumerate(lines):
    line_num = index + 1
    
    # Track character balances within running paragraphs
    open_brackets = line.count("[")
    close_brackets = line.count("]")
    open_braces = line.count("{")
    close_braces = line.count("}")
    
    # Flag rows where tags do not cleanly balance out
    if open_brackets != close_brackets:
        print(f"[-] Row {line_num}: Unbalanced Square Brackets -> [ found: {open_brackets}, ] found: {close_brackets}")
        print(f"    Code: {line.strip()[:80]}...\n")
        
    if open_braces != close_braces:
        # Filter out obvious structural multi-line blocks like \begin{}
        if not any(tag in line for tag in ["\\begin{", "\\end{", "\\title{", "\\author{"]):
            print(f"[-] Row {line_num}: Unbalanced Curly Braces -> {{ found: {open_braces}, }} found: {close_braces}")
            print(f"    Code: {line.strip()[:80]}...\n")

print("[SUCCESS] Analysis complete. Verify the flagged row outputs above.")
