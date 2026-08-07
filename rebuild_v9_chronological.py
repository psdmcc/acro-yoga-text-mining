import os
import re
import unicodedata

def build_diachronic_v9(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"Error: Master backup file not found at {src_path}")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Step 1: Splitting main_article_v7.tex into macro-chapters...")

    # Isolate preamble cleanly
    parts = re.split(r"\\begin\{document\}", content, maxsplit=1, flags=re.IGNORECASE)
    preamble = parts[0].strip()
    body = parts[1]

    # Explicit regex section targets to segment the entire document cleanly with zero word loss
    section_patterns = [
        r"\\section\{Introduction:",
        r"\\section\{Somatic\s+Capital\s+and\s+the\s+Economics\s+of\s+the\s+Frontier\}",
        r"\\section\{Tactical\s+Espionage\s+and\s+the\s+Kau\[ṭt]ilyan\s+Matrix\}",
        r"\\section\{Methodology:",
        r"\\section\{Diachronic\s+Spatial\s+Topographies\s+and\s+Shamanic\s+Rites\}",
        r"\\section\{Applied\s+Yoga\s+and\s+the\s+Geopolitics\s+of\s+Erasure:",
        r"\\section\{The\s+Weaponized\s+Breath:",
        r"\\section\{The\s+Courtly\s+Capture:",
        r"\\section\{The\s+Diachronic\s+Climax:",
        r"\\section\{Conclusion\}"
    ]

    # Dynamically extract the text blocks step-by-step
    chunks = {}
    remainder = body

    for i, pat in enumerate(section_patterns):
        match_curr = re.search(pat, remainder, flags=re.IGNORECASE | re.UNICODE)
        if not match_curr:
            print(f"Error: Failed to match section index {i}: {pat}")
            return
        
        if i < len(section_patterns) - 1:
            next_pat = section_patterns[i+1]
            match_next = re.search(next_pat, remainder, flags=re.IGNORECASE | re.UNICODE)
            if not match_next:
                print(f"Error: Failed to locate boundary for section index {i}")
                return
            chunks[i] = remainder[match_curr.start():match_next.start()].strip()
            remainder = remainder[match_next.start():]
        else:
            chunks[i] = remainder[match_curr.start():].strip()

    print("Step 2: Injecting the new Amaraugha and Haṭhapradīpikā 3.81 data matrix...")

    # Prepare the raw text insertion block
    amaraugha_prose = (
        "\n\nThe evolution of physical mechanics across the medieval manual strata marks a radical paradigm shift "
        "from the internal sublimation of fluids to explicit, highly graphic mechanical interventions. In the early fourfold "
        "system codified in the \\textit{Amaraugha} of Gorakṣanātha, the method of forceful yoga, or haṭhayoga, was intentionally "
        "re-engineered away from earlier Buddhist Vajrayāna models \\citep{Birch2024}. While the eleventh-century \\textit{Amṛtasiddhi} "
        "focused strictly on the physiological retention and replenishment of generative fluid, or bindu, within the cranial vault "
        "to ward off death, the \\textit{Amaraugha} systematically repurposed these physical methods for moving kuṇḍalinī and "
        "forcing prāṇa through the central channel to attain a Śaiva form of meditative absorption, or rājayoga \\citep{Birch2024}. "
        "This transition is structurally preserved in regional legends documenting the conversion of masters from a Vajra lineage, "
        "or vajraolī, to the Śaiva Amara lineage, or amaraolī, at Kadri \\citep{Birch2024}. Consequently, the \\textit{Amaraugha} "
        "presents a highly non-physical, interiorized definition of vajroli, treating fluid retention as an incidental byproduct "
        "of breath control, internal resonance, and mental absorption rather than an active manual exercise \\citep{Birch2024}.\n\n"
        "This doctrinal simplicity and sublimation collapsed by the mid-fifteenth century with the compilation of the archetypal "
        "\\textit{Haṭhapradīpikā}, which dramatically expanded the physical repertoire of yoga to include complex therapeutic "
        "interventions and raw sexual fluid manipulation. This late medieval development re-introduced graphic, outer physical mechanics "
        "directly into the vajroli apparatus. For instance, in \\textit{Haṭhapradīpikā} 3.81, the text abandons purely mental control "
        "and mandates direct urogenital catheterization and mechanical aeration:\n\n"
        "\\begin{quote}\n"
        "\\textit{yatnataḥ śaranālena phūtkāraṃ vajrakandare /}\\\\\n"
        "\\textit{śanaiḥ śanaiḥ prakurvīta vāyusaṃcārakāraṇāt //} (HP 3.81) \\\\\n"
        "Using a hollow stalk of bamboo grass, the yogi should carefully and very gently blow into the opening of the penis "
        "in order to make air move into the urethra.\n"
        "\\end{quote}\n\n"
        "Pharmacologically and structurally, this specific method utilizes an external instrument, the śaranāla, to manually "
        "dilate the urogenital passage and force air currents into the bladder matrix. By comparing the \\textit{Amaraugha} with this "
        "later fifteenth-century text, we expose a deep historical inversion: physical yoga did not grow increasingly spiritualized "
        "over time, but rather shifted from an initial Śaiva interiorization of energy pathways back to a transgressive, invasive "
        "mastery of the physical anatomy.\n"
    )

    # Inject the new prose smoothly right into the end of Section 4 (Diachronic Spatial Topographies / Yogini Axis)
    chunks[4] = chunks[4] + amaraugha_prose

    print("Step 3: Compiling definitive linear diachronic text timeline flow...")

    # Assemble into perfect chronological order: Vedic -> Maurya -> Medieval -> Colonial -> Modern
    v9_reordered_flow = [
        preamble,
        "\n\n% Missing Unicode definitions injected into preamble dynamically to prevent compilation crashes\n",
        "\\DeclareUnicodeCharacter{1E45}{\\d{n}} % Velar nasal ṅ\n",
        "\\DeclareUnicodeCharacter{1E7F}{\\d{v}} % Under-dot v for ṿ\n",
        "\\DeclareUnicodeCharacter{1EA1}{\\d{a}} % Under-dot a for ạ\n",
        "\\usepackage{textalpha} % Greek font mapping\n",
        "\\usepackage{textgreek} % Greek text support\n\n",
        "\\begin{document}\n\n",
        
        "%% CHRONOLOGICAL REGION 1: INTRODUCTION\n",
        chunks[0], "\n\n", # Introduction: The Contortionist Turn
        
        "%% CHRONOLOGICAL REGION 2: QUANTITATIVE PIPELINE & METHODOLOGY (UPFRONT)\n",
        chunks[3], "\n\n", # Methodology: Parallel-Core Processing and Jaccard Filters
        
        "%% CHRONOLOGICAL REGION 3: VEDIC & ARCHAIC FRONTIERS\n",
        chunks[6], "\n\n", # The Weaponized Breath: Atharvavedic & Vedic Core
        
        "%% CHRONOLOGICAL REGION 4: CLASSICAL IMPERIAL APPARATUS\n",
        chunks[2], "\n\n", # Tactical Espionage and the Kauṭilyan Matrix
        
        "%% CHRONOLOGICAL REGION 5: MEDIEVAL GUILDS & CORPORATE FORTRESSES\n",
        chunks[1], "\n\n", # Somatic Capital and the Economics of the Frontier
        
        "%% CHRONOLOGICAL REGION 6: TANTRIC TRANSMUTATION & YOGINI CULTS\n",
        chunks[4], "\n\n", # Diachronic Spatial Topographies and Shamanic Rites
        
        "%% CHRONOLOGICAL REGION 7: LATE MEDIEVAL MARTIAL GRAPPLING & INTERTEXTUAL STRATA\n",
        chunks[7], "\n\n", # The Courtly Capture: Postural Weaponization (Mānasollāsa)
        
        "%% CHRONOLOGICAL REGION 8: COLONIAL ENCLOSURE & LABOUR MARKETS\n",
        chunks[8], "\n\n", # The Diachronic Climax: Colonial Capture
        
        "%% CHRONOLOGICAL REGION 9: CONTEMPORARY INSCRIPTIONS & GEOPOLITICS OF ERASURE\n",
        chunks[5], "\n\n", # Applied Yoga and the Geopolitics of Erasure (Modern wellness critique)
        
        "%% CHRONOLOGICAL REGION 10: CONCLUSIONS\n",
        chunks[9]           # Conclusion + Bibliography
    ]

    final_text = "".join(v9_reordered_flow)

    # Fix 4: Force-replace the repeating graphics asset path with your correct chronology timeline chart
    final_text = final_text.replace(
        "\\includegraphics[width=\\textwidth]{outputs/visualizations/\nsomatic_overlap_matrix.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion.",
        "\\includegraphics[width=\\textwidth]{/Users/croma/acro-yoga-text-mining/outputs/visualizations/somatic_chronology_timeline.png}\n \\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic\nContortion."
    )
    final_text = final_text.replace(
        "\\includegraphics[width=0.8\\textwidth]{outputs/visualizations/somatic_continuum.png}",
        "\\includegraphics[width=0.8\\textwidth]{/Users/croma/acro-yoga-text-mining/outputs/visualizations/somatic_chronology_timeline.png}"
    )
    final_text = final_text.replace("gr. \\textgreek{g'omfos}", "gr. γόμφος")

    # Fix 5: Clear unclosed quotes before bibliography boundary to prevent crash loops
    if final_text.count("\\begin{quote}") > final_text.count("\\end{quote}"):
        diff = final_text.count("\\begin{quote}") - final_text.count("\\end{quote}")
        final_text = final_text.replace("\\begin{thebibliography}", "\\end{quote}\n" * diff + "\\begin{thebibliography}")

    # Standardize Unicode strings to NFC
    normalized_text = unicodedata.normalize('NFC', final_text)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(normalized_text)

    print(f"\nSuccess! Chronologically reordered manuscript written fully intact to: {dest_path}")

if __name__ == '__main__':
    # Build directly from the pristine main_article_v7.tex backup file
    build_diachronic_v9('/Users/croma/acro-yoga-text-mining/main_article_v7.tex', '/Users/croma/acro-yoga-text-mining/main_article_v9.tex')
