import os
import pandas_datareader as pdr
import pandas as pd
from datetime import datetime 
import numpy as np
import requests

alpha_vantage_api = 'QO234RMNT7YYSXZ3'
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

import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"symbol":"TSLA","function":"GLOBAL_QUOTE"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "QO234RMNT7YYSXZ3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)