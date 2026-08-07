import os

TARGET_FILE = "main_article_v5.tex"

if not os.path.exists(TARGET_FILE):
    print(f"[!] Error: {TARGET_FILE} not found.")
    exit()

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Define the exact incomplete text block to locate and replace
old_text = "Hidden within subterranean temple vaults to escape frontier military raids, these institutional enclosures acted as"

new_text = r"""Hidden within subterranean temple vaults to escape frontier military raids, these institutional enclosures acted as the ultimate philological filter, inadvertently preserving the gritty, material realities of marginalized kinetic technology while institutional scholasticism systematically stripped them of their socio-political threat. 

This process of capture and abstraction becomes strikingly visible when read against the living, terrestrial counterparts preserved within the subaltern ritual topographies of Highland Odisha, as documented in the longitudinal ethnography of \citet{Berger2015, Berger2023}. Throughout this tribal frontier, the long bamboo pole (\textit{lat} / \textit{lati}) remains a volatile apparatus of somatic possession and structural leverage, serving as the material locus for what Alfred Gell terms ``equilibrium play''\gdash the intentional disruption of bodily balance to instantiate the divine \citep{Gell1980, Berger2023}. For instance, during the \textit{Kodru Parbu} buffalo sacrifice of the Dongria Kondh, the highest-status ritual object associated with the sun deity is the \textit{satara bonda}\gdash a metal pinnacle fixed atop a long bamboo pole \citep{Berger2023}. To bring the deity down into the human sphere, a shaman (\textit{bejuni}) must actively scale this vertical apparatus, shaking violently at an elevation of several meters before collapsing into a trance state \citep{Berger2023}. 

This vertical somatic manipulation reaches its kinetic climax during the \textit{Ganga Porbo} festival of the Joria Porja, where specialized dancers known as the \textit{Dengudi} scale towering stilts fashioned from silk-cotton wood to perform the \textit{Goro Boga} (``foot-offering'') \citep{Berger2015}. By walking and spinning high above the assembly, the performers physically transform their own bodies into a living, mobile ``high shrine'' (\textit{deng-gudi}), executing a vertiginous choreography dictated entirely by the possessing deity \citep{Berger2015}. Crucially, this verticality collapses back into raw, territorial violence during the \textit{Paik Kel} (``wrestling/martial play''), when outcasts of the \textit{Ghasi} lineage enter the ritual arena wielding sharpened bamboo harvesting poles (\textit{sulda}) normally used to stack millet bundles \citep{Berger2015}. Spinning and rushing forward with these improvised weapons, the subaltern war-bands engage in a ferocious, dirt-covered melee, using their heavy wooden stilts and rods to physically tackle and pinning opponents to the ground \citep{Berger2015}. 

When mapped onto our graph-theoretic model, this ethnographic data provides the missing links for the ``Contortionist Turn.'' The Highland Odisha material demonstrates a continuous socio-performative continuum where the external, material bamboo pole (\textit{stambha} / \textit{lati}) is simultaneously a defensive weapon of frontier survival, an apparatus of high-altitude acrobatic equilibrium, and an absolute physical support for structural immanence. It is precisely this dangerous, multi-sensory external technology that the later scholastic manuals captured, disarmed, and flattened into the internal channels of the yogic body."""

if old_text in content:
    content = content.replace(old_text, new_text)
    print("[SUCCESS] Text successfully dropped into the exact paragraph window.")
else:
    print("[!] Warning: Could not find the incomplete sentence anchor.")

# 2. Append the bibliography entries directly above the closing environment tag
bib_anchor = r"\end{thebibliography}"
bib_entries = r"""\bibitem[Berger(2015)]{Berger2015}
Berger, Peter. 2015. \textit{Feeding, Sharing, and Devouring: Ritual and Society in Highland Odisha, India}. Translated by Jennifer R. Ottman. Berlin: De Gruyter.

\bibitem[Berger(2023)]{Berger2023}
Berger, Peter. 2023. \textit{Subaltern Sovereigns: Rituals of Rule and Regeneration in Highland Odisha, India}. Berlin: De Gruyter.

\end{thebibliography}"""

if bib_anchor in content:
    content = content.replace(bib_anchor, bib_entries)
    print("[SUCCESS] Berger bibliography entries successfully appended.")
else:
    print("[!] Warning: Could not locate \end{thebibliography} to append entries.")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(content)
