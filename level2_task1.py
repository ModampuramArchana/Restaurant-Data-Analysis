import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Plot distribution of aggregate ratings
plt.figure(figsize=(8,5))
plt.hist(df["Aggregate rating"], bins=10, edgecolor="black")
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.show()

# Most common rating
most_common_rating = df["Aggregate rating"].mode()[0]
print("Most Common Rating:", most_common_rating)

# Average number of votes
average_votes = df["Votes"].mean()
print("Average Number of Votes:", round(average_votes, 2))