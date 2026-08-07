import os
import re
import unicodedata

def build_perfect_v7(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"Error: Source file not found at {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Re-assembling main_article_v7.tex with exact index mapping and NFC normalization...")

    # Fix 1: Resolve the repeating Figure Graphic path bug across density profiles
    content = content.replace(
        "\\includegraphics[width=\\textwidth]{outputs/visualizations/\nsomatic_overlap_matrix.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion.",
        "\\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_contortion_density_profiles.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion."
    )
    
    # Uncomment and map the somatic_continuum.png graphic apparatus on page 38
    content = content.replace(
        "\\begin{figure}[htbp]\n\\centering\n%\\includegraphics[width=0.8\\textwidth]{somatic_continuum.png}",
        "\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{outputs/visualizations/somatic_continuum.png}"
    )

    # Fix 2: Purge the redundant text loop on page 15
    redundant_text_block = (
        "Long before the vocabulary of \\textit{stambha} was internalised by late\xad"
        "medieval monastic text-composers to define quietistic spinal \n"
        "pathways, the external timber column operated as a volatile \n"
        "materialist axis of risk, environmental survival, and structural \n"
        "containment managed along the unstable thresholds of the Aryan \n"
        "frontier citep{mccartney2025}."
    )
    content = content.replace(redundant_text_block, "")

    # Highly robust short-prefix patterns that match uniquely across your document
    patterns = [
        r"\\begin\{document\}",
        r"\\subsection\{De-Spiritualizing",
        r"\\subsection\{The\s+Materialist\s+Triad",
        r"\\subsection\{The\s+Vedic\s+Bedrock",
        r"\\subsection\{The\s+Yogin[īi]\s+Axis",
        r"\\subsection\{Socio-Legal\s+Negotiations",
        r"\\subsection\{The\s+Kau[ṭt]ilyan\s+Matrix",
        r"\\section\{Methodology",
        r"\\subsection\{Diachronic\s+Spatial\s+Analogues",
        r"\\subsection\{The\s+Enclosed\s+Column",
        r"\\subsection\{The\s+Indigenous\s+Substrate"
    ]

    parts = []
    current_remainder = content
    
    for i, p in enumerate(patterns):
        split_result = re.split(p, current_remainder, maxsplit=1, flags=re.IGNORECASE | re.UNICODE)
        if len(split_result) < 2:
            print(f"Error: Failed to match structural anchor pattern index {i}: {p}")
            return
        parts.append(split_result[0])
        match_obj = re.search(p, current_remainder, flags=re.IGNORECASE | re.UNICODE)
        current_remainder = match_obj.group(0) + split_result[1]
    parts.append(current_remainder)

    # Re-assemble the manuscript components across the clean five-chapter matrix with zero loss
    v7_document_flow = [
        parts[0], "\\begin{document}\n",
        parts[1],
        parts[2],
        
        "\n\n% =====================================================================\n",
        "% SECTION 2: THE MATERIALIST TRIAD & CORPORATE FORTRESSES\n",
        "% =====================================================================\n",
        "\\section{Somatic Capital and the Economics of the Frontier}\n",
        "\\label{sec:somatic_capital_frontier_economics}\n\n",
        parts[3],
        parts[6],

        "\n\n% =====================================================================\n",
        "% SECTION 3: TACTICAL GEOGRAPHY & STATE COVERT SURVEILLANCE\n",
        "% =====================================================================\n",
        "\\section{Tactical Espionage and the Kauṭilyan Matrix}\n",
        "\\label{sec:tactical_espionage_kautilyan_matrix}\n\n",
        parts[4],
        parts[7],

        "\n\n% =====================================================================\n",
        "% SECTION 4: COMPUTATIONAL TEXT-MINING METHODOLOGY\n",
        "% =====================================================================\n",
        "\\section{Methodology: Parallel-Core Processing and Jaccard Filters}\n",
        "\\label{sec:methodology_processing_jaccard_filters}\n\n",
        parts[8],

        "\n\n% =====================================================================\n",
        "% SECTION 5: ETHNOGRAPHIC STUDIES & DIACHRONIC ANALOGUES\n",
        "% =====================================================================\n",
        "\\section{Diachronic Spatial Topographies and Shamanic Rites}\n",
        "\\label{sec:diachronic_spatial_topographies}\n\n",
        parts[5],
        parts[9],
        parts[10],
        parts[11]
    ]

    final_text = "".join(v7_document_flow)
    
    # Critical step: Convert all characters to Canonical Composition (NFC)
    # This prevents inputenc from crashing on loose combining character diacritics
    normalized_text = unicodedata.normalize('NFC', final_text)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(normalized_text)

    print(f"\nSuccess! Pristine main_article_v7.tex generated at: {dest_path}")

if __name__ == '__main__':
    src = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    dest = '/Users/croma/acro-yoga-text-mining/main_article_v7.tex'
    build_perfect_v7(src, dest)
