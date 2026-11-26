import pandas as pd
import matplotlib.pyplot as plt

# Dataset load cheyyadam
df = pd.read_csv("Dataset.csv")

# Price Range count
price_count = df["Price range"].value_counts().sort_index()

print("Price Range Distribution:")
print(price_count)

# Bar Graph
plt.bar(price_count.index, price_count.values)
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.show()