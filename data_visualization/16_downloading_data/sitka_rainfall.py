from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('16_downloading_data/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# print(header_row)

# Extract dates, and high and low temperatures.
dates, pcrp = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        pcrpd = float(row[5])
    except:
        print("Error in data.")
    else:
        dates.append(current_date)
        pcrp.append(pcrpd)

# print(highs)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, pcrp, color='blue', alpha=0.5)

# Format plot.
ax.set_title('Daily rainfall amount, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Amount of water', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()