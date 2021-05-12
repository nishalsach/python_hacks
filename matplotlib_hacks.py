######### 1. Lines for Custom Legends  #########

# Can be modified to dots too

from matplotlib.lines import Line2D

custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])


########## 2. MPL Configs ###############

# mpl config to make sure grid is always behind the plot
plt.rcParams['axes.axisbelow'] = True
