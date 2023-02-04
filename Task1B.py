# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""
    stations = build_station_list()
    listx = stations_by_distance(stations, (52.2053, 0.1218))
    print(f'The first 10 elements are :{listx[:10]}')
    print(f'The last 10 elements are : {listx[-10:]}')

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IB Flood Warning System ***")
    run()

