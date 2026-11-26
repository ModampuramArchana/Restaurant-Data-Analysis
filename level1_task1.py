import pandas as pd

df = pd.read_csv("Dataset.csv")

# Top 3 cuisines
top_cuisines = df["Cuisines"].value_counts().head(3)

print("Top 3 Cuisines:")
print(top_cuisines)
# Percentage of Top 3 Cuisines

total_restaurants = len(df)

print("\nPercentage of Top 3 Cuisines:")

for cuisine, count in top_cuisines.items():
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine}: {percentage:.2f}%")