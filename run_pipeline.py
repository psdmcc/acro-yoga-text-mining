import os
import re
import subprocess
import urllib.request
import zipfile
import pandas as pd
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
import seaborn as sns

# 1. ABSOLUTE PATH CONFIGURATION
BASE_DIR = "/Users/croma/acro-yoga-text-mining"
GRETIL_DIR = os.path.join(BASE_DIR, "corpus/raw_gretil")
DCS_DIR = os.path.join(BASE_DIR, "corpus/raw_dcs")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs/metrics")
VIS_DIR = os.path.join(BASE_DIR, "outputs/visualizations")
CSV_DESTINATION = os.path.join(OUTPUT_DIR, "gretil_somatic_density.csv")
IMG_DESTINATION = os.path.join(VIS_DIR, "somatic_overlap_matrix.png")

# EXPANDED LEXICON ARRAY
SOMATIC_LEXICON = {
    "postural_contortion": ["āsana", "pīṭha", "dārdura", "vṛścika", "tarakṣu", "padma", "śalabh"],
    "apparatus_pole": ["vaṃśa", "stambha", "khām", "gaṇe", "stamba", "veṇu"],
    "subaltern_tribal": ["caṇḍāla", "ḍomba", "naṭa", "plavaka", "jambhaka", "kollāṭ", "śailūṣa", "bāhirika"],
    "poison_necromancy": ["viṣa", "gara", "māraṇa", "śmaśāna", "vetāla", "kāpālika", "bhūta", "pūti", "śava"],
    "sorcery_magic": ["indrajāla", "jāḍū", "camatkāra", "abhicāra", "mohana", "vismaya", "sādhana", "māyā", "kuhaka", "gāruḍa"],
    "espionage_subversion": ["gūḍhapuruṣa", "cara", "spāśa", "satrin", "tikṣṇa", "rasada", "bhikṣukī", "chadman", "kāpāṭika"],
    "climbing_leaping": ["ārohaṇa", "langhana", "plavana", "utpatana", "skandhana", "kūrdana"],
    "caravan_trade_transit": ["sārthavāha", "vaṇij", "paṇya", "vipṇi", "patha", "mārga", "śulka", "saṃvāha", "deśāntara"]
}

MASTER_PATTERNS = {cat: re.compile("|".join(words), re.IGNORECASE) for cat, words in SOMATIC_LEXICON.items()}

# 2. AUTOMATED DCS INGESTION
def sync_dcs_nodes():
    os.makedirs(DCS_DIR, exist_ok=True)
    if len(os.listdir(DCS_DIR)) == 0:
        print("[*] Downloading Oliver Hellwig's DCS data corpus...")
        archive_path = os.path.join(BASE_DIR, "dcs_main.zip")
        
        link_domain = "https://github.com"
        link_account = "OliverHellwig"
        link_repo = "sanskrit"
        link_suffix = "archive/refs/heads/master.zip"
        dcs_url = f"{link_domain}/{link_account}/{link_repo}/{link_suffix}"
        
        try:
            urllib.request.urlretrieve(dcs_url, archive_path)
            print("[+] Download complete. Extracting CoNLL-U annotation rows...")
            
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    if "/dcs/data/conllu/" in member and member.endswith(".conllu"):
                        filename = os.path.basename(member)
                        if filename:
                            source = zip_ref.read(member)
                            with open(os.path.join(DCS_DIR, filename), "wb") as f:
                                f.write(source)
            print("[+] DCS lemmatization nodes successfully cached local.")
        except Exception as e:
            print(f"[!] DCS download error: {e}")
        finally:
            if os.path.exists(archive_path):
                os.remove(archive_path)
    else:
        print("[*] Verified local DCS data nodes. Skipping asset download loop.")

# 3. HIGH-SPEED PARALLEL SCANNER
def clean_manuscript(text):
    cleaned = re.sub(r'<.*?>', '', text)
    if "THE TEXT:" in cleaned:
        cleaned = cleaned.split("THE TEXT:", 1)
    return cleaned

