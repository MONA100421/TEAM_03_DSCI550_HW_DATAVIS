import pandas as pd
import os
import json

def aggregate_by_state(input_tsv, output_json):
    df = pd.read_csv(input_tsv, sep='\t')

    # Group by state and sum haunted house count
    df["Haunted Houses Count per County"] = pd.to_numeric(
        df["Haunted Houses Count per County"], errors="coerce"
    )
    state_agg = df.groupby("state")["Haunted Houses Count per County"].sum().reset_index()

    # Rename columns for D3
    state_agg.columns = ["state", "haunted_total"]

    # Convert to dictionary
    data_dict = {row["state"]: row["haunted_total"] for _, row in state_agg.iterrows()}

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(data_dict, f, indent=2)

    print(f"✅ Aggregated and saved to {output_json}")

if __name__ == "__main__":
    aggregate_by_state(
        input_tsv="../data/merged_data_v2_with_entities.tsv",
        output_json="../data/haunted_by_state.json"
    )
