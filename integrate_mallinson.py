import os
import unicodedata

def integrate_new_evidence(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Target file not found at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Locating the existing Birch and Amaraugha material inside Section 5...")

    # Define a clean, distinct target text block from your active section to anchor our injection point
    anchor_target = (
        "In the early fourfold system codified in the \\textit{Amaraugha} of Gorakṣanātha, "
        "the method of forceful yoga, or haṭhayoga, was intentionally re-engineered away from "
        "earlier Buddhist Vajrayāna models \\citep{Birch2024}."
    )

    # Prepare the synthesized text replacement block that integrates both materials into a unified linear flow
    integrated_expansion = (
        "In the early fourfold system codified in the \\textit{Amaraugha} of Gorakṣanātha, "
        "the method of forceful yoga, or haṭhayoga, was intentionally re-engineered away from "
        "earlier Buddhist Vajrayāna models \\citep{Birch2024}. This structural shift relies fundamentally "
        "on the foundational physiological paradigm established in the eleventh-century \\textit{Amṛtasiddhi} "
        "of Mādhavacandra, which represents the earliest known codification of an explicitly physical method of yoga "
        "\\citep{Mallinson2021}. Prior to this text, the somatic lexicon of tantric Buddhism treated bodily fluids "
        "as vehicles for ritualized, transgressive sexual mechanics. The \\textit{Amṛtasiddhi} enacts a radical internal "
        "inversion by deploying the word bindu strictly to denote semen, while identifying it directly with the physical "
        "substance of amṛta, or immortality \\citep{Mallinson2021}. Within this framework, fluid preservation and cranial "
        "retention, known as bindudhāraṇa, are elevated to the primary mechanism of yogic liberation, making the text's seventh "
        "chapter (\\textit{Bindudhāraṇaviveka}) its longest and most doctrinally dense segment \\citep{Mallinson2021}.\n\n"
        "This transition explicitly rejects the mainstream Vajrayāna sexual yoga paradigm, which relied on a fourfold grid of blisses, "
        "or ānandas, experienced during physical union, culminating in the bliss of cessation, or viramānanda, at the moment of "
        "ejaculation \\citep{Mallinson2021}. The \\textit{Amṛtasiddhi} actively bars sexual intercourse and completely eliminates "
        "viramānanda, identifying ejaculation as kālānanda—the bliss of death by time—and declaring bindu to be the vital source "
        "of all blisses whose downward dissipation triggers mortal decay \\citep{Mallinson2021}. By forcing the downward-moving "
        "ejaculatory breath to reverse its trajectory, the yogin forces both bindu and prāṇa upward through the central channel, "
        "or madhyamā, to capture the remaining three blisses: ānanda, paramānanda, and sahajānanda \\citep{Mallinson2021}. "
        "In this celibate re-organization, the supreme innimate bliss, or sahajānanda, is no longer experienced through a physical consort "
        "but is instead literalized as an internal, cranial state of absorption achieved when the upward-driven solar and lunar currents "
        "merge at the apex of the spinal column \\citep{Mallinson2021}. This structural adaptation is further mirrored in the text's mapping "
        "of the classic tantric moments, or kṣaṇas, and voids, or śūnyas, onto its four developmental hatha stages, adopting a highly "
        "specialized sequence—śūnya, atiśūnya, mahāśūnya, and prabhāsvara—shared uniquely with the Buddhist \\textit{Svādhiṣṭhānakramaprabheda} "
        "\\citep{Mallinson2021}.\n\n"
        "Beyond its physiological re-engineering of tantric bliss, the foundational hatha repertoire adopted by the \\textit{Amaraugha} "
        "and subsequent manuals is structured entirely as an internalized, somatic replication of medieval mercurial alchemy, or "
        "rasashastra \\citep{Mallinson2021}. The diagnostic nomenclature of the three primordial hatha practices—mahāmudrā, mahābandha, "
        "and mahāvedha—is drawn directly from the operational purification processes, or saṃskāras, used to fix volatile mercury "
        "\\citep{Mallinson2021}. In literal alchemical manufacturing, a saṃpuṭa designates a closed crucible formed by joining two clay "
        "bowls, or puṭas, which are hermetically bound with a sealing paste composed of ash or mud, technically termed a mudrā, to "
        "prevent the escape of gaseous reagents under extreme heat \\citep{Mallinson2021}. The alchemical \\textit{Rasacintāmaṇi} (3.87) "
        "explicitly characterizes this physical crucible enclosure as a mahāmudrā \\citep{Mallinson2021}.\n\n"
        "The \\textit{Amṛtasiddhi} operationalizes this chemical apparatus by transforming the living human biological container "
        "into a literal saṃpuṭa. By executing simultaneous muscular constrictions at the perineum and the throat, the yogin seals the "
        "volatile breath and seminal elements within the somatic trunk, transforming the torso into an un-leaking alchemical reactor "
        "\\citep{Mallinson2021}. This replication extends to the mechanics of bandha (thermal stabilization of mercury into an inert, "
        "solid mass, as mirrored in the lock binding the vital winds) and vedha (the projective amalgamation whereby an active alchemical "
        "reagent penetrates base metal, somatically literalized as using the concentrated kinetic force of the prāṇa to forcefully pierce "
        "the structural knots along the central path) \\citep{Mallinson2021}. The text deploys the standard rasashastra purifications "
        "of jāraṇa (digestion) and cāraṇa (activation) to strip away systemic impurities within the bindu network, while māraṇa (chemical "
        "killing or calcination) defines the complete stilling of the breath and the absolute immobilization of the semen \\citep{Mallinson2021}. "
        "Furthermore, the text characterizes the operational states of fixed bindu utilizing the precise chemical adjectives applied to "
        "stabilized mercury: mūrchita (thickened), baddha (bound), līna (dissolved), and niścala (motionless) \\citep{Mallinson2021}. "
        "This rigorous alchemical blueprint suffered severe scholastic decay among later medieval manual-composers and commentators who lost "
        "touch with the original rasashastra architecture. The second stage of hatha practice, the ghaṭa (pot) stage, originally derived its "
        "title from the body's comparison to an alchemical crucible vessel, also called a ghaṭa \\citep{Mallinson2021}. Yet, by the time of "
        "the \\textit{Dattātreyayogāśāstra}, this was replaced by a false folk etymology based on the root \\textit{ghaṭate} (``to unite''), "
        "while later commentators like Brahmānanda and Śivānanda completely misread the technical alchemical term for a double-crucible, or "
        "dvipuṭā, interpreting it erroneously as a reference to the two nostrils \\citep{Mallinson2021}."
    )

    if anchor_target in content:
        content = content.replace(anchor_target, integrated_expansion)
        normalized_text = unicodedata.normalize('NFC', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(normalized_text)
        print("Success! Mallinson 2021 alchemical and physiology datasets smoothly integrated into Section 5.")
    else:
        print("Error: Could not locate the precise text anchor within your current Section 5 text body.")

if __name__ == '__main__':
    target_file = '/Users/croma/acro-yoga-text-mining/main_article_v9.tex'
    integrate_new_evidence(target_file)
