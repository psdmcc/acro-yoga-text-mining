import re
import os

TARGET_FILE = "main_article_v4.tex"

# Comprehensive character map for any remaining individual Greek letters
GREEK_CHAR_MAP = {
    'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'e', 'θ': 'th',
    'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x', 'ο': 'o', 'π': 'p',
    'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'y', 'φ': 'ph', 'χ': 'ch', 'ψ': 'ps',
    'ω': 'o', 'ό': 'o', 'ά': 'a', 'έ': 'e', 'ί': 'i', 'ύ': 'y', 'ώ': 'o'
}

def clean_all_greek_remnants():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: {TARGET_FILE} not found.")
        return

    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    # Target specific compound string discovered on line 391
    text = text.replace("φαρμακόμαντις", "pharmakomantis")

    # Fallback loop: convert any individual loose Greek characters to Latin equivalents
    clean_chars = []
    for char in text:
        if char in GREEK_CHAR_MAP:
            clean_chars.append(GREEK_CHAR_MAP[char])
        else:
            clean_chars.append(char)
            
    final_text = "".join(clean_chars)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(final_text)

    print("[SUCCESS] All trapped Greek Unicode characters romanized.")

if __name__ == "__main__":
    clean_all_greek_remnants()
