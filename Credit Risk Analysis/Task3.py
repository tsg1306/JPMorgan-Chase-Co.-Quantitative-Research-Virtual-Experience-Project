import numpy as np
import pandas as pd

import sklearn
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


def predict_default(credit_lines_outstanding, loan_amt_outstanding, total_debt_outstanding, income, years_employed, fico_score):
    df=pd.read_csv("C:/Users/33614/Desktop/Certif/JP_Forgae/Data/Task 3 and 4_Loan_Data.csv",index_col=0)

    X=df.copy()
    X['loan_to_income']=X['loan_amt_outstanding']/X['income']
    y=X.pop("default")

    # Define the model
    model = XGBRegressor(n_estimators=10000, learning_rate=0.001, n_jobs=2) # Your code here

    # Fit the model
    model.fit(X, y) # Your code here

    sample = pd.DataFrame({
        "credit_lines_outstanding": [credit_lines_outstanding],
        "loan_amt_outstanding": [loan_amt_outstanding],
        "total_debt_outstanding": [total_debt_outstanding],
        "income": [income],
        "years_employed": [years_employed],
        "fico_score": [fico_score],
        "loan_to_income": [loan_amt_outstanding/income if income != 0 else 0]
    })

    sample_prob = model.predict(sample)
    return min(1,max(0, sample_prob[0]))

#Example usage 1:
probability = predict_default(5, 20000, 15000, 60000, 10, 700)
print("Predicted probability of default:", probability)