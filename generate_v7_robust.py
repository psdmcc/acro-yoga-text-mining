import os
import re

def create_version_7_robust(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"Error: Source file not found at {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Generating main_article_v7.tex with flexible structural mapping...")

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

    # Define flexible regex markers that ignore formatting noise, newlines, and soft hyphens (\xad)
    patterns = [
        r"\\begin\{document\}",
        r"\\subsection\{De-Spiritualizing\s+the\s+Stasis\}",
        r"\\subsection\{The\s+Materialist\s+Triad\s+and\s+the\s+Guild\s+Network\}",
        r"\\subsection\{The\s+Vedic\s+Bedrock:\s*Seasonal\s+Warfare\s+and\s+Autumnal\s+Mobilization\}",
        r"\\subsection\{The\s+Yogini\s+Axis\s+and\s+Somatic\s+Emblems:\s*Taxonomies,\s*Totems,\s*(?:and\s+)?Infrastructures\}",
        r"\\subsection\{Socio-Legal\s+Negotiations:\s*Caste\s+Pur\xad?ā?\xad?n?a?s\s+and\s+the\s+Subaltern\s+Kinetic\s+Continuum\}",
        r"\\subsection\{The\s+Kau\xad?ṭ?i?l?y?a?n?\s*Matrix:\s*Espionage,\s*Panoptic\s+Surveillance,\s+and\s+Intelligence\}",
        r"\\section\{Methodology:\s*Parallel-Core\s+Processing\s+and\s+Jaccard\s+Filters\}",
        r"\\subsection\{Diachronic\s+Spatial\s+Analogues:\s*The\s+Ethnographic\s+Mapping\s+of\s+the\s+Na\xad?ṭ\s+and\s+Kab\xad?ū?tari\}",
        r"\\subsection\{The\s+Enclosed\s+Column:\s*Pylwan\s+Gopauls,\s*Kolh\xad?ā\xad?ṭ?i\s+Poles,\s+and\s+(?:the\s+)?State\s+Surveillance\s+Grid\}",
        r"\\subsection\{The\s+Indigenous\s+Substrate:\s*Kol\s+Cosmologies\s+and\s+Shamanic\s+Pole-Ascent\}"
    ]

    # Dynamically split the document matrix step-by-step using a lookahead safety check
    parts = []
    current_remainder = content
    
    for i, p in enumerate(patterns):
        split_result = re.split(p, current_remainder, maxsplit=1, flags=re.IGNORECASE | re.UNICODE)
        if len(split_result) < 2:
            print(f"Error: Failed to match structural anchor pattern index {i}: {p}")
            print("Aborting to preserve repository safety.")
            return
        parts.append(split_result[0])
        current_remainder = split_result[1]
    parts.append(current_remainder) # Append final trailing document segment

    # Map variables cleanly from structural extraction pieces
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

    # Re-assemble document flow into the optimized 5-section paradigm
    v7_document_flow = [
        preamble, "\\begin{document}\n",
        abstract_and_intro,
        "\\subsection{De-Spiritualizing the Stasis}\n", de_spirit_block,
        
        "\n\n% =====================================================================\n",
        "% SECTION 2: THE MATERIALIST TRIAD & CORPORATE FORTRESSES\n",
        "% =====================================================================\n",
        "\\section{Somatic Capital and the Economics of the Frontier}\n",
        "\\label{sec:somatic_capital_frontier_economics}\n\n",
        "\\subsection{The Materialist Triad and the Guild Network}\n", triad_block,
        "\\subsection{Socio-Legal Negotiations: Caste Purāṇas and the Kinetic Continuum}\n", socio_legal_block,

        "\n\n% =====================================================================\n",
        "% SECTION 3: TACTICAL GEOGRAPHY & STATE COVERT SURVEILLANCE\n",
        "% =====================================================================\n",
        "\\section{Tactical Espionage and the Kauṭilyan Matrix}\n",
        "\\label{sec:tactical_espionage_kautilyan_matrix}\n\n",
        "\\subsection{The Vedic Bedrock: Seasonal Warfare and Autumnal Mobilization}\n", bedrock_block,
        "\\subsection{The Kauṭilyan Matrix: Espionage, Panoptic Surveillance, and Intelligence}\n", kautilya_block,

        "\n\n% =====================================================================\n",
        "% SECTION 4: COMPUTATIONAL TEXT-MINING METHODOLOGY\n",
        "% =====================================================================\n",
        "\\section{Methodology: Parallel-Core Processing and Jaccard Filters}\n",
        "\\label{sec:methodology_processing_jaccard_filters}\n\n", methodology_core,

        "\n\n% =====================================================================\n",
        "% SECTION 5: ETHNOGRAPHIC STUDIES & DIACHRONIC ANALOGUES\n",
        "% =====================================================================\n",
        "\\section{Diachronic Spatial Topographies and Shamanic Rites}\n",
        "\\label{sec:diachronic_spatial_topographies}\n\n",
        "\\subsection{The Yogini Axis and Somatic Emblems: Taxonomies, Totems, and Infrastructures}\n", yogini_block,
        "\\subsection{Diachronic Spatial Analogues: The Ethnographic Mapping of the Naṭ and Kabūtari}\n", diachronic_block,
        "\\subsection{The Enclosed Column: Pylwan Gopauls, Kolhāṭi Poles, and the State Grid}\n", enclosed_block,
        "\\subsection{The Indigenous Substrate: Kol Cosmologies and Shamanic Pole-Ascent}\n", indigenous_block
    ]

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.writelines(v7_document_flow)

    print(f"\nSuccess! Version 7 initialized at: {dest_path}")
    print(" -> Robust processing completed: New sections re-indexed cleanly.")

if __name__ == '__main__':
    src = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    dest = '/Users/croma/acro-yoga-text-mining/main_article_v7.tex'
    create_version_7_robust(src, dest)
