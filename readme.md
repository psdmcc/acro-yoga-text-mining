# The Acro-Yoga Complex: Text-Mining and the Contortionist Turn (CT)

This repository contains the data pipeline, computational lexicons, and the LaTeX manuscript for **"The Contortionist Turn: Diachronic Mapping of the Acro-Yoga Complex."** 

By running multi-core collocation sweeps across 20,529 text nodes from GRETIL, the Digital Corpus of Sanskrit (DCS), and late antique heresiologies, this project mathematically tracks how volatile, subaltern physical techniques were systematically captured and sanitized by elite text-composers across three millennia.

---

## 📊 Analytical Core Indices

The text-mining engine scores the text nodes along two distinct mathematical axes of subversion:
* **Subversive Mobility Index ($X$-Axis)**: Evaluates the density of spatial border evasion, caravan transit metrics, and active espionage parameters (`sārthavāha`, `cara`, `kāpaṭika`, `laṅghana`).
* **Somatic Contortion Index ($Y$-Axis)**: Evaluates the density of manual joint-crushing holds, close-quarters submission grips, and vertical physical apparatuses (`jambha`, `niṣpipeṣa`, `stambhana`, `kūrmāsana`).

---

## ⚙️ Project Pipeline Execution

To re-calculate the sliding-window proximity scores and re-generate the diachronic plots, run the backend modules sequentially within your local terminal:

```bash
# 1. Initialize raw text layer extraction and regex compilation loop
python3 extract.py

# 2. Execute the 248-hit subaltern lemma sweep and collocation matrix
python3 query_subaltern.py

# 3. Render the Barnes-Hut network visualizations and scatter plots
python3 visualize.py
```

---

## 📚 Historiographical Alignment

The empirical data visualizations produced by this workspace are theoretically anchored within the critical sociology of:
* **William R. Pinch (1996, 2012, 2020)**: Armed monastic labor pools and mercenary capital cartels.
* **David N. Lorenzen (1978)**: Medieval Pāśupata transgressive boundary friction.
* **Rosalind O'Hanlon (2007)**: Wrestling gymnasia (`tālīm khānā`) and spectacular display technologies (`prekṣaṇīya kām`).
* **Patrick Olivelle (1987, 2011)**: State surveillance and Kautilyan containment of mobile mendicants.
* **Chris Danta (2015)**: The aesthetics of verticality and structural normalization.

---

## 📄 LaTeX Compilation

To compile the finalized manuscript alongside the generated figures and the `references.bib` bibliography array, make sure your LaTeX engine is configured to use **LuaLaTeX** or **XeLaTeX** to support the `fontspec` system font package:

```bash
lualatex main_article.tex
bibtex main_article
lualatex main_article.tex
```
