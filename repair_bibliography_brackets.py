import re
import os

TARGET_FILE = "main_article_v4.tex"

def repair_brackets():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: {TARGET_FILE} not found.")
        return

    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    print("[*] Sweeping bibliography for broken citation braces...")

    # Rule 1: Locate any malformed or unclosed bibitem syntax variants
    # (e.g., missing matching brackets in newly injected bibliography lines)
    fixed_text = text
    
    # Fix potential trailing bracket orphans sitting on lines by themselves near the end
    fixed_text = re.sub(r'\n\]\n', '\n', fixed_text)
    
    # Clean up standard VAM citation or recent entries if brackets were malformed
    fixed_text = fixed_text.replace(r"\bibitem[Victoria and Albert Museum(2024)", r"\bibitem[Victoria and Albert Museum(2024)]")
    fixed_text = fixed_text.replace(r"\bibitem[Victoria and Albert Museum(2024)]]", r"\bibitem[Victoria and Albert Museum(2024)]")
    
    # Rule 2: Ensure \end{document} is cleanly positioned on its own pristine row
    fixed_text = re.sub(r'\\end\{document\}.*', r'\\end{document}', fixed_text, flags=re.DOTALL)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(fixed_text)

    print("[SUCCESS] Structural bibliography parameters balanced.")

if __name__ == "__main__":
    repair_brackets()