def process_single_file(file_path):
    file_name = os.path.basename(file_path)
    is_dcs = file_path.endswith('.conllu')
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_data = f.read()
    except Exception:
        return None

    if is_dcs:
        lemmas = []
        for line in raw_data.split('\n'):
            if line.startswith('#') or not line.strip():
                continue
            parts = line.split('\t')
            if len(parts) > 2:
                lemma_string = parts[2].strip()
                if lemma_string:
                    lemmas.append(lemma_string)
        body_text = " ".join(lemmas)
        total_tokens = len(lemmas)
    else:
        body_text = clean_manuscript(raw_data)
        total_tokens = len(body_text.split())
        
    if total_tokens < 100:
        return None
        
    file_row = {"file_name": file_name, "corpus_origin": "DCS" if is_dcs else "GRETIL", "total_words": total_tokens}
    for category, pattern in MASTER_PATTERNS.items():
        occurrences = len(pattern.findall(body_text))
        file_row[f"{category}_raw_count"] = occurrences
        file_row[f"{category}_density_10k"] = round((occurrences / total_tokens) * 10000, 2) if total_tokens > 0 else 0
        
    return file_row

def run_parallel_text_mining():
    print(f"[*] Deploying text-mining array across {cpu_count()} CPU threads...")
    all_files = []
    for folder, ext in [(GRETIL_DIR, ('.txt', '.htm', '.html')), (DCS_DIR, ('.conllu',))]:
        if os.path.exists(folder):
            for root, _, files in os.walk(folder):
                for f in files:
                    if f.endswith(ext):
                        all_files.append(os.path.join(root, f))
                        
    print(f"[*] Total files loaded into multi-core grid: {len(all_files)}")
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_single_file, all_files)
        
    df = pd.DataFrame([r for r in results if r is not None])
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(CSV_DESTINATION, index=False)
    print(f"[+] Consolidated database table updated at: {CSV_DESTINATION}")

# 4. COMPREHENSIVE MULTI-DIMENSIONAL ACADEMIC SCATTER PLOT
def generate_academic_plot():
    if not os.path.exists(CSV_DESTINATION):
        return
    df = pd.read_csv(CSV_DESTINATION)
    
    # Establish a complex research axis score combining transit, trade, climbing, and espionage
    df['subversive_mobility_score'] = (
        df['caravan_trade_transit_density_10k'] + 
        df['espionage_subversion_density_10k'] + 
        df['climbing_leaping_density_10k']
    )
    df['somatic_contortion_score'] = (
        df['postural_contortion_density_10k'] + 
        df['apparatus_pole_density_10k']
    )
    
    overlap_df = df[(df['subversive_mobility_score'] > 0) & (df['somatic_contortion_score'] > 0)]
    if overlap_df.empty:
        print("[!] No active text overlaps identified for plot generation.")
        return

    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(13, 9), dpi=300)

    sns.scatterplot(
        data=overlap_df, x='subversive_mobility_score', y='somatic_contortion_score',
        hue='corpus_origin', palette={'GRETIL': '#4A154B', 'DCS': '#007A5A'},
        size='total_words', sizes=(40, 500), alpha=0.7, edgecolor='black', linewidth=0.5, ax=ax
    )

    top_outliers = overlap_df.assign(
        total_score=overlap_df['subversive_mobility_score'] * overlap_df['somatic_contortion_score']
    ).nlargest(8, 'total_score')

    for idx, row in top_outliers.iterrows():
        clean_label = row['file_name'].replace('_u.htm', '').replace('.txt', '').replace('.conllu', '')
        ax.annotate(
            clean_label, (row['subversive_mobility_score'], row['somatic_contortion_score']),
            textcoords="offset points", xytext=(6, 6), ha='left', fontsize=8, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.4, ec="gray", lw=0.5)
        )

    ax.set_title("The Acro-Yoga Complex: Subversive Mobility vs. Somatic Contortion\n(Composite Density Profiles Aggregated Across GRETIL & DCS)", fontsize=11, fontweight='bold', pad=15)
    ax.set_xlabel("Subversive Mobility Index (Caravan Transit + Espionage + Leaping Density)", fontsize=10)
    ax.set_ylabel("Somatic Contortion Index (Postural + Pole Apparatus Density)", fontsize=10)
    plt.tight_layout()
    os.makedirs(VIS_DIR, exist_ok=True)
    plt.savefig(IMG_DESTINATION, bbox_inches='tight')
    plt.close()
    print(f"[+] Expanded multi-source academic scatter plot successfully rendered at: {IMG_DESTINATION}")

if __name__ == "__main__":
    sync_dcs_nodes()
    run_parallel_text_mining()
    generate_academic_plot()
