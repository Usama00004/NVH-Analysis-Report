# NVH Analysis Task Report

This repository contains the complete documentation and resources for the **NVH (Noise, Vibration, and Harshness) Analysis** project focused on electric bikes. The analysis uses synthetic data generated via Python and comprehensive Power BI dashboards to explore NVH metrics across various bike manufacturers and operating conditions.

## Project Overview

![Project Architecture](images/architecture.jpg)

The NVH analysis evaluates noise, vibration, and harshness characteristics to identify comfort and regulatory compliance issues in electric bikes. The study involves:

- Synthetic data generation using Python libraries (`pandas`, `numpy`, `random`)
- Data cleaning, transformation, and modeling in Power BI using Power Query (M language) and DAX
- Interactive visualizations and dashboards built with Power BI Desktop
- Online sharing of reports via Power BI Service

## Repository Contents

- `NVH_Analysis_Report.pdf` – Final detailed analysis report (LaTeX compiled PDF)
- `architecture.jpg` – Project architecture diagram used in the report
- `data/` – Folder containing synthetic data CSV files (fact and dimension tables)
- `python/` – Python scripts for synthetic data generation
- `powerbi/` – Power BI Desktop (.pbix) files with dashboards and data models
- `README.md` – This file

## Key Features

- Star schema data modeling for efficient analysis
- Use of Power BI features: Power Query, DAX measures, slicers, drill-throughs, and bookmarks
- Synthetic data simulating multiple manufacturers, conditions, and test scenarios
- Interactive dashboards showcasing noise, vibration, and harshness insights
- Automated scheduled data refresh configured in Power BI Service

## Important Notes

- The dataset is generated randomly using a Python function for demonstration purposes.
- Metrics and trends in the report will change with each data refresh.
- The project aims to showcase data modeling, analysis, and visualization techniques for NVH data in electric bikes.

## Online Report Access

Access the live, interactive Power BI report here:

[Power BI Live Report](https://app.powerbi.com/view?r=eyJrIjoiNmFhODkxNTQtMzE1ZS00NGY2LTg0OGQtZTNjZTU4ODZhYjM3IiwidCI6IjRmOGE3YmJkLTA2NGItNDEzNC1hZDc2LTU0ZmYyNTVmODllNiIsImMiOjl9&pageName=4d4b68f8a00b62dbe04e)

## About the Author

Prepared by: **Usama Tahir**
- [Portfolio](https://usama00004.github.io/portfolio/)
- [LinkedIn](https://www.linkedin.com/in/usamatahir-00004)




