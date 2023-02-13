import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():


    #Build list of stations
     stations = build_station_list()
     station_list = stations_highest_rel_level(stations,5)

     for station in station_list:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        date_list=[]
        level_list=[]
        for date, level in zip(dates, levels):
            date_list.append(date)
            level_list.append(level)
        
        plot_water_levels(station,10, level_list)
    
    # # Station name to find
    # station_name = "Cam"

    # # Find station
    # station_cam = None
    # for station in stations:
    #     if station.name == station_name:
    #         station_cam = station
    #         break

    # # Check that station could be found. Return if not found.
    # if not station_cam:
    #     print("Station {} could not be found".format(station_name))
    #     return

    # dt = 2
    # dates, levels = fetch_measure_levels(
    #     station_cam.measure_id, dt=datetime.timedelta(days=dt))

    # # Print level history
    # for date, level in zip(dates, levels):
    #     print(date, level)

    # plot_water_levels(,,dt,)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
