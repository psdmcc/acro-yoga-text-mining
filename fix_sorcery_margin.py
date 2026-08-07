TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Remove accidental manual line breaks immediately following the sorcery token
text = text.replace(r"(acrobatic_sorcery).\\", "(acrobatic_sorcery).")
text = text.replace(r"(acrobatic_sorcery).\newline", "(acrobatic_sorcery).")
text = text.replace(r"(acrobatic_sorcery). \\", "(acrobatic_sorcery).")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Manual line break removed. Paragraph justification restored.")
