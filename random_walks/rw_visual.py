from random_walk import RandomWalk
from matplotlib import pyplot as plt
from plotly import offline
from plotly.graph_objects import Layout, Scatter

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk using matplotlib.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # # Emphasize the first and last points.
    # ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    # Plot the points in the walk using plotly.
    my_layout = Layout(title='Random Walk', xaxis={'visible': False}, yaxis={'visible': False})
    data = Scatter(x=rw.x_values, y=rw.y_values)
    offline.plot({'data': data, 'layout': my_layout}, filename='random_walk.html')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
