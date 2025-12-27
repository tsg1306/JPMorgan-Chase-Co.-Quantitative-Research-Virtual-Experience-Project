# JP Morgan Chase & Co. - Software Engineering Job Simulation

This repository contains my completed work for the JP Morgan Chase & Co. Software Engineering Job Simulation on Forage. The project demonstrates the application of quantitative finance, machine learning, and data engineering to solve industry-specific challenges.

## 📜 Certificate
**[View My Completion Certificate](https://www.theforage.com/completion-certificates/Sj7temL583QAYpHXD/bWqaecPDbYAwSDqJy_Sj7temL583QAYpHXD_69496db46607d700f0a906b2_1766525186332_completion_certificate.pdf)**

---

## 🎓 Key Learning Outcomes

* **Quantitative Finance**: Developed a deep understanding of how to price complex financial instruments like storage contracts using Net Present Value (NPV).
* **Time Series Analysis**: Learned to isolate seasonal patterns and trends from commodity price data to make informed market predictions.
* **Advanced Machine Learning**: Mastered gradient boosting techniques with **XGBoost** and focused on the importance of feature engineering and mutual information over automated pipelines.
* **Optimization Strategies**: Applied algorithmic thinking to credit scoring, moving from simple grouping to statistical optimization using Log-Likelihood and search algorithms.

---

## 🚀 Project Sections

### 1. Natural Gas Price Prediction 📈
**Objective**: Forecast natural gas prices to assist in trading and storage decisions.

* **Methodology**: Utilized `statsmodels` for **Seasonal Decomposition** to isolate the trend, seasonality, and residuals in 4 years of historical price data.
* **Implementation**: Developed a forecasting model to predict future price points based on identified monthly cyclical patterns.
* **Skills**: Time series analysis, statistical modeling, and data visualization.

---

### 2. Commodity Storage Contract Pricing 💰
**Objective**: Build a robust pricing engine for natural gas storage contracts.

* **Methodology**: Modeled a comprehensive financial framework considering injection/withdrawal schedules, storage capacity limits, and daily accrual costs.
* **Logic**: Calculated the Net Present Value (NPV) by integrating price forecasts with logistical constraints and the time value of money.
* **Skills**: Financial engineering, derivatives pricing, and decision algorithms.

---

### 3. Credit Risk Analysis 🎯
**Objective**: Predict loan default probabilities and quantify expected financial losses.

* **Model**: Implemented an **XGBoost Classifier** to handle complex non-linear relationships in the borrower data.
* **Feature Engineering**: Instead of standard pipelines, I focused on manual feature mapping, specifically calculating **debt-over-income ratios** to maximize **Mutual Information** between features and the target variable.
* **Evaluation**: Validated model performance using **Confusion Matrices** to meticulously track precision and recall for default cases.
* **Skills**: Supervised learning, risk management, and feature optimization.

---

### 4. FICO Score Bucketing & Optimization 📊
**Objective**: Create a rating system by segmenting FICO scores into discrete, optimized buckets.

* **Methodology**: Developed a custom **Log-Likelihood** objective function to measure the quality of the score segmentation.
* **Optimization**: Employed a **Brute Force** search algorithm to identify the exact boundaries that maximize the statistical significance of each credit bucket.
* **Skills**: Statistical optimization, credit scoring methodologies, and algorithmic problem solving.

---

## 🛠️ Technical Stack

* **Language**: Python
* **Machine Learning**: XGBoost, Scikit-learn (Mutual Information, Confusion Matrix)
* **Time Series**: Statsmodels (Seasonal Decomposition)
* **Data Analysis**: Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn

---

## 📂 Project Structure

```text
.
├── Natural Gas Prediction/      # Seasonal decomposition and forecasting
├── Commodity Storage/          # Storage contract pricing logic
├── Credit Risk Analysis/       # XGBoost model and engineered features
└── Bucket FICO scores/         # Log-likelihood optimization scripts
