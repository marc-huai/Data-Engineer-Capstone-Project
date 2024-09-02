
## README: Rocket League Data Pipeline Capstone Project

### **Project Overview**
The Rocket League Data Pipeline Capstone Project is designed to analyze Rocket League match data to assess player performance, game dynamics, and team strategies. This project aims to build a robust data pipeline that efficiently processes, cleans, and stores the data, enabling advanced analytics and predictive modeling.

### **Current State of the Project**
1. **Data Collection**:
   - Multiple CSV files containing match data have been collected from various sources.
   - Data includes player positions, velocities, ball dynamics, scoring events, and more.

2. **Data Exploration**:
   - Conducted exploratory data analysis (EDA) using Python libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`).
   - Loaded all CSV files into a single Pandas DataFrame for comprehensive data handling.
   - Identified key patterns, anomalies, and data quality issues that required attention.

3. **Data Cleaning and Preparation**:
   - Addressed missing values, corrected data types, and converted data into Parquet format for optimized storage and query performance.
   - Prepared the data for downstream analytics by ensuring it is clean, consistent, and efficient to query.

4. **Data Modeling**:
   - Designed a Star Schema to support analytical queries.
   - Developed a `FACT_GAME_EVENTS` table as the central table, supported by dimension tables (`DIM_GAME`, `DIM_PLAYER`, `DIM_EVENT`, `DIM_TEAM`).

5. **Feature Engineering**:
   - Extracted features such as player speed, distance to the ball, and player positions to enrich the dataset.
   - These features enable deeper analysis and support predictive modeling efforts.

6. **Visualization and Insights**:
   - Created visualizations, including 3D scatter plots and distribution plots, to identify patterns and insights from the data.
   - Used these insights to inform further analysis and modeling steps.

7. **Next Steps**:
   - Transition from EDA to the development of a full ETL (Extract, Transform, Load) pipeline.
   - Focus on integrating the cleaned data into a database or data warehouse.
   - Prepare the data for advanced analytics, machine learning, and visualization.

### **Rationale for the Current State**
- **Data Collection**: Collecting comprehensive data across multiple matches provides a large, diverse dataset that captures various game scenarios.
- **Data Exploration**: EDA helps to understand the data structure and identify initial data quality issues, ensuring that only relevant, high-quality data is used for further analysis.
- **Data Cleaning**: Converting data into Parquet format and addressing data quality issues improves both storage efficiency and query performance, making the dataset more accessible for analytical tasks.
- **Data Modeling**: The Star Schema is chosen for its simplicity and effectiveness in handling complex analytical queries, providing a clear structure for data aggregation and reporting.
- **Feature Engineering**: Feature extraction enriches the dataset with metrics crucial for performance analysis and predictive modeling, enabling more robust insights and decision-making.
- **Visualization**: Visualizing data allows for the identification of patterns and relationships that are not immediately apparent, guiding the analytical focus and strategy.

### **Project Goals**
- Build a comprehensive data pipeline that can handle large volumes of Rocket League match data.
- Ensure data is clean, consistent, and optimized for storage and query performance.
- Enable advanced analytics and modeling to derive actionable insights on player performance, game dynamics, and strategies.
- Create visualizations that clearly communicate insights and findings to stakeholders.

### **Tools and Technologies**
- **Data Exploration and Processing**: Python, Pandas, Numpy, Matplotlib, Seaborn
- **Data Storage**: Parquet, Azure Blob Storage
- **Data Modeling**: SQL, Star Schema Design
- **Visualization**: 3D Scatter Plots, Distribution Plots, Power BI/Tableau
- **ETL Development**: Azure Data Factory, PySpark

### **Conclusion**
The current state of the Rocket League Data Pipeline Capstone Project lays a strong foundation for advanced analytics. By focusing on data quality, efficient storage, and robust modeling, the project is well-positioned to achieve its goals of delivering actionable insights and supporting data-driven decision-making in the context of Rocket League gameplay analysis.

---

