import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates, and precipitation from this file.
    dates, precipitation = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcp = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            precipitation.append(prcp)

# plot the precipitation.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.bar(dates, precipitation, width=1, alpha=0.5, color='blue')

# format plot.
ax.set_title("Daily precipitation - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (in)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()