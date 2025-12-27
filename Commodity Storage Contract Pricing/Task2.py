from Task1 import forecast_natural_gas_prices

import pandas as pd
import numpy as np

def pricing_natural_gas_storage(injection_date, withdraw_date, injection_rate, withdraw_rate, storage_capacity, storage_cost_per_MMBtu_per_day):
    injection=np.array([injection_rate for i in range(storage_capacity//injection_rate)]+[storage_capacity%injection_rate])
    withdraw=np.array([storage_capacity%withdraw_rate]+[withdraw_rate for i in range(storage_capacity//withdraw_rate)])
    injection_days=len(injection)
    withdraw_days=len(withdraw)
    total_days=(withdraw_date>injection_date) * ((pd.to_datetime(withdraw_date)-pd.to_datetime(injection_date)).days)

    #Calcul des différents couts et revenus
    injection_costs=np.array([forecast_natural_gas_prices("C:/Users/33614/Desktop/Certif/JP_Forgae/Data/Nat_Gas.csv",(pd.to_datetime(injection_date)+pd.Timedelta(days=i)).strftime("%Y-%m-%d"))*injection[i] for i in range(injection_days)])
    withdraw_revenues=np.array([forecast_natural_gas_prices("C:/Users/33614/Desktop/Certif/JP_Forgae/Data/Nat_Gas.csv",(pd.to_datetime(withdraw_date)-pd.Timedelta(days=withdraw_days-1-i)).strftime("%Y-%m-%d"))*withdraw[i] for i in range(withdraw_days)])
    full_storage_costs=[storage_cost_per_MMBtu_per_day*storage_capacity for i in range(total_days-injection_days-withdraw_days)]
    injection_storage_costs=[storage_cost_per_MMBtu_per_day*sum(injection[:i+1]) for i in range(injection_days)]
    withdraw_storage_costs=[storage_cost_per_MMBtu_per_day*(storage_capacity - sum(withdraw[:i+1])) for i in range(withdraw_days)]
    storage_costs=np.array(full_storage_costs + injection_storage_costs + withdraw_storage_costs)

    injection_cost=sum(injection_costs)
    withdraw_revenue=sum(withdraw_revenues)
    storage_cost=sum(storage_costs)
    total_profit=withdraw_revenue - injection_cost - storage_cost

    return total_profit

#Example d'usage 1
profit1=pricing_natural_gas_storage(
    injection_date="2023-06-13",  # date d'injection au format YYYY-MM-DD
    withdraw_date="2024-01-28",  # date de retrait au format YYYY-MM-DD
    injection_rate=100000,  # volume d'injection en MMBtu/jour
    withdraw_rate=200000,  # volume de retrait en MMBtu/jour
    storage_capacity=1150000,  # capacité de stockage en MMBtu
    storage_cost_per_MMBtu_per_day=0.0032  # coût de stockage par MMBtu par jour
)
print(f"Total profit from natural gas storage operation: {profit1} $")
print("Parameters used:")
print(f"  Injection date: {"2023-06-13"}")
print(f"  Withdraw date: {"2024-01-28"}")
print(f"  Injection rate: {100000} MMBtu/day")
print(f"  Withdraw rate: {200000} MMBtu/day")
print(f"  Storage capacity: {1150000} MMBtu")
print(f"  Storage cost per MMBtu per day: ${0.0032}")

#Example d'usage 2
profit2=pricing_natural_gas_storage(
    injection_date="2023-05-23",  # date d'injection au format YYYY-MM-DD
    withdraw_date="2023-12-30",  # date de retrait au format YYYY-MM-DD
    injection_rate=100000,  # volume d'injection en MMBtu/jour
    withdraw_rate=200000,  # volume de retrait en MMBtu/jour
    storage_capacity=1150000,  # capacité de stockage en MMBtu
    storage_cost_per_MMBtu_per_day=0.0032  # coût de stockage par MMBtu par jour
)
print(f"Total profit from natural gas storage operation: {profit2} $")
print("Parameters used:")
print(f"  Injection date: {"2023-05-23"}")
print(f"  Withdraw date: {"2023-12-30"}")
print(f"  Injection rate: {100000} MMBtu/day")
print(f"  Withdraw rate: {200000} MMBtu/day")
print(f"  Storage capacity: {1150000} MMBtu")
print(f"  Storage cost per MMBtu per day: ${0.0032}")

#Example d'usage 3
profit3=pricing_natural_gas_storage(
    injection_date="2023-07-01",  # date d'injection au format YYYY-MM-DD
    withdraw_date="2024-02-15",  # date de retrait au format YYYY-MM-DD
    injection_rate=150000,  # volume d'injection en MMBtu/jour
    withdraw_rate=150000,  # volume de retrait en MMBtu/jour
    storage_capacity=900000,  # capacité de stockage en MMBtu
    storage_cost_per_MMBtu_per_day=0.0070  # coût de stockage par MMBtu par jour
)
print(f"Total profit from natural gas storage operation: {profit3} $")
print("Parameters used:")
print(f"  Injection date: {"2023-07-01"}")
print(f"  Withdraw date: {"2024-02-15"}")
print(f"  Injection rate: {150000} MMBtu/day")
print(f"  Withdraw rate: {150000} MMBtu/day")
print(f"  Storage capacity: {900000} MMBtu")
print(f"  Storage cost per MMBtu per day: ${0.0070}")
