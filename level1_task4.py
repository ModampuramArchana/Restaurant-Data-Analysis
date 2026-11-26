import pandas as pd

# Dataset load cheyyadam
df = pd.read_csv("Dataset.csv")

# Online Delivery percentage
online_delivery = df["Has Online delivery"].value_counts()

total_restaurants = len(df)

yes_percentage = (online_delivery["Yes"] / total_restaurants) * 100
no_percentage = (online_delivery["No"] / total_restaurants) * 100

print("Percentage of Restaurants with Online Delivery")
print(f"Yes : {yes_percentage:.2f}%")
print(f"No  : {no_percentage:.2f}%")

# Average Rating Comparison
average_rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()

print("\nAverage Rating:")
print(average_rating)