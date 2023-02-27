# Task2C
# Jasper Hersov
# 18/02/2023

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
     stations = build_station_list()
     update_water_levels(stations)

     station_list = stations_highest_rel_level(stations, 5)

     for station in station_list:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        
        plot_water_level_with_fit(station, dates, levels, 4)


 
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()