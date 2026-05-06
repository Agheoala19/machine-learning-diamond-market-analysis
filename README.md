# Diamond Market Econometric Analysis & Prediction System

## Overview
This project is an advanced, interactive web application built with **Python** and **Streamlit**. It is designed to perform econometric analysis, statistical processing, and machine learning predictions on the diamond market. By integrating multiple analytical modules, the application transforms raw dataset records into actionable business and economic insights.

## Key Features
* **Interactive Web Dashboard**: A user-friendly interface built with Streamlit, organized logically into tabs for different analytical stages.
* **Data Preprocessing & EDA**: Automated handling of missing values, outlier detection (using IQR), feature scaling, and categorical encoding.
* **Statistical & Visual Analysis**: Descriptive statistics, group-by operations, correlation heatmaps, and distribution histograms using Seaborn and Matplotlib.
* **Geospatial Analysis**: Cartographic representation of key economic and logistics hubs (e.g., Antwerp, Mumbai, New York) using **GeoPandas** and Shapely.
* **Machine Learning & Econometrics**:
    * **Clustering**: Automatic product portfolio segmentation using the **K-Means** algorithm.
    * **Multiple Regression**: Ordinary Least Squares (OLS) models via **Statsmodels** to analyze the impact of physical characteristics on diamond prices.
    * **Classification**: **Logistic Regression** to classify diamonds into different value/price categories, complete with accuracy scores and classification reports.

## Tech Stack
* **Programming Language**: Python 3.x
* **Web Framework**: Streamlit
* **Data Manipulation**: Pandas, NumPy
* **Machine Learning**: Scikit-learn, Statsmodels
* **Geospatial Analysis**: GeoPandas, Shapely
* **Data Visualization**: Matplotlib, Seaborn

## Project Structure
├── app.py                     # Main Streamlit application
├── preprocessing.py           # Data cleaning, scaling, and encoding functions
├── statistics_module.py       # Descriptive statistics and aggregation logic
├── visualization_module.py    # Plotting functions (histograms, correlation matrices)
├── clustering_module.py       # K-Means clustering implementation
├── regression_module.py       # OLS and Logistic Regression models
├── geo_module.py              # Geospatial mapping and plotting
├── data.csv                   # Dataset sample (1000 records for optimal performance)
└── README.md                  # Project documentation

## Business Value & Context
This project was developed to demonstrate end-to-end data science capabilities—from raw data ingestion to deploying a functional application. It addresses real-world economic challenges such as pricing strategy optimization, market segmentation, and spatial distribution tracking of assets.
