from ib_insync import *
import pandas as pd

# Connect to TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)  # Port 7497 for TWS, 4002 for IB Gateway

# Define the contract for gold futures
contract = Future(symbol='GC', lastTradeDateOrContractMonth='202408', exchange='COMEX', currency='USD')

# Request historical market data for the last 6 months
endDateTime = ''
durationStr = '6 M'
barSizeSetting = '1 day'
whatToShow = 'TRADES'
useRTH = True
formatDate = 1

historical_data = ib.reqHistoricalData(
    contract,
    endDateTime=endDateTime,
    durationStr=durationStr,
    barSizeSetting=barSizeSetting,
    whatToShow=whatToShow,
    useRTH=useRTH,
    formatDate=formatDate
)

# Convert historical data to DataFrame
df = util.df(historical_data)

# Print the historical market data
print(df)

# Disconnect
ib.disconnect()
