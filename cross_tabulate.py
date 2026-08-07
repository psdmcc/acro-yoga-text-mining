import csv
import os
import sys
from collections import defaultdict

INPUT_FILE = "outputs/precision_somatic_hits.csv"

GENRE_MAPPING = {
    "MBh": "Epics (Mahābhārata)", "Rām": "Epics (Rāmāyaṇa)",
    "ṚV": "Vedic (Saṃhitās)", "AV": "Vedic (Saṃhitās)", "MS": "Vedic (Saṃhitās)",
    "AB": "Vedic (Brāhmaṇas)", "Baudh": "Vedic (Sūtras)", "Bhār": "Vedic (Sūtras)",
    "Op": "Upanisadic Lit", "Pur": "Purāṇic Lit",
    "Suśr": "Āyurveda (Medical)", "AHS": "Āyurveda (Medical)",
    "Gor": "Yoga (Nātha)", "YS": "Yoga (Classical)", "TĀ": "Tantric Lit",
    "Divyāv": "Buddhist Sanskrit", "LAS": "Buddhist Sanskrit"
}

def get_genre(filename):
    for key, genre in GENRE_MAPPING.items():
        if key in filename:
            return genre
    return "Other Technical Śāstra"

def analyze_cross_tab():
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: Clean precision dataset '{INPUT_FILE}' not found.")
        return

    matrix = defaultdict(lambda: defaultdict(int))
    
    with open(INPUT_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # Skip header row safely
        
        for row in reader:
            if len(row) < 3:
                continue
            
            # Index 1 = File, Index 2 = Lemma
            filename = row[1]
            lemma = row[2].strip().lower()
            
            genre = get_genre(filename)
            matrix[genre][lemma] += 1

    print("\n" + "="*75)
    print("📊 SUBALTERN-SOMATIC MATRIX: CROSS-TABULATION BY TEXT GENRE")
    print("="*75)
    
    sorted_genres = sorted(matrix.items(), key=lambda x: sum(x[1].values()), reverse=True)
    
    for genre, lemmas in sorted_genres:
        total_genre_hits = sum(lemmas.values())
        print(f"\n📁 {genre.upper()} (Total Hits: {total_genre_hits})")
        print("-" * 50)
        
        sorted_lemmas = sorted(lemmas.items(), key=lambda x: x[1], reverse=True)
        for lemma, count in sorted_lemmas[:8]:
            percentage = (count / total_genre_hits) * 100
            print(f"    ↳ {lemma:<15} : {count:<4} ({percentage:.1f}%)")
            
    print("="*75 + "\n")

if __name__ == "__main__":
    analyze_cross_tab()
