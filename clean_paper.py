import os
import re

# Absolute path targeting your exact manuscript source file
INPUT_PAPER_PATH = os.path.expanduser("./main_article_new.tex")
OUTPUT_PAPER_PATH = os.path.expanduser("./main_article_new_cleaned.tex")

# Precision regex targeting Kanji, Han characters, Kana, and CJK punctuation blocks
CJK_PURGE_REGEX = re.compile(
    r'[\u4e00-\u9fff]|'  # CJK Unified Ideographs (Common Kanji/Hanzi)
    r'[\u3400-\u4dbf]|'  # CJK Extension A
    r'[\u3040-\u309f]|'  # Hiragana
    r'[\u30a0-\u30ff]|'  # Katakana
    r'[\u3000-\u303f]'   # CJK Symbols and Punctuation
)

def purge_stray_manuscript_glyphs():
    if not os.path.exists(INPUT_PAPER_PATH):
        print(f"Error: Could not locate your paper file at {INPUT_PAPER_PATH}")
        print("Please ensure this script is run from the directory containing main_article_new.tex")
        return

    print(f"Opening manuscript source file: {INPUT_PAPER_PATH}...")
    with open(INPUT_PAPER_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        latex_content = f.read()

    # Track structural matches prior to execution
    stray_matches = CJK_PURGE_REGEX.findall(latex_content)
    total_stray_glyphs = len(stray_matches)

    if total_stray_glyphs == 0:
        print("Success! Clean compile verified: No stray Kanji found in main_article_new.tex.")
        return

    print(f"Isolated {total_stray_glyphs} stray glyph(s). Target characters: {set(stray_matches)}")
    
    # Execute full purge
    cleaned_content = CJK_PURGE_REGEX.sub('', latex_content)

    with open(OUTPUT_PAPER_PATH, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"Purge complete! Written clean document to: {OUTPUT_PAPER_PATH}")
    print("Review this file, then rename/overwrite it to main_article_new.tex to compile safely.")

if __name__ == "__main__":
    purge_stray_manuscript_glyphs()
