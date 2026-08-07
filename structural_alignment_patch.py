import re
import os

TARGET_FILE = "main_article_v4.tex"

def force_structural_alignment():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: {TARGET_FILE} not found.")
        return

    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    print("[*] Re-aligning multi-line font scopes and balancing braces...")

    # Fix Row 17 preamble leak
    text = text.replace(r"\texttt{u4556787@anu.edu.au}}", r"\texttt{u4556787@anu.edu.au}")

    # Fix KSS Dombar multi-line leak (Rows 594-595)
    bad_kss = (
        r"\textit{tatra ve\d{n}ubh\d{r}ta\d{h} kecid \d{d}omb\={a}\d{h} stambha\'sramojjval\={a}\d{h} |\n"
        r"va\d{m}\'sanartin uccai\d{h}stha\d{m} cakru\d{h} k\={a}yapras\={a}dhanam} (KSS 12.1.28)"
    )
    # Check fallback variations if text spacing fluctuates
    text = text.replace(
        r"\textit{tatra ve\d{n}ubh\d{r}ta\d{h} kecid \d{d}omb\={a}\d{h} stambha\'sramojjval\={a}\d{h} | \\" + "\n" + r"va\d{m}\'sanartin uccai\d{h}stha\d{m} cakru\d{h} k\={a}yapras\={a}dhanam}",
        r"\noindent\textit{tatra ve\d{n}ubh\d{r}ta\d{h} kecid \d{d}omb\={a}\d{h} stambha\'sramojjval\={a}\d{h} |} \\\n\noindent\textit{va\d{m}\'sanartin uccai\d{h}stha\d{m} cakru\d{h} k\={a}yapras\={a}dhanam}"
    )

    # Fix MŪ Kirata multi-line leak (Rows 619-620)
    text = text.replace(
        r"\textit{m\={a}y\={a}kir\={a}taprakato yath\={a} ti\d{s}\d{t}hati k\={a}nane \\" + "\n" + r"cittaspandastath\={a} stabdho granthibhedena \'s\={a}myati}",
        r"\noindent\textit{m\={a}y\={a}kir\={a}taprakato yath\={a} ti\d{s}\d{t}hati k\={a}nane |} \\\n\noindent\textit{cittaspandastath\={a} stabdho granthibhedena \'s\={a}myati}"
    )

    # Fix MP 9.79 multi-line leak (Rows 427-429)
    text = text.replace(
        r"\textit{medoharo k\={a}pahara\'stath\={a}gnikara api | \\" + "\n" + r"gurustambhahara\'scaiva ka\d{n}\d{t}h\={a}mayarogaharastath\={a} || MP 9.79 ||}",
        r"\noindent\textit{medoharo k\={a}pahara\'stath\={a}gnikara api |} \\\n\noindent\textit{gurustambhahara\'scaiva ka\d{n}\d{t}h\={a}mayarogaharastath\={a} || MP 9.79 ||}"
    )

    # Fix MP 7.5 multi-line leak (Rows 438-441 / 484-485)
    text = text.replace(
        r"\textit{anna\d{m} da\'sagu\d{n}a\d{m} pi\d{s}\d{t}a\d{m} pi\d{s}\d{t}\={a}d da\'sagu\d{n}a\d{m} paya\d{h} | \\" + "\n" + r"pi\d{s}\d{t}ena vardhate pr\={a}\d{n}a\d{h} \'saurya\d{m} m\={a}\d{m}s\={a}t praj\={a}yate ||}",
        r"\noindent\textit{anna\d{m} da\'sagu\d{n}a\d{m} pi\d{s}\d{t}a\d{m} pi\d{s}\d{t}\={a}d da\'sagu\d{n}a\d{m} paya\d{h} |} \\\n\noindent\textit{pi\d{s}\d{t}ena vardhate pr\={a}\d{n}a\d{h} \'saurya\d{m} m\={a}\d{m}s\={a}t praj\={a}yate ||}"
    )

    # Clean any loose stray multi-line quote bounds remaining
    text = re.sub(r'\\textit\{([^}]+)\s*\\\s*\n\s*([^}]+)\}', r'\\noindent\\textit{\1} \\\\\n\\noindent\\textit{\2}', text)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(text)

    print("[SUCCESS] Multi-line string scopes balanced and closed.")

if __name__ == "__main__":
    force_structural_alignment()
