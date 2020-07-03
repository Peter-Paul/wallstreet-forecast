from alpha_vantage.timeseries import TimeSeries


def get_data(symbol, key, time):
    if symbol and key:
        period = time + "min"
        ts = TimeSeries(key=key, output_format="pandas")
        symbol_ts = ts.get_intraday(symbol.upper(), interval=period, outputsize="full")
        return symbol_ts[0]

    elif not symbol:
        print("No symbol was input")
    elif not key:
        print("No key was input")
