import pandas as pd
import numpy as np

import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

import sys


#if len(sys.argv) <= 1:
#    raise ValueError("Veuillez fournir la date au format YYYY-MM.")
#date = sys.argv[1]

def forecast_natural_gas_prices(file_path,date):
    month_forecast=int(date[:4])*12 + int(date[5:7]) - (2020*12 +10)
    number_of_day_per_month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    day_of_this_month=number_of_day_per_month[int(date[5:7])]
    day=int(date[8:]) if len(date)>8 else day_of_this_month

    df = pd.read_csv(file_path,index_col=0,parse_dates=True,date_format=lambda x: pd.to_datetime(x, format="%m/%d/%y"))

    decomposition = seasonal_decompose(df['Prices'], model='additive', period=12)
    Coeff = (decomposition.trend.dropna().iloc[-1]-decomposition.trend.dropna().iloc[-13]) / 12
    Season= decomposition.seasonal.iloc[-12:]
    P0=decomposition.trend.dropna().iloc[0]

    i = np.arange(month_forecast)
    seasonal_values = Season.values
    series = P0 + i * Coeff + seasonal_values[i % 12]
    start_date = pd.Timestamp('2020-10-01')
    dates = pd.date_range(start=start_date, periods=month_forecast, freq='ME')
    forecasted = pd.Series(series, index=dates)

    #print the last prices of the forecasted series
    #we asume linear interpolation between two months
    return ((day_of_this_month-day)/day_of_this_month)*forecasted.iloc[-2]+(day/day_of_this_month)*forecasted.iloc[-1]

print(forecast_natural_gas_prices("C:/Users/33614/Desktop/Certif/JP_Forgae/Data/Nat_Gas.csv","2022-09-30"))
