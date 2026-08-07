TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Forcing manual number overrides on line 54 reference tags...")

# Swap out the dynamic macro with a hardcoded, hyperlinked static text string
text = text.replace(r"Figure~\ref{fig:kamatchi_acrobats}", "Figure~1")
text = text.replace(r"Figure\ref{fig:kamatchi_acrobats}", "Figure~1")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Cross-reference manually locked to Figure 1.")
