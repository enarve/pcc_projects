import plotly.express as px

from die import Die

# Create two D8.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in list.
times_to_roll = 100000
results = []
for roll_num in range(times_to_roll):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# print(results)

# Visualize the results
title = f"Results of Rolling two D8 dice {times_to_roll} Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)
fig.show()