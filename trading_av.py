## Plan
# This is an automated system with the following functionalities;
# There should be a database having all user info, transaction info
# Authenticates a given user to get access to the system
# Asks a user what type of stock they want to analyse (Crypto, Shares, Commodities, Currencies etc)
# Rank stocks and select best 10 performing stocks at that given time
# Incase its a company, provide important financial information about that company
# Further rank stocks in a given group and select at most 5 given they've passed ranking parameters
# Ask the user whether it's a long term or short term analysis (timing)
# If short, ask the user how long they plan to be active (Proposed to have it close 2 hours to close of the market)
# Open a console / port where some chart with the required settings will run realtime
# Provide transaction report at the end of each day whether if long or short term analysis

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

stock = input("What stock do you want? :")
print("")


def rsi_dataframe(stock=stock):
    api_key = "QO234RMNT7YYSXZ3"
    period = 60
    ts = TimeSeries(key=api_key, output_format="pandas")
    data_ts = ts.get_intraday(stock.upper(), interval="1min", outputsize="full")

    ti = TechIndicators(key=api_key, output_format="pandas")
    data_ti, meta_data_ti = ti.get_rsi(
        symbol=stock.upper(), interval="1min", time_period=period, series_type="close"
    )

    df = data_ts[0][period::]
    df.index = pd.Index(map(lambda x: str(x)[:-3], df.index))
    df2 = data_ti

    total_df = pd.concat([df, df2], axis=1, sort=True)
    return print(total_df)


rsi_dataframe()
