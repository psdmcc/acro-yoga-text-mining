import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. PATH CONFIGURATION
BASE_DIR = "/Users/croma/acro-yoga-text-mining"
CSV_PATH = os.path.join(BASE_DIR, "outputs/metrics/gretil_somatic_density.csv")
IMG_PATH = os.path.join(BASE_DIR, "outputs/visualizations/somatic_chronology_timeline.png")

# 2. ANCIENT & MEDIEVAL TEXT CHRONOLOGY DICTIONARY MAP
# Maps specific GRETIL/DCS file signatures to estimated historical centuries
CHRONOLOGY_MAP = {
    # Vedic, Epic, and Early Sūtra Layers (Pre-Common Era to Early CE)
    "sa_baudhAyanadharmasUtra.htm": -2,
    "Baudhayanadharmasutra": -2,
    "Arthasastra": -3,
    "sa_vinayasUtra.htm": 4,
    "Vinayasutra": 4,
    "Manusmrti": 2,
    "ram_": 2,
    
    # Classical & Early Medieval Layers (5th - 10th Century CE)
    "Harsacarita": 7,
    "sa_bharata": 5,
    "sa_kezava-kauzikapaddhati.htm": 6,
    "Vaikhanasa": 4,
    "sa_daNDin": 7,
    
    # Late Medieval Scholastic & Courtly Layers (11th - 16th Century CE)
    "Manasollasa": 12,
    "sa_jayatIrtha": 14,
    "sa_rUpagosvAmin": 16,
    "Mallapurana": 15,
    "Skandapurana": 10,
    "sa_nAradapurANa.htm": 10,
    "sa_garuDapurANa.htm": 10,
    "vcpss_u.htm": 14, # Kullukabhatta Manu Gloss
    "schnzsw_u.htm": 18 # Schmidt Dictionary Archive
}

def assign_century(file_name):
    for key, century in CHRONOLOGY_MAP.items():
        if key.lower() in file_name.lower():
            return century
    # Fallback default estimations based on general textual markers
    if "purana" in file_name.lower():
        return 9
    if "sutra" in file_name.lower():
        return 2
    if "b12" in file_name.lower() or "b13" in file_name.lower():
        return 2 # Mahabharata Epic Layers
    return None

def build_timeline_matrix():
    if not os.path.exists(CSV_PATH):
        print(f"[!] Source dataset missing at: {CSV_PATH}")
        return

    print("[*] Ingesting metrics database for historical timeline mapping...")
    df = pd.read_csv(CSV_PATH)
    
    # Apply chronological century tags
    df['century'] = df['file_name'].apply(assign_century)
    
    # Calculate custom composite indexes
    df['subversive_mobility_score'] = (
        df['caravan_trade_transit_density_10k'] + 
        df['espionage_subversion_density_10k'] + 
        df['climbing_leaping_density_10k']
    )
    df['somatic_contortion_score'] = (
        df['postural_contortion_density_10k'] + 
        df['apparatus_pole_density_10k']
    )
    
    # Isolate relevant data nodes
    timeline_df = df[df['century'].notna() & ((df['subversive_mobility_score'] > 0) | (df['somatic_contortion_score'] > 0))]
    
    if timeline_df.empty:
        print("[!] No chronologically mapped text nodes found with current data slices.")
        return

    # 3. RENDER HISTORICAL EVOLUTION PLOT
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)

    # Plot the historic trajectory lines
    sns.lineplot(
        data=timeline_df, x='century', y='subversive_mobility_score', 
        color='#007A5A', label='Subversive Mobility Index (Clandestine Transit / Leaping / Spies)', 
        marker='o', errorbar=None, ax=ax, linewidth=2
    )
    sns.lineplot(
        data=timeline_df, x='century', y='somatic_contortion_score', 
        color='#4A154B', label='Somatic Contortion Index (Postural Stasis / Pole Apparatus)', 
        marker='s', errorbar=None, ax=ax, linewidth=2
    )

    # Label top historical transition outliers
    top_outliers = timeline_df.nlargest(6, 'somatic_contortion_score')
    for idx, row in top_outliers.iterrows():
        clean_label = row['file_name'].split('-')[0].replace('_u.htm', '').replace('.conllu', '')
        ax.annotate(
            clean_label, (row['century'], row['somatic_contortion_score']),
            textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.4, ec="gray", lw=0.5)
        )

    # Clean up x-axis century formatting labels (BCE to CE)
    ax.set_title("The Contortionist Turn: Diachronic Evolution of the Acro-Yoga Complex\n(Historical Tracking of Normalized Composite Densities Over Two Millennia)", fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel("Historical Timeline (Century of Composition)", fontsize=10)
    ax.set_ylabel("Normalized Semantic Density (Per 10k Words)", fontsize=10)
    
    def format_century(val, pos):
        if val < 0: return f"{int(abs(val))} BCE"
        if val == 0: return "1st CE"
        return f"{int(val)}th CE"
    ax.xaxis.set_major_formatter(format_century)
    
    ax.legend(loc="upper left", frameon=True)
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(IMG_PATH), exist_ok=True)
    plt.savefig(IMG_PATH, bbox_inches='tight')
    plt.close()
    print(f"[+] Historical timeline chart successfully rendered at: {IMG_PATH}")

if __name__ == "__main__":
    build_timeline_matrix()
