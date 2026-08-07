import json
import os

json_path = os.path.expanduser("~/acro-yoga-text-mining/extracted_intersections.json")

if not os.path.exists(json_path):
    print(f"[!] Error: Cannot find {json_path}")
    exit()

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"=========================================================================")
print(f"PARSED INTERSECTION PREVIEW: TOTAL VALID FILES = {len(data)}")
print(f"=========================================================================\n")

# Display the first 5 file intersections as a preview
for idx, entry in enumerate(data[:5]):
    print(f"[{idx + 1}] FILE SOURCE: {entry['file']}")
    print(f"    ---------------------------------------------------------------------")
    for inter in entry['intersections']:
        print(f"    • Subaltern Anchor : {inter['tribe_token'].upper()}")
        print(f"    • Target Category  : {inter['target_category']}")
        print(f"    • Matched Keyword  : {inter['matched_term']}")
        
        # Reconstruct the 11-word sliding window text
        context_str = " ".join(inter['context_window'])
        print(f"    • Context Window   : \"... {context_str} ...\"")
        print()
    print("=" * 73)
