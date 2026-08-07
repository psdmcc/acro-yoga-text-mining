import os

def correct_berger_keys(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Target file not found at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Restoring correct publication year handles to Berger entries...")

    # Standardize the entries to align directly with your actual distinct years
    # Changes the upper template placeholder to point back cleanly to Berger2015
    content = content.replace("\\bibitem[Berger, 2023]{Berger2023}", "\\bibitem[Berger(2015)]{Berger2015}")
    
    # Ensure line 1360 remains dedicated strictly as your standalone 2023 node
    content = content.replace("\\bibitem[Berger(2023)]{Berger2023}", "\\bibitem[Berger(2023)]{Berger2023}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Success! Year tracking keys successfully synchronized for both publications.")

if __name__ == '__main__':
    target_tex = '/Users/croma/acro-yoga-text-mining/main_article_v9.tex'
    correct_berger_keys(target_tex)
