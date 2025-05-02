import pandas as pd
import json
import os

def prepare_parallel_data(input_tsv, output_json, top_n):
    df = pd.read_csv(input_tsv, sep='\t')

    df = df.dropna(subset=["city", "state", "Haunted Houses Count per County", "crime_rate_per_100000", "year_of_nearest_historical_place"])
    df["Haunted Houses Count per County"] = pd.to_numeric(df["Haunted Houses Count per County"], errors="coerce")
    df["crime_rate"] = pd.to_numeric(df["crime_rate_per_100000"], errors="coerce")
    df["year_of_nearest_historical_place"] = pd.to_numeric(df["year_of_nearest_historical_place"], errors="coerce")

    df = df.dropna()

    df["historic_age"] = 2025 - df["year_of_nearest_historical_place"]

    grouped = df.groupby(["state", "city"]).agg({
        "Haunted Houses Count per County": "sum",
        "crime_rate": "mean",
        "historic_age": "mean"
    }).reset_index()

    top_cities = grouped.sort_values("Haunted Houses Count per County", ascending=False).head(top_n)

    result = []
    for _, row in top_cities.iterrows():
        result.append({
            "city": f"{row['city']}, {row['state']}",
            "haunted": row["Haunted Houses Count per County"],
            "crime": row["crime_rate"],
            "historic_age": row["historic_age"]
        })

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Parallel data saved to {output_json}")

if __name__ == "__main__":
    prepare_parallel_data(
        input_tsv="../data/merged_data_v2_with_entities.tsv",
        output_json="../data/parallel_data.json",
        top_n=50
    )
