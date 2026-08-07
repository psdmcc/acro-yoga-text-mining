import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("[*] Inspecting and sanitizing line 200 environment structures...")

# Look around line 200 (index 199) for any rogue figure blocks trapped inside paragraphs/equations
for i in range(max(0, 180), min(len(lines), 220)):
    if r"\begin{figure}" in lines[i]:
        print(f"[!] Found trapped figure environment on line {i+1}. Removing to restore outer paragraph mode.")
        lines[i] = lines[i].replace(r"\begin{figure}[htbp]", "").replace(r"\begin{figure}", "")
    if r"\centering" in lines[i] and i < 210:
        lines[i] = lines[i].replace(r"\centering", "")
    if r"\end{figure}" in lines[i] and i < 215:
        lines[i] = lines[i].replace(r"\end{figure}", "")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write("".join(lines))

print("[SUCCESS] Trapped environment anchors successfully removed from restricted blocks.")
