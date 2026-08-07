TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Repairing multi-line figure reference layout splits...")

# Target the exact multi-line text arrangement split by the editor's carriage return
bad_split = "As illustrated in Figure \n    2,"
alternate_bad_split = "As illustrated in Figure \n    \\ref{fig:kamatchi_acrobats}"

# Force clean, dynamic macro alignment
content = content.replace("As illustrated in Figure \n    2", "As illustrated in Figure~\\ref{fig:kamatchi_acrobats}")
content = content.replace("As illustrated in Figure \n    \\ref{fig:kamatchi_acrobats}", "As illustrated in Figure~\\ref{fig:kamatchi_acrobats}")

# Fallback loose string sweep to capture any variations in editor spacing gaps
content = content.replace("Figure \n    2", "Figure~\\ref{fig:kamatchi_acrobats}")
content = content.replace("Figure \n    \\ref{fig:kamatchi_acrobats}", "Figure~\\ref{fig:kamatchi_acrobats}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Cross-reference hyperlink dynamically locked to Figure 1.")
