# JP Morgan Chase & Co. - Software Engineering Job Simulation

This repository contains my completed work for the JP Morgan Chase & Co. Software Engineering Job Simulation on Forage. The project demonstrates the application of quantitative finance, machine learning, and data engineering to solve industry-specific challenges.

## 📜 Certificate
**[View My Completion Certificate](https://www.theforage.com/completion-certificates/Sj7temL583QAYpHXD/bWqaecPDbYAwSDqJy_Sj7temL583QAYpHXD_69496db46607d700f0a906b2_1766525186332_completion_certificate.pdf)**

---

## 🚀 Project Overview

### 1. Natural Gas Price Prediction
* **Objective**: Forecast natural gas prices to assist in trading and storage decisions.
* **Methodology**: 
    * Utilized `statsmodels` for **Seasonal Decomposition** to isolate trend, seasonality, and residuals in historical price data.
    * Developed a forecasting model to predict future price points based on identified cyclical patterns.
* **Key Skills**: Time series analysis, statistical modeling with `statsmodels`.

### 2. Commodity Storage Contract Pricing
* **Objective**: Build a pricing engine for natural gas storage contracts.
* **Methodology**: 
    * Modeled injection/withdrawal schedules, storage limits, and daily costs.
    * Calculated the Net Present Value (NPV) of contracts by integrating market price forecasts and logistical constraints.
* **Key Skills**: Financial derivatives pricing, contract valuation.

### 3. Credit Risk Analysis (Machine Learning)
* **Objective**: Predict loan default probabilities to estimate expected financial losses.
* **Methodology**: 
    * **Model**: Implemented an **XGBoost Classifier** for gradient-boosted decision trees.
    * **Feature Engineering**: Mapped and engineered new features (e.g., loan-to-income and debt-to-income ratios) to maximize **Mutual Information** and improve model predictive power.
    * **Evaluation**: Assessed model performance using **Confusion Matrices** to analyze Type I and Type II errors.
* **Key Skills**: Supervised learning, feature engineering, risk quantification.

### 4. FICO Score Bucketing & Optimization
* **Objective**: Create an optimized rating system by segmenting FICO scores into discrete buckets.
* **Methodology**: 
    * Developed a custom **Log-Likelihood** function to evaluate the quality of score segmentation.
    * Employed a **Brute Force** optimization approach to identify the boundaries that maximize the log-likelihood across buckets.
* **Key Skills**: Statistical optimization, credit scoring, algorithmic problem solving.

---

## 🛠️ Technical Stack

* **Language**: Python
* **Machine Learning**: XGBoost, Scikit-learn
* **Time Series**: Statsmodels
* **Data Analysis**: Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn

---

## 📂 Project Structure

```text
.
├── Natural Gas Prediction/      # Seasonal decomposition and price forecasting
├── Commodity Storage/          # Storage contract pricing engine
├── Credit Risk Analysis/       # XGBoost model and feature engineering
└── Bucket FICO scores/         # Log-likelihood optimization scripts
