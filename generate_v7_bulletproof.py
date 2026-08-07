import os
import re

def create_version_7_bulletproof(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"Error: Source file not found at {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Generating main_article_v7.tex with short-prefix structural anchors...")

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
            print("Aborting operation to protect source integrity.")
            return
        # split_result[0] is the text before the match. split_result[1] is the text after.
        # To keep the original section headers intact, we will re-inject the matched text
        # by capturing what re.search finds for that pattern.
        match_obj = re.search(p, current_remainder, flags=re.IGNORECASE | re.UNICODE)
        matched_text = match_obj.group(0)
        
        parts.append(split_result[0])
        current_remainder = matched_text + split_result[1]
    parts.append(current_remainder)

    # Map the document arrays safely
    preamble = parts[0]
    abstract_and_intro = parts[1]
    de_spirit_block = parts[2]
    triad_block = parts[3]
    bedrock_block = parts[4]
    yogini_block = parts[5]
    socio_legal_block = parts[6]
    kautilya_block = parts[7]
    methodology_core = parts[8]
    diachronic_block = parts[9]
    enclosed_block = parts[10]
    indigenous_block = parts[11]

    # Re-assemble the manuscript components across the clean five-chapter matrix
    v7_document_flow = [
        preamble, "\\begin{document}\n",
        abstract_and_intro,
        de_spirit_block,
        
        "\n\n% =====================================================================\n",
        "% SECTION 2: THE MATERIALIST TRIAD & CORPORATE FORTRESSES\n",
        "% =====================================================================\n",
        "\\section{Somatic Capital and the Economics of the Frontier}\n",
        "\\label{sec:somatic_capital_frontier_economics}\n\n",
        triad_block,
        socio_legal_block,

        "\n\n% =====================================================================\n",
        "% SECTION 3: TACTICAL GEOGRAPHY & STATE COVERT SURVEILLANCE\n",
        "% =====================================================================\n",
        "\\section{Tactical Espionage and the Kauṭilyan Matrix}\n",
        "\\label{sec:tactical_espionage_kautilyan_matrix}\n\n",
        bedrock_block,
        kautilya_block,

        "\n\n% =====================================================================\n",
        "% SECTION 4: COMPUTATIONAL TEXT-MINING METHODOLOGY\n",
        "% =====================================================================\n",
        "\\section{Methodology: Parallel-Core Processing and Jaccard Filters}\n",
        "\\label{sec:methodology_processing_jaccard_filters}\n\n",
        methodology_core,

        "\n\n% =====================================================================\n",
        "% SECTION 5: ETHNOGRAPHIC STUDIES & DIACHRONIC ANALOGUES\n",
        "% =====================================================================\n",
        "\\section{Diachronic Spatial Topographies and Shamanic Rites}\n",
        "\\label{sec:diachronic_spatial_topographies}\n\n",
        yogini_block,
        diachronic_block,
        enclosed_block,
        indigenous_block
    ]

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.writelines(v7_document_flow)

    print(f"\nSuccess! Version 7 cleanly initialized at: {dest_path}")
    print(" -> Short-prefix structural mapping completed successfully.")

if __name__ == '__main__':
    src = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    dest = '/Users/croma/acro-yoga-text-mining/main_article_v7.tex'
    create_version_7_bulletproof(src, dest)
