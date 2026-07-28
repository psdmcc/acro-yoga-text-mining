import os
import re
import subprocess
import pandas as pd
from multiprocessing import Pool, cpu_count

# 1. CORE CONFIGURATION
BASE_DIR = "/Users/croma/acro-yoga-text-mining"
DATA_DIR = os.path.join(BASE_DIR, "corpus/raw_gretil")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs/metrics")
CSV_DESTINATION = os.path.join(OUTPUT_DIR, "gretil_somatic_density.csv")

SOMATIC_LEXICON = {
    "postural_contortion": [r"āsana", r"pīṭha", r"dārdura", r"vṛścika", r"tarakṣu", r"padma", r"śalabh"],
    "apparatus_pole": [r"vaṃśa", r"stambha", r"khām", r"gaṇe", r"stamba", r"veṇu"],
    "occult_magic": [r"indrajāla", r"jāḍū", r"camatkāra", r"abhicāra", r"mohana", r"vismaya", r"sādhana", r"kārmaṇa"],
    "subaltern_tribal": [r"caṇḍāla", r"ḍomba", r"naṭa", r"plavaka", r"jambhaka", r"kollāṭ", r"śailūṣa", r"bāhirika"],
    "necromancy_mortuary": [r"aṭṭhi", r"dhovana", r"śmaśāna", r"pūti", r"bhūta", r"kāpālika"]
}

compiled_lexicon = {cat: [re.compile(p, re.IGNORECASE) for p in patterns] 
                    for cat, patterns in SOMATIC_LEXICON.items()}

def clean_manuscript(text):
    cleaned = re.sub(r'<.*?>', '', text)
    if "THE TEXT:" in cleaned:
        cleaned = cleaned.split("THE TEXT:", 1)[1]
    return cleaned

# 2. PARALLEL WORKER ENGINE (Processes 1 single file)
def process_single_file(file_path):
    file_name = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_data = f.read()
    except Exception:
        return None
        
    body_text = clean_manuscript(raw_data)
    total_tokens = len(body_text.split())
    
    if total_tokens < 100:
        return None
        
    file_row = {
        "file_name": file_name,
        "total_words": total_tokens
    }
    
    for category, regex_patterns in compiled_lexicon.items():
        occurrences = sum(len(pattern.findall(body_text)) for pattern in regex_patterns)
        file_row[f"{category}_raw_count"] = occurrences
        file_row[f"{category}_density_10k"] = round((occurrences / total_tokens) * 10000, 2)
        
    return file_row

# 3. MULTI-CORE ORCHESTRATION PIPELINE
def run_parallel_text_mining():
    print(f"[*] Launching parallel processing grid using {cpu_count()} CPU cores...")
    
    # Collect absolute paths of all targeting text segments
    all_files = []
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(('.txt', '.htm', '.html')):
                all_files.append(os.path.join(root, file))
                
    print(f"[*] Total files loaded into memory grid: {len(all_files)}")
    
    # Fire up multi-core processing array
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_single_file, all_files)
        
    # Drop empty execution frames
    matrix_output = [r for r in results if r is not None]
    
    df = pd.DataFrame(matrix_output)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(CSV_DESTINATION, index=False)
    print(f"[+] Multi-core processing successful! Logs saved to: {CSV_DESTINATION}")

# 4. SECURE DEPLOYMENT LAYER
def deploy_to_github():
    print("[*] Initializing automated Git deployment...")
    os.chdir(BASE_DIR)
    
    # Explicitly overwrite remote path pointers to circumvent truncation glitches
    subprocess.run(["git", "remote", "set-url", "origin", "https://github.com"], capture_output=True)
    
    try:
        subprocess.run(["git", "add", "run_pipeline.py", CSV_DESTINATION], check=True)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("    [!] Cloud architecture is already completely synchronized.")
            return

        subprocess.run(["git", "commit", "-m", "Automated update: multi-core text mining execution matrix"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("[+] Pipeline completely updated on your online repository profile!")
    except subprocess.CalledProcessError as e:
        print(f"[!] Git upload block encountered: {e}")

if __name__ == "__main__":
    # Skipping download tracking since 403MiB library payload is already securely extracted local
    run_parallel_text_mining()
    deploy_to_github()
