import matplotlib.pyplot as plt

x_values = [x+1 for x in range(5000)]
y_values = [x*x*x for x in x_values]

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, s=10, c=y_values, cmap=plt.cm.plasma)

# set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# plt.show()
plt.savefig('cubes_plot.png')#, bbox_inches='tight')
