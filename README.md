# 🕸️ TEAM03 – Haunted Places Web Data Visualization (DSCI 550)

## 📌 Project Overview

This project builds a **web-based data visualization app** to showcase insights from our previous Haunted Places data analysis. Using **D3.js**, **MEMEX ImageSpace**, and **GeoParser**, we created an interactive mini-site that integrates:

- Sightings and trends across time and space
- Visual similarity of haunted place images
- Location-based insights via named entity recognition

The project highlights our multimodal approach to analyzing and visualizing social media-style haunted data.

---

## 👥 Team Members

| Name                 | Email              |
|----------------------|--------------------|
| Zili Yang            | ziliy@usc.edu      |
| Chen Yi Weng         | wengchen@usc.edu   |
| Aadarsh Sudhir Ghiya | aadarshs@usc.edu   |
| Niromikha Jayakumar  | njayakum@usc.edu   |
| Yung Yee Chia        | yungyeec@usc.edu   |
| Colin Leahey         | cleahey@usc.edu    |

---

## 📂 Directory Structure

```
TEAM_03_DSCI550_HW_DATAVIS/
│
├── Data/
│   ├── haunted_places_v2.tsv
│   ├── haunted_places_summary.json
│   └── geo_locations_subset.json
│
├── Source Code/
│   ├── scripts/
│   │   ├── tsv_to_json_converter.py
│   │   ├── data_summary_generator.py
│   │   └── ingestion_imagecat.py
│   └── notebooks/
│       └── visualization_prep.ipynb
│
├── Website/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
│
├── Requirements.txt
├── Readme.txt
└── TEAM03_DATAVIS_Report.pdf
```

---

## ✅ Completed Tasks

### 1. Data Preparation
- Converted `TSV` data to `JSON` using `etllib` and custom Python scripts.
- Aggregated summaries for D3-ready formats.

### 2. D3 Visualizations
Five interactive charts were created:
- 📊 Bar chart: Top Named Entities
- 📈 Line chart: Sightings over time
- 🌍 Choropleth: Sightings by U.S. state
- 🔦 Sunlight vs. Sightings scatter plot
- 🌲 Similarity Tree: Haunted image objects

### 3. ImageSpace Deployment
- Installed via Docker.
- Indexed images using `Tika` and `ImageCat`.
- Searched for visual similarity via SMQTK and FLANN.

### 4. GeoParser Visualization
- Extracted and mapped location entities using GeoParser.
- Compared locations from assignments 1 and 2.

### 5. ElasticSearch Integration
- Docker-based setup.
- Indexed selected features for search and filtering.

---

## ⚙️ Setup Instructions

### 🔧 Dependencies

- Python 3.8+
- Docker + Docker Compose
- Node.js & npm
- Tesseract OCR
- ElasticSearch / Solr
- Tika-Python, SMQTK, ImageCat

```bash
pip install -r Requirements.txt
```

### 🚀 Run Locally

```bash
# Step 1: Convert and summarize data
cd Source Code/scripts/
python tsv_to_json_converter.py
python data_summary_generator.py

# Step 2: Launch website
cd Website/
python -m http.server 8080

# Visit: http://localhost:8080
```
