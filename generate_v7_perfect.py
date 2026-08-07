import os
import re
import unicodedata

def build_perfect_v7(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"Error: Source file not found at {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Executing precise macro-extraction for main_article_v7.tex...")

    # Fix 1: Resolve the repeating Figure Graphic path bug across density profiles
    content = content.replace(
        "\\includegraphics[width=\\textwidth]{outputs/visualizations/\nsomatic_overlap_matrix.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion.",
        "\\includegraphics[width=\\textwidth]{outputs/visualizations/somatic_contortion_density_profiles.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion."
    )
    
    # Fix 2: Dynamic Extension Fix — Strip .png to let LaTeX auto-resolve the graphic file format
    content = content.replace(
        "\\begin{figure}[htbp]\n\\centering\n%\\includegraphics[width=0.8\\textwidth]{somatic_continuum.png}",
        "\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{outputs/visualizations/somatic_continuum}"
    )

    # Fix 3: Purge the redundant text loop on page 15
    redundant_text_block = (
        "Long before the vocabulary of \\textit{stambha} was internalised by late\xad"
        "medieval monastic text-composers to define quietistic spinal \n"
        "pathways, the external timber column operated as a volatile \n"
        "materialist axis of risk, environmental survival, and structural \n"
        "containment managed along the unstable thresholds of the Aryan \n"
        "frontier citep{mccartney2025}."
    )
    content = content.replace(redundant_text_block, "")

    # Isolate Preamble cleanly
    preamble_match = re.search(r"([\s\S]*?)\\begin\{document\}", content, re.IGNORECASE)
    preamble = preamble_match.group(1)

    # Inject the missing Unicode character definition array for ṅ (U+1E45) right into the preamble
    missing_unicode_def = "\n\\DeclareUnicodeCharacter{1E45}{\\d{n}} % Velar nasal n (dot below for \u1e45)\n"
    preamble = preamble + missing_unicode_def

    # Extract standalone text blocks using safe, independent text anchors
    intro_match = re.search(r"\\begin\{document\}([\s\S]*?)\\subsection\{De-Spiritualizing", content, re.IGNORECASE)
    intro_text = intro_match.group(1)

    despirit_match = re.search(r"\\subsection\{De-Spiritualizing[\s\S]*?\}([\s\S]*?)\\subsection\{The\s+Materialist\s+Triad", content, re.IGNORECASE)
    despirit_text = despirit_match.group(1)

    triad_match = re.search(r"\\subsection\{The\s+Materialist\s+Triad[\s\S]*?\}([\s\S]*?)\\subsection\{The\s+Vedic\s+Bedrock", content, re.IGNORECASE)
    triad_text = triad_match.group(1)

    bedrock_match = re.search(r"\\subsection\{The\s+Vedic\s+Bedrock[\s\S]*?\}([\s\S]*?)\\subsection\{The\s+Yogin[īi]\s+Axis", content, re.IGNORECASE)
    bedrock_text = bedrock_match.group(1)

    yogini_match = re.search(r"\\subsection\{The\s+Yogin[īi]\s+Axis[\s\S]*?\}([\s\S]*?)\\subsection\{Socio-Legal\s+Negotiations", content, re.IGNORECASE)
    yogini_text = yogini_match.group(1)

    sociolegal_match = re.search(r"\\subsection\{Socio-Legal\s+Negotiations[\s\S]*?\}([\s\S]*?)\\subsection\{The\s+Kau[ṭt]ilyan\s+Matrix", content, re.IGNORECASE)
    sociolegal_text = sociolegal_match.group(1)

    kautilya_match = re.search(r"\\subsection\{The\s+Kau[ṭt]ilyan\s+Matrix[\s\S]*?\}([\s\S]*?)\\section\{Methodology", content, re.IGNORECASE)
    kautilya_text = kautilya_match.group(1)

    methodology_match = re.search(r"\\section\{Methodology:[\s\S]*?\}([\s\S]*?)\\subsection\{Diachronic\s+Spatial\s+Analogues", content, re.IGNORECASE)
    methodology_text = methodology_match.group(1)

    diachronic_match = re.search(r"\\subsection\{Diachronic\s+Spatial\s+Analogues[\s\S]*?\}([\s\S]*?)\\subsection\{The\s+Enclosed\s+Column", content, re.IGNORECASE)
    diachronic_text = diachronic_match.group(1)

    enclosed_match = re.search(r"\\subsection\{The\s+Enclosed\s+Column[\s\S]*?\}([\s\S]*?)\\subsection\{The\s+Indigenous\s+Substrate", content, re.IGNORECASE)
    enclosed_text = enclosed_match.group(1)

    remainder_match = re.search(r"\\subsection\{The\s+Indigenous\s+Substrate[\s\S]*?\}([\s\S]*?$)", content, re.IGNORECASE)
    remainder_text = remainder_match.group(1)

    # Re-assemble the pristine 5-section paradigm with single document bounds
    v7_clean_flow = [
        preamble,
        "\\begin{document}\n",
        intro_text,
        "\\subsection{De-Spiritualizing the Stasis}\n", despirit_text,
        
        "\n\n% =====================================================================\n",
        "% SECTION 2: THE MATERIALIST TRIAD & CORPORATE FORTRESSES\n",
        "% =====================================================================\n",
        "\\section{Somatic Capital and the Economics of the Frontier}\n",
        "\\label{sec:somatic_capital_frontier_economics}\n\n",
        "\\subsection{The Materialist Triad and the Guild Network}\n", triad_text,
        "\\subsection{Socio-Legal Negotiations: Caste Purāṇas and the Subaltern Kinetic Continuum}\n", sociolegal_text,

        "\n\n% =====================================================================\n",
        "% SECTION 3: TACTICAL GEOGRAPHY & STATE COVERT SURVEILLANCE\n",
        "% =====================================================================\n",
        "\\section{Tactical Espionage and the Kauṭilyan Matrix}\n",
        "\\label{sec:tactical_espionage_kautilyan_matrix}\n\n",
        "\\subsection{The Vedic Bedrock: Seasonal Warfare and Autumnal Mobilization}\n", bedrock_text,
        "\\subsection{The Kauṭilyan Matrix: Espionage, Panoptic Surveillance, and Intelligence}\n", kautilya_text,

        "\n\n% =====================================================================\n",
        "% SECTION 4: COMPUTATIONAL TEXT-MINING METHODOLOGY\n",
        "% =====================================================================\n",
        "\\section{Methodology: Parallel-Core Processing and Jaccard Filters}\n",
        "\\label{sec:methodology_processing_jaccard_filters}\n\n", methodology_text,

        "\n\n% =====================================================================\n",
        "% SECTION 5: ETHNOGRAPHIC STUDIES & DIACHRONIC ANALOGUES\n",
        "% =====================================================================\n",
        "\\section{Diachronic Spatial Topographies and Shamanic Rites}\n",
        "\\label{sec:diachronic_spatial_topographies}\n\n",
        "\\subsection{The Yogini Axis and Somatic Emblems: Taxonomies, Totems, and Infrastructures}\n", yogini_text,
        "\\subsection{Diachronic Spatial Analogues: The Ethnographic Mapping of the Naṭ and Kabūtari}\n", diachronic_text,
        "\\subsection{The Enclosed Column: Pylwan Gopauls, Kolhāṭi Poles, and the State Surveillance Grid}\n", enclosed_text,
        "\\subsection{The Indigenous Substrate: Kol Cosmologies and Shamanic Pole-Ascent}\n", remainder_text
    ]

    final_text = "".join(v7_clean_flow)
    normalized_text = unicodedata.normalize('NFC', final_text)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(normalized_text)

    print(f"\nSuccess! Pristine main_article_v7.tex generated at: {dest_path}")

if __name__ == '__main__':
    src = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    dest = '/Users/croma/acro-yoga-text-mining/main_article_v7.tex'
    build_perfect_v7(src, dest)
