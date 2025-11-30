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
