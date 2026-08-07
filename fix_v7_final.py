import os
import re

def build_pristine_v7(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"Error: Source file not found at {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Re-assembling main_article_v7.tex with pristine body boundaries...")

    # Clean up figure paths and text loops in the raw content first
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

    # Clean extraction using strict content block boundaries
    preamble, body = content.split("\\begin{document}", 1)
    
    # Isolate chapters using specific content markers
    parts = {}
    
    # Extract structural chunks sequentially to guarantee zero word loss
    abstract_and_intro, remain = body.split("\\subsection{De-Spiritualizing the Stasis}", 1)
    de_spirit, remain = remain.split("\\subsection{The Materialist Triad and the Guild Network}", 1)
    triad, remain = remain.split("\\subsection{The Vedic Bedrock: Seasonal Warfare and Autumnal \nMobilization}", 1)
    bedrock, remain = remain.split("\\subsection{The Yogini Axis and Somatic Emblems: Taxonomies, Totems, \nand Infrastructures}", 1)
    yogini, remain = remain.split("\\subsection{Socio-Legal Negotiations: Caste Pur\xadanas and the \nSubaltern Kinetic Continuum}", 1)
    socio_legal, remain = remain.split("\\subsection{The Kau\xadtilyan Matrix: Espionage, Panoptic Surveillance, \nand Intelligence}", 1)
    kautilya, methodology_all = remain.split("\\section{Methodology: Parallel-Core Processing and Jaccard Filters}", 1)
    
    methodology_core, ethno_all = methodology_all.split("\\subsection{Diachronic Spatial Analogues: The Ethnographic Mapping \nof the Na\xadt and Kab\u016btari}", 1)
    diachronic, ethno_all = ethno_all.split("\\subsection{The Enclosed Column: Pylwan Gopauls, Kolh\xadā\xadti Poles, and \nthe State Surveillance Grid}", 1)
    enclosed, remains_of_doc = ethno_all.split("\\subsection{The Indigenous Substrate: Kol Cosmologies and Shamanic \nPole-Ascent}", 1)

    # Re-build the five-section matrix with clean headers and no boundary loops
    v7_clean_flow = [
        preamble,
        "\\begin{document}\n",
        abstract_and_intro,
        "\\subsection{De-Spiritualizing the Stasis}\n", de_spirit,
        
        "\n\n% =====================================================================\n",
        "% SECTION 2: THE MATERIALIST TRIAD & CORPORATE FORTRESSES\n",
        "% =====================================================================\n",
        "\\section{Somatic Capital and the Economics of the Frontier}\n",
        "\\label{sec:somatic_capital_frontier_economics}\n\n",
        "\\subsection{The Materialist Triad and the Guild Network}\n", triad,
        "\\subsection{Socio-Legal Negotiations: Caste Purāṇas and the Kinetic Continuum}\n", socio_legal,

        "\n\n% =====================================================================\n",
        "% SECTION 3: TACTICAL GEOGRAPHY & STATE COVERT SURVEILLANCE\n",
        "% =====================================================================\n",
        "\\section{Tactical Espionage and the Kauṭilyan Matrix}\n",
        "\\label{sec:tactical_espionage_kautilyan_matrix}\n\n",
        "\\subsection{The Vedic Bedrock: Seasonal Warfare and Autumnal Mobilization}\n", bedrock,
        "\\subsection{The Kauṭilyan Matrix: Espionage, Panoptic Surveillance, and Intelligence}\n", kautilya,

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
        "\\subsection{The Yogini Axis and Somatic Emblems: Taxonomies, Totems, and Infrastructures}\n", yogini,
        "\\subsection{Diachronic Spatial Analogues: The Ethnographic Mapping of the Naṭ and Kabūtari}\n", diachronic,
        "\\subsection{The Enclosed Column: Pylwan Gopauls, Kolhāṭi Poles, and the State Grid}\n", enclosed,
        "\\subsection{The Indigenous Substrate: Kol Cosmologies and Shamanic Pole-Ascent}\n", remains_of_doc
    ]

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.writelines(v7_clean_flow)

    print(f"\nSuccess! Pristine main_article_v7.tex generated at: {dest_path}")

if __name__ == '__main__':
    src = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    dest = '/Users/croma/acro-yoga-text-mining/main_article_v7.tex'
    build_pristine_v7(src, dest)
