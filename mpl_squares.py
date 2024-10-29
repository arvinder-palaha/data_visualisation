import matplotlib.pyplot as plt

input_values = [x+1 for x in range(5)]
squares = [x*x for x in input_values]

print(plt.style.available)
plt.style.use('seaborn-v0_8-paper')
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
