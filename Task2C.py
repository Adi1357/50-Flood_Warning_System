# Task2C
# Jasper Hersov
# 12/02/2023

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)

    for stat in stations_highest_rel_level(stations, 10):
        print(stat[0],stat[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()