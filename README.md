# NVH Visualization using Python & Power BI

This project demonstrates how to generate dummy data using Python and then visualize it using **Power BI**. It's designed to simulate a real-world workflow for **data analysis**, **dashboard building**, and **business intelligence** tasks.

## 🧰 Tech Stack

- **Python** (Data generation, processing)
- **Pandas** (Data manipulation)
- **NumPy / Faker** (Dummy data generation)
- **Power BI** (Data visualization and dashboard creation)

---

## 📊 Project Overview

1. **Data Generation (Python)**  
   Python scripts are used to create realistic dummy data for a fictional business use case. Examples include:
   - Sales data
   - Customer information
   - Product inventory
   - Time-series metrics

2. **Data Cleaning & Transformation**  
   Using `pandas`, the generated data is cleaned, formatted, and exported as `.csv` or `.xlsx` for use in Power BI.

3. **Visualization (Power BI)**  
   The generated data is imported into Power BI, where multiple visuals such as:
   - Bar charts
   - Line graphs
   - Pie charts
   - KPI cards
   - Slicers & filters  
   are created to provide insights.

---

## 📂 Project Structure

```plaintext
dummy-data-powerbi/
│
├── data/
│   └── dummy_sales_data.csv         # Exported dataset for Power BI
│
├── notebooks/
│   └── generate_data.ipynb          # Jupyter Notebook for data generation
│
├── scripts/
│   └── generate_data.py             # Script to generate and export dummy data
│
├── visuals/
│   └── dashboard_screenshot.png     # Sample Power BI dashboard image
│
├── DummyDataDashboard.pbix          # Power BI report file
│
└── README.md                        # This file
