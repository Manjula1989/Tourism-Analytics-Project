# Tourism Experience Analytics: Classification, Prediction, and Recommendation System

## Project Overview
This project analyzes tourism data to provide personalized recommendations, predict user satisfaction, and classify potential user behavior. It leverages **Python and Streamlit** for data preprocessing, visualization, and interactive reporting.

**Skills Gained:** Data Cleaning & Preprocessing, Exploratory Data Analysis (EDA), Data Visualization, SQL, Streamlit, Machine Learning (Regression, Classification, Recommendation).

**Domain:** Tourism

---

## Problem Statement
Tourism agencies and travel platforms aim to enhance user experiences by leveraging data to provide personalized recommendations, predict satisfaction, and classify potential user behavior. The project covers three objectives:

1. **Regression:** Predict attraction ratings based on user and attraction data.  
2. **Classification:** Predict user visit mode (Business, Family, Couples, Friends, etc.).  
3. **Recommendations:** Suggest attractions based on user preferences and similar users’ data.  

---

## Dataset Description

- **Transaction Data:** User visits to attractions with ratings and visit details.  
- **User Data:** User demographics including continent, country, region, and city.  
- **City Data:** City details to link users and attractions.  
- **Attraction Type Data:** Type of tourist attraction (e.g., Beach, Museum).  
- **Visit Mode Data:** Types of visit modes (Business, Family, Couples, Friends).  
- **Country, Region, Continent Data:** Linking users and attractions geographically.  
- **Item Data:** Attractions with city, type, and address details.  

---

## Features

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Visualizations using Matplotlib & Seaborn  
- Regression, Classification & Recommendation Models  
- Streamlit App for interactive user predictions and recommendations  

---

## Run the Streamlit App

1. Clone the repository:
```bash
git clone https://github.com/Manjula1989/Tourism-Analytics-Project.git
cd Tourism-Analytics-Project
pip install -r requirements.txt
streamlit run tourism_app.py


http://localhost:8501

Note: Large model files (e.g., rf_rating_model.pkl and rf_visitmode_model.pkl) are not included in this repository due to GitHub file size limits. You can generate them locally using the provided scripts (insights_charts.py or model training scripts).


Tourism-Analytics-Project/
│
├── tourism_app.py          # Streamlit application
├── insights_charts.py      # Generates charts for EDA
├── cleaned_tourism_data.csv
├── README.md
├── requirements.txt
└── other supporting files



