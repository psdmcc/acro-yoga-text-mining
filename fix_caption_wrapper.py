TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Target the exact area where the timeline caption is unanchored
bad_caption_block = r"""    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}"""

good_caption_block = r"""\begin{figure}[htbp]
    \centering
    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}"""

text = text.replace(bad_caption_block, good_caption_block)

# Ensure it closes out cleanly at the bottom
text = text.replace(r"somatic_chronology_timeline.png}", r"somatic_chronology_timeline.png}\n\end{figure}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("[SUCCESS] Caption block successfully anchored inside a valid float mode.")
