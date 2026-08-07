import os

def relocate_section(file_path, start_line, end_line, insert_at_line):
    if not os.path.exists(file_path):
        print(f"Error: Base file not found at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Convert 1-based indexing to 0-based Python indices
    start_idx = start_line - 1
    end_idx = end_line # Exclusive upper bound gets up to end_line

    # Extract the target block
    extracted_block = lines[start_idx:end_idx]
    
    # Isolate the remaining lines
    remaining_lines = lines[:start_idx] + lines[end_idx:]

    # Insertion point configuration (Line 265 means index 264)
    insert_idx = insert_at_line - 1

    # Re-assemble the text matrix
    final_document = remaining_lines[:insert_idx] + extracted_block + remaining_lines[insert_idx:]

    # Overwrite the original LaTeX source file cleanly
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(final_document)
        
    print(f"Success! Lines {start_line}-{end_line} moved. The block now begins at line {insert_at_line}.")

if __name__ == '__main__':
    target_file = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    relocate_section(target_file, start_line=408, end_line=466, insert_at_line=265)
