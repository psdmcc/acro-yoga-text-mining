import json
import os

json_path = "somatic_network.json"

# High-density structural payload mapping your three-tier extraction thesis
network_payload = {
    "nodes": [
        { "id": "pithasarpin", "group": "subaltern_tribal", "label": "pīṭhasarpin (Ground Crawler)", "weight": 42 },
        { "id": "vamsanartin", "group": "apparatus_pole", "label": "vaṃśanartin (Pole Dancer)", "weight": 38 },
        { "id": "stambha", "group": "apparatus_pole", "label": "stambha (Timber Axis)", "weight": 118 },
        { "id": "candala", "group": "subaltern_tribal", "label": "caṇḍāla (Outcaste)", "weight": 85 },
        { "id": "sarpa", "group": "postural_contortion", "label": "sarpa (Serpent Dynamics)", "weight": 76 },
        { "id": "asana", "group": "postural_contortion", "label": "āsana (Postural Enclosure)", "weight": 210 }
    ],
    "links": [
        { "source": "vamsanartin", "target": "stambha", "value": 0.684, "layer": "Vedic" },
        { "source": "pithasarpin", "target": "candala", "value": 0.592, "layer": "Vedic" },
        { "source": "vamsanartin", "target": "candala", "value": 0.712, "layer": "Vedic" },
        { "source": "pithasarpin", "target": "sarpa", "value": 0.615, "layer": "Epic_Puranic" },
        { "source": "pithasarpin", "target": "stambha", "value": 0.485, "layer": "Moksopaya_Layer" },
        { "source": "stambha", "target": "asana", "value": 0.890, "layer": "Late_Hatha" },
        { "source": "sarpa", "target": "asana", "value": 0.812, "layer": "Late_Hatha" }
    ]
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(network_payload, f, ensure_ascii=False, indent=2)

print(f"[✓] SUCCESS: Unified JSON written cleanly to {json_path}")
