with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Fix the broken backslash right before vacana on line 86
text = text.replace(r"\vacana\d{m}", r"vacana\d{m}")

# Fix the broken backslash prefixing vrttilopam on line 89
text = text.replace(r"\v\d{r}ttilopa\d{m}", r"\d{r}ttilopa\d{m}")

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Multi-line word corruptions repaired.")
