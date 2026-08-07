import os

def insert_consolidated_text(file_path):
    if not os.path.exists(file_path):
        print("Error: File not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Define the precise content block
    consolidated_prose = [
        "\\subsection{The Liturgical Mapping of Somatic States and Performer Networks}\n",
        "Chapter 30 of the \\textit{Vajasaneyi Samhita} and Chapter 3.4 of the \\textit{Taittirīya Brāhmaṇa} function as systematic state censuses that capture and categorize early Indian specialized and non-Aryan tribal knowledge. Rather than recording literal sacrifices, these manuals construct a proto-pharmacological grid where human archetypes map directly to distinct neurological states, spatial coordinates, and cosmic elements. Within this state archival framework, the administrative mandate pairs the quantitative study of structural anatomy, or aṅgavidyā, directly with jambhakavidyā---the subaltern science of metabolic freezing, physical deception, and deceptive camouflage. \n",
        "\n",
        "To emphasize this structural interconnectedness between state espionage apparatuses and peripatetic guilds of performers, we begin with Sastri's translation of jambhakavidyā as ``legerdemain'' or sleight-of-hand \\citep{shamasastri1929}. To fully comprehend this integration of the performer and the operative in early India, one must trace the dual identity of jambhaka, which has an Indo-European etymology related to the jaws and teeth of animals within the context of crushing and devouring (see Pāṇini 7.1.61; RV 1.30.9), as a charm (MBh 5.64.16), and as the name of several evil spirits. \n",
        "\n",
        "The structural pairing of the vamśānartin, or bamboo pole acrobat, and the pīṭhasarpin, or ground-crawler, captures a precise pharmacodynamic polarity within this liturgical mapping. Bound directly to the horizontal plane of the earth, or bhūmi, the pīṭhasarpin represents the flaccid paralysis, motor collapse, and neuromuscular failure induced by raw tropical poisons and neurotoxins. Conversely, the vamśānartin is assigned to the mid-air atmosphere, or antarikṣa, and paired with the concept of terror, or bhīsa. \n",
        "\n",
        "In this configuration, the acrobat represents the somatic mastery of equilibrium over vertigo, where the vertical axis acts as an internal stabilizer that prevents the nervous system from collapsing into panic, catatonia, or the profound state of delirium known as pramada. This structural juxtaposition sets up an ancient technological spectrum of bodily control: the crawling pīṭhasarpin embodies the somatic collapse of the poison-strike, while the elevated vamśānartin represents the defensive antidote-axis capable of anchoring the mind against spatial disorientation.\n",
        "\n",
        "\\subsection{Tribal Geography, Tactical Espionage, and Alchemical Decipherment}\n",
        "The Vedic texts cluster indigenous, forest-dwelling groups alongside specific environmental coordinates and states of acute drug delirium. Tied directly to the air element, the Caṇḍāla represents the master of invisible, moving, and volatile currents, matching the properties of wind, or vāyu. Meanwhile, the mountain-dwelling Kirātas are positioned as keepers of deep caves, or guhā, while the jambhaka, the snapping-jaw or seizure demon, is fixed to high mountain ridges, or sānu. This distribution tracks the native habitat of extreme convulsants and neurotoxic roots, such as aconite and strychnine, that clinically induce full-body rigid tetany, muscle spasms, and severe lockjaw. \n",
        "\n",
        "In Book 14 of the \\textit{Arthaśāstra}, Kauṭilya transitions from conventional statecraft to a highly sophisticated system of biochemical manipulation, or aupaniṣadika, that directly weaponizes this tribal geography. Rather than relying on simple poisons, the text mandates specific combinations of toxic flora to induce systemic psychological and physiological failure. Central to these formulations is the pairing of dhattūra (\\textit{Datura metel}) with eraṇḍa (\\textit{Ricinus communis}). For instance, in the preparation of incapacitating powders, or yoga, in the book dealing with esoteric practices and the chapter explaining the means to injure an enemy, or paraghātprayoga, the formulation to cause death or insensibility, or maraṇaprayoga, begins with:\n",
        "\n",
        "\\begin{quote}\n",
        "\\textit{dhattūrasya ca bījāni eraṇḍamūlaṃ ca saṃcūrṇya\\dots}  (KAŚ 14.1.177) \\\\\n",
        "Having pulverized the seeds of \\textit{dhattūra} and the roots of \\textit{eraṇḍa}\\\\dots\\\\\n",
        "\\end{quote}\n",
        "\n",
        "Pharmacologically, this pairing represents a calculated exploitation of botanical properties. The tropane alkaloids of dhattūra induce immediate pupillary dilation and acute delirium, rendering the target disoriented and highly suggestible. Concurrently, the ribosome-inactivating proteins within eraṇḍa trigger localized cellular necrosis and profound physical distress \\citep{toxicology_datura, rip_necrosis,scopolamine_suggest}. This targeted disruption aligns directly with Kauṭilya's tactical intent in the open verses, where these flora are first combined (KAŚ 14.1.1--3). When deployed by state spies disguised as traveling performers, peripatetic actors, or ascetic sorcerers, these chemical agents effectively simulated demonic possession or divine wrath, directly bridging the gap between street illusion, the jambhaka seizure-state, and covert state security \\citep{kangle1972, olivelle2013}.\n",
        "\n",
        "Centuries after the codification of the imperial manuals, heterodox Left-Hand Path Tantric, Hatha Yoga, and Rasashastra mercurial alchemy lineages unzipped these Vedic and administrative ciphers. They abandoned orthodox altars, ventured back to outcaste spaces, and transformed these state-level social categories into an operational laboratory manual. Alchemists discovered that soaking mountain aconite in an alkaline matrix, such as cow's urine, achieves shodhana purification by buffering its jaw-locking execution vector—the clinical footprint of the mountain-sloping jambhaka—leaving the central nervous system exposed to a borderless, ego-dissolving surge. \n",
        "\n",
        "Furthermore, in early vernacular riddle-poetry, known as ulaṭbāṃsī, and classical Hatha Yoga texts, the physical bamboo pole, or vamśa, was explicitly internalized as the human central spinal channel, or suṣumṇā. The practitioner mimics the sky-acrobat, utilizing the vertical column to anchor their witness-awareness and maintain perfect stability. By stepping onto this razor-thin vertical line of gravity, the yogin preserves an unmoving center of awareness, preventing the mind from falling into the horizontal, paralyzed, and delirious collapse of the earth-bound pīṭhasarpin while intense chemical deliriants systematically dismantle the ordinary ego.\n"
    ]

    # Convert 1-based line bounds (323 to 484 inclusive) into 0-based indices
    # lines[:322] captures up to line 322. lines[484:] captures everything from line 485 onward.
    updated_document = lines[:322] + consolidated_prose + lines[484:]

    temp_path = file_path + ".tmp"
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_document)

    os.replace(temp_path, file_path)
    print("Success! Lines 323-484 have been overwritten with your consolidated narrative.")

if __name__ == '__main__':
    target = '/Users/croma/acro-yoga-text-mining/main_article_v6.tex'
    insert_consolidated_text(target)
