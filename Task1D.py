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
    print(f"{len(listx)} stations. First 10 - [{listx[slice(10)]}]")


    dictx = stations_by_river(stations)
    print(dictx['River Aire'])
    print(dictx['River Cam'])
    print(dictx['River Thames'])




if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
