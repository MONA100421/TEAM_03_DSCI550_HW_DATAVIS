import pandas as pd
import os
import json

def prepare_data(input_tsv, output_json, n=100):
    # Read TSV
    df = pd.read_csv(input_tsv, sep='\t')

    # Select relevant columns
    subset = df[[
        "city", "state", "latitude", "longitude", 
        "Haunted Houses Count per County", 
        "crime_rate_per_100000", "year_of_nearest_historical_place"
    ]].copy()

    # Rename columns
    subset.columns = [
        "city", "state", "lat", "lon", 
        "haunted_count", "crime_rate", "year"
    ]

    # Convert to proper numeric values
    for col in ["lat", "lon", "haunted_count", "crime_rate", "year"]:
        subset[col] = pd.to_numeric(subset[col], errors="coerce")

    # Drop essential NaNs
    subset.dropna(subset=["city", "haunted_count", "lat", "lon"], inplace=True)

    # # Limit to top N
    # subset = subset.head(n)

    # Convert to native Python types with NaN-safe checks
    def convert_row(row):
        return {
            "city": row["city"],
            "state": row["state"],
            "lat": float(row["lat"]),
            "lon": float(row["lon"]),
            "haunted_count": float(row["haunted_count"]),
            "crime_rate": float(row["crime_rate"]) if not pd.isna(row["crime_rate"]) else None,
            "year": int(row["year"]) if not pd.isna(row["year"]) else None
        }

    records = [convert_row(row) for _, row in subset.iterrows()]

    # Save JSON
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(records, f, indent=2)

    print(f"✅ Cleaned and saved {len(records)} records to {output_json}")

if __name__ == "__main__":
    prepare_data(
        input_tsv="../data/merged_data_v2_with_entities.tsv",
        output_json="../data/haunted_places_subset.json"
    )
