# insights_charts.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path
file_path = r"D:\internship project\Tourism dataset\cleaned_tourism_data.csv"

# Load cleaned data
df = pd.read_csv(file_path)

# Fill missing Ratings with the average
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())

# Set Seaborn style
sns.set(style="whitegrid")

# ------------------------------
# Top 10 Cities by Number of Visits
# ------------------------------
plt.figure(figsize=(10,5))
top_cities = df['CityName'].value_counts().head(10)
sns.barplot(x=top_cities.index, y=top_cities.values, palette="viridis")
plt.title("Top 10 Cities by Number of Visits")
plt.xticks(rotation=45)
plt.ylabel("Number of Visits")
plt.tight_layout()
plt.savefig("TopCitiesVisits.png")
plt.show()

# ------------------------------
# Top 10 Cities by Average Rating
# ------------------------------
plt.figure(figsize=(10,5))
avg_rating = df.groupby('CityName')['Rating'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=avg_rating.index, y=avg_rating.values, palette="magma")
plt.title("Top 10 Cities by Average Rating")
plt.xticks(rotation=45)
plt.ylabel("Average Rating")
plt.tight_layout()
plt.savefig("TopCitiesRating.png")
plt.show()

# ------------------------------
# Top 10 Attraction Types
# ------------------------------
plt.figure(figsize=(10,5))
top_attractions = df['AttractionType'].value_counts().head(10)
sns.barplot(x=top_attractions.values, y=top_attractions.index, palette="coolwarm")
plt.title("Top 10 Attraction Types")
plt.xlabel("Count")
plt.ylabel("Attraction Type")
plt.tight_layout()
plt.savefig("TopAttractions.png")
plt.show()

# ------------------------------
# Visits per Year
# ------------------------------
plt.figure(figsize=(10,5))
visits_year = df['VisitYear'].value_counts().sort_index()
sns.lineplot(x=visits_year.index, y=visits_year.values, marker="o")
plt.title("Visits per Year")
plt.xlabel("Year")
plt.ylabel("Number of Visits")
plt.tight_layout()
plt.savefig("VisitsPerYear.png")
plt.show()

# ------------------------------
# Visits per Month
# ------------------------------
plt.figure(figsize=(10,5))
visits_month = df['VisitMonth'].value_counts().sort_index()
sns.lineplot(x=visits_month.index, y=visits_month.values, marker="o")
plt.title("Visits per Month")
plt.xlabel("Month")
plt.ylabel("Number of Visits")
plt.tight_layout()
plt.savefig("VisitsPerMonth.png")
plt.show()

print("✅ All Insights and Charts Completed! Charts saved as PNG files in your project folder.")
