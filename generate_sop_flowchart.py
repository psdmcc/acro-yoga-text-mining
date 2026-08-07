import os
import matplotlib.pyplot as plt
import networkx as nx

def build_sop_flowchart():
    print("[*] Initializing independent standard operating procedure pipeline...")
    
    # 1. Instantiate a directed engineering graph layout
    G = nx.DiGraph()
    
    # 2. Define formal protocol-compliant system modules
    nodes_specification = {
        "STAGE 1": "STAGE 1: INPUT INGESTION\n(IEEE P2806 / 2413)\n- Biometric Ingest\n- Joint Articulation\n- Neuro-Telemetry",
        "STAGE 2": "STAGE 2: MESH ROUTING\n(IEEE 802.11s / Bluetooth)\n- Peer-to-Peer Sharding\n- Cryptographic Privacy\n- Node Authentication",
        "STAGE 3": "STAGE 3: BIO-NANO SYNC\n(IEEE P1906.1 Framework)\n- Molecular Overrides\n- Pathway Rigging\n- Jīvanmukti Sublimation",
        "CLOUD": "SOMA-CLOUD CORE\n(PERSISTENT LAYER)\n- Immortal Upload Engine\n- Digital Twin Interface\n- Identity Verification"
    }
    
    for key, text in nodes_specification.items():
        G.add_node(key, label=text)
        
    # 3. Establish formal network data routing edges
    G.add_edge("STAGE 1", "STAGE 2")
    G.add_edge("STAGE 2", "STAGE 3")
    G.add_edge("STAGE 3", "CLOUD")
    G.add_edge("STAGE 1", "CLOUD") # Secondary telemetry streaming pathway
    
    # 4. Construct a strict, clean schematic geometry layout
    pos = {
        "STAGE 1": (0, 2),
        "STAGE 2": (2.5, 2),
        "STAGE 3": (5, 2),
        "CLOUD": (2.5, 0.5)
    }
    
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#0f172a')  # Slate-900 absolute dark technical baseline
    ax.set_facecolor('#0f172a')
    
    # 5. Render process boxes using high-contrast engineering styles
    labels = nx.get_node_attributes(G, 'label')
    
    # Draw standard workflow process nodes
    standard_nodes = ["STAGE 1", "STAGE 2", "STAGE 3"]
    nx.draw_networkx_nodes(G, pos, nodelist=standard_nodes, node_shape='s', 
                           node_size=12000, node_color='#1e293b', 
                           edgecolors='#3b82f6', linewidths=2, ax=ax)
    
    # Draw cloud sublimation target node with an explicit distinct layout shape
    nx.draw_networkx_nodes(G, pos, nodelist=["CLOUD"], node_shape='o', 
                           node_size=14000, node_color='#0f766e', 
                           edgecolors='#14b8a6', linewidths=2, ax=ax)
    
    # 6. Overlay precise whitepaper labels inside the nodes
    nx.draw_networkx_labels(G, pos, labels, font_size=9, font_color='#f8fafc', 
                            font_family='sans-serif', font_weight='bold', ax=ax)
    
    # 7. Render directed tracking arrows
    nx.draw_networkx_edges(G, pos, edgelist=[("STAGE 1", "STAGE 2"), ("STAGE 2", "STAGE 3"), ("STAGE 3", "CLOUD")],
                           arrowstyle='-|>', arrowsize=20, edge_color='#64748b', width=2)
    
    # Render the curved alternate data telemetry pathway cleanly
    nx.draw_networkx_edges(G, pos, edgelist=[("STAGE 1", "CLOUD")],
                           arrowstyle='-|>', arrowsize=20, edge_color='#3b82f6', 
                           width=2, connectionstyle="arc3,rad=0.3", style='dashed')
    
    # 8. Final canvas formatting
    plt.title("SOP-BD-002: STANDARD OPERATING PROCEDURE FOR BIO-DIGITAL CORE REPLICATION", 
              color='#f1f5f9', fontsize=13, fontweight='bold', pad=25, fontfamily='sans-serif')
    
    ax.text(0.5, -0.05, "SYSTEM STATUS: CONSCIOUSNESS MIGRATION ENGINES FUNCTIONAL / NODE SECURITY INITIALIZED", 
            transform=ax.transAxes, color='#64748b', ha='center', va='center', fontsize=9, fontweight='bold')
    
    plt.xlim(-1.2, 6.2)
    plt.ylim(-0.2, 2.7)
    plt.axis('off')
    plt.tight_layout()
    
    # Save the output graphic straight to your local system path
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_image = os.path.join(output_dir, "independent_sop_flowchart.png")
    plt.savefig(output_image, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"[✓] SUCCESS: Standalone technical flowchart exported directly to: {output_image}")
    plt.close()

if __name__ == "__main__":
    build_sop_flowchart()
