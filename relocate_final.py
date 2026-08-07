import os
import sys

def force_atomic_relocate(file_path, start_line, end_line, insert_at_line):
    if not os.path.exists(file_path):
        print(f"Error: Target file not found at {file_path}")
        return

    # Read the true, raw contents of the file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Convert 1-based text lines to 0-based Python array indices
    start_idx = start_line - 1
    end_idx = end_line  # Exclusive slice boundary picks up to end_line

    # 1. Extract the target Arthaśāstra text segment precisely
    extracted_block = lines[start_idx:end_idx]
    print(f"Extracted segment length: {len(extracted_block)} lines.")
    
    # 2. Isolate the rest of the document by dropping the block out
    remaining_lines = lines[:start_idx] + lines[end_idx:]

    # 3. Define the insertion index (Line 265 maps to index 264)
    insert_idx = insert_at_line - 1

    # 4. Re-assemble the text matrix cleanly
    final_document = remaining_lines[:insert_idx] + extracted_block + remaining_lines[insert_idx:]

    # Atomic write pattern to break open background editor caches
    temp_file = file_path + ".tmp"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.writelines(final_document)

    # Force the OS kernel to instantly replace the target file on the disk
    os.replace(temp_file, file_path)
    print(f"\nSuccess! Lines {start_line}-{end_line} safely relocated.")
    print(f"The text block now begins exactly at line {insert_at_line}.")

if __name__ == '__main__':
    target = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    force_atomic_relocate(target, start_line=410, end_line=468, insert_at_line=265)
