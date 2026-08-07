import csv
import os
from collections import Counter

INPUT_FILE = "outputs/real_corpus_hits.csv"
OUTPUT_CLEAN = "outputs/precision_somatic_hits.csv"

# Words we want to look at with strict absolute matching to remove root bleed-through
STRICT_TARGETS = {
    "āsana", "padma", "śalabha", "vṛścika", "kūrmāsana",
    "stambha", "caṇḍāla", "ḍomba", "plavaka", "śabara", 
    "kirāta", "pulinda", "naṭa", "laṅghaka", "māyāvin", 
    "indrajālin", "śava", "gūḍhapuruṣa"
}

def clean_data():
    if not os.path.exists(INPUT_FILE):
        print("[!] Missing input file.")
        return

    clean_count = 0
    precise_frequencies = Counter()
    cleaned_rows = []

    with open(INPUT_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lemma = row["Lemma"].strip().lower()
            
            # Match strictly against our targeted, non-ambiguous vocabulary list
            if lemma in STRICT_TARGETS:
                clean_count += 1
                precise_frequencies[lemma] += 1
                cleaned_rows.append(row)

    # Save filtered output
    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_CLEAN, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Hit_Number", "File", "Lemma", "Sanskrit_Context", "Raw_Entry"])
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print("\n" + "="*50)
    # Correct item sorting index for numeric distribution tracking
    print(f"🎯 PRECISION SCAN COMPLETED (Isolated {clean_count} High-Value Hits)")
    print("="*50)
    for word, count in precise_frequencies.most_common():
        print(f"    - {word:<15}: {count} occurrences")
    print("="*50 + "\n")

if __name__ == "__main__":
    clean_data()
