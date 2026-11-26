import pandas as pd

# Dataset load cheyyadam
df = pd.read_csv("Dataset.csv")

# City-wise restaurant count
city_count = df["City"].value_counts()

print("City with Highest Number of Restaurants:")
print(city_count.head(1))
# Average rating for each city
average_rating = df.groupby("City")["Aggregate rating"].mean()

print("\nAverage Rating of Each City:")
print(average_rating)