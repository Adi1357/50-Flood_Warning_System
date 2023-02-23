import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.dates as mdt
from floodsystem.analysis import polyfit


#Task 2G
def flood_warning(stations,days):
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=days))
        poly, d0 = polyfit(dates, levels, 5)
        latest_gradient = poly.deriv(m=1)(mdt.date2num(dates[-1]) - d0)
        print(latest_gradient)
        

