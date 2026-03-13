import pandas as pd
import os

print("Loading datasets...")

trader = pd.read_csv("data/historical_data.csv")
sentiment = pd.read_csv("data/fear_greed_index.csv")

trader["Timestamp IST"] = pd.to_datetime(trader["Timestamp IST"], dayfirst=True)
sentiment["date"] = pd.to_datetime(sentiment["date"])

trader["date"] = trader["Timestamp IST"].dt.date
sentiment["date"] = sentiment["date"].dt.date

data = pd.merge(trader, sentiment, on="date", how="left")

print("Merged dataset shape:", data.shape)

profit_by_sentiment = data.groupby("classification")["Closed PnL"].mean()

print("\nAverage Profit by Sentiment:")
print(profit_by_sentiment)

top_traders = (
    data.groupby("Account")["Closed PnL"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Traders:")
print(top_traders)

top_coins = (
    data.groupby("Coin")["Closed PnL"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Coins:")
print(top_coins)

os.makedirs("results", exist_ok=True)

top_traders.to_csv("results/top_traders.csv")
top_coins.to_csv("results/top_coins.csv")

print("\nAnalysis complete.")