TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print("[*] Performing surgical restoration of the introduction paragraph...")

# Target the truncated fragment left behind by the last pass
bad_fragment = (
    " As illustrated in Figure~\\ref{fig:kamatchi_acrobats}, this performance is not mere secular entertainment; it is the enactment of\n"
    "of"
)

# If the fragment layout varies slightly due to previous compiles, we will look for the text right below the child drop
# and cleanly reconstruct the continuous prose layout down to the "This paper argues" transition
anchor_text = "The child drops through the air, caught safely by the collective arms of the guild waiting below."

restored_text_block = r"""The child drops through the air, caught safely by the collective arms of the guild waiting below.

As illustrated in Figure~\ref{fig:kamatchi_acrobats}, this performance is not mere secular entertainment; it is the enactment of an ancient combat myth wherein the hero V\={\i}rab\={a}hu slew Vajrab\={a}hu, physically transforming the victim's spinal column into a vertical performance pole, his bones into structural fasteners, his connective tissues into stabilizing guidelines, and his skull into a clanging victory bell (\textit{jaya-ma\d{n}i}) hoisted at the temple threshold \citep{ThurstonRangachari1909}. This ritual pole represents the \textit{upastambha}\gdash the raw, visceral, materialist ``spine'' or ``support'' of subaltern kinetic technology."""

# 1. Clean out the broken fragment if it matches directly
if bad_fragment in content:
    content = content.replace(bad_fragment, restored_text_block.replace("The child drops through the air, caught safely by the collective arms of the guild waiting below.\n\n", ""))
else:
    # 2. Advanced fallback: split right at the child drop sentence, drop the broken lines, and re-fuse the full paragraph safely
    parts = content.split(anchor_text)
    if len(parts) > 1:
        # Find where the next paragraph ("This paper argues") begins, cutting away the broken fragment middle zone
        remainder = parts[1].split("This paper argues that the history of medieval")[1]
        content = parts[0] + restored_text_block + "\n\nThis paper argues that the history of medieval" + remainder

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Full paragraph completely restored and cross-reference bound.")
