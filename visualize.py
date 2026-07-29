#!/usr/bin/env python3
"""
Somatic Text Mining - Graph Physics Visualization Engine
Author: Patrick S. D. McCartney
Description: Generates an interactive force-directed physics layout mapping 
             the topological cluster distances between subaltern alchemical, 
             toxicological, and Maurya/Patristic espionage nodes.
"""

import os
import json
import networkx as nx
from pyvis.network import Network

def build_somatic_network():
    # 1. Initialize NetworkX Directed Graph Container
    G = nx.DiGraph()

    # 2. Define Node Thematic Clusters and Attributions
    nodes_metadata = {
        # --- SUBALTERN ALCHEMICAL & TOXICOLOGICAL NODES ---
        "viṣa": {"group": "toxicology", "label": "viṣa (Sanskrit Poison Payload)", "size": 35},
        "viṣa-stambhana": {"group": "toxicology", "label": "viṣa-stambhana (Venom Freezing)", "size": 30},
        "rasāyana": {"group": "alchemy", "label": "rasāyana (Alchemical Immortality)", "size": 25},
        "bindu": {"group": "alchemy", "label": "bindu (Vital Humoral Fluid)", "size": 25},
        "cāri-candra": {"group": "alchemy", "label": "cāri candra (Four Moons Matrix)", "size": 25},
        "sapera": {"group": "subaltern", "label": "sapera (Nomadic Snake-Handlers)", "size": 20},
        "ḍomba": {"group": "subaltern", "label": "ḍomba (Peripatetic Acrobat Guilds)", "size": 20},
        
        # --- MAURYA CLANDESTINE STATECRAFT NODES ---
        "jambhakavidyā": {"group": "statecraft", "label": "jambhakavidyā (Metabolic Freezing)", "size": 35},
        "aṅgavidyā": {"group": "statecraft", "label": "aṅgavidyā (Lethal Anatomy Grid)", "size": 28},
        "gūḍhapuruṣa": {"group": "statecraft", "label": "gūḍhapuruṣa (Clandestine Field Agents)", "size": 30},
        "sattrin": {"group": "statecraft", "label": "sattrin (Stationary Covert Undercovers)", "size": 28},
        "bandhanāgāra": {"group": "statecraft", "label": "bandhanāgāra (Panoptic Prison Hub)", "size": 25},
        
        # --- CROSS-CORPUS PATRISTIC TRANSCULTURAL NODES ---
        "ios": {"group": "patristic", "label": "ios (ἰός; Hellenistic Venom/Corrosion)", "size": 40},
        "echidna": {"group": "patristic", "label": "echidna (Temple Snake-Priestess)", "size": 22},
        "chrīō": {"group": "patristic", "label": "chrīō (Sacramental Enclosure Coating)", "size": 25}
    }

    for node, meta in nodes_metadata.items():
        G.add_node(node, **meta)

    # 3. Establish Causal Directed Edges (Extraction & Capture Trajectories)
    edges = [
        # Subaltern extraction pipeline straight to Maurya Statecraft
        ("sapera", "viṣa-stambhana"),
        ("viṣa-stambhana", "viṣa"),
        ("viṣa", "jambhakavidyā"),
        ("ḍomba", "jambhakavidyā"),
        ("jambhakavidyā", "gūḍhapuruṣa"),
        ("aṅgavidyā", "gūḍhapuruṣa"),
        ("gūḍhapuruṣa", "sattrin"),
        ("sattrin", "bandhanāgāra"),
        
        # Alchemical internalizations tracking Debnath/Lorenzen/Mallinson nodes
        ("rasāyana", "bindu"),
        ("cāri-candra", "bindu"),
        ("bindu", "viṣa-stambhana"),
        
        # Transcultural Patristic corporate capture trajectory
        ("echidna", "ios"),
        ("ios", "chrīō"),
        ("jambhakavidyā", "ios")  # The structural cross-corpus bottleneck bridge
    ]
    G.add_edges_from(edges)

    # 4. Compute High-Fidelity Topological Metrics
    print("[*] Computing Brandes betweenness centrality and PageRank metrics...")
    betweenness = nx.betweenness_centrality(G, normalized=True)
    pagerank = nx.pagerank(G)

    # Inject calculations back into node attributes for visualization rendering
    for node in G.nodes():
        G.nodes[node]['title'] = (
            f"<b>{G.nodes[node]['label']}</b><br>"
            f"Betweenness Centrality: {betweenness[node]:.4f}<br>"
            f"PageRank Score: {pagerank[node]:.4f}"
        )
        # Dynamically scale node sizing based on bridging power (betweenness)
        G.nodes[node]['size'] = G.nodes[node]['size'] + (betweenness[node] * 60)

    # 5. Initialize and Calibrate PyVis Interactive HTML Graphics Dashboard
    print("[*] Calibrating force-directed graph physics parameters...")
    net = Network(height="800px", width="100%", bgcolor="#1a1a1a", font_color="#ffffff", directed=True)
    
    # Map colors based on distinct historical/methodological clusters
    color_map = {
        "toxicology": "#e74c3c",  # Deep Red
        "alchemy": "#9b59b6",     # Royal Purple
        "subaltern": "#f1c40f",   # Nomad Yellow
        "statecraft": "#3498db",  # Clandestine Blue
        "patristic": "#2ecc71"    # Hellenistic Green
    }

    for node, attrs in G.nodes(data=True):
        net.add_node(
            node, 
            label=node, 
            title=attrs['title'], 
            size=attrs['size'], 
            color=color_map[attrs['group']]
        )

    for source, target in G.edges():
        net.add_edge(source, target, color="#aaaaaa", arrowStrikethrough=False)

    # Configure Barnes-Hut simulation layout options to lock cluster distances perfectly
    net.set_options("""
    var options = {
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -12000,
          "centralGravity": 0.2,
          "springLength": 180,
          "springConstant": 0.04,
          "damping": 0.85,
          "avoidOverlap": 0.8
        },
        "minVelocity": 0.75
      },
      "interaction": {
        "hover": true,
        "navigationButtons": true,
        "tooltipDelay": 150
      }
    }
    """)

    output_html = "somatic_network.html"
    net.save_graph(output_html)
    print(f"[+] Success! Interactive network compiled and saved natively to: {output_html}")

if __name__ == "__main__":
    build_somatic_network()
