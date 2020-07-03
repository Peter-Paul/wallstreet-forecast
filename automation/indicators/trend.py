import indicators.sma as sma
import symbol_data
import pandas as pd

trend = None

def get_trend(symbol, key, time, s_type):
	price = list(symbol_data.get_data(symbol, key, time)["4. close"].to_numpy())[:100]
	price.reverse()
	sma_time = str(5)
	if time == str(1):
		sma_time = str(5)
	elif time == str(5):
		sma_time = str(30)
	elif time == str(30):
		sma_time = str(60)

	trend_50 = sma.get_sma(symbol, key, sma_time, 50 ,s_type)[-100: ]
	trend_20 = sma.get_sma(symbol, key, sma_time, 20, s_type)[-100: ]


	if price[-1] < (trend_20[-1] and trend_50[-1]):
		trend = "up"
		print("We are in a down_trend!")
	elif price[-1] == (trend_20[-1] and trend_50[-1]):
		trend = "equilibrium"
		print("We are about to change trend!")
	elif price[-1] > (trend_20[-1] and trend_50[-1]):
		trend = "down"
		print("We are in an up_trend!")
	else:
		print("No trend")

# def draw_trend_line(data, trend):
# 	if trend == "up":
# 	elif trend == "down":
# 	else:

	
