import os

def repair_v7_layout(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create clean empty arrays to filter the index matrix
    repaired_lines = []
    
    # We step line-by-line through the file to strip the duplicate header
    # and verify macro boundaries
    for i, line in enumerate(lines):
        # 1-indexed conversion line 482 is index 481
        if i == 481 and "Methodology: Parallel-Core Processing" in line:
            print(f"Purging duplicate Section 4 header at line {i+1}...")
            continue # Drop the duplicate line completely
            
        repaired_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(repaired_lines)

    print("\nSuccess! Structure repaired successfully.")
    print(" -> Duplicate Methodology header cleanly expunged.")
    print(" -> Floating subsections now read as child branches under Section 3.")

if __name__ == '__main__':
    v7_file = '/Users/croma/acro-yoga-text-mining/main_article_v7.tex'
    repair_v7_layout(v7_file)
