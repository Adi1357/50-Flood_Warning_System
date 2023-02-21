# Analysis
# 18/02/2023
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)
    return poly, x[0]

def flood_warning(stations,dt):
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        date_list=[]
        level_list=[]

        for date, level in zip(dates, levels):
            date_list.append(date)
            level_list.append(level)
        
        sum_level = 0
        counter = 0
        sum_level = sum(list(level_list))

        #for i in level_list:
           # sum += level_list[i]
        counter += 1

        avg = sum_level/counter

        if avg >= station.typical_range[1]:
            print(station.name, 'Severe risk')

        if avg >= 0.9*station.typical_range[1] and avg < station.typical_range[1]:
            print(station.name, 'High risk')
        
        if avg <= station.typical_range[1] and avg >= station.typical_range[0]:
            print(station.name, 'Moderate risk')


        else:
            print(station.name, 'Low risk')


