import os

def assign_book_suffixes(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Target file not found at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Mapping suffixes to James Birch's dual 2024 book publications...")

    # 1. Update the first book entry (line 1177) to Birch2024a
    old_bib_a = "\\bibitem[Birch(2024)]{Birch2024}"
    new_bib_a = "\\bibitem[Birch(2024a)]{Birch2024a}"
    content = content.replace(old_bib_a, new_bib_a)

    # 2. Update the second book entry (line 1190) to Birch2024b
    old_bib_b = "\\bibitem[Birch, 2024]{Birch2024}"
    new_bib_b = "\\bibitem[Birch(2024b)]{Birch2024b}"
    content = content.replace(old_bib_b, new_bib_b)

    # 3. Synchronize your in-text citations inside Section 5 to point to the correct Amaraugha book (2024a)
    content = content.replace("\\citep{Birch2024}", "\\citep{Birch2024a}")
    content = content.replace("\\cite{Birch2024}", "\\cite{Birch2024a}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Success! Suffixes assigned. Both 2024 books are now independent database nodes.")

if __name__ == '__main__':
    target_tex = '/Users/croma/acro-yoga-text-mining/main_article_v9.tex'
    assign_book_suffixes(target_tex)
