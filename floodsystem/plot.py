import numpy as np
import matplotlib.dates as mdt
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def plot_water_levels(station, dt, levels):
   

   dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

   date_list=[]
   level_list=[]


   for date, level in zip(dates, levels):
      date_list.append(date)
      level_list.append(level)

   plt.plot(date_list, level_list)

    # Add axis labels, rotate date labels and add plot title
   plt.xlabel('date')
   plt.ylabel('water level (m)')
   plt.xticks(rotation=45)
   plt.title(station.name)

    # Display plot
   plt.tight_layout()  # This makes sure plot does not cut off date labels

   plt.show()


#Task 2F
def plot_water_level_with_fit(station, dates, levels, p):
   plt.plot(dates, levels)

   poly, d0 = polyfit(dates, levels, p)

   plt.plot(dates, poly(mdt.date2num(np.array(dates))-d0))

   plt.plot(dates, np.repeat(station.typical_range[0], len(dates)), label="Typical range low")
   plt.plot(dates, np.repeat(station.typical_range[1], len(dates)), label="Typical range high")

   plt.xlabel('date')
   plt.ylabel('water level (m)')
   plt.xticks(rotation=45)
   plt.title(station.name)
   plt.tight_layout()
   plt.show()
