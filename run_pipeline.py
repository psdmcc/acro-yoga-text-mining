import os
import re
import subprocess
import pandas as pd

# 1. CORE DEFINITIONS & CONFIGURATION
BASE_DIR = "/Users/croma/acro-yoga-text-mining"
DATA_DIR = os.path.join(BASE_DIR, "corpus/raw_gretil")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs/metrics")
CSV_DESTINATION = os.path.join(OUTPUT_DIR, "gretil_somatic_density.csv")
GRETIL_URL = "https://github.com/psdmcc/acro-yoga-text-mining"

SOMATIC_LEXICON = {
    "postural_contortion": [r"āsana", r"pīṭha", r"dārdura", r"vṛścika", r"tarakṣu", r"padma", r"śalabh"],
    "apparatus_pole": [r"vaṃśa", r"stambha", r"khām", r"gaṇe", r"stamba", r"veṇu"],
    "occult_magic": [r"indrajāla", r"jāḍū", r"camatkāra", r"abhicāra", r"mohana", r"vismaya", r"sādhana", r"kārmaṇa"],
    "subaltern_tribal": [r"caṇḍāla", r"ḍomba", r"naṭa", r"plavaka", r"jambhaka", r"kollāṭ", r"śailūṣa", r"bāhirika"],
    "necromancy_mortuary": [r"aṭṭhi", r"dhovana", r"śmaśāna", r"pūti", r"bhūta", r"kāpālika"]
}

compiled_lexicon = {cat: [re.compile(p, re.IGNORECASE) for p in patterns] 
                    for cat, patterns in SOMATIC_LEXICON.items()}

# 2. AUTOMATED DATA ACQUISITION LAYER
def sync_gretil_corpus():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_DIR) or len([f for f in os.listdir(DATA_DIR) if f.endswith(('.txt', '.htm', '.html'))]) == 0:
        print("[*] Corpus layer missing. Downloading GRETIL library via Git...")
        temp_clone = os.path.join(BASE_DIR, "GRETIL-mirror")
        
        subprocess.run(["git", "clone", "--depth", "1", GRETIL_URL, temp_clone], check=True)
        
        for root, dirs, files in os.walk(temp_clone):
            for file in files:
                if file.endswith(('.txt', '.htm', '.html')):
                    src = os.path.join(root, file)
                    dest = os.path.join(DATA_DIR, file)
                    os.rename(src, dest)
                    
        subprocess.run(["rm", "-rf", temp_clone], check=True)
        print("[+] GRETIL corpus layer extracted and stabilized.")
    else:
        print("[*] Existing GRETIL corpus layer identified local. Skipping download module.")

# 3. COMPUTATIONAL ANALYTICS ENGINE
def clean_manuscript(text):
    cleaned = re.sub(r'<.*?>', '', text)
    if "THE TEXT:" in cleaned:
        cleaned = cleaned.split("THE TEXT:", 1)
    return cleaned

def run_text_mining():
    print("[*] Launching multi-threaded lexical scanning array across texts...")
    matrix_output = []

    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(('.txt', '.htm', '.html')):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        raw_data = f.read()
                except Exception:
                    continue
                
                body_text = clean_manuscript(raw_data)
                total_tokens = len(body_text.split())
                
                if total_tokens < 100:
                    continue
                
                file_row = {
                    "file_name": file,
                    "total_words": total_tokens
                }
                
                for category, regex_patterns in compiled_lexicon.items():
                    occurrences = 0
                    for pattern in regex_patterns:
                        occurrences += len(pattern.findall(body_text))
                    file_row[f"{category}_raw_count"] = occurrences
                    file_row[f"{category}_density_10k"] = round((occurrences / total_tokens) * 10000, 2)
                
                matrix_output.append(file_row)
                
    df = pd.DataFrame(matrix_output)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(CSV_DESTINATION, index=False)
    print(f"[+] Output logs saved to: {CSV_DESTINATION}")

# 4. CLOUD TRANSMISSION LAYER
def deploy_to_github():
    print("[*] Initializing automated Git cloud deployment...")
    os.chdir(BASE_DIR)
    try:
        subprocess.run(["git", "add", "run_pipeline.py", CSV_DESTINATION], check=True)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("    [!] Cloud architecture is already up to date.")
            return

        subprocess.run(["git", "commit", "-m", "Automated updates: compiled GRETIL somatic density metrics"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("[+] Pipeline completely updated on your online repository.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Git cloud transmission halted: {e}")

if __name__ == "__main__":
    sync_gretil_corpus()
    run_text_mining()
    deploy_to_github()
