import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Trader Behavior Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Trader Behavior vs Market Sentiment")

st.write(
    "Analysis of cryptocurrency trader performance using the Fear & Greed Index."
)

@st.cache_data
def load_data():
    trader = pd.read_csv("data/historical_data.csv")
    sentiment = pd.read_csv("data/fear_greed_index.csv")

    trader["Timestamp IST"] = pd.to_datetime(trader["Timestamp IST"], dayfirst=True)
    sentiment["date"] = pd.to_datetime(sentiment["date"])

    trader["date"] = trader["Timestamp IST"].dt.date
    sentiment["date"] = sentiment["date"].dt.date

    data = pd.merge(trader, sentiment, on="date", how="left")

    return data

data = load_data()

# ==============================
# Metrics
# ==============================

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(data))
col2.metric("Unique Traders", data["Account"].nunique())
col3.metric("Assets Traded", data["Coin"].nunique())

# ==============================
# Profit vs Sentiment
# ==============================

st.subheader("Average Profit by Market Sentiment")

profit = data.groupby("classification")["Closed PnL"].mean()

st.bar_chart(profit)

# ==============================
# Trades by Sentiment
# ==============================

st.subheader("Trades Distribution by Sentiment")

trade_counts = data["classification"].value_counts()

st.bar_chart(trade_counts)

# ==============================
# Buy vs Sell
# ==============================

st.subheader("Buy vs Sell Behavior")

buy_sell = pd.crosstab(data["classification"], data["Side"])

st.bar_chart(buy_sell)

# ==============================
# Top Traders
# ==============================

st.subheader("Top 10 Traders by Profit")

top_traders = (
    data.groupby("Account")["Closed PnL"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(top_traders)

# ==============================
# Top Coins
# ==============================

st.subheader("Most Profitable Coins")

top_coins = (
    data.groupby("Coin")["Closed PnL"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(top_coins)