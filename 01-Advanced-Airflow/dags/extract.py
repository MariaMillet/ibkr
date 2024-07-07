import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

AIRFLOW_HOME = os.getenv("AIRFLOW_HOME")

from ib_insync import *
import pandas as pd

# Connect to TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

# Request account summary
account_summary = ib.accountSummary()

# Display account summary
for item in account_summary:
    print(f"{item.tag}: {item.value}")

# Request portfolio positions
portfolio = ib.positions()

# Display portfolio positions
for position in portfolio:
    print(f"{position.contract.symbol} {position.position} {position.marketPrice} {position.marketValue}")

# Assuming we have a function to calculate portfolio risk metrics
def calculate_portfolio_risk(positions):
    # Placeholder function for risk calculation
    # You can implement specific risk calculations based on your requirements
    risk_metrics = {}
    for position in positions:
        # Example: Calculating a simple exposure metric
        risk_metrics[position.contract.symbol] = position.marketValue
    return risk_metrics

# Calculate and display portfolio risk metrics
risk_metrics = calculate_portfolio_risk(portfolio)
for symbol, risk in risk_metrics.items():
    print(f"Risk for {symbol}: {risk}")

# Disconnect
ib.disconnect()

# with DAG(
#     "extract",
#     default_args={"depends_on_past": True},
#     start_date=datetime(2021, 6, 1),
#     end_date=datetime(2021, 12, 31),
#     schedule_interval="@monthly",
# ) as dag:
#     object_name = "yellow_tripdata_" + "{{ ds[:7] }}.parquet"
#     trip_data_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{object_name}"
#     filename = f"{AIRFLOW_HOME}/data/bronze/{object_name}"

#     curl_trip_data_task = BashOperator(
#         task_id="curl_trip_data",
#         bash_command=f"curl {trip_data_url} > {filename}",
#     )

#     curl_trip_data_task
