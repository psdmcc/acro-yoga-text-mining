import re
import os

TARGET_FILE = "main_article_v4.tex"

# Direct phonetic translations for the exact Greek variables in your text
GREEK_TRANSLITERATIONS = {
    "ἰός": "ios",
    "χρίεσθαι": "chriesthai",
    "φάρμακον": "pharmakon",
    "ἐχίδνης": "echidnes",
    "ἔχεις": "echeis",
    "ἔχιδνα": "echidna"
}

def clear_greek_macros():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: {TARGET_FILE} not found.")
        return

    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    # Create safety backup snapshot
    with open(TARGET_FILE + ".greekbak", 'w', encoding='utf-8') as b_f:
        b_f.write(text)

    print("[*] Parsing text for remaining \\textgreek macro structures...")
    
    # Locate all raw instances of \textgreek{...}
    pattern = r"\\textgreek\{([^}]+)\}"
    matches = re.findall(pattern, text)
    
    for greek_word in set(matches):
        # Match against our translation table, or default to a lowercase raw fallback string
        clean_latin_word = GREEK_TRANSLITERATIONS.get(greek_word, greek_word.lower())
        latex_replacement = f"\\textit{{{clean_latin_word}}}"
        
        # Globally swap the broken macro out for clean academic italics
        text = text.replace(f"\\textgreek{{{greek_word}}}", latex_replacement)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(text)

    print("[SUCCESS] All Greek fonts converted into standard italic strings.")

if __name__ == "__main__":
    clear_greek_macros()
