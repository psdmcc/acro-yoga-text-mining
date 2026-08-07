import csv
import os
from collections import Counter, defaultdict

INPUT_FILE = "outputs/real_corpus_hits.csv"

# Broad metadata taxonomy to group your Sanskrit texts by historical genre
GENRE_MAPPING = {
    "MBh": "Epics (Mahābhārata)",
    "Rām": "Epics (Rāmāyaṇa)",
    "ṚV": "Vedic (Saṃhitās)",
    "AV": "Vedic (Saṃhitās)",
    "MS": "Vedic (Saṃhitās)",
    "AB": "Vedic (Brāhmaṇas/Sūtras)",
    "Śāṅkh": "Vedic (Brāhmaṇas/Sūtras)",
    "Baudh": "Vedic (Brāhmaṇas/Sūtras)",
    "Bhār": "Vedic (Brāhmaṇas/Sūtras)",
    "Op": "Upanisadic Literature",
    "Pur": "Purāṇic Literature",
    "Suśr": "Medical/Āyurveda",
    "AHS": "Medical/Āyurveda",
    "SarvSund": "Medical/Āyurveda",
    "Gor": "Yoga/Nātha Texts",
    "YS": "Yoga/Philosophical",
    "TĀ": "Tantric Literature",
    "ArthaŚ": "Political/Arthaśāstra",
    "Smṛ": "Dharmaśāstra/Legal Texts"
}

def identify_genre(filename):
    """Parses DCS/GRETIL file naming conventions to classify texts."""
    for key, genre in GENRE_MAPPING.items():
        if key in filename:
            return genre
    return "Other/Technical Shastra"

def run_analysis():
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: '{INPUT_FILE}' not found yet. Wait for the main sweep script to finish!")
        return

    print("[*] Launching Subaltern-Somatic Corpus Data Analysis Engine...")
    
    total_hits = 0
    lemma_frequencies = Counter()
    genre_distribution = Counter()
    text_specific_hits = defaultdict(int)
    
    # Read and parse the newly generated CSV file
    with open(INPUT_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_hits += 1
            lemma = row["Lemma"]
            filename = row["File"]
            
            lemma_frequencies[lemma] += 1
            text_specific_hits[filename] += 1
            
            # Categorize the text genre using filename markers
            genre = identify_genre(filename)
            genre_distribution[genre] += 1

    # Output analytical insights directly to the dashboard terminal
    print("\n" + "="*60)
    print(f"📊 ABSOLUTE CORPUS ANALYSIS REPORT (Total Hits: {total_hits})")
    print("="*60)
    
    print("\n[1] TOP 10 MOST FREQUENT LEMMAS:")
    for lemma, count in lemma_frequencies.most_common(10):
        print(f"    - {lemma:<18} : {count} occurrences")
        
    print("\n[2] HITS DISTRIBUTED BY HISTORICAL GENRE:")
    for genre, count in genre_distribution.most_common():
        percentage = (count / total_hits) * 100
        print(f"    - {genre:<25} : {count:<5} ({percentage:.1f}%)")
        
    print("\n[3] TOP 5 HOTSPOT TEXT FILES:")
    sorted_texts = sorted(text_specific_hits.items(), key=lambda x: x[1], reverse=True)
    for filename, count in sorted_texts[:5]:
        print(f"    - {filename:<50} : {count} hits")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_analysis()
