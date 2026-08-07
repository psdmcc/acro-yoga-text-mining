import os
import re

def build_pristine_v7_robust(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"Error: Source file not found at {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Re-assembling main_article_v7.tex via robust regex pipeline...")

    # Standardize image assets and clean the page 15 text loop from the stream
    content = content.replace(
        "\\includegraphics[width=\\textwidth]{outputs/visualizations/\nsomatic_overlap_matrix.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion.",
        "\\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_contortion_density_profiles.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion."
    )
    content = content.replace(
        "\\begin{figure}[htbp]\n\\centering\n%\\includegraphics[width=0.8\\textwidth]{somatic_continuum.png}",
        "\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{outputs/visualizations/somatic_continuum.png}"
    )
    redundant_text_block = (
        "Long before the vocabulary of \\textit{stambha} was internalised by late\xad"
        "medieval monastic text-composers to define quietistic spinal \n"
        "pathways, the external timber column operated as a volatile \n"
        "materialist axis of risk, environmental survival, and structural \n"
        "containment managed along the unstable thresholds of the Aryan \n"
        "frontier citep{mccartney2025}."
    )
    content = content.replace(redundant_text_block, "")

    # Isolate preamble from body exactly once to prevent any ! LaTeX Error loops
    body_split = re.split(r"\\begin\{document\}", content, maxsplit=1, flags=re.IGNORECASE)
    if len(body_split) < 2:
        print("Error: Could not locate \\begin{document} marker.")
        return
    preamble = body_split[0]
    body = body_split[1]

    # Chronological regex targets to extract blocks without lines or whitespace collisions
    patterns = [
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

    # Slice out the chapters sequentially from the isolated body string
    blocks = []
    remainder = body
    
    for i, p in enumerate(patterns):
        res = re.split(p, remainder, maxsplit=1, flags=re.IGNORECASE | re.UNICODE)
        if len(res) < 2:
            print(f"Error: Failed to find target text landmark index {i}: {p}")
            return
        blocks.append(res[0])
        # Re-inject the matched heading prefix to prevent losing section labels
        matched_head = re.search(p, remainder, flags=re.IGNORECASE | re.UNICODE).group(0)
        remainder = matched_head + res[1]
    blocks.append(remainder) # Add trailing document remainder

    # Unpack the segmented block matrix into variables
    abstract_and_intro = blocks[0]
    de_spirit = blocks[1]
    triad = blocks[2]
    bedrock = blocks[3]
    yogini = blocks[4]
    socio_legal = blocks[5]
    kautilya = blocks[6]
    methodology_core = blocks[7]
    diachronic = blocks[8]
    enclosed = blocks[9]
    indigenous_remainder = blocks[10]

    # Re-assemble the pristine 5-section text paradigm
    v7_clean_flow = [
        preamble,
        "\\begin{document}\n",
        abstract_and_intro,
        de_spirit,
        
        "\n\n% =====================================================================\n",
        "% SECTION 2: THE MATERIALIST TRIAD & CORPORATE FORTRESSES\n",
        "% =====================================================================\n",
        "\\section{Somatic Capital and the Economics of the Frontier}\n",
        "\\label{sec:somatic_capital_frontier_economics}\n\n",
        triad,
        socio_legal,

        "\n\n% =====================================================================\n",
        "% SECTION 3: TACTICAL GEOGRAPHY & STATE COVERT SURVEILLANCE\n",
        "% =====================================================================\n",
        "\\section{Tactical Espionage and the Kauṭilyan Matrix}\n",
        "\\label{sec:tactical_espionage_kautilyan_matrix}\n\n",
        bedrock,
        kautilya,

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
        yogini,
        diachronic,
        enclosed,
        indigenous_remainder
    ]

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.writelines(v7_clean_flow)

    print(f"\nSuccess! Pristine main_article_v7.tex generated at: {dest_path}")

if __name__ == '__main__':
    src = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    dest = '/Users/croma/acro-yoga-text-mining/main_article_v7.tex'
    build_pristine_v7_robust(src, dest)
