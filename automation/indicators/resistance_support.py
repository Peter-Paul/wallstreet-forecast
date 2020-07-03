import numpy as np
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas as pd

result = []
counts = []
def get_support_resistance(data):
    all_data = []
    for x in data:
        all_data.append( [ x, data.count(x)] )
        counts.append(data.count(x))
    unrepeated = []
    for x in all_data:
        if x not in unrepeated:
            unrepeated.append(x)
    sorted_result = sorted(unrepeated, key = lambda i: i[1], reverse=True)
    arr = np.array(sorted_result)

    for x in list(arr):
        if x[1] > np.quantile(np.array(counts), 0.8):
            result.append(x)
    return result

def r_s_levels(data):
    for x in range(4):
        get_support_resistance(data.take([2], axis=1).to_numpy())
        
