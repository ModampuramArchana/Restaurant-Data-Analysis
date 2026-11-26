import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Restaurants in each city
city_count = df["City"].value_counts().head(10)

print("Top 10 Cities with Most Restaurants:")
print(city_count)

# Bar chart
plt.figure(figsize=(10,5))
city_count.plot(kind="bar")
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()