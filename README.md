Cellular_Network_Mapping

What is this project about?
This project is a cellular network performance mapping tool. It collects geotagged signal strength data from mobile devices, processes it, and generates interactive heatmaps that visualize network coverage and quality across geographic areas.

What problem does it solve?
Mobile users and network engineers often struggle to identify weak coverage zones, dropped connections, and handoff issues in real-world environments. Traditional carrier maps are generalized and do not reflect actual on the ground performance.
This project solves the problem by providing data-driven, location-specific insights into cellular signal strength and quality, helping to:
- Detect dead zones and poor coverage areas
- Understand handoffs between cells
- Compare performance across different network types (LTE, 5G, etc.

How is the problem being solved?
The solution combines data collection, cleaning, and visualization in a reproducible workflow:
- Data Collection: Signal metrics (RSSI, cell ID, network type) are logged using mobile apps such as Network Cell Info Pro.
- Data Cleaning: Raw logs are processed into structured CSV files stored in data/cleaned/ folder using a python script (combined clean data.py).
- Visualization: A Python script (scripts/heatmap.py) uses pandas, folium, and geopandas to generate interactive heatmaps. Kepler.gl is used for advanced geospatial visualization, enabling dynamic filtering, layering, and exploration of cellular signal data.
- Deployment: Docker ensures reproducibility; the project can be built and run consistently across environments.
- Output: Results are saved as .html maps in the visualizations/ folder, which can be opened in any browser.

# Project Objectives
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
  - `/visualizations`
  - `/scripts`
  - `/docs`


# Data Collection Tool
- App: Network Cell Info Pro (Android)
- Metrics Collected: RSRP,PCI, Cell ID, Network Type, TAC
- Export Format: CSV
- Logging Method: Walk test with GPS enabled, 1-second interval



# Project structure
cellular-mapping-project/
├── Dockerfile
├── requirements.txt
├── README.md
├── scripts/
│   └── heatmap.py
├── data/
│   ├── raw/                # raw signal logs
│   └── processed/            # processed datasets
│       └── combined_cleaned_network_data.csv
└── visualizations/
    └── signal_strength_heatmap.html/ Kepler.gl.html
    



# Setup Instructions
git clone https://github.com/nanannepa-alt/cellular_network_mapping.git

# Install Dependencies
```bash
pip install -r requirements.txt

# Python scripts/Heatmap.py
This:
- Generates an interactive map (visualizations/signal_strength_heatmap.html)
- Prints analysis summaries:
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
- Raw data → data/raw/
- Cleaned data → data/processed/combined_cleaned_network_data.csv
- Scripts → scripts/heatmap.py
- Visualization → visualizations/signal_strength_heatmap.html
- Documentation → README.md














