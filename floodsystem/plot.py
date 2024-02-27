import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import numpy as np
import matplotlib.dates as mdates



def plot_water_levels(station, dates, levels):
    typical_low = station.typical_range[0]
    typical_high = station.typical_range[1]


    plt.plot(levels,dates)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

    
def plot_water_level_with_fit(station, dates, levels, p):
    y0 = levels
    y1 = np.polyfit(mdates.date2num(dates), y0, p)
    polynomial_fit = np.poly1d(y1)
    date_range = np.linspace(mdates.date2num(min(dates)), mdates.date2num(max(dates)), 1000)
    plt.plot(dates, y0, label='Original data', color='blue')
    plt.plot(mdates.num2date(date_range), polynomial_fit(date_range), label=f'Polynomial fit to degree {p}', color='red')
    plt.xlabel("Dates")
    plt.ylabel("Water level")
    plt.legend()
    plt.title(station.name)
    plt.show()