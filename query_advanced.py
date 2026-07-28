import os
import re

dcs_dir = "corpus/raw_dcs"
gretil_dir = "corpus/raw_gretil"

print("[*] Launching targeted multi-index cross-corpus text sweep...")

# 1. LEMMATIZED DCS EXTRACTION LOOP
if os.path.exists(dcs_dir):
    for f in os.listdir(dcs_dir):
        if f.endswith('.conllu'):
            with open(os.path.join(dcs_dir, f), "r", encoding="utf-8") as file:
                content = file.read()
            sentences = content.split("\n\n")
            for s in sentences:
                clean_s = re.sub(r'\s+', ' ', s).strip()
                # Flexibly target the overlap between esoteric physiology and clandestine performance
                if any(re.search(w, clean_s, re.I) for w in ["marma", "pra?na"]) and \
                   any(re.search(p, clean_s, re.I) for p in ["gudha", "cara", "nata"]):
                    for line in s.split("\n"):
                        if line.startswith("# text ="):
                            print(f"\n[DCS CELL COLLOCATION] Found in {f}:")
                            print(line.replace('# text =', '').strip())

# 2. RAW STRING GRETIL EXTRACTION LOOP
if os.path.exists(gretil_dir):
    for f in os.listdir(gretil_dir):
        if f.endswith(('.txt', '.htm', '.html')):
            with open(os.path.join(gretil_dir, f), "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            paras = re.split(r"\n\n|<br>|<p>", content)
            for p in paras:
                clean_p = re.sub(r"<.*?>|\n", " ", p).strip()
                clean_p = re.sub(r"\s+", " ", clean_p)
                if any(re.search(w, clean_p, re.I) for w in ["marma", "pra?na"]) and \
                   any(re.search(p, clean_p, re.I) for p in ["gudha", "cara", "nata"]):
                    if 40 < len(clean_p) < 700:
                        print(f"\n[GRETIL CELL COLLOCATION] Found in {f}:")
                        print(clean_p)
