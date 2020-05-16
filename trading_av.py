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
