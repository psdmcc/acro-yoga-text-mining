TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Target the unescaped URL string and replace underscores with compiler-safe escapes
bad_url = r"https://vam.ac.uk"
good_url = r"https://vam.ac.uk\_of\_eleven\_paintings\_of\_painting\_unknown/"

text = text.replace(bad_url, good_url)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] V&A Museum URL string successfully escaped.")
