import os
import re
import glob
import json
from concurrent.futures import ProcessPoolExecutor

# Calibrated Regex List - Modified with flexible wildcards to catch complex Sanskrit compounds
NEW_LEMMA_CONFIG = {
    "pharmacology_botany": [
        r"mūlavi.*k rētā", r"viṣa.*stambha", r"garuḍāñjana", 
        r"dattura", r"mṛtasaṃjīvinī", r"kāladaṣṭa"
    ],
    "acrobatic_sorcery": [
        r"jambhaka", r"māyā", r"vaṃśanartin", 
        r"stambha.*śrama", r"laṅghana"
    ],
    "subaltern_extractors": [
        r"pulka[ś|s]a", r"sopāka", r"kirāta", 
        r"pulinda", r"vaiṇa", r"antyāvasāyin"
    ]
}

BASE_DIR = os.path.expanduser("~/acro-yoga-text-mining/corpus")
TARGET_DIRS = ["raw_dcs", "raw_gretil"]

# CALIBRATION: Expanding window size to 150 to capture whole stanzas and commentaries
WINDOW_SIZE = 150

TAG_SCRUB_REGEX = re.compile(r'<[^>]*>')

def process_file_worker(file_path):
    """
    Optimized worker. Compares category regexes across expanded 
    sliding context windows to pull valid intersections.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_content = f.read()
        
        if not raw_content:
            return None
            
        # Fast HTML tag removal 
        cleaned_text = TAG_SCRUB_REGEX.sub(' ', raw_content)
        tokens = [w.strip() for w in cleaned_text.split() if w.strip()]
        num_tokens = len(tokens)
        
        if num_tokens == 0:
            return None
            
        file_results = {
            "file": os.path.basename(file_path),
            "intersections": []
        }
        
        # Pre-compile categories
        compiled_regexes = {cat: [re.compile(p, re.IGNORECASE) for p in patterns] 
                            for cat, patterns in NEW_LEMMA_CONFIG.items()}

        # Scan text stream for tribal anchors
        for idx, token in enumerate(tokens):
            is_tribe = False
            for rx in compiled_regexes["subaltern_extractors"]:
                if rx.search(token):
                    is_tribe = True
                    break
                    
            if is_tribe:
                # Capture an inclusive 300-word window envelope around the anchor
                start_win = max(0, idx - WINDOW_SIZE)
                end_win = min(num_tokens, idx + WINDOW_SIZE + 1)
                window_string = " ".join(tokens[start_win:end_win])
                
                # Check for semantic overlaps inside this expanded window string
                for category in ["pharmacology_botany", "acrobatic_sorcery"]:
                    for rx in compiled_regexes[category]:
                        match = rx.search(window_string)
                        if match:
                            file_results["intersections"].append({
                                "tribe_token": token,
                                "target_category": category,
                                "matched_term": match.group(0),
                                "context_window": tokens[start_win:end_win]
                            })
                            
        if file_results["intersections"]:
            # Diagnostic flag: alert the terminal instantly when a file hits
            print(f"  [+] Match discovered in file: {file_results['file']}")
            return file_results
        return None
    except Exception:
        return None

def main():
    print("=========================================================================")
    print("LAUNCHING CALIBRATED MULTI-CORE JACCARD EXTRACTION ENGINE")
    print("=========================================================================")
    
    all_files = []
    for sub_dir in TARGET_DIRS:
        full_path = os.path.join(BASE_DIR, sub_dir)
        if os.path.exists(full_path):
            all_files.extend(glob.glob(os.path.join(full_path, "**/*"), recursive=True))
            
    all_files = [f for f in all_files if os.path.isfile(f)]
    print(f"[*] Discovered {len(all_files)} total text/HTML files.")
    print("[*] Running parallel calibrated extraction loops...")
    
    aggregated_results = []
    
    with ProcessPoolExecutor() as executor:
        for res in executor.map(process_file_worker, all_files, chunksize=50):
            if res:
                aggregated_results.append(res)
                
    print(f"\n[SUCCESS] Calibrated matrix extraction finished.")
    print(f"[+] Total files with valid subaltern intersections: {len(aggregated_results)}")
    
    output_path = os.path.expanduser("~/acro-yoga-text-mining/extracted_intersections.json")
    with open(output_path, 'w', encoding='utf-8') as out_f:
        json.dump(aggregated_results, out_f, indent=4, ensure_ascii=False)
    print(f"[+] Data configurations successfully written to: {output_path}")

if __name__ == "__main__":
    main()
