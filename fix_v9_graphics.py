import os
import re

def link_true_visual_assets(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Target file missing at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Locating figure blocks and mapping unique image channels...")

    # Isolate the document into parts to target specific figure instances sequentially
    # This prevents replacing every single figure block with the same line
    fig_blocks = re.split(r"(\\begin\{figure\b[\s\S]*?\\end\{figure\})", content)
    
    matrix_count = 0
    repaired_blocks = []

    for block in fig_blocks:
        if "\\begin{figure}" in block:
            # If the block contains a graphic call
            if "somatic_overlap_matrix.png" in block or "somatic_chronology_timeline.png" in block or "somatic_continuum" in block:
                matrix_count += 1
                
                # First Figure Instance (Section 2: Methodology Processing Pipeline)
                if matrix_count == 1:
                    print(f" -> Mapping Figure {matrix_count} cleanly to Matrix Pipeline Asset.")
                    block = re.sub(
                        r"\\includegraphics\[[^\]]*\]\{[^\\}]*\}",
                        "\\includegraphics[width=\\textwidth]{/Users/croma/acro-yoga-text-mining/outputs/visualizations/somatic_overlap_matrix.png}",
                        block
                    )
                
                # Subsequent Figure Instances (Downstream Chronological Timeline Data Profiles)
                else:
                    print(f" -> Mapping Figure {matrix_count} cleanly to Diachronic Timeline Asset.")
                    block = re.sub(
                        r"\\includegraphics\[[^\]]*\]\{[^\\}]*\}",
                        "\\includegraphics[width=\\textwidth]{/Users/croma/acro-yoga-text-mining/outputs/visualizations/somatic_chronology_timeline.png}",
                        block
                    )
        repaired_blocks.append(block)

    final_content = "".join(repaired_blocks)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("\nSuccess! Visual asset channels successfully separated on your disk layout.")

if __name__ == '__main__':
    target_tex = '/Users/croma/acro-yoga-text-mining/main_article_v9.tex'
    link_true_visual_assets(target_tex)
