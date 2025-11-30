# cellular_network_mapping
Mapping and analyzing cellular network performance using geotagged signal data
## Project Objectives
- Collect geotagged cellular signal data (RSSI, RSRP, RSRQ, network type, cell ID).
- Visualize signal strength and coverage on interactive maps.
- Identify dead zones, handoff patterns, and performance trends.

# Design Overview
- Mobile app for data collection (Network cell Info Lite).
- Python scripts for data cleaning and transformation.
- Mapping tools (Folium) for visualization.
- GitHub repository structure for organizing raw data, processed outputs, and codebase.

# Requirements
- Mobile device with signal logging capability.
- GPS-enabled data collection.
- Python environment with pandas, geopandas, and mapping libraries.
- GitHub repo with folders:
  - `/raw_data`
  - `/processed_data`
  - `/maps`
  - `/scripts`
  - `/docs`


# Data Collection Tool
- **App**: Network Cell Info Pro (Android)
- **Metrics Collected**: RSSI, RSRP, RSRQ, SINR, Cell ID, Network Type, GPS
- **Export Format**: CSV
- **Logging Method**: Walk test with GPS enabled, 1-second interval


# Setup Instructions
# Install Dependencies
```bash
pip install -r requirements.txt

python scripts/Heatmap.py
This will:
- Generate an interactive map (visualizations/signal_strength_heatmap.html)
- Print analysis summaries:
- Dead zones (RSRP < -110 dBm)
- Average RSRP per Cell ID
- LTE vs 5G comparison


# Kepler.gl Visualization
- Using Kepler.gl demo.
- Upload data/processed/combined_cleaned_network_data.csv.
- HTML Export → visualizations/kepler_map.html (interactive map)


Deliverables
- Interactive Folium map (signal_strength_heatmap.html)
- Interactive Kepler map (kepler_map.html)












