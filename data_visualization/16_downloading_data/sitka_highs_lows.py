from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('16_downloading_data/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

tmin_index = header_row.index('TMIN')
tmax_index = header_row.index('TMAX')
station_name = ''

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# print(header_row)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    if not station_name:
        station_name = row[1].title()
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[tmax_index])
    low = int(row[tmin_index])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# print(highs)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_ylim([0, 140])

# Format plot.
ax.set_title(f'Daily high and low temperatures\n{station_name}, 2021', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
# ax.get_yscale()
ax.tick_params(labelsize=16)

plt.show()