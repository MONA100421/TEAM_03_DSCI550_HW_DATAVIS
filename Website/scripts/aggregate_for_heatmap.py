import pandas as pd
import os
import json

def aggregate_for_heatmap(input_tsv, output_json, top_n=20):
    df = pd.read_csv(input_tsv, sep='\t')

    df["Haunted Houses Count per County"] = pd.to_numeric(df["Haunted Houses Count per County"], errors="coerce")
    df = df.dropna(subset=["city", "state", "Haunted Houses Count per County"])

    # Group by city + state
    grouped = df.groupby(["state", "city"])["Haunted Houses Count per County"].sum().reset_index()

    # Get top N cities by haunted count
    top_cities = grouped.sort_values("Haunted Houses Count per County", ascending=False).head(top_n)

    # Format to JSON
    result = [
        {
            "state": row["state"],
            "city": row["city"],
            "count": int(row["Haunted Houses Count per County"])
        }
        for _, row in top_cities.iterrows()
    ]

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Created heatmap data with top {top_n} cities")

if __name__ == "__main__":
    aggregate_for_heatmap(
        input_tsv="../data/merged_data_v2_with_entities.tsv",
        output_json="../data/heatmap_city_state.json",
        top_n=30
    )
