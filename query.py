import os
import re

dcs_dir = "corpus/raw_dcs"
gretil_dir = "corpus/raw_gretil"

# 1. Targeted DCS extraction loop
if os.path.exists(dcs_dir):
    for f in os.listdir(dcs_dir):
        if any(k.lower() in f.lower() for k in ["artha", "vaikh", "skand"]):
            with open(os.path.join(dcs_dir, f), "r", encoding="utf-8") as file:
                content = file.read()
            sentences = content.split("\n\n")
            for s in sentences:
                clean_s = re.sub(r'\s+', ' ', s).strip()
                # Use flexible regex arrays to account for Sandhi changes (e.g. caṇḍāla/caṇḍālo)
                if any(re.search(w, clean_s, re.I) for w in ["ca?nd[aa]la", "domba", "nata", "gudha", "cara", "langhana", "vis[aa]", "paMya"]) and \
                   any(re.search(p, clean_s, re.I) for p in ["asana", "stambha", "pitha"]):
                    for line in s.split("\n"):
                        if line.startswith("# text ="):
                            print(f"\n[DCS HIT] {f}:\n{line.replace('# text =', '').strip()}")

# 2. Targeted GRETIL extraction loop
if os.path.exists(gretil_dir):
    for f in os.listdir(gretil_dir):
        if any(k.lower() in f.lower() for k in ["b12c200", "b12c121", "b09c044", "bsa033", "pars1"]):
            with open(os.path.join(gretil_dir, f), "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            paras = re.split(r"\n\n|<br>|<p>", content)
            for p in paras:
                clean_p = re.sub(r"<.*?>|\n", " ", p).strip()
                clean_p = re.sub(r"\s+", " ", clean_p)
                if any(re.search(w, clean_p, re.I) for w in ["ca?nd[aa]la", "domba", "nata", "gudha", "cara", "langhana", "vis[aa]", "paMya"]) and \
                   any(re.search(p, clean_p, re.I) for p in ["asana", "stambha", "pitha"]):
                    if len(clean_p) > 30:
                        print(f"\n[GRETIL HIT] {f}:\n{clean_p[:650]}...\n")
