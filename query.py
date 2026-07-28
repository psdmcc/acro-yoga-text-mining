import os
import re

dcs_dir = "corpus/raw_dcs"
gretil_dir = "corpus/raw_gretil"

if os.path.exists(dcs_dir):
    for f in os.listdir(dcs_dir):
        if any(k.lower() in f.lower() for k in ["artha", "vaikh", "skand"]):
            with open(os.path.join(dcs_dir, f), "r", encoding="utf-8") as file:
                content = file.read()
            for s in content.split("\n\n"):
                if any(re.search(w, s, re.I) for w in ["ca?nd[aa]la", "nata", "gudha", "cara", "langhana", "vis[aa]"]) and \
                   any(re.search(p, s, re.I) for p in ["asana", "stambha", "pitha"]):
                    print(f"\n=== DCS EXPANDED HIT: {f} ===")
                    print(s.strip())
                    print("="*40)
