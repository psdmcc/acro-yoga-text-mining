TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

print("[*] Sanitizing absolute image path tokens on line 52...")

# Replace the problematic absolute directory path string with a clean bare filename
bad_path = r"\includegraphics[width=0.85\textwidth]{/Users/croma/acro-yoga-text-mining/kamatchiamma.jpg}"
good_path = r"\includegraphics[width=0.85\textwidth]{kamatchiamma.jpg}"

text = text.replace(bad_path, good_path)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Localized relative filename mapping applied.")
