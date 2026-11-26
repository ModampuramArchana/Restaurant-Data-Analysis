import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# Restaurant chains (same restaurant name appearing more than once)
chains = df["Restaurant Name"].value_counts()
chains = chains[chains > 1]

print("Top 10 Restaurant Chains:")
print(chains.head(10))

# Average rating of restaurant chains
chain_ratings = df.groupby("Restaurant Name")["Aggregate rating"].mean()
print("\nTop 10 Chains by Average Rating:")
print(chain_ratings.loc[chains.index].sort_values(ascending=False).head(10))

# Average votes (popularity) of restaurant chains
chain_votes = df.groupby("Restaurant Name")["Votes"].mean()
print("\nTop 10 Chains by Average Votes:")
print(chain_votes.loc[chains.index].sort_values(ascending=False).head(10))