import pandas as pd
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("combined_cleaned_network_data.csv")

# Show columns for debugging
print("Columns in CSV:", df.columns.tolist())

# Try to detect latitude/longitude column names
lat_candidates = [c for c in df.columns if 'lat' in c.lower()]
lon_candidates = [c for c in df.columns if 'lon' in c.lower() or 'long' in c.lower()]

if not lat_candidates or not lon_candidates:
    raise ValueError("No latitude/longitude columns found. Please check your CSV headers.")

lat_col = lat_candidates[0]
lon_col = lon_candidates[0]

# Detect signal strength column (RSSI or RSRP)
signal_candidates = [c for c in df.columns if 'rssi' in c.lower() or 'rsrp' in c.lower()]
if not signal_candidates:
    raise ValueError("No signal strength column found (RSSI/RSRP). Please check your CSV headers.")

signal_col = signal_candidates[0]

# Initialize map centered around your data
m = folium.Map(location=[df[lat_col].mean(), df[lon_col].mean()], zoom_start=13)

# Prepare heatmap data
heat_data = [[row[lat_col], row[lon_col], row[signal_col]] for _, row in df.iterrows()]

# Add heatmap layer
HeatMap(heat_data,
        min_opacity=0.5,
        radius=15,
        blur=10,
        gradient={0.2: 'red', 0.5: 'yellow', 0.8: 'green'}).add_to(m)

# Save to HTML
m.save("signal_strength_heatmap.html")
print("Heatmap saved as signal_strength_heatmap.html")