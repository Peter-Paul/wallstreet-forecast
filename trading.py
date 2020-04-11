import os
import pandas_datareader as pdr
import pandas as pd
from datetime import datetime 
import numpy as np
import requests
headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=f54e98af5e545e54292c91e9f9bbd5c654056a7a", headers=headers)
print(requestResponse.json())


os.environ["TIINGO_API_KEY"] = "f54e98af5e545e54292c91e9f9bbd5c654056a7a"
os.environ["QUANDL_API_KEY"] = "Wp9YzVgMWtnktXfdKA9Q"
start = datetime(2018, 9,1)
end  = datetime(2019,9,1)
tesla = pdr.get_data_tiingo('TSLA', api_key=os.getenv(
    'TIINGO_API_KEY'), start=start, end=end)
# apple = pdr.get_data_quandl('TSLA', api_key=os.getenv('QUANDL_API_KEY'), start= datetime(2018, 4, 10), end = datetime(2018, 4,11))
for v in tesla.values[0:3]:
    data = v[0:1]
