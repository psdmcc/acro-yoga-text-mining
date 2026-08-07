#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_network_v5.py
Author: AI Research Collaborator (Patrick S. D. McCartney Cross-Cultural Initiative)
Date: July 2026

Description:
    Advanced programmatic configuration script designed to inject the 
    under-examined subaltern technical guilds, pathologized Amarakośa 
    muscular profiles, and Kauṭilyan tactical parameters directly into 
    the parallel-core dictionary framework.
"""

import os
import json

# Uncensored Subaltern Socio-Technical Taxonomy (Unicode Diacritic Compliant)
NEW_LEMMAS = {
    "subaltern_tribal": [
        "pulka\u015ba", "pulka\u015b\u012b", "pulkasa", "pulkas\u012b",
        "sop\u0101ka", "kir\u0101ta", "pulinda", "vai\u1e47a", "anty\u0101vas\u0101yin",
        "ca\u1e47\u1e0d\u0101la", "\u015bumbha", "khasa", "m\u0101gadha", "k\u1e63atta", "m\u016blavikr\u0113t\u0101",
        "\u1e0domba", "\u1e0domb\u0101", "plavaka", "plavak\u0101", "koll\u0101\u1e6da", "r\u016bp\u0101j\u012bv\u0101"
    ],
    "postural_contortion": [
        "vikal\u0101\u1e45ga", "kharva", "v\u0101mana", "praj\u00f1u\u1e25", "\u016brdhvaj\u00f1u\u1e25",
        "sa\u1e43j\u00f1u\u1e25", "sa\u1e43hataj\u0101nuka\u1e25", "pragataj\u0101nuka\u1e25", "kubja", "ku\u1e47i\u1e25", 
        "pa\u1e45gu", "mu\u1e47\u1e0da", "tundila", "m\u0101\u1e43salo", "a\u1e43sala\u1e25", "balav\u0101n", 
        "durbala\u1e25", "ch\u0101to", "am\u0101\u1e43so", "ava\u1e6d\u012b\u1e6da", "avan\u0101\u1e6da", "avabhra\u1e6da"
    ],
    "apparatus_pole": [
        "va\u1e43\u015ba", "stambha", "ve\u1e47u", "va\u1e43\u015banartin", "stambha\u015brama", "la\u1e45ghana"
    ],
    "poison_necromancy": [
        "vi\u1e63a", "gara", "\u015bamana", "bh\u016bta", "\u015bava", "m\u1e5btasa\u1e43j\u012bvin\u012b", 
        "dattura", "garu\u1e0d\u0101\u00f1jana", "\u015bal\u0101k\u0101", "k\u0101lada\u1e63\u1e6da", "manushyakap\u0101lasthi", "vi\u1e63astambhana"
    ],
    "espionage_subversion": [
        "g\u016b\u1e0dhapuru\u1e63a", "cara", "sattrin", "k\u0101pa\u1e6dika", "chadman", "jambhaka", "jambhakavidy\u0101", "m\u0101y\u0101"
    ]
}

def inject_lemmas_v5(database_dict):
    """
    Executes a clean, memory-safe merge of the update_network_v5 subaltern 
    taxonomies into the active text-mining pipeline configuration, executing
    strict sorting and deduplication.
    """
    print("[*] update_network_v5: Injecting expanded socio-technical subaltern categories...")
    
    for category, lemma_list in NEW_LEMMAS.items():
        if category not in database_dict:
            database_dict[category] = []
        
        # Merge, scrub duplicates, and alphabetize to preserve clean indexing logs
        combined = list(set(database_dict[category] + lemma_list))
        database_dict[category] = sorted(combined)
        
        print(f"  [+] Category '{category}': Total nodes is now {len(database_dict[category])}")
        
    return database_dict

def main():
    """
    Standalone testing routine designed to automatically sync files if executed 
    directly within your acro-yoga-text-mining project workspace.
    """
    json_path = "somatic_network.json"
    
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                current_db = json.load(f)
            
            updated_db = inject_lemmas_v5(current_db)
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(updated_db, f, indent=4, ensure_ascii=False)
                
            print(f"[SUCCESS] v5 configurations successfully synchronized with '{json_path}'.")
        except Exception as e:
            print(f"[ERROR] Failed to modify file programmatically: {str(e)}")
    else:
        # Mock initialization run for verification
        print(f"[!] '{json_path}' not detected in active directory workspace.")
        print("[*] Running trial generation loop using virgin dictionary data...")
        mock_db = {}
        inject_lemmas_v5(mock_db)

if __name__ == "__main__":
    main()
