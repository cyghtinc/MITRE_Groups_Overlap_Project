from stix2 import MemoryStore, Filter
import json

# Load MITRE ATT&CK STIX bundle
with open("enterprise-attack.json", "r", encoding="utf-8") as f:
    bundle = json.load(f)

# Create an in-memory STIX object store
store = MemoryStore(stix_data=bundle["objects"])

# Get all intrusion sets (i.e., threat groups)
groups = store.query([
    Filter("type", "=", "intrusion-set")
])

# Dictionary to store techniques per group (e.g., {"G0006": ["T1059", "T1003.001", ...]})
group_techniques = {}

for group in groups:
    group_id = group["id"]
    group_ext_id = next(
        (ref["external_id"] for ref in group.get("external_references", []) if "external_id" in ref),
        None
    )
    if not group_ext_id:
        continue

    # Find all "uses" relationships for this group
    uses_relationships = store.query([
        Filter("type", "=", "relationship"),
        Filter("relationship_type", "=", "uses"),
        Filter("source_ref", "=", group_id)
    ])

    techniques_used = set()
    for rel in uses_relationships:
        target_id = rel.get("target_ref", "")
        if not target_id.startswith("attack-pattern"):
            continue

        target_obj = store.get(target_id)
        if not target_obj:
            continue

        ext_id = next(
            (ref["external_id"] for ref in target_obj.get("external_references", []) if "external_id" in ref),
            None
        )

        if ext_id:
            techniques_used.add(ext_id)

    # Save techniques list to dict
    group_techniques[group_ext_id] = sorted(techniques_used)

# Save results to JSON
with open("techniques_by_group_full_with_subtechniques.json", "w", encoding="utf-8") as f:
    json.dump(group_techniques, f, indent=2)

print("✅ techniques_by_group_full_with_subtechniques.json created successfully.")
