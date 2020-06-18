import os
import symbol_data as sd
import settings

stock = input("Enter stock symbol you want?:")
time_range = input("Intraday (I), Daily (D), Weekly (W), Monthly (M)? :")
time = input("Enter digit to use for time interval (1, 5, 30, 60)? :") 
settings.putkey()
data = sd.get_data(stock,str(os.getenv('A_V_KEY')),str(time))

print(data)