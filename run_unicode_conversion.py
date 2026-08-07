import re

def absolute_bibliography_sanitization():
    file_path = "main_article_v5.tex"
    print(f"[*] Accessing {file_path} for final absolute bibitem tag stripping...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Strip parenthetical style brackets: \bibitem[Author(Year)]{Key} -> \bibitem{Key}
    text = re.sub(r'\\bibitem\[[^\]\n]+\([^)]+\)\]\{([^}]+)\}', r'\\bibitem{\1}', text)

    # 2. Strip simple author-comma-year brackets: \bibitem[Author, Year]{Key} -> \bibitem{Key}
    text = re.sub(r'\\bibitem\[[^\]\n]+\]\{([^}]+)\}', r'\\bibitem{\1}', text)

    # 3. Clean up the residual un-braced velar nasals found inside the reference text strings
    text = text.replace(r"\.{n}", "ṅ")
    text = text.replace(r"\.{N}", "Ṅ")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
        
    print("[✓] COMPLETED: The entire bibliography has been successfully sanitized to pure numerical bibitems.")

if __name__ == "__main__":
    absolute_bibliography_sanitization()
