import pandas as pd
import os
from glob import glob

RAW_DIR = "Data/raw"
OUTPUT_DIR = "Data/processed"
OUTPUT_FILE = "311_legacy_raw_merged.csv"

os.makedirs(OUTPUT_DIR, exist_ok=True)

csv_files = glob(os.path.join(RAW_DIR, "*.csv"))

print(f"Found {len(csv_files)} raw files")

dfs = []

for file in csv_files:
    print(f"Reading {file}")
    df = pd.read_csv(file, low_memory=False)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

# Remove exact duplicate rows only
merged_df = merged_df.drop_duplicates()

output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
merged_df.to_csv(output_path, index=False)

print(f"Merged dataset saved to {output_path}")
print(f"Final shape: {merged_df.shape}")
