import os
import re
import math
import collections
import pandas as pd

# Standard lower IAST patterns optimized for plain-text extraction
LEMMA_PATTERNS = {
    'pithasarpin_crawler': [
        r'pīṭhasarp', r'pīṭhasarpī', r'pīṭhasarpina', r'pīṭhasarpibhi', r'pīṭhasarpa'
    ],
    'vaṃśanartin_pole': [
        r'vaṃśanart', r'vaṃśanartin', r'vaṃśanartinam', r'vaṃśanartina', r'vaṃśanartibhi', r'vaṃsanart'
    ],
    'stambha_axis': [
        r'stambha', r'stambhan', r'stambh', r'stambhitavya', r'stambham', r'thambha'
    ],
    'sarpa_serpent': [
        r'sarpa', r'sarpin', r'sarpati', r'sarpana', r'sarpiḥ', r'sarpī'
    ],
    'candala_outcaste': [
        r'caṇḍāl', r'caṇḍālam', r'caṇḍālai', r'caṇḍālī', r'caṇḍālas', r'caṇḍal'
    ],
    'merudanda_spine': [
        r'merudaṇḍa', r'meruda\.nd\.(a|ā)', r'merudanda', r'vajradaṇḍa', r'vīṇādaṇḍa'
    ],
    'vamsadanda_pneumatics': [
        r'vaṃśadaṇḍa', r'va\.mśada\.nd\.(a|ā)', r'vamsadanda', r'śūnyapadavī', r'mahāpatha', r'granthibheda'
    ],
    'bandha_valves': [
        r'mūlabandha', r'jālandharabandha', r'uḍḍīyanabandha', r'stambhana'
    ],
    'candali_reversion': [
        r'caṇḍālī', r'ca\.nd\ālī', r'candali', r'avadhūtī', r'nirmāṇakāya', r'mahasukha'
    ]
}

def calculate_shannon_entropy(text_tokens):
    """Calculates vocabulary diversity/entropy (H) within context windows."""
    if not text_tokens:
        return 0.0
    counts = collections.Counter(text_tokens)
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def strip_html_tags(text):
    """Removes HTML blocks, headers, and style rules from text-mining view."""
    # Strip style/head blocks entirely
    text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<head.*?>.*?</head>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Strip standard single tags
    text = re.sub(r'<[^>]*>', ' ', text)
    # Normalize spaces
    return re.sub(r'\s+', ' ', text)

def scan_text_layers(target_directories):
    """Iterates through all text/html files running pure substring checks across data blocks."""
    print("[*] Initializing automated multi-format IAST text mining pass...")
    results = []
    
    files_processed = 0
    for directory in target_directories:
        if not os.path.exists(directory):
            print(f"[!] Directory path variant '{directory}' not detected locally. Skipping...")
            continue
            
        print(f"[*] Sweeping repository track: {directory}")
        # Match both standard txt files and raw html scapes from GRETIL/DCS
        files = [f for f in os.listdir(directory) if f.endswith(('.txt', '.html', '.htm'))]
        
        for file_name in files:
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                raw_content = f.read()
            
            # Clean HTML metadata boilerplate before scanning tokens
            content = strip_html_tags(raw_content).lower()
                
            file_metrics = {
                'Source_Repo': os.path.basename(directory),
                'Text_Layer': file_name, 
                'Total_Chars': len(content)
            }
            
            all_window_tokens = []
            has_matches = False
            
            for lemma_name, patterns in LEMMA_PATTERNS.items():
                combined_regex = "|".join(patterns)
                matches = list(re.finditer(combined_regex, content))
                count = len(matches)
                file_metrics[f'{lemma_name}_Count'] = count
                if count > 0:
                    has_matches = True
                
                # Pull raw text context (+/- 120 characters) around the match to parse adjacent tokens
                for match in matches:
                    start_idx = max(0, match.start() - 120)
                    end_idx = min(len(content), match.end() + 120)
                    snippet = content[start_idx:end_idx]
                    # Isolate alphabetical text slices, scrubbing out line numbering noise
                    words = re.findall(r'[a-zA-Zāīūṛṝḷḹṅñṭḍṇśṣṃḥ]+', snippet)
                    all_window_tokens.extend(words)
                    
            # Compute localized Shannon Entropy
            file_metrics['Contextual_Entropy_H'] = calculate_shannon_entropy(all_window_tokens)
            
            if has_matches:
                results.append(file_metrics)
                files_processed += 1
                if files_processed % 10 == 0 or files_processed == 1:
                    print(f"  [+] Logged layer {files_processed}: {file_name} | Entropy H: {file_metrics['Contextual_Entropy_H']}")

    if not results:
        print("\n[!] Loop finished: Zero hits detected across the targeted files.")
        print("[*] Confirm files are located in 'corpus/raw_dcs' or 'corpus/raw_gretil'.")
        return

    # Export metrics table
    df = pd.DataFrame(results)
    output_csv = "outputs/subaltern_extraction_metrics.csv"
    os.makedirs("outputs", exist_ok=True)
    df.to_csv(output_csv, index=False)
    
    print("\n" + "="*70)
    print(f"[✓] SUCCESS: Managed multi-format pipeline run completed cleanly!")
    print(f"[✓] Data dashboard metrics output to: {output_csv}")
    print(f"[✓] Successfully isolated {files_processed} distinct files with target data.")
    print("="*70 + "\n")
    print(df.head(15).to_string(index=False))

if __name__ == "__main__":
    scan_text_layers(target_directories=["corpus/raw_dcs", "corpus/raw_gretil"])
