
# 🕸️ TEAM03 – Haunted Places Web Data Visualization (DSCI 550)

A web-based data visualization project exploring patterns and sociocultural correlations among haunted place records in the United States. This project was developed for the DSCI 550: Data Visualization course at the University of Southern California.

## 🔮 Project Overview

Using a rich dataset of haunted locations across the U.S., we applied a combination of geospatial processing, D3.js charting, and open-source mapping tools (Leaflet) to explore:

- Temporal and spatial clustering of hauntings
- Correlations with social indicators such as crime rate, religious adherence, and binge drinking
- Differences in haunting descriptions (apparition types, time of day, etc.)
- Data quality and feature extraction insights from earlier assignments

## 👥 Team Members

| Name                 | Email              |
|----------------------|--------------------|
| Zili Yang            | ziliy@usc.edu      |
| Chen Yi Weng         | wengchen@usc.edu   |
| Aadarsh Sudhir Ghiya | aadarshs@usc.edu   |
| Niromikha Jayakumar  | njayakum@usc.edu   |
| Yung Yee Chia        | yungyeec@usc.edu   |
| Colin Leahey         | cleahey@usc.edu    |

## 🌍 Features and Visualizations

The following 13 interactive visualizations are included:

1. **Bar Chart** - Haunted House Count by City
2. **Bubble Map** - Haunted Place Density
3. **Line Chart** - Historical Year of Nearest Landmark
4. **Scatter Plot** - Haunted Count vs Crime Rate
5. **Parallel Coordinates** - Haunted, Crime, Historical Age
6. **Density × Religious Adherence**
7. **Density × Binge Drinking Rate**
8. **Apparition Types Map**
9. **Average Daylight Hours Choropleth**
10. **Time of Day Map**
11. **Heatmap of Haunted Places**
12. **Density × Daylight Hours**
13. **Geo-validation Screenshots for Anomalies**

Each chart is paired with a narrative description and insight based on pattern recognition and data storytelling.

## 🛠️ Tech Stack

- HTML / CSS / JavaScript
- Bootstrap 4.5
- D3.js v7
- Leaflet.js for geo-visualizations
- Python (Pandas / JSON handling)
- Apache Tika + GeoParser (exploratory)
- PostgreSQL (ImageSpace ingestion)
- Docker (for ImageSpace + SMQTK deployment)

## 📁 Directory Structure

```

TEAM_03_DSCI550_HW_DATAVIS/
│
├── Website/
│   ├── index.html / Website.html            # Main interactive dashboard
│   ├── visualizations/                      # Embedded HTMLs for each chart
│   ├── data/                                # All preprocessed JSON + TSV files
│   ├── scripts/                             # Python scripts for TSV → JSON conversion
│   └── Images/                              # Ghost\_Woman background, USC logo
│
├── Imagespace\_Screenshots/                  # Screenshots of ImageSpace similarity interface
│   ├── ImageSpace\_Similarity\_Result\_ListView\.png
│   └── ImageSpace\_Similarity\_GridView\_ThumbnailsMissing.png
│
├── Visual\_Assets/                           # All exported map visuals (PNG)
│   ├── Correlation Between Haunted Places Density and Adherents Percentage.png
│   ├── Correlation Between Haunted Places Density and Binge Drinking Rate.png
│   ├── Haunted Places by Apparition Type.png
│   ├── Haunted Places by Average Daylight Hours.png
│   ├── Haunted Places by Time of Day.png
│   ├── Heatmap for Haunted Places.png
│   └── Normalized Density x Avg Daylight Hours.png
│
├── TEAM_03_DSCI550_HW_DATAVIS.pdf                 # Final PDF version of report
├── README.md                                # This file
└── hauntedplaces\_core.tar.gz                # Original data archive

```

## 📊 Scripts

| Script Name                  | Purpose                                                  |
|-----------------------------|----------------------------------------------------------|
| `prepare_data.py`           | Cleans TSV and extracts haunted places to JSON           |
| `prepare_data_100.py`       | Samples top N haunted places for simplified map rendering|
| `aggregate_by_year.py`      | Groups haunted records by historical landmark year       |
| `aggregate_parallel_data.py`| Prepares city summaries for parallel coordinates plot     |

## 🧪 Known Issues

- GeoParser (via Tika) was difficult to run due to legacy dependencies.
- ImageSpace indexing succeeded, but thumbnails failed to render in SMQTK.
- Many `time_of_day` fields defaulted to "Unknown" due to extraction issues.
- Some haunted places were mislocated internationally (e.g., UK, India).
```