import csv

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        date = row[2]
        dates.append(date)

print(highs)
