import sys
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.station import inconsistent_typical_range_stations


stations = build_station_list()

def test_1B():
    assert len(stations_by_distance(stations, (1,1))) == len(stations)

def test_1D():
    assert len(rivers_with_station(stations)) < len(stations)
    assert type(stations_by_river(stations)) == dict

def test_1F():
    assert  len(inconsistent_typical_range_stations(stations)) <= len(stations)

