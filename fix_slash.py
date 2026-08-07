with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the specific crashed slash string with an explicit text-mode slash character
bad_string = r"\textit{na\d{t}as}/\textit{la\dot{n}ghakas}"
good_string = r"\textit{na\d{t}as}\text{/}\textit{la\dot{n}ghakas}"
text = text.replace(bad_string, good_string)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Slash syntax wrapped in text macro.")
