import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import os

# -----------------------------
# File paths
# -----------------------------
DATA_PATH = r"D:\internship project\Tourism dataset\cleaned_tourism_data_final.csv"
RATING_MODEL_PATH = r"D:\internship project\Tourism dataset\rf_rating_model.pkl"
VISIT_MODEL_PATH = r"D:\internship project\Tourism dataset\rf_visitmode_model.pkl"

# -----------------------------
# Load & clean data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, low_memory=False)

    # Fill numeric columns with median
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        df[col].fillna(df[col].median(), inplace=True)

    # Fill categorical columns with mode
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Feature Engineering
    df['UserAvgRating'] = df.groupby('UserId')['Rating'].transform('mean')
    df['AttractionAvgRating'] = df.groupby('Attraction')['Rating'].transform('mean')
    df['VisitYearMonth'] = df['VisitYear'].astype(str) + '-' + df['VisitMonth'].astype(str)

    # Encode categorical columns for models
    le = LabelEncoder()
    for col in ['AttractionType', 'VisitMode', 'Continent', 'Country']:
        if col in df.columns:
            df[col] = le.fit_transform(df[col])

    return df

# -----------------------------
# Load models
# -----------------------------
@st.cache_resource
def load_models():
    rating_model = joblib.load(RATING_MODEL_PATH)
    visit_model = joblib.load(VISIT_MODEL_PATH)
    return rating_model, visit_model

# -----------------------------
# Load everything
# -----------------------------
df = load_data()
rating_model, visit_model = load_models()

valid_users = df['UserId'].unique()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🌍 Tourism Experience Analytics")

# 1️⃣ Explore Data
st.subheader("1️⃣ Explore Data")
st.dataframe(df.head())
st.markdown("### 📊 Dataset Summary")
st.write("👤 Total Users:", df["UserId"].nunique())
st.write("🏛️ Total Attractions:", df["Attraction"].nunique())
st.write("⭐ Average Rating:", round(df["Rating"].mean(), 2))

# 2️⃣ Predict Ratings & Visit Mode
st.subheader("2️⃣ Predict Ratings & Visit Mode")
user_id = st.selectbox("Select UserId:", valid_users)

if st.button("Predict"):
    st.write(f"⭐ Predictions for User {user_id}...")
    try:
        user_data = df[df['UserId'] == user_id].copy()
        if user_data.empty:
            st.warning("No data found for this user.")
        else:
            # Rating Prediction
            rating_features = user_data[['VisitYear', 'VisitMonth', 'UserAvgRating', 'AttractionAvgRating']]
            rating_pred = rating_model.predict(rating_features)

            # Visit Mode Prediction
            visit_features = user_data[['VisitYear', 'VisitMonth', 'UserAvgRating', 'AttractionAvgRating', 'AttractionType']].copy()
            visit_pred = visit_model.predict(visit_features)

            st.write("✅ Predicted Ratings (first 10):", rating_pred[:10])
            st.write("✅ Predicted Visit Modes (first 10):", visit_pred[:10])
    except Exception as e:
        st.error(f"Prediction failed ⚠️: {e}")

# 3️⃣ Top Attractions Overall
st.subheader("3️⃣ Top Attractions Overall")
top_attractions = df.groupby("Attraction")["Rating"].mean().sort_values(ascending=False).head(10)
st.markdown("🏆 **Top 10 Attractions**")
for attraction, rating in top_attractions.items():
    st.write(f"⭐ {attraction} — Avg Rating: {round(rating,2)}")

# 4️⃣ Personalized Recommendations
st.subheader("4️⃣ Personalized Recommendations")
try:
    user_ratings = df[df['UserId']==user_id][['Attraction','Rating']].copy()
    if user_ratings.empty:
        st.info("No personalized recommendations available for this user.")
    else:
        top_recommendations = user_ratings.sort_values(by='Rating', ascending=False).head(5)
        st.markdown("🎯 Recommended Attractions for You:")
        for _, row in top_recommendations.iterrows():
            st.write(f"⭐ {row['Attraction']} — Your Rating: {round(row['Rating'],2)}")
except Exception as e:
    st.error(f"Recommendation failed ⚠️: {e}")
