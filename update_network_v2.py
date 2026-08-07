import json
import os

JSON_FILE = "somatic_network.json"

# New technical terms extracted from the epic, shastric, and vernacular registries
NEW_LEMMAS = {
    "postural_contortion": ["saṃkocita", "vikucita", "āhita", "dhṛtam"],
    "apparatus_pole": ["mallakhamb"],
    "espionage_subversion": ["cāṇūra", "muṣṭika", "kuvalayāpīḍa"],
    "epic_grappling_tactics": [
        "āsphoṭa", "gajadanta", "gajayuddha", "bāhuvighaṭṭita", 
        "kakṣābandha", "urohasta", "tṛṇpīḍa", "pūrṇakumbha", 
        "pūrṇayoga", "pṛṣṭhabhaṅga", "bāhuniḥsṛta"
    ],
    "indo_persian_vernacular": ["gā’o pachāṛ", "ghoṛā pachāṛ", "āhū pachāṛ"]
}

def inject_lemmas():
    if not os.path.exists(JSON_FILE):
        print(f"Error: '{JSON_FILE}' not found. Initializing a clean dictionary configuration...")
        database = {
            "postural_contortion": ["āsana", "vṛścika", "padma", "śalabha"],
            "apparatus_pole": ["vaṃśa", "stambha", "veṇu"],
            "subaltern_tribal": ["caṇḍāla", "ḍomba", "plavaka", "jambhaka", "ābhīra"],
            "poison_necromancy": ["viṣa", "gara", "śamana", "bhūta", "śava"],
            "espionage_subversion": ["gūḍhapuruṣa", "cara", "sattrin", "kāpaṭika", "chadman"]
        }
    else:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                database = json.load(f)
            except json.JSONDecodeError:
                print("Corrupt JSON detected. Overwriting with clean baseline matrix.")
                return

    print("=" * 70)
    print("INJECTING EPIC MARTIAL TACTICS AND VERNACULAR DAWS INTO NETWORKS")
    print("=" * 70)

    # Merge new lemma lists into corresponding categories
    for category, words in NEW_LEMMAS.items():
        if category not in database:
            database[category] = []
        
        added_words = []
        for word in words:
            if word not in database[category]:
                database[category].append(word)
                added_words.append(word)
        
        if added_words:
            print(f" -> Category [{category}]: Injected {added_words}")

    # Save the expanded payload back to disk safely
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=4, ensure_ascii=False)

    print("=" * 70)
    print(f"SUCCESS: '{JSON_FILE}' updated smoothly with epic datasets!")
    print("=" * 70)

if __name__ == "__main__":
    inject_lemmas()
