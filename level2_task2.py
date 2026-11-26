import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# Top 10 most common cuisine combinations
top_cuisines = df["Cuisines"].value_counts().head(10)

print("Top 10 Most Common Cuisine Combinations:")
print(top_cuisines)

# Average rating for each cuisine combination
avg_rating = df.groupby("Cuisines")["Aggregate rating"].mean()

# Top 10 cuisine combinations based on average rating
top_rated = avg_rating.sort_values(ascending=False).head(10)

print("\nTop 10 Cuisine Combinations by Average Rating:")
print(top_rated)