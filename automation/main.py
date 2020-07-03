import os
import symbol_data as sd
import settings
import indicators.trend as tnd
import timer

stock = input("Enter stock symbol you want?:")
time_range = input("Intraday (I), Daily (D), Weekly (W), Monthly (M)? :")
time = str(input("Enter digit to use for time interval (1, 5, 30, 60)? :"))
settings.putkey()
key = str(os.getenv("A_V_KEY"))

def run_trend():
	return tnd.get_trend(stock, key, time, "close")
# data = sd.get_data(stock,key,time)
timer.set_interval(run_trend, (int(time) * 60))
# print(p_t)
