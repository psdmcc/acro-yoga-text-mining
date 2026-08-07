import json
import os

JSON_FILE = "somatic_network.json"

# New technical terms extracted from the philological ledger
NEW_LEMMAS = {
    "subaltern_tribal": ["sopāka", "syamīka", "grāmaṇī"],
    "poison_necromancy": ["asita", "tuttha", "mahāpañcaviṣa", "kalpasthāna", "puṭapāka"],
    "botanical_dyes": ["aklikā", "kutsalā", "klītakikā", "kṣumā", "dūlikā", "cāraṭikā"],
    "transcultural_hellenistic": ["kollourion", "enchrisai", "laistēs", "porneia", "daimon", "theurgy"]
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
    print("INJECTING NEW LEXICAL CLUSTERS INTO SOMATIC NETWORK GRAPH")
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
    print(f"SUCCESS: '{JSON_FILE}' updated smoothly!")
    print("=" * 70)

if __name__ == "__main__":
    inject_lemmas()
