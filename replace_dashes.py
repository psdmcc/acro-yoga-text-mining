import os
import re

# Targeted files topology list
TARGET_FILES = ["main_article_v4.tex", "main_article_new.tex"]

# Matches unspaced em-dashes (—) or classic TeX em-dashes (---)
# Captures optional surrounding whitespace to prevent creating double spaces
EM_DASH_REGEX = re.compile(r'\s*---\s*|\s*—\s*')

def reformat_manuscript_dashes():
    print("=" * 70)
    print("LAUNCHING MANUSCRIPT TYPOGRAPHIC CLEANUP ENGINE")
    print("=" * 70)
    
    for filename in TARGET_FILES:
        file_path = os.path.expanduser(f"./{filename}")
        
        if not os.path.exists(file_path):
            print(f"Skipping: '{filename}' (File not found in current directory)")
            continue
            
        print(f"Processing structural typography inside -> {filename}...")
        
        # Read raw content layers
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Count total matches before making replacements
        total_matches = len(EM_DASH_REGEX.findall(content))
        
        if total_matches == 0:
            print(f"  * Success! Zero unspaced em-dashes detected in {filename}.")
            print("-" * 70)
            continue
            
        # Swap unspaced em-dashes with cleanly spaced standard LaTeX en-dashes
        cleaned_content = EM_DASH_REGEX.sub(' -- ', content)
        
        # Save content layer back to disk safely
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
            
        print(f"  * Purge Complete: Reformatted {total_matches} dash constraints inside {filename}!")
        print("-" * 70)

if __name__ == "__main__":
    reformat_manuscript_dashes()
