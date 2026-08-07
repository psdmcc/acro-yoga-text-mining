import csv
import os
import matplotlib.pyplot as plt
from collections import defaultdict

INPUT_FILE = "outputs/precision_somatic_hits.csv"
OUTPUT_IMAGE = "outputs/subaltern_somatic_distribution.png"

GENRE_MAPPING = {
    "MBh": "Epics (MBh)", "Rām": "Epics (Rām)",
    "Pur": "Purāṇic Lit", "Suśr": "Āyurveda", "AHS": "Āyurveda",
    "Divyāv": "Buddhist Skt", "LAS": "Buddhist Skt",
    "TĀ": "Tantric Lit", "Gor": "Yoga", "YS": "Yoga"
}

# Explicit categories based on your project's theoretical framework
SUBALTERN_TERMS = {"caṇḍāla", "ḍomba", "plavaka", "śabara", "kirāta", "pulinda", "naṭa", "laṅghaka"}
SOMATIC_TERMS = {"āsana", "padma", "stambha", "śava", "śalabha", "vṛścika", "kūrmāsana"}

def get_genre(filename):
    for key, genre in GENRE_MAPPING.items():
        if key in filename:
            return genre
    return "Other Technical"

def generate_chart():
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: '{INPUT_FILE}' not found.")
        return

    # Tracking dictionaries for group metrics
    somatic_counts = defaultdict(int)
    subaltern_counts = defaultdict(int)
    all_genres = set()

    with open(INPUT_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header
        
        for row in reader:
            if len(row) < 3:
                continue
            filename = row[1]
            lemma = row[2].strip().lower()
            genre = get_genre(filename)
            
            all_genres.add(genre)
            if lemma in SOMATIC_TERMS:
                somatic_counts[genre] += 1
            elif lemma in SUBALTERN_TERMS:
                subaltern_counts[genre] += 1

    # Sort genres by total combined density for clean chart presentation
    sorted_genres = sorted(list(all_genres), key=lambda g: somatic_counts[g] + subaltern_counts[g], reverse=True)
    
    # Extract aligned data blocks
    genres_labels = sorted_genres
    somatic_data = [somatic_counts[g] for g in sorted_genres]
    subaltern_data = [subaltern_counts[g] for g in sorted_genres]

    # Initialize professional plot canvas
    fig, ax = plt.subplots(figsize=(12, 7))
    x = range(len(genres_labels))
    width = 0.35

    # Plot dual overlapping bar tracks
    rects1 = ax.bar([i - width/2 for i in x], somatic_data, width, label='Somatic Tech (āsana, stambha, etc.)', color='#2b5c8f')
    rects2 = ax.bar([i + width/2 for i in x], subaltern_data, width, label='Subaltern Contexts (caṇḍāla, naṭa, etc.)', color='#d95f02')

    # Formatting and labeling
    ax.set_ylabel('Absolute Token Occurrences (Log Scale)', fontsize=12, fontweight='bold')
    ax.set_title('Historical Distribution of Subaltern & Somatic Terms in Sanskrit Corpora', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(genres_labels, rotation=45, ha='right', fontsize=10)
    ax.set_yscale('log') # Logarithmic scale handles the massive data scale variance perfectly
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # Automatically add value markers on top of bars
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            if height > 0:
                ax.annotate(f'{height}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=8, alpha=0.8)

    autolabel(rects1)
    autolabel(rects2)

    plt.tight_layout()
    os.makedirs("outputs", exist_ok=True)
    plt.savefig(OUTPUT_IMAGE, dpi=300)
    print(f"[✓] SUCCESS: Professional chart exported directly to: {OUTPUT_IMAGE}")

if __name__ == "__main__":
    generate_chart()
