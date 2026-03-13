import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Trader Behavior Analysis",
    layout="wide"
)

st.title("📊 Trader Behavior vs Market Sentiment")

# -----------------------------
# Load Data
# -----------------------------

@st.cache_data
def load_data():
    trader = pd.read_csv("data/historical_data.csv")
    sentiment = pd.read_csv("data/fear_greed_index.csv")

    trader["Timestamp IST"] = pd.to_datetime(trader["Timestamp IST"], dayfirst=True)
    sentiment["timestamp"] = pd.to_datetime(sentiment["timestamp"], unit="s")

    trader["date"] = trader["Timestamp IST"].dt.date
    sentiment["date"] = sentiment["timestamp"].dt.date

    data = pd.merge(trader, sentiment, on="date", how="left")
    data = data.dropna(subset=["classification"])

    return data

data = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Filters")

selected_coin = st.sidebar.multiselect(
    "Select Coin",
    options=data["Coin"].unique(),
    default=data["Coin"].unique()[:10]
)

selected_sentiment = st.sidebar.multiselect(
    "Market Sentiment",
    options=data["classification"].unique(),
    default=data["classification"].unique()
)

filtered_data = data[
    (data["Coin"].isin(selected_coin)) &
    (data["classification"].isin(selected_sentiment))
]

# -----------------------------
# Metrics (Responsive)
# -----------------------------

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", f"{len(filtered_data):,}")
col2.metric("Unique Traders", filtered_data["Account"].nunique())
col3.metric("Assets Traded", filtered_data["Coin"].nunique())

# -----------------------------
# Charts Section
# -----------------------------

st.subheader("Market Insights")

chart_col1, chart_col2 = st.columns(2)

# Profit vs Sentiment
with chart_col1:
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(
        x="classification",
        y="Closed PnL",
        data=filtered_data,
        ax=ax
    )
    plt.xticks(rotation=30)
    st.pyplot(fig, use_container_width=True)

# Trade Count
with chart_col2:
    fig, ax = plt.subplots(figsize=(6,4))
    filtered_data["classification"].value_counts().plot(
        kind="bar",
        ax=ax
    )
    st.pyplot(fig, use_container_width=True)

# -----------------------------
# Buy Sell Chart
# -----------------------------

st.subheader("Buy vs Sell Behavior")

fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    x="classification",
    hue="Side",
    data=filtered_data,
    ax=ax
)

plt.xticks(rotation=30)

st.pyplot(fig, use_container_width=True)

# -----------------------------
# Tables Section
# -----------------------------

table_col1, table_col2 = st.columns(2)

# Top Traders
with table_col1:
    st.subheader("Top Traders")

    top_traders = (
        filtered_data.groupby("Account")["Closed PnL"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(top_traders, use_container_width=True)

# Top Coins
with table_col2:
    st.subheader("Most Profitable Coins")

    coin_profit = (
        filtered_data.groupby("Coin")["Closed PnL"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(coin_profit, use_container_width=True)

st.success("Dashboard Ready 🚀")