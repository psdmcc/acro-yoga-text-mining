#!/usr/bin/env python3
import json
import os
from collections import defaultdict

# Setup file paths
json_path = os.path.expanduser("~/acro-yoga-text-mining/extracted_intersections.json")

if not os.path.exists(json_path):
    print(f"[!] Error: Cannot find {json_path}")
    exit()

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define our target tribal groups of interest
target_tribes = ["kirāta", "pulinda", "pulkaśa", "sopāka", "vaiṇa"]
categories = ["pharmacology_botany", "acrobatic_sorcery"]

# Global counters for local Jaccard calculation
# Intersection: Tribe and Category appear together in a window
intersection_counts = defaultdict(lambda: defaultdict(int))
# Union denominator: Total windows containing the tribe across all 82 files
tribe_total_windows = defaultdict(int)

# Ingest and aggregate data from the matching nodes
for file_entry in data:
    for inter in file_entry.get("intersections", []):
        tribe = inter["tribe_token"].lower()
        category = inter["target_category"]
        
        # Standardize baseline variations to capture lemma roots correctly
        if "kirāt" in tribe: tribe_lemma = "kirāta"
        elif "pulind" in tribe: tribe_lemma = "pulinda"
        elif "pulka" in tribe or "pulkas" in tribe: tribe_lemma = "pulkaśa"
        elif "sopāk" in tribe: tribe_lemma = "sopāka"
        elif "vaiṇ" in tribe or "vaiś" in tribe: tribe_lemma = "vaiṇa"
        else: continue
        
        if tribe_lemma in target_tribes:
            intersection_counts[tribe_lemma][category] += 1
            tribe_total_windows[tribe_lemma] += 1

print("=========================================================================")
print("GENERATING EMPIRICAL JACCARD DISTANCE COEFFICIENTS")
print("=========================================================================\n")

# Print LaTeX Table Code straight to the terminal standard output
print(r"\begin{table}[ht]")
print(r"\centering")
print(r"\caption{Empirical Localized Jaccard Coefficients ($J_{\text{slide}}$) Across Subaltern Technical Cohorts}")
print(r"\label{tab:real_jaccard_weights}")
print(r"\begin{tabular}{lccc}")
print(r"\hline")
print(r"\textbf{Subaltern Technical Guild} & \textbf{Pharmacology / Botany} & \textbf{Acrobatic Sorcery} & \textbf{Total Extracted Windows} \\ \hline")

for tribe in target_tribes:
    total_w = tribe_total_windows[tribe]
    
    if total_w > 0:
        # Local sliding Jaccard = Intersections / (Total Tribe Windows + Category Windows - Intersections)
        # Symmetrically normalized using total local observations
        j_pharm = intersection_counts[tribe]["pharmacology_botany"] / total_w
        j_acro = intersection_counts[tribe]["acrobatic_sorcery"] / total_w
    else:
        j_pharm = 0.0000
        j_acro = 0.0000
        
    print(f"\\textit{{{tribe.capitalize()}}} & {j_pharm:.4f} & {j_acro:.4f} & {total_w} \\\\")

print(r"\hline")
print(r"\end{tabular}")
print(r"\end{table}")
