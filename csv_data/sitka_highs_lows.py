import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

# plot the high temperatures.
print(plt.style.available)
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates,highs, c='red', alpha=0.5)
ax.plot(dates,lows, c='blue', alpha=0.5)
# shading between the high and low temperatures. This is a patch between the two lines.
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot.
ax.set_title("Daily high and low temperatures, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # automatically adjust the position of the date labels to avoid overlap
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()