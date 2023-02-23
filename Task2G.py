from floodsystem.flood_warning import flood_warning  
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)

    print(flood_warning(stations, 10))
    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    print("PRINTING CURRENT GRADIENTS OF WATER LEVEL CURVE FOR ALL STATIONS")
    run()
    