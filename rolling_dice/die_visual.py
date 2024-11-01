from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline
from matplotlib import pyplot as plt

# Create two dice.
die_1 = Die(6)
die_2 = Die(6)
# die_3 = Die(6)

# Make some rolls, and store the results in a list.
results = [die_1.roll() * die_2.roll() for _ in range(100_000)]

# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# Visualize the results using plotly.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 100,000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_times.html')

# Visualise the results using matplotlib.
fig, ax = plt.subplots(figsize=(12, 4))
ax.bar(x_values, frequencies)
ax.set_title('Results of rolling two D6 100,000 times')
ax.set_xlabel('Result')
ax.set_ylabel('Frequency of Result')
ax.yaxis.grid(True)
for i, v in enumerate(frequencies):
    if v > 0:
        ax.text(x_values[i], v, str(v), ha='center', va='bottom')
plt.show()