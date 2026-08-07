TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Replacing hardcoded figure labels with automated cross-references...")

# Target the exact mismatched string description and update it with a dynamic macro
text = text.replace("As illustrated in Figure 2", "As illustrated in Figure~\\ref{fig:kamatchi_acrobats}")
text = text.replace("as illustrated in Figure 2", "as illustrated in Figure~\\ref{fig:kamatchi_acrobats}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Cross-reference mapping successfully normalized.")
