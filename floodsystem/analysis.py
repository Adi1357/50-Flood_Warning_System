# Analysis
# 18/02/2023

import numpy as np
import matplotlib.dates as mdt

def polyfit(dates, levels, p):
    x = mdt.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)
    return poly, x[0]



  


