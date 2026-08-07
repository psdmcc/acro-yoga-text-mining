import os
import re

def sort_bib_by_text_appearance(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Step 1: Extracting global in-text citation keys in appearance order...")
    
    # Isolate document body after \begin{document} to track appearances accurately
    body_parts = re.split(r"\\begin\{document\}", content, maxsplit=1, flags=re.IGNORECASE)
    if len(body_parts) < 2:
        print("Error: Could not locate \\begin{document} marker.")
        return
    body_text = body_parts[1].split("\\begin{thebibliography}")[0]

    # Find all citation keys inside \citep{...}, \cite{...}, and \citet{...}
    raw_citations = re.findall(r"\\cite[pt]?\{([^\}]+)\}", body_text)
    
    ordered_keys = []
    seen_keys = set()
    
    for citation_group in raw_citations:
        keys = [k.strip() for k in citation_group.split(',')]
        for key in keys:
            if key not in seen_keys:
                seen_keys.add(key)
                ordered_keys.append(key)

    print(f" -> Tracked {len(ordered_keys)} unique citation targets across the text stream.")

    print("Step 2: Parsing bibliography blocks...")
    
    start_match = re.search(r"\\begin\{thebibliography\}\{.*?\}", content)
    end_match = re.search(r"\\end\{thebibliography\}", content)
    
    if not (start_match and end_match):
        print("Error: Could not locate the bibliography boundaries.")
        return

    bib_start_idx = start_match.end()
    bib_end_idx = end_match.start()

    pre_bib = content[:bib_start_idx]
    bib_body = content[bib_start_idx:bib_end_idx]
    post_bib = content[bib_end_idx:]

    # Segment the bibliography body by individual \bibitem elements
    entries = re.split(r'(?=\\bibitem)', bib_body)
    entries = [e.strip() for e in entries if e.strip()]

    # Map bibitem entries to their unique database citation keys
    bib_map = {}
    orphan_entries = []
    
    for entry in entries:
        key_match = re.search(r'\\bibitem\[[^\]]*\]\{([^\}]+)\}', entry)
        if not key_match:
            key_match = re.search(r'\\bibitem\{([^\}]+)\}', entry)
            
        if key_match:
            bib_map[key_match.group(1).strip()] = entry
        else:
            orphan_entries.append(entry)

    print("Step 3: Reordering bibliography entries ordinally...")
    
    sorted_entries = []
    for key in ordered_keys:
        if key in bib_map:
            sorted_entries.append(bib_map[key])
            del bib_map[key]

    # Append any leftover references that were not directly cited inline to the bottom
    leftovers = list(bib_map.values()) + orphan_entries
    if leftovers:
        print(f" -> Appending {len(leftovers)} uncited references to the end of the bibliography.")
        sorted_entries.extend(leftovers)

    # Reassemble the manuscript string matrix
    sorted_bib_body = "\n\n" + "\n\n".join(sorted_entries) + "\n\n"
    final_document = pre_bib + sorted_bib_body + post_bib

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_document)

    print("Success! Bibliography has been ordinally re-indexed by order of appearance.")

if __name__ == '__main__':
    target = '/Users/croma/acro-yoga-text-mining/main_article_v9.tex'
    sort_bib_by_text_appearance(file_path=target)
