import os
import re
import subprocess
import pandas as pd
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CORE CONFIGURATION
BASE_DIR = "/Users/croma/acro-yoga-text-mining"
DATA_DIR = os.path.join(BASE_DIR, "corpus/raw_gretil")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs/metrics")
VIS_DIR = os.path.join(BASE_DIR, "outputs/visualizations")
CSV_DESTINATION = os.path.join(OUTPUT_DIR, "gretil_somatic_density.csv")
IMG_DESTINATION = os.path.join(VIS_DIR, "somatic_overlap_matrix.png")

SOMATIC_LEXICON = {
    "postural_contortion": ["āsana", "pīṭha", "dārdura", "vṛścika", "tarakṣu", "padma", "śalabh"],
    "apparatus_pole": ["vaṃśa", "stambha", "khām", "gaṇe", "stamba", "veṇu"],
    "occult_magic": ["indrajāla", "jāḍū", "camatkāra", "abhicāra", "mohana", "vismaya", "sādhana", "kārmaṇa"],
    "subaltern_tribal": ["caṇḍāla", "ḍomba", "naṭa", "plavaka", "jambhaka", "kollāṭ", "śailūṣa", "bāhirika"],
    "necromancy_mortuary": ["aṭṭhi", "dhovana", "śmaśāna", "pūti", "bhūta", "kāpālika"]
}

MASTER_PATTERNS = {}
for category, words in SOMATIC_LEXICON.items():
    MASTER_PATTERNS[category] = re.compile("|".join(words), re.IGNORECASE)

def clean_manuscript(text):
    cleaned = re.sub(r'<.*?>', '', text)
    if "THE TEXT:" in cleaned:
        cleaned = cleaned.split("THE TEXT:", 1)[1]
    return cleaned

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
        
    file_row = {"file_name": file_name, "total_words": total_tokens}
    
    for category, pattern in MASTER_PATTERNS.items():
        occurrences = len(pattern.findall(body_text))
        file_row[f"{category}_raw_count"] = occurrences
        file_row[f"{category}_density_10k"] = round((occurrences / total_tokens) * 10000, 2) if total_tokens > 0 else 0
        
    return file_row

# 2. RUN PARALLEL DATA MINING
def execute_text_mining():
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

# 3. GENERATE ACADEMIC SCATTER PLOT
def generate_academic_plot():
    if not os.path.exists(CSV_DESTINATION):
        return

    print("[*] Parsing textual analytics table to isolate density intersections...")
    df = pd.read_csv(CSV_DESTINATION)
    overlap_df = df[(df['subaltern_tribal_raw_count'] > 0) & (df['postural_contortion_raw_count'] > 0)]

    if overlap_df.empty:
        print("[!] No overlapping hits identified yet across current regex constraints.")
        return

    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)

    sns.scatterplot(
        data=overlap_df, x='subaltern_tribal_density_10k', y='postural_contortion_density_10k',
        size='total_words', sizes=(40, 400), alpha=0.6, color='#4A154B', edgecolor='black', linewidth=0.5, ax=ax
    )

    top_outliers = overlap_df.assign(
        score=overlap_df['subaltern_tribal_density_10k'] * overlap_df['postural_contortion_density_10k']
    ).nlargest(5, 'score')

    for idx, row in top_outliers.iterrows():
        clean_label = row['file_name'].replace('_u.htm', '').replace('.txt', '')
        ax.annotate(
            clean_label, (row['subaltern_tribal_density_10k'], row['postural_contortion_density_10k']),
            textcoords="offset points", xytext=(5, 5), ha='left', fontsize=8, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.3, ec="gray", lw=0.5)
        )

    ax.set_title("The Acro-Yoga Complex: Subaltern-Postural Semantic Overlap Matrix\n(Normalized Density Per 10k Tokens Across GRETIL)", fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel("Subaltern / Tribal Identity Vocabulary Density (Per 10k Words)", fontsize=10)
    ax.set_ylabel("Postural / Contortionist Somatic Density (Per 10k Words)", fontsize=10)
    
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[-3:], labels[-3:], title="Manuscript Word Count", loc="upper right", frameon=True)

    plt.tight_layout()
    os.makedirs(VIS_DIR, exist_ok=True)
    plt.savefig(IMG_DESTINATION, bbox_inches='tight')
    plt.close()
    print(f"[+] Academic plot compiled and exported cleanly to: {IMG_DESTINATION}")

# 4. SECURE CLOUD DEPLOYMENT
def deploy_to_github():
    print("[*] Initializing automated Git deployment...")
    os.chdir(BASE_DIR)
    
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", "https://github.com"], check=True)
    
    try:
        subprocess.run(["git", "add", "run_pipeline.py", CSV_DESTINATION, IMG_DESTINATION], check=True)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("    [!] Cloud architecture is completely synchronized.")
            return

        subprocess.run(["git", "commit", "-m", "Automated update: fast single-pass text mining and visualization"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("[+] Pipeline completely updated on your online repository profile!")
    except subprocess.CalledProcessError as e:
        print(f"[!] Git upload block encountered: {e}")

if __name__ == "__main__":
    execute_text_mining()
    generate_academic_plot()
    deploy_to_github()
