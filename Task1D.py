# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    listx= rivers_with_station(stations)
    print(f"{len(listx)} stations. First 10 - [{listx[slice(10)]}]\n")


    dictx = stations_by_river(stations)
    print(f"The dictionary for the River Aire {dictx['River Aire']}\n")
    print(f"The dictionary for the River Cam {dictx['River Cam']}\n")
    print(f"The dictionary for the River Thames {dictx['River Thames']}\n")




if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
