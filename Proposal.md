# Proposal: Rocket League Match Data Pipeline

## Introduction
This project aims to create a data pipeline to ingest, process, and store Rocket League match data for analysis and insights.
[Dataset Link](https://www.kaggle.com/competitions/tabular-playground-series-oct-2022/data)

## Interests and Goals
- **Industries or Domains:** Esports and gaming.
- **Types of Data:** Sensor data, real-time event data from professional Rocket League matches.
- **Objectives:**
  - Develop a data pipeline to ingest, process, and store Rocket League match data in a data warehouse.

## Datasets
- **Source:** Kaggle Tabular Playground Series - Oct 2022.
- **Description:** Position and velocity data of players and ball, additional match information.

## Skills and Tools
- **Technologies/Tools:** Azure Data Factory, PySpark, Python, MySQL Server, Jupyter Notebook, Docker.
- **Concepts:** ETL processes, data warehousing, real-time data processing.

## Methodology

### Data Ingestion:
- **Process:** Use Azure Data Factory to automate the ingestion of Rocket League match data from Kaggle.
- **Storage:** Store ingested data in Azure Blob Storage.

### Data Storage:
- **Raw Data Storage:** Store raw data in Azure Blob Storage.
- **Processed Data Storage:** Load processed data into MySQL Server hosted on Azure.

### Data Processing:
- **Cleaning and Preprocessing:** Use PySpark within a Jupyter Notebook to clean and preprocess the data.
- **Feature Engineering:** Perform feature engineering to create relevant features from raw data.

### Data Analysis:
- **Analysis:** Analyze processed data to extract insights about match dynamics and player performance.
- **Storage:** Store analysis results in MySQL Server.

### Visualization:
- **Exploratory Data Analysis:** Use Jupyter Notebook for EDA and visualizations.
- **Interactive Dashboards:** Create interactive dashboards with Power BI or Tableau connected to MySQL Server.

### Deployment:
- **Containerization:** Containerize the data pipeline using Docker for easy deployment and scalability.
- **Deployment:** Deploy the Docker container on Azure Kubernetes Service (AKS).

## Impact and Utility
- **Impact:** Provide insights for competitive analysis and strategy development in Rocket League.
- **Value:** Helps teams and analysts understand game dynamics and improve performance.

## Expected Outcomes
- **Results:** 
  - A robust data pipeline to ingest, process, and store Rocket League match data.
  - Insights into match dynamics and player performance.

## Timeline
- **Phase 1: Data Ingestion and Storage (1 week):**
  - Set up Azure Data Factory for data ingestion.
  - Store raw data in Azure Blob Storage.

- **Phase 2: Data Processing and Feature Engineering (2 weeks):**
  - Clean and preprocess data using PySpark.
  - Perform feature engineering.

- **Phase 3: Data Analysis, Visualization, and Reporting (1 week):**
  - Analyze processed data.
  - Create interactive dashboards using Power BI or Tableau.
