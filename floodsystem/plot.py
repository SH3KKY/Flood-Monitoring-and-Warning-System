import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import datetime



def plot_water_levels(station, dates, levels):
    typical_low = station.typical_range[0]
    typical_high = station.typical_range[1]


    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


# Unfortunately github codespaces doesn't show matplotlib figures so i can't really do the rest of this... lets hope it works