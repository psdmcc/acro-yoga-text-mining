import os
import re

path = 'corpus/raw_gretil/pars1__u.htm'

if os.path.exists(path):
    print(f"[*] Reading {path}...")
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    # Split by standard GRETIL line and formatting demarcations
    paras = re.split(r'\n\n|<br>|<p>', text)
    count = 0
    
    for para in paras:
        clean_p = re.sub(r'<.*?>|\n', ' ', para).strip()
        # Clean double spaces caused by removing tags
        clean_p = re.sub(r'\s+', ' ', clean_p)
        
        # Test for active subaltern-somatic proximity intersection
        if any(re.search(w, clean_p, re.IGNORECASE) for w in ['caṇḍāla', 'ḍomba', 'naṭa']) and \
           any(re.search(p, clean_p, re.IGNORECASE) for p in ['āsana', 'pīṭha', 'stambha']):
            
            if len(clean_p) > 30:
                count += 1
                print(f"\n--- CRITICAL CROSSOVER EXTRACT #{count} ---")
                print(clean_p)
                print("-" * 50)
                
    if count == 0:
        print("[*] Scan finished. No active overlapping terms found inside the same formatting block.")
else:
    print(f"[!] Path mismatch. File missing at: {path}")
