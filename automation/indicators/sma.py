from alpha_vantage.techindicators import TechIndicators


def get_sma(symbol, key, time, t_p ,s_type):
    if symbol and key:
        period = time + "min"
        ti = TechIndicators(key=key, output_format="pandas")
        symbol_ti = ti.get_sma(
            symbol.upper(), interval=period, time_period=int(t_p), series_type=s_type
        )
        return list(symbol_ti[0]["SMA"].to_numpy())
