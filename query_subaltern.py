import os
import re

dcs_dir = "corpus/raw_dcs"
print("[*] Initializing deep subaltern lemma sweep for ḍomba and jambhaka...")

# Compiled regex patterns targeting basic and inflected forms of the target lemmata
domba_pattern = re.compile(r'\b(ḍomba|domba|ḍumb|ḍomb|ḍonb)\w*', re.IGNORECASE)
jambhaka_pattern = re.compile(r'\b(jambhaka|jambh|zambhaka)\w*', re.IGNORECASE)

if not os.path.exists(dcs_dir):
    print(f"[!] Target DCS directory not found at: {dcs_dir}")
else:
    found_count = 0
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
