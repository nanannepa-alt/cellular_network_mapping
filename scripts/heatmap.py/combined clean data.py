import pandas as pd
import glob
import os

# Step 1: Define input and output paths
input_folder = 'data/raw/'
output_file = 'data/cleaned/combined_cleaned_network_data.csv'

# Step 2: Find all CSV files in the raw data folder
csv_files = glob.glob(os.path.join(input_folder, '*.csv'))

# Step 3: Load and combine all CSVs
df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    df['source_file'] = os.path.basename(file)  # Optional: track origin
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

# Step 4: Rename columns for consistency
combined_df.rename(columns={
    'lat': 'Latitude',
    'lon': 'Longitude',
    'signal': 'RSRP',  # Assuming LTE and signal is RSRP
    'act': 'NetworkType',
    'cellid': 'CellID',
    'measured_at': 'Timestamp'
}, inplace=True)

# Step 5: Drop rows with missing GPS or signal
combined_df.dropna(subset=['Latitude', 'Longitude', 'RSRP'], inplace=True)

# Step 6: Convert signal to numeric
combined_df['RSRP'] = pd.to_numeric(combined_df['RSRP'], errors='coerce')

# Step 7: Filter for valid RSRP range
combined_df = combined_df[(combined_df['RSRP'] >= -140) & (combined_df['RSRP'] <= -44)]

# Step 8: Save cleaned data
combined_df.to_csv(output_file, index=False)

print(f"✅ Combined and cleaned data saved to: {output_file}")
print(combined_df[['Timestamp', 'Latitude', 'Longitude', 'RSRP', 'NetworkType', 'CellID']].head())
print(df.columns)

df.rename(columns={
    'Latitude': 'latitude',
    'Longitude': 'longitude',
    'RSRP': 'RSSI'   # if you want consistency
}, inplace=True)

