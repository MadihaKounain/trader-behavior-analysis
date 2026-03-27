# 📊 Trader Behavior vs Market Sentiment Analysis

## 📌 Objective

This project analyzes the relationship between trader performance and market sentiment (Fear vs Greed) using historical trading data.

---

## 📂 Datasets Used

* Historical Trader Data (Hyperliquid)
* Bitcoin Fear & Greed Index

---

## ⚙️ Approach

### 1. Data Preprocessing

* Cleaned column names
* Converted timestamps to datetime
* Extracted date for merging
* Merged datasets on common date

### 2. Feature Engineering

* Created profit indicator (`is_profit`)
* Categorized trade sizes (`size_category`)
* Derived risk proxy using trade size

### 3. Analysis Performed

* Profitability vs Market Sentiment
* Win Rate vs Sentiment
* Trade Size Behavior
* Profit Distribution Analysis

---

## 📊 Key Insights

* Traders tend to take larger and riskier trades during **Greed** phases
* More cautious behavior is observed during **Fear** periods
* Profitability varies significantly across sentiment conditions
* Trade success rates indicate behavioral bias influenced by market psychology

---

## 📈 Visualizations

* Profit vs Sentiment
* Win Rate vs Sentiment
* Trade Size Distribution
* Profit Distribution

(All charts saved in `/outputs/charts/`)

---

## 🛠 Tools & Technologies

* Python
* Pandas
* Matplotlib
* Seaborn

---

## 🚀 Conclusion

Market sentiment plays a significant role in influencing trader behavior and performance.
Understanding these patterns can help design smarter and more adaptive trading strategies.

---

## 📁 Project Structure

```
trader-behavior-analysis/
│── data/
│── notebooks/
│── src/
│── outputs/
│── README.md
```

---

## 📬 Submission

This project demonstrates data analysis, feature engineering, and insight generation for real-world trading data.
