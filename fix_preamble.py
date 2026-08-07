import re

with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    content = f.read()

# Locate the abstract block and document boundary
abstract_match = re.search(r"\\begin\{abstract\}.*?\\end\{abstract\}", content, re.DOTALL)
if abstract_match:
    abstract_text = abstract_match.group(0)
    
    # Strip the duplicated/misplaced macro definitions out of the abstract text body
    clean_abstract = re.sub(r"\\DeclareUnicodeCharacter\{.*?\}.*?\n", "", abstract_text)
    clean_abstract = re.sub(r"\\definecolor\{RED\}.*?\n", "", clean_abstract)
    
    # Overwrite the document slice with a clean, structural sequence
    content = content.replace(abstract_text, clean_abstract)

# Standardize the exact entry into the main text body
content = re.sub(r"\\end\{abstract\}\s*\\begin\{document\}", "\\end{abstract}\n\\begin{document}", content)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Layout sequence re-ordered.")
