import os
import csv

TARGET_DIRECTORIES = ["corpus/raw_dcs", "corpus/raw_gretil"]
print("[*] Initializing dedicated CoNLL-U Sanskrit Lemma sweep...")

SOMATIC_LEXICON = {
    "postural_contortion": ["āsana", "padma", "śalabha", "vṛścika", "kūrmāsana"],
    "apparatus_pole": ["stambha", "stambhanena", "stambhaiḥ", "stambhitavya", "stambhakrīḍa", "rajjuyāyin", "vaṃśanartin"],
    "subaltern_tribal": ["caṇḍāla", "ḍomba", "plavaka", "jambhaka", "śabara", "kirāta", "pulinda", "pīṭhasarpin", "ābhirika"],
    "street_tumblers_performers": ["kalāyana", "jhampāka", "jhampāru", "plavitṛ", "praṇālī", "pānila", "kācapātra", "śailūṣa", "kaṭakhādaka", "kelaka", "bharata", "kevala", "cakradhāra", "cakrin", "naṭa", "laṅghaka"],
    "sorcery_necromancy_expropriation": ["indrajālin", "māyākāra", "indrajālika", "abhicāravid", "mantrin", "māyāvin", "māntrika", "indrajālajña", "bṛsaya", "siddhanara", "durnarendra", "piśācavidyā", "pretasiddhi", "bhūtavidyā", "śmaśānamantrajapana", "bhautikavidyā", "śava", "gara"],
    "espionage_subversion": ["gūḍhapuruṣa", "cara", "satrin", "rasada", "chadman", "yogin", "sārthavāha"]
}

# Flatten unique target tracking array
all_terms = sorted(list(set(t.lower().strip() for terms in SOMATIC_LEXICON.values() for t in terms)), key=len, reverse=True)
lemma_counts = {term: 0 for term in all_terms}

found_count = 0
file_count = 0
extracted_rows = []

for directory in TARGET_DIRECTORIES:
    if not os.path.exists(directory):
        print(f"[!] Warning: Path '{directory}' not found locally. Skipping...")
        continue
        
    print(f"[*] Sweeping repository: {directory}")
    for root_dir, _, files in os.walk(directory):
        for f in files:
            if f.startswith('.') or not f.endswith('.conllu'):
                continue
                
            file_path = os.path.join(root_dir, f)
            file_count += 1
            
            if file_count % 100 == 0:
                print(f"    [ Processing CoNLL-U asset #{file_count}: {f} ]")
                
            try:
                with open(file_path, "r", encoding="utf-8", errors="replace") as file:
                    for line in file:
                        cleaned_line = line.strip()
                        # Skip blank lines and structural header comments
                        if not cleaned_line or cleaned_line.startswith('#'):
                            continue
                        
                        columns = cleaned_line.split('\t')
                        # CoNLL-U standard maps the explicit base Lemma string to index position 2
                        if len(columns) >= 3:
                            token_lemma = columns[2].lower().strip()
                            
                            for term in all_terms:
                                # Target exact match or compound occurrences cleanly
                                if term == token_lemma or term in token_lemma:
                                    found_count += 1
                                    lemma_counts[term] += 1
                                    
                                    extracted_rows.append({
                                        "Hit_Number": found_count,
                                        "File": f,
                                        "Lemma": term,
                                        "Sanskrit_Context": f"Token: {columns[1]} | Lemma: {columns[2]}",
                                        "Raw_Entry": cleaned_line[:100]
                                    })
            except Exception as e:
                print(f"[!] Error processing file {f}: {e}")
                continue

print(f"\n[+] CoNLL-U sweep completed. Total files parsed: {file_count}")
print(f"[+] Total accurate matches isolated: {found_count}")

# Save clean structured data straight onto disk
os.makedirs("outputs", exist_ok=True)
output_file = "outputs/real_corpus_hits.csv"
with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Hit_Number", "File", "Lemma", "Sanskrit_Context", "Raw_Entry"])
    writer.writeheader()
    writer.writerows(extracted_rows)
    
print("\n" + "="*50)
print(f"[✓] SUCCESS: Unified multi-corpus data logged directly to: {output_file}")
print("="*50)
print("\n[✓] UNIFIED REAL LEMMA DISTRIBUTION SUMMARY (DCS + GRETIL):")

# Correct tuple value sorting targeting element index [1] (the numeric count)
sorted_summary = sorted(lemma_counts.items(), key=lambda item: item[1], reverse=True)
for lemma, count in sorted_summary:
    if count > 0:
        print(f"    - {lemma}: {count} occurrences")
print("="*50 + "\n")
