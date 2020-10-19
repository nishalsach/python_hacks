## Stack Link: https://stackoverflow.com/questions/33381330/histogram-with-boxplot-above-in-python

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")

x = np.random.randn(100)

f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, 
                                    gridspec_kw={"height_ratios": (.15, .85)})

sns.boxplot(x, ax=ax_box)
sns.distplot(x, ax=ax_hist)

ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
