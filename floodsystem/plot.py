import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):
   
   dt = 10
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