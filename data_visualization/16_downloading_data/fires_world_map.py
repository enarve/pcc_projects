from pathlib import Path
import csv

import plotly.express as px

# Read data.
path = Path('16_downloading_data/eq_data/world_fires_1_day.csv')
contents = path.read_text(encoding='utf-8')
rows = csv.reader(contents.splitlines())

# Examine all fires in the dataset.
mags, lons, lats, eq_titles = [], [], [], []
next(rows)
for row in rows:
    try:
        mags.append(float(row[2]))
        lons.append(float(row[1]))
        lats.append(float(row[0]))
    except:
        print("Error.")

title = "World Fires"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='agsunset',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     )
fig.show()