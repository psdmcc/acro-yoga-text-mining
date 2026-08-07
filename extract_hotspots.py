import csv
import os

INPUT_FILE = "outputs/precision_somatic_hits.csv"
OUTPUT_REPORT = "outputs/subaltern_somatic_citations.txt"

SUBALTERN_TERMS = {"caṇḍāla", "ḍomba", "plavaka", "śabara", "kirāta", "pulinda", "naṭa", "laṅghaka"}
SOMATIC_TERMS = {"āsana", "padma", "stambha", "śava", "śalabha", "vṛścika", "kūrmāsana"}

def generate_citation_report():
    if not os.path.exists(INPUT_FILE):
        print("[!] Precision dataset not found.")
        return

    print("[*] Filtering text lines for direct Subaltern-Somatic overlap...")
    
    # Track which files have subaltern terms and which have somatic terms
    file_subalterns = {}
    file_somatics = {}
    
    # Store rows to read through them again
    all_rows = []
    
    with open(INPUT_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None) # Skip header
        
        for row in reader:
            if len(row) < 5:
                continue
            filename = row[1]
            lemma = row[2].strip().lower()
            context = row[3]
            raw_entry = row[4]
            
            all_rows.append((filename, lemma, context, raw_entry))
            
            if lemma in SUBALTERN_TERMS:
                if filename not in file_subalterns:
                    file_subalterns[filename] = set()
                file_subalterns[filename].add(lemma)
                
            if lemma in SOMATIC_TERMS:
                if filename not in file_somatics:
                    file_somatics[filename] = set()
                file_somatics[filename].add(lemma)

    # Find the files where BOTH categories show up
    shared_hotspot_files = set(file_subalterns.keys()) & set(file_somatics.keys())
    
    print(f"[✓] Found {len(shared_hotspot_files)} specific text chapters with absolute category overlaps.")
    
    # Write entries out into a clean reading report
    with open(OUTPUT_REPORT, "w", encoding="utf-8") as out:
        out.write("===================================================================\n")
        out.write("📖 PRIMARY SOURCE CITATION REPORT: SUBALTERN-SOMATIC HOTSPOTS\n")
        out.write("===================================================================\n\n")
        
        for target_file in sorted(shared_hotspot_files):
            out.write(f"📄 FILE: {target_file}\n")
            out.write(f"   ↳ Subaltern footprint: {list(file_subalterns[target_file])}\n")
            out.write(f"   ↳ Somatic footprint:   {list(file_somatics[target_file])}\n")
            out.write("-" * 68 + "\n")
            
            # Print up to 4 contextual text quotes from this file to keep it readable
            printed = 0
            for filename, lemma, context, raw_entry in all_rows:
                if filename == target_file:
                    out.write(f"   [{lemma.upper()}] -> {context}\n")
                    printed += 1
                    if printed >= 4:
                        out.write("   [... additional entries truncated for brevity ...]\n")
                        break
            out.write("\n" + "="*68 + "\n\n")

    print(f"[✓] SUCCESS: Citation report generated at: {OUTPUT_REPORT}")

if __name__ == "__main__":
    generate_citation_report()
