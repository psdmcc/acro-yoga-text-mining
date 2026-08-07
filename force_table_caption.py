TARGET_FILE = "main_article_v5.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean up any accidental figure markers injected by the previous pass
content = content.replace(r"\begin{figure}[htbp]", "")

# 2. Target line 217 specifically and ensure it sits right beneath a clean \begin{table} hook
bad_block = r"""\begin{table}[htbp]
    \centering
    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}"""

# Force absolute structure reset
content = content.replace(
    r"\caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}",
    r"\begin{table}[htbp]\n    \centering\n    \caption{The Acro-Yoga Complex: Subversive Mobility vs. Somatic Chronology}"
)

# Clean double table entries if any were created
content = content.replace(r"\begin{table}[htbp]" + "\n" + r"\begin{table}[htbp]", r"\begin{table}[htbp]")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Table environment anchors balanced on line 217.")
