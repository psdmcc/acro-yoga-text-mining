import json
import os

JSON_FILE = "somatic_network.json"

# Master vocabulary extraction pass from the new text-critical ledger
NEW_LEMMAS = {
    "poison_necromancy": [
        "garuḍāñjana", "manushyakapālasthi", "mṛtasaṃjīvinī", 
        "kāladaṣṭasya", "nasyaṃ", "sarpavisha"
    ],
    "postural_contortion": [
        "vṛścikāsana", "timira", "unmīlita"
    ],
    "transcultural_hellenistic": [
        "kollourion", "tropicamide", "ios", "xriesthai", 
        "pharmakon_androthonon", "echidnae", "magas", 
        "orexis", "epode", "gorgon"
    ],
    "epic_grappling_tactics": [
        "viṣame", "sarpa_daṣṭa", "mukhastambhakaraṃ"
    ]
}

def inject_final_matrix():
    if not os.path.exists(JSON_FILE):
        print(f"Initializing clean data shell...")
        database = {"postural_contortion": [], "poison_necromancy": [], "transcultural_hellenistic": [], "epic_grappling_tactics": []}
    else:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            database = json.load(f)

    print("=" * 70)
    print("EXECUTING MASTER DATA INJECTION VECTOR: ALCHEMICAL TOXICOLOGY")
    print("=" * 70)

    for category, words in NEW_LEMMAS.items():
        if category not in database:
            database[category] = []
        added = []
        for word in words:
            if word not in database[category]:
                database[category].append(word)
                added.append(word)
        if added:
            print(f" -> [{category}]: Injected {added}")

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=4, ensure_ascii=False)
        
    print("=" * 70)
    print("DATA PAYLOAD STABILIZED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    inject_final_matrix()
