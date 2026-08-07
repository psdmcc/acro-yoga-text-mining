import os
import re
import itertools
from collections import defaultdict
from bs4 import BeautifulSoup

# Define absolute repository paths based on your file infrastructure layout
BASE_DIR = os.path.expanduser("~/acro-yoga-text-mining/corpus")
TARGET_DIRS = ["raw_dcs", "raw_gretil"]
WINDOW_SIZE = 5  # Number of words to check on either side

# Comprehensive regex dictionaries to catch base lemmas and standard Sanskrit sandhi/inflection arrays
TARGET_REGEXES = {
    "yoga": re.compile(r'\b(yog[aa\u0101][\u1e45\u1e4d\u1e25s\u1e63\u0101n]*)\b', re.IGNORECASE),
    "malla": re.compile(r'\b(mall[aa\u0101][\u1e45\u1e4d\u1e25s\u1e63\u0101n]*)\b', re.IGNORECASE),
    "stambha": re.compile(r'\b(stambh[aa\u0101][\u1e45\u1e4d\u1e25s\u1e63\u0101n]*)\b', re.IGNORECASE)
}

CLEAN_WORD_REGEX = re.compile(r'[^\w\s\u0300-\u036f\u1e00-\u1eff]')

def clean_text_from_html(file_path):
    """Extracts raw content and strips markup boilerplate from GRETI/DCS files."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if file_path.endswith(('.htm', '.html')):
            soup = BeautifulSoup(content, 'html.parser')
            return soup.get_text(separator=' ')
        return content
    except Exception as e:
        print(f"Error reading file {os.path.basename(file_path)}: {e}")
        return ""

def compute_sliding_jaccard():
    # Store unique context word sets for each target keyword
    context_sets = defaultdict(set)
    term_hit_counts = defaultdict(int)
    
    print("=" * 70)
    print("LAUNCHING SLIDING-WINDOW JACCARD COEFFICIENT MATRIX EXTRACTION")
    print("=" * 70)

    for target in TARGET_DIRS:
        dir_path = os.path.join(BASE_DIR, target)
        if not os.path.exists(dir_path):
            continue
            
        print(f"Scanning context profiles inside directory: {target}...")
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.startswith('.') or not file.endswith(('.htm', '.html', '.txt')):
                    continue
                    
                full_path = os.path.join(root, file)
                raw_text = clean_text_from_html(full_path)
                
                # Tokenize into a continuous linear word stream while retaining diacritics
                words = CLEAN_WORD_REGEX.sub('', raw_text).split()
                
                for idx, word in enumerate(words):
                    # Check each token against our target terms definitions
                    for label, regex in TARGET_REGEXES.items():
                        if regex.match(word):
                            term_hit_counts[label] += 1
                            
                            # Isolate boundary indices for the context frame
                            start_idx = max(0, idx - WINDOW_SIZE)
                            end_idx = min(len(words), idx + WINDOW_SIZE + 1)
                            
                            # Extract words inside the sliding window, skipping the target word itself
                            for n_idx in range(start_idx, end_idx):
                                if n_idx != idx:
                                    neighbor_word = words[n_idx].lower()
                                    # Filter out short noise particles (e.g., ca, vā, api) under 3 letters
                                    if len(neighbor_word) >= 3:
                                        context_sets[label].add(neighbor_word)

    print("\n" + "=" * 70)
    print("CORPUS NEIGHBORHOOD DISTRIBUTION SUMMARY")
    print("=" * 70)
    for label in TARGET_REGEXES.keys():
        print(f"  * Keyword '{label}': Total Hits = {term_hit_counts[label]}, Unique Neighbor Vocab Size = {len(context_sets[label])}")

    print("\n" + "=" * 70)
    print(f"COMPUTED PAIRWISE JACCARD MATRIX (WINDOW SIZE: +/- {WINDOW_SIZE})")
    print("=" * 70)
    print(f"{'TERM PAIR':<25} | {'INTERSECTION':<12} | {'UNION':<10} | {'JACCARD INDEX'}")
    print("-" * 70)

    # Compute pairwise structural networks coefficients
    for term_a, term_b in itertools.combinations(TARGET_REGEXES.keys(), 2):
        set_a = context_sets[term_a]
        set_b = context_sets[term_b]
        
        intersection_set = set_a.intersection(set_b)
        union_set = set_a.union(set_b)
        
        len_intersect = len(intersection_set)
        len_union = len(union_set)
        
        jaccard_score = len_intersect / len_union if len_union > 0 else 0.0
        
        pair_label = f"'{term_a}' <-> '{term_b}'"
        print(f"{pair_label:<25} | {len_intersect:<12} | {len_union:<10} | {jaccard_score:.4f} ({jaccard_score*100:.1f}%)")
        
        # Print a small subset of shared semantic vectors if an intersection exists
        if len_intersect > 0:
            sample_words = list(intersection_set)[:6]
            print(f"    └─ Sample Shared Context: {', '.join(sample_words)}...")

if __name__ == "__main__":
    compute_sliding_jaccard()

