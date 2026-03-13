Here is a complete README.md in pure Markdown that you can copy-paste directly into your repo.

# 📊 Trader Behavior vs Market Sentiment Analysis

## Overview

This project analyzes the relationship between **cryptocurrency trader performance** and **market sentiment** using the **Bitcoin Fear & Greed Index** combined with **historical trading data from Hyperliquid**.

The goal is to identify patterns between trader profitability and market sentiment and uncover insights that can help design smarter trading strategies.

This project includes:

- Data analysis using Python
- Visual insights into trader behavior
- Profitability analysis across market sentiment regimes
- An interactive **Streamlit dashboard** for exploring results

---

# 🎯 Project Objective

Financial markets are strongly influenced by trader sentiment. This project investigates:

- How trader profitability varies during **Fear vs Greed markets**
- Trading activity patterns across sentiment regimes
- Which assets produce the **highest trading profits**
- Buy vs Sell behavior during different market conditions
- Distribution of profits among traders

Understanding these patterns can help improve **trading strategies**, **risk management**, and **market analysis tools**.

---

# 📂 Dataset Description

## 1️⃣ Historical Trader Data

This dataset contains trading records from **Hyperliquid**.

### Key Columns

| Column | Description |
|------|-------------|
| Account | Trader wallet address |
| Coin | Cryptocurrency traded |
| Execution Price | Price at which trade executed |
| Size Tokens | Quantity traded |
| Size USD | Trade value in USD |
| Side | Buy or Sell |
| Timestamp IST | Trade timestamp |
| Closed PnL | Profit or Loss from trade |

---

## 2️⃣ Bitcoin Fear & Greed Index

This dataset represents market sentiment based on a score from **0–100**.

Sentiment categories include:

- Extreme Fear
- Fear
- Neutral
- Greed
- Extreme Greed

The sentiment index helps analyze how traders behave under different market conditions.

---

# ⚙️ Methodology

The analysis pipeline follows these steps:

1. Load trader and sentiment datasets
2. Convert timestamps into datetime format
3. Extract trading dates
4. Merge trading data with sentiment data using date
5. Clean the dataset and remove missing values
6. Perform sentiment-based analysis of trader behavior
7. Generate visual insights

---

# 📊 Key Analyses

## Profit vs Market Sentiment

This analysis examines how trader profitability changes across different sentiment regimes.

Visualization used:

- Boxplot of **Closed PnL vs Market Sentiment**

---

## Trading Activity vs Sentiment

Measures how many trades occur during each sentiment regime.

Visualization used:

- Bar chart of **trade count by sentiment**

---

## Buy vs Sell Behavior

Analyzes whether traders prefer long or short positions during different market conditions.

Visualization used:

- Buy vs Sell distribution by sentiment

---

## Top Traders

Identifies traders generating the **highest total profit**.

---

## Most Profitable Coins

Identifies assets generating the **largest cumulative profit**.

---

# 🔍 Key Insights

Important findings from the analysis:

- **Extreme Greed markets produced the highest average profit per trade**
- **Fear markets generated the highest trading activity**
- Major crypto assets such as **SOL, ETH, and BTC dominated profitable trades**
- A small number of traders generated a **large share of total profits**

These patterns indicate that **market sentiment significantly influences trading behavior and profitability**.

---

# 🖥 Interactive Dashboard

The project includes an interactive **Streamlit dashboard** that allows users to explore the results.

Dashboard features:

- Dataset overview metrics
- Profit vs sentiment visualization
- Trading activity charts
- Buy vs Sell analysis
- Top trader leaderboard
- Most profitable coins

---

# 📁 Project Structure


trader-behavior-analysis
│
├── data
│ ├── historical_data.csv
│ └── fear_greed_index.csv
│
├── scripts
│ └── analysis.py
│
├── results
│ ├── profit_vs_sentiment.png
│ ├── trades_by_sentiment.png
│ ├── buy_sell_sentiment.png
│ ├── top_traders.csv
│ └── top_coins.csv
│
├── app.py
├── requirements.txt
└── README.md


---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository


git clone https://github.com/YOUR_USERNAME/trader-behavior-analysis

cd trader-behavior-analysis


---

## 2️⃣ Create Conda Environment


conda create -n trader_analysis python=3.10
conda activate trader_analysis


---

## 3️⃣ Install Dependencies


pip install -r requirements.txt


---

## 4️⃣ Run Data Analysis


python scripts/analysis.py


This will generate charts and results inside the **results/** folder.

---

## 5️⃣ Run the Dashboard


streamlit run app.py


The dashboard will open at:


http://localhost:8501


---

# 📈 Future Improvements

Potential extensions for this project:

- Trader **win-rate analysis** across sentiment regimes
- Risk-adjusted performance metrics
- Time-series analysis of sentiment impact
- Machine learning models to predict trader profitability
- Real-time sentiment monitoring dashboard

---

# 👨‍💻 Author

**Aryan Kumar Poddar**

B.Tech Computer Science & Engineering  
Galgotias University