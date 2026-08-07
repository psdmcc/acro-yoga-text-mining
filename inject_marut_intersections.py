import os

TARGET_FILE = "main_article_v4.tex"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Locate the previous Dog-Sorcerer text segment to map out the expansion
bad_anchor = r"Whether interpreted through the filter of structural scapegoating \citep{Strelan2003} or the chthonic purification rites of Hecate, this dual-line layout shows that the handling of non-orthodox herbal compounds (\textit{pharmaka}) and ecstatic somatic movement was systematically barred from the institutional enclosure."

good_anchor = r"""Whether interpreted through the filter of structural scapegoating \citep{Strelan2003} or the chthonic purification rites of Hecate, this dual-line layout shows that the handling of non-orthodox herbal compounds (\textit{pharmaka}) and ecstatic somatic movement was systematically barred from the institutional enclosure. 

Our algorithmic lemma sweep across the early corpus repositories (GRETIL/DCS) confirms that this frontier configuration does not merely operate on parallel tracks; rather, it represents a direct topological intersection. In the storm-dance strata of the \textit{\d{R}gveda} (RV 7.56), the kinetic shaking tokens (\textit{vadhun}, \textit{ga\d{n}a}, \textit{n\d{r}tya}) actively co-occur with the volatile deployment of un-orthodox sorcery/healing frameworks (\textit{m\={a}y\={a}}, \textit{bhe\d{s}aja}) and specific mountain topography keys (\textit{giristh\={a}}, \textit{ara\d{n}ya}). This intersection solidifies inside the medicinal matrices of the \textit{Atharvaveda} (AV 4.13), where the mechanics of weaponized paralysis (\textit{stambha}) and destructive sorcery (\textit{abhic\={a}rika}, \textit{k\d{r}ty\={a}}) are explicitly mapped directly onto the territorial domains of indigenous forest populations (\textit{ni\d{s}\d{a}da}). Furthermore, the sa\d{m}hit\={a} record explicitly items this volatile frontier network within the \textit{\'{S}atarudriya} matrix (\textit{Taittir\={\i}ya Sa\d{m}hit\={a}} 4.5), tying the mobile warfare of the proto-Maruts (\textit{carati}, \textit{y\={a}tu}) straight to the pharmaceutical expertise of wild mountaineers and non-Brahmanical outlaws (\textit{kir\={a}ta}, \textit{vanya}). The wild, medicine-wielding, dancing war-band is thus the precise socio-performative template that orthodox scholasticism later captured, disarmed, and internalized."""

if bad_anchor in text:
    text = text.replace(bad_anchor, good_anchor)
    print("[SUCCESS] Marut sorcery/pharmacology corpus sweep integrated into running text.")
else:
    print("[!] Warning: Target paragraph anchor not found. Checking fallback alternatives...")
    # Secondary broad structural check to ensure text finds a place
    if "The technology was stolen, but the lineage was amputated." in text:
        text = text.replace("The technology was stolen, but the lineage was amputated.", 
                            good_anchor + "\n\nThe technology was stolen, but the lineage was amputated.")
        print("[SUCCESS] Integrated via baseline lineage anchor.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(text)
