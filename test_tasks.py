import sys
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

stations = build_station_list()


    
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)


test_station_1 = MonitoringStation(station_id= "test_station_1", measure_id = "measure_station_1", label = "some station_1", coord= (1.0, 2.0), typical_range = (-2.3, 3.4445), river = "River 1", town= "My Town_1")
test_station_2 = MonitoringStation(station_id= "test_station_2", measure_id = "measure_station_2", label = "some station_2", coord= (2.0, 3.0), typical_range = (-12.3, 45.45), river = "River 2", town= "My Town_2")
test_station_3 = MonitoringStation(station_id= "test_station_3", measure_id = "measure_station_3", label = "some station_3", coord= (3.0, 4.0), typical_range = (-0.3, 4.5), river = "River 3", town= "My Town_3")
test_station_4 = MonitoringStation(station_id= "test_station_4", measure_id = "measure_station_4", label = "some station_4", coord= (4.0, 5.0), typical_range = (-1.3, 4.45), river = "River 4", town= "My Town_4")

test_list= (test_station_1, test_station_2, test_station_3, test_station_4)
#Test 1B
def test_stations_by_distance():
    test_list_1B = stations_by_distance(test_list, (1,1))
    assert test_list_1B[0][0:2] == ("some station_1","My Town_1")
    assert test_list_1B[1][0:2] == ("some station_2","My Town_2")
    assert test_list_1B[2][0:2] == ("some station_3","My Town_3")

#Test 1D
def test_rivers_with_station():
    test_rivers_list = rivers_with_station(test_list)
    assert test_rivers_list == ['River 1', 'River 2', 'River 3', 'River 4']

def test_stations_by_river():
    test_dic= stations_by_river(test_list)
    assert test_dic['River 1'] == ['some station_1']
    assert test_dic['River 2'] == ['some station_2']
    assert test_dic['River 3'] == ['some station_3']

#Test 1F

def test_inconsistent_typical_range_stations():
    test_inconsistentx_list = inconsistent_typical_range_stations(test_list)
    assert test_inconsistentx_list == []






def test_1C():
    assert len(stations_within_radius(stations, (0, 0), 40000)) == len(stations)



def test_1E():
    assert len(rivers_by_station_number(stations, 9)) == 9

