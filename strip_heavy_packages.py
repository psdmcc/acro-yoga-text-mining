def strip_problematic_packages():
    file_path = "main_article_v6.tex"
    print(f"[*] Accessing {file_path} to temporarily disable microtype and hyperref...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Comment out the specific packages causing the font-shipout loop
    text = text.replace(r"\usepackage{microtype}", r"% \usepackage{microtype}")
    text = text.replace(r"\usepackage{hyperref}", r"% \usepackage{hyperref}")
    text = text.replace(r"\usepackage[{microtype}]", r"% \usepackage{microtype}")
    text = text.replace(r"\usepackage[{hyperref}]", r"% \usepackage{hyperref}")
    
    # Also strip any lingering hypersetup blocks that would throw errors without hyperref
    text = text.replace(r"\hypersetup", r"% \hypersetup")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
        
    print("[✓] STRIP COMPLETE: microtype and hyperref have been safely commented out.")

if __name__ == "__main__":
    strip_problematic_packages()
