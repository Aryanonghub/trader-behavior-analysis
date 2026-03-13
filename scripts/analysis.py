import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Loading datasets...")

# -----------------------
# Load datasets
# -----------------------

trader = pd.read_csv("data/historical_data.csv")
sentiment = pd.read_csv("data/fear_greed_index.csv")

# -----------------------
# Convert timestamps
# -----------------------

trader["Timestamp IST"] = pd.to_datetime(
    trader["Timestamp IST"],
    dayfirst=True
)

sentiment["timestamp"] = pd.to_datetime(
    sentiment["timestamp"],
    unit="s"
)

# -----------------------
# Extract date
# -----------------------

trader["date"] = trader["Timestamp IST"].dt.date
sentiment["date"] = sentiment["timestamp"].dt.date

# -----------------------
# Merge datasets
# -----------------------

data = pd.merge(
    trader,
    sentiment,
    on="date",
    how="left"
)

print("Merged dataset shape:", data.shape)

# -----------------------
# Remove rows without sentiment
# -----------------------

data = data.dropna(subset=["classification"])

print("\nSentiment distribution:")
print(data["classification"].value_counts())

# -----------------------
# Create results folder
# -----------------------

os.makedirs("results", exist_ok=True)

# -----------------------
# Profit vs Sentiment
# -----------------------

profit_by_sentiment = data.groupby("classification")["Closed PnL"].mean()

print("\nAverage Profit by Sentiment:")
print(profit_by_sentiment)

# -----------------------
# Visualization 1
# -----------------------

plt.figure(figsize=(8,5))

sns.boxplot(
    x="classification",
    y="Closed PnL",
    data=data
)

plt.title("Trader Profit vs Market Sentiment")
plt.xticks(rotation=30)

plt.savefig("results/profit_vs_sentiment.png")
plt.close()

# -----------------------
# Visualization 2
# -----------------------

plt.figure(figsize=(8,5))

data["classification"].value_counts().plot(kind="bar")

plt.title("Trade Count by Sentiment")

plt.savefig("results/trades_by_sentiment.png")
plt.close()

# -----------------------
# Visualization 3
# -----------------------

plt.figure(figsize=(8,5))

sns.countplot(
    x="classification",
    hue="Side",
    data=data
)

plt.title("Buy vs Sell Trades by Sentiment")
plt.xticks(rotation=30)

plt.savefig("results/buy_sell_sentiment.png")
plt.close()

# -----------------------
# Top Traders
# -----------------------

top_traders = (
    data.groupby("Account")["Closed PnL"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Traders by Profit:")
print(top_traders)

top_traders.to_csv("results/top_traders.csv")

# -----------------------
# Most Profitable Coins
# -----------------------

coin_profit = (
    data.groupby("Coin")["Closed PnL"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nMost Profitable Coins:")
print(coin_profit)

coin_profit.to_csv("results/top_coins.csv")

print("\nAnalysis complete.")
print("Charts saved in /results folder")