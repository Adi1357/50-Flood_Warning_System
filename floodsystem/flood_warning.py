import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.dates as mdt
from floodsystem.analysis import polyfit


#Task 2G
def flood_warning(station,days):
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=days))
        poly, d0 = polyfit(dates, levels, 5)
        latest_gradient = poly.deriv(m=1)(mdt.date2num(dates[-1]) - d0)
        return latest_gradient





def consistent(stations, dt):
   

    
    consistent_list = []
    for station in stations:

        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        date_list=[]
        level_list=[]

        for date, level in zip(dates, levels):
            date_list.append(date)
            level_list.append(level)
            if all(v is not None or 0 for v in level_list) and all(x is not None or 0 for x in date_list):
                consistent_list.append(station)
    return consistent_list


     
def flood_warning_rel(station, dt):
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        date_list=[]
        level_list=[]

        for date, level in zip(dates, levels):
            date_list.append(date)
            level_list.append(level)

        sum_level = 0
        counter = 0
        sum_level = sum(list(level_list))


        counter += 1

        avg = sum_level/counter

        if avg >= station.typical_range[1]:
            return 'Severe risk'

        if avg >= 0.9*station.typical_range[1] and avg < station.typical_range[1]:
            return 'High risk'

        if avg <= station.typical_range[1] and avg >= station.typical_range[0]:
            return 'Moderate risk'
        else:
            return 'Low risk'

