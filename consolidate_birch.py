import os
import re
import unicodedata

def merge_to_single_birch(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Target file missing at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Step 1: Consolidating inline citations back to a single Birch2024 node...")
    
    # Global in-text citation adjustments
    content = content.replace("Birch2024a", "Birch2024")
    content = content.replace("Birch2024b", "Birch2024")
    content = content.replace("Birch(2024a)", "Birch(2024)")
    content = content.replace("Birch(2024b)", "Birch(2024)")

    print("Step 2: Re-allocating bibliography items and sorting ordinally...")
    
    # Isolate text body before the bibliography to track the chronological appearance sequence
    body_parts = re.split(r"\\begin\{thebibliography\}", content, maxsplit=1, flags=re.IGNORECASE)
    text_before_bib = body_parts[0]

    # Trace all inline citations step-by-step to lock down the ordinal progression
    raw_citations = re.findall(r"\\cite[pt]?\{([^\}]+)\}", text_before_bib)
    ordered_keys = []
    seen_keys = set()
    
    for group in raw_citations:
        for key in [k.strip() for k in group.split(',')]:
            if key and key not in seen_keys:
                seen_keys.add(key)
                ordered_keys.append(key)

    # Decouple the bibliography block cleanly from the document tail
    end_split = re.split(r"\\end\{thebibliography\}", content, maxsplit=1, flags=re.IGNORECASE)
    main_body_and_bib_start = end_split[0]
    post_bib_content = "\n\\end{thebibliography}\n\\end{document}\n"

    pre_bib_content = re.split(r"\\begin\{thebibliography\}", main_body_and_bib_start, maxsplit=1, flags=re.IGNORECASE)[0]
    raw_bib_body = re.split(r"\\begin\{thebibliography\}", main_body_and_bib_start, maxsplit=1, flags=re.IGNORECASE)[1]

    # Segment the bibliography string into standalone bibitem elements
    entries = re.split(r'(?=\\bibitem)', raw_bib_body)
    entries = [e.strip() for e in entries if e.strip()]

    # Map bibitem entries to their unique database citation keys
    bib_map = {}
    orphan_entries = []
    
    for entry in entries:
        # Clean out any leftover interior suffix traces inside the bibitem blocks
        entry = entry.replace("Birch2024a", "Birch2024").replace("Birch2024b", "Birch2024")
        entry = entry.replace("Birch(2024a)", "Birch(2024)").replace("Birch(2024b)", "Birch(2024)")
        
        key_match = re.search(r'\\bibitem\[[^\]]*\]\{([^\}]+)\}', entry)
        if not key_match:
            key_match = re.search(r'\\bibitem\{([^\}]+)\}', entry)
            
        if key_match:
            k = key_match.group(1).strip()
            # If the single Birch node is already mapped, skip the old duplicate book row completely
            if k == "Birch2024" and k in bib_map:
                continue
            bib_map[k] = entry
        else:
            orphan_entries.append(entry)

    # Reordering bibliography entries ordinally
    sorted_entries = []
    for key in ordered_keys:
        if key in bib_map:
            sorted_entries.append(bib_map[key])
            del bib_map[key]

    # Append any remaining un-cited data records smoothly to the base of the list
    leftovers = list(bib_map.values()) + orphan_entries
    if leftovers:
        sorted_entries.extend(leftovers)

    # Reassemble the entire document stream perfectly with balanced tags
    sorted_bib_body = "\n\n" + "\n\n".join(sorted_entries) + "\n\n"
    
    final_document = (
        pre_bib_content.strip() + 
        "\n\n\\begin{thebibliography}{99}\n" + 
        sorted_bib_body + 
        post_bib_content
    )

    # Normalize Unicode string matrices to NFC
    normalized_text = unicodedata.normalize('NFC', final_document)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(normalized_text)

    print("Success! Suffixes removed and unified Birch2024 citation node ordinally indexed.")

if __name__ == '__main__':
    target_doc = '/Users/croma/acro-yoga-text-mining/main_article_v9.tex'
    merge_to_single_birch(target_doc)
