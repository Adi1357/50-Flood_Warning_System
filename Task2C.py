# Task2C
# Jasper Hersov
# 12/02/2023

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    station_list = stations_highest_rel_level(stations, 10)
    

    for station in station_list:
         print(station.name,station.relative_water_level())

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
    