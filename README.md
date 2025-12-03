# Cellular Network Mapping

# What is this project about?
This project is a cellular network performance mapping tool. It collects geotagged signal strength data from mobile devices, processes it, and generates interactive heatmaps that visualize network coverage and quality across geographic areas.

# What problem does it solve?
Mobile users and network engineers often struggle to identify weak coverage zones, dropped connections, and handoff issues in real-world environments. Traditional carrier maps are generalized and do not reflect actual on the ground performance.
This project solves the problem by providing data-driven, location-specific insights into cellular signal strength and quality, helping to:
- Detect dead zones and poor coverage areas
- Understand handoffs between cells
- Compare performance across different network types (LTE, 5G, etc.

# How is the problem being solved?
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
├── Dockerfile                     # containerized environment (repo is self-contained, reproducible and easy to share)
├── requirements.txt               # lists all python packages of this project
├── README.md                      # configuration files 
├── scripts/                       # Python scripts for processing & visualization      
│   ├── combined clean data.py     # compute RSSI, RSRP, RSRQ trends
│   └──heatmap.py                  # visualization script
├── data/
│   ├── raw/                       # raw signal logs from mobile app
│   │   └── raw.csv        
│   └── processed/                 # final datasets ready for visualization
│       └── processed.csv
├── visualizations/                # outputs of mapping & analysis
│   ├── heatmaps/                  # static & interactive heatmaps
│   │   ├── signal_strength_heatmap.html
│   └── kepler/                    # Kepler.gl exports
│       └── kepler.gl.html
└── docs/                          # documentation & reports
    ├── documentation.md
    └── report.md

# Summary of Cellular Network Performance
The analysis of the collected geotagged signal data provides a clear picture of how coverage, trends, limitations, and network behavior manifest in the study area. Coverage is generally strong in central zones, with reliable RSSI and RSRP values, but weaker signals appear at the periphery, highlighting potential dead zones. Because the data was gathered with limited movement, the coverage patterns are spatially clustered, offering a localized rather than comprehensive view of performance.
Trends across the dataset reveal that LTE is the dominant network type, with occasional handoffs to 5G and 3G depending on location. Signal strength is consistently higher in open areas, while attenuation is evident in dense urban or obstructed environments. Cell ID changes align with handoff points, confirming expected network behavior. Overall, the temporal stability of the data suggests steady connectivity during the logging period.
The study does face limitations. The short duration and constrained mobility reduce the diversity of scenarios captured, meaning the dataset cannot fully represent broader geographic or temporal variations. Measurements are device‑specific and may not generalize across different hardware. Environmental factors such as weather, building materials, and interference were not systematically controlled, and the dataset does not include latency or uplink performance, which are critical for end‑to‑end analysis.
Despite these constraints, the observed network behavior aligns with the principles of cellular communication. Handoffs occur smoothly, with adaptive resource allocation reflected in the interplay of RSSI, RSRP, and RSRQ values. The network demonstrates reliability, though performance varies with geography and environment. This highlights both the strengths and the challenges of cellular systems: while they maintain robust connectivity, localized weak zones and environmental influences remain persistent issues.











# Setup Instructions
git clone https://github.com/nanannepa-alt/cellular_network_mapping.git

# Dependencies
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














