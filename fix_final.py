import re
import os

with open("main_article_v4.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Remove all latexdiff/xcolor text marker macros to fix the red text globally
text = re.sub(r'\\DIFadd\{([^}]+)\}', r'\1', text)
text = re.sub(r'\\DIFdel\{([^}]+)\}', r'', text)
text = re.sub(r'\\textcolor\{red\}\{([^}]+)\}', r'\1', text)

# Explicitly swap the broken structural string snippet back to a standard cite layout
bad_chunk = r"g, \citet{Mallinson2007} tracks this corporate lineage"
good_chunk = r"g, \citet{Mallinson2007} tracks this corporate lineage"
text = text.replace(bad_chunk, good_chunk)

with open("main_article_v4.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Text strings cleaned.")
