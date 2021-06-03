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

########## 2. Categorical Variable to Colours ###############

# x, y, and category_values should all be the same length (the # of data points)

import matplotlib.pyplot as plt
from matplotlib.cm import viridis

num_categories = len(set(category_values))

colors = [viridis(float(i)/num_categories) for i in category_values]


#### OR

# If your categorical variable takes str values

categorical_version = df['colname'].astype('category').cat.codes

num_categories = len(set(categorical_version))
colors = [viridis(float(i)/num_categories) for i in categorical_version]

# Now pass for plotting
plt.scatter(x=df.culmen_length_mm,
            y=df.culmen_depth_mm,
            c=colors)
