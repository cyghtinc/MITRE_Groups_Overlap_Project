import pandas as pd
import json
from itertools import combinations

def split_techniques(techniques):
    base = set()
    sub = set()
    for t in techniques:
        if '.' in t:
            sub.add(t)
        else:
            base.add(t)
    return base, sub

def compare_groups_same_country(groups_csv, techniques_file, target_country):
    with open(techniques_file, "r") as f:
        techniques_dict = json.load(f)

    df = pd.read_csv(groups_csv)
    df.columns = df.columns.str.strip().str.replace(r'\s+', ' ', regex=True)
    name_col = [col for col in df.columns if "name" in col.lower()][0]
    group_names = dict(zip(df["Group ID"], df[name_col]))

    country_groups = df[df["Country"].str.lower() == target_country.lower()]
    group_ids = country_groups["Group ID"].dropna().tolist()

    print(f"\n🟦 Country: {target_country}")
    for gid in group_ids:
        print(f"  - {gid}: {group_names.get(gid, 'Unknown')}")

    print("\n🔍 Comparing groups:\n")
    results = []

    for g1, g2 in combinations(group_ids, 2):
        t1_all = set(techniques_dict.get(g1, []))
        t2_all = set(techniques_dict.get(g2, []))

        t1_base, t1_sub = split_techniques(t1_all)
        t2_base, t2_sub = split_techniques(t2_all)

        shared_base = t1_base & t2_base
        shared_sub = t1_sub & t2_sub

        # Overlap percentages
        base_overlap = len(shared_base) / max(len(t1_base), len(t2_base), 1) * 100
        sub_overlap = len(shared_sub) / max(len(t1_sub), len(t2_sub), 1) * 100
        total_overlap = (len(shared_base) + len(shared_sub)) / max(len(t1_all), len(t2_all), 1) * 100

        result = {
            "Group 1": g1,
            "Group 2": g2,
            "Group 1 Name": group_names.get(g1, ""),
            "Group 2 Name": group_names.get(g2, ""),
            "Group 1 Techniques": ", ".join(sorted(t1_all)),
            "Group 2 Techniques": ", ".join(sorted(t2_all)),
            "Group 1 Techniques Count": len(t1_base),
            "Group 1 Sub-Techniques Count": len(t1_sub),
            "Group 2 Techniques Count": len(t2_base),
            "Group 2 Sub-Techniques Count": len(t2_sub),
            "Shared Techniques": ", ".join(sorted(shared_base)),
            "Shared Sub-Techniques": ", ".join(sorted(shared_sub)),
            "Technique Overlap (%)": round(base_overlap, 2),
            "Sub-Technique Overlap (%)": round(sub_overlap, 2),
            "Shared Total Count": len(shared_base) + len(shared_sub),
            "Total Overlap (%)": round(total_overlap, 2)
        }

        print(f"{g1} ({group_names.get(g1)}) vs {g2} ({group_names.get(g2)}):")
        print(f"  Techniques Overlap: {result['Technique Overlap (%)']}%")
        print(f"  Sub-Techniques Overlap: {result['Sub-Technique Overlap (%)']}%")
        print(f"  Shared Total: {result['Shared Total Count']}\n")

        results.append(result)

    output_df = pd.DataFrame(results)
    output_file = f"comparison_{target_country}_detailed.csv"
    output_df.to_csv(output_file, index=False)
    print(f"\n✅ Results saved to {output_file}")

if __name__ == "__main__":
    csv_file = "mitre_groups_enriched.csv"
    techniques_file = "techniques_by_group_full_with_subtechniques.json"
    country = "Iran"  # change as needed

    compare_groups_same_country(csv_file, techniques_file, country)
