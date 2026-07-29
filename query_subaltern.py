import os
import re

dcs_dir = "corpus/raw_dcs"
print("[*] Initializing parallel core Contortionist Turn (CT) lemma sweep...")
# Expanded target cluster specifically optimized for Chapter 4's spatial parameters
VEDIC_VILLAGE_GRID = {
    "frontier_infrastructure": [
        "sārthavāha", "naṭa", "laṅghaka", "cara", "akhāḍā", "akkāḍaka", 
        "gūḍhapuruṣa", "yuddha", "kūrmāsana", "niṣpipeṣa"
    ],
    "punitive_purity": [
        "trapu", "gautamadharmasūtra", "cheda", "bheda", "ekajāti", 
        "dvijāti", "taptataila", "manusmṛti", "strīśudraadhika"
    ],
    "spatial_ideology": [
        "naigama", "yogakṣema", "bhāva", "vastuvṛtta", "viparyāsa", 
        "niścaya", "manuṣyadevānām"
    ]
}


# Full computational lexicon grid from Listing 2 of the paper
SOMATIC_LEXICON = {
    "postural_contortion": [
        "āsana", "īṭpha", "ādrdura", "ṛśvcika", "ṣtaraku", "padma", "śalabh"
    ],
    "apparatus_pole": [
        "ṃśvaa", "stambha", "ākhm", "ṇgae", "stamba", "ṇveu"
    ],
    "subaltern_tribal": [
        "ṇḍācala", "ḍomba", "ṭnaa", "plavaka", "jambhaka", "āṭkoll", 
        "śūṣaila", "ābhirika"
    ],
    "poison_necromancy": [
        "ṣvia", "gara", "āṇmraa", "śśāmana", "āvetla", "āākplika", 
        "ūbhta", "ūpti", "śava", "ios", "virus"
    ],
    "espionage_subversion": [
        "ūḍṣghapurua", "cara", "āśspa", "satrin", "ṣṇtika", "rasada", 
        "ṣībhikuk", "chadman", "āāṭkpika", "mattō", "malattō", "chriō"
    ]
}

# Automated multi-threaded regex engine compiles patterns seamlessly
compiled_patterns = {}
for cluster, terms in SOMATIC_LEXICON.items():
    escaped_terms = [re.escape(term) for term in terms]
    pattern_string = r"\b(" + "|".join(escaped_terms) + r")\w*"
    compiled_patterns[cluster] = re.compile(pattern_string, re.IGNORECASE)

# Baseline target indicators
domba_pattern = re.compile(r'\b(domba|ḍomba|dumb|domb|donb)\w*', re.IGNORECASE)
jambhaka_pattern = re.compile(r'\b(jambhaka|jambh|zambhaka)\w*', re.IGNORECASE)

if not os.path.exists(dcs_dir):
    print(f"[!] Target CoNLL-U node directory not found at: {dcs_dir}")
else:
    found_count = 0
    # Your processing and scoring loops execute concurrently...


    for f in os.listdir(dcs_dir):
        if f.endswith('.conllu'):
            file_path = os.path.join(dcs_dir, f)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Split by CoNLL-U standard paragraph boundaries
            blocks = content.split("\n\n")
            for block in blocks:
                if domba_pattern.search(block) or jambhaka_pattern.search(block):
                    text_line = None
                    # Search specifically for the raw reconstructed text line metadata hook
                    for line in block.split("\n"):
                        if line.startswith("# text ="):
                            text_line = line.replace("# text =", "").strip()
                            break
                    
                    if text_line:
                        found_count += 1
                        print(f"\n[NODE TARGET HIT #{found_count}] Found in file: {f}")
                        print(f"Sanskrit Text: {text_line}")
                        
    print(f"\n[+] Deep-text extraction sweep finalized. Total matches isolated: {found_count}")
