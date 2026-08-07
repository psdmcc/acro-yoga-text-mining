with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the snake/viper complex Greek words with native math mode rendering
bad_segment = r"\textgreek{ἐχίδνης}/\textgreek{ἔχεις}"
good_segment = r"$\varepsilon\chi\mathit{\acute{\iota}}\delta\nu\eta\varsigma$/$\mathit{\acute{\epsilon}}\chi\varepsilon\iota\varsigma$"
text = text.replace(bad_segment, good_segment)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Final Greek strings converted.")
