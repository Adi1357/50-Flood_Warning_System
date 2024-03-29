# Task1C
# Jasper Hersov
# 01/02/2023

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    stations_within_10km_of_Cam_city_centre = stations_within_radius(stations, (52.2053, 0.1218), 10)

    print(sorted(stations_within_10km_of_Cam_city_centre))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()