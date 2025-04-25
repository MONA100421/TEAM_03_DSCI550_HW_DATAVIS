import pandas as pd
import os
import json

def aggregate_by_year(input_tsv, output_json):
    df = pd.read_csv(input_tsv, sep='\t')

    df["year"] = pd.to_numeric(df["year_of_nearest_historical_place"], errors="coerce")
    df = df.dropna(subset=["year"])

    # Group by year and count
    year_agg = df.groupby("year").size().reset_index(name="count")
    year_agg = year_agg.sort_values("year")

    # Convert to list of dicts
    records = [{"year": int(row["year"]), "count": int(row["count"])} for _, row in year_agg.iterrows()]

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(records, f, indent=2)

    print(f"✅ Saved haunted_by_year.json with {len(records)} records")

if __name__ == "__main__":
    aggregate_by_year(
        input_tsv="../data/merged_data_v2_with_entities.tsv",
        output_json="../data/haunted_by_year.json"
    )
