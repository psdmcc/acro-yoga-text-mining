def fix_abstract_syntax():
    file_path = "main_article_v6.tex"
    print(f"[*] Reading {file_path} to repair abstract math toggles...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # The exact broken string from your line 48 snippet
    broken_str = "coefficients ($J_{\\text{slide}}$ within an inclusive 300-word context envelope)"
    fixed_str = "coefficients ($J_{\\text{slide}}$) within an inclusive 300-word context envelope"

    if broken_str in text:
        text = text.replace(broken_str, fixed_str)
        print("[✓] Found and corrected the open math block successfully!")
    else:
        print("[!] Exact match not found. Sweeping via sliding window correction...")
        # Broad fallback swap to catch variations in whitespace
        text = text.replace("($J_{\\text{slide}}$ within", "($J_{\\text{slide}}$) within")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    fix_abstract_syntax()
with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Remove misplaced document initializations inside the header space
text = text.replace("\\begin{document}\n\\maketitle", "")

# Locate the abstract block and place the document triggers in the exact correct order
text = text.replace("\\begin{abstract}", "\\begin{abstract}")
text = text.replace("\\end{abstract}", "\\end{abstract}\n\\begin{document}\n\\maketitle")

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Abstract layout corrected.")
