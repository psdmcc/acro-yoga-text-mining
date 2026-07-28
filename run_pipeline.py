import os
import re
import subprocess
import pandas as pd
from multiprocessing import Pool, cpu_count

# 1. CONFIGURATION
BASE_DIR = "/Users/croma/acro-yoga-text-mining"
DATA_DIR = os.path.join(BASE_DIR, "corpus/raw_gretil")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs/metrics")
CSV_DESTINATION = os.path.join(OUTPUT_DIR, "gretil_somatic_density.csv")

# Flattening targets into an optimized dict for single-pass processing
SOMATIC_LEXICON = {
    "postural_contortion": ["āsana", "pīṭha", "dārdura", "vṛścika", "tarakṣu", "padma", "śalabh"],
    "apparatus_pole": ["vaṃśa", "stambha", "khām", "gaṇe", "stamba", "veṇu"],
    "occult_magic": ["indrajāla", "jāḍū", "camatkāra", "abhicāra", "mohana", "vismaya", "sādhana", "kārmaṇa"],
    "subaltern_tribal": ["caṇḍāla", "ḍomba", "naṭa", "plavaka", "jambhaka", "kollāṭ", "śailūṣa", "bāhirika"],
    "necromancy_mortuary": ["aṭṭhi", "dhovana", "śmaśāna", "pūti", "bhūta", "kāpālika"]
}

# Build a single master regex pattern to scan the text in one single pass
MASTER_PATTERNS = {}
for category, words in SOMATIC_LEXICON.items():
    combined_pattern = "|".join(words)
    MASTER_PATTERNS[category] = re.compile(combined_pattern, re.IGNORECASE)

def clean_manuscript(text):
    # Strips basic HTML brackets instantly
    cleaned = re.sub(r'<.*?>', '', text)
    if "THE TEXT:" in cleaned:
        cleaned = cleaned.split("THE TEXT:", 1)[1]
    return cleaned

# 2. FAST SINGLE-PASS FILE WORKER
def process_single_file(file_path):
    file_name = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_data = f.read()
    except Exception:
        return None
        
    body_text = clean_manuscript(raw_data)
    words_list = body_text.split()
    total_tokens = len(words_list)
    
    if total_tokens < 100:
        return None
        
    file_row = {
        "file_name": file_name,
        "total_words": total_tokens
    }
    
    # Single pass scanning per category without string backtracking loops
    for category, pattern in MASTER_PATTERNS.items():
        occurrences = len(pattern.findall(body_text))
        file_row[f"{category}_raw_count"] = occurrences
        file_row[f"{category}_density_10k"] = round((occurrences / total_tokens) * 10000, 2) if total_tokens > 0 else 0
        
    return file_row

# 3. MULTI-CORE ORCHESTRATION PIPELINE
def run_parallel_text_mining():
    print(f"[*] Launching fast processing grid using {cpu_count()} CPU cores...")
    
    all_files = []
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(('.txt', '.htm', '.html')):
                all_files.append(os.path.join(root, file))
                
    print(f"[*] Total files loaded into memory grid: {len(all_files)}")
    
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_single_file, all_files)
        
    matrix_output = [r for r in results if r is not None]
    
    df = pd.DataFrame(matrix_output)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(CSV_DESTINATION, index=False)
    print(f"[+] Processing successful! Master sheet generated at: {CSV_DESTINATION}")

# 4. SECURE DEPLOYMENT LAYER
def deploy_to_github():
    print("[*] Initializing automated Git deployment...")
    os.chdir(BASE_DIR)
    
    # Direct repair configuration pointers to prevent truncation errors
    subprocess.run(["git", "remote", "set-url", "origin", "https://github.com"], capture_output=True)
    
    try:
        subprocess.run(["git", "add", "run_pipeline.py", CSV_DESTINATION], check=True)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("    [!] Cloud architecture is completely synchronized.")
            return

        subprocess.run(["git", "commit", "-m", "Automated update: fast single-pass text mining matrix"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("[+] Pipeline completely updated on your online repository profile!")
    except subprocess.CalledProcessError as e:
        print(f"[!] Git upload block encountered: {e}")

if __name__ == "__main__":
    run_parallel_text_mining()
    deploy_to_github()
