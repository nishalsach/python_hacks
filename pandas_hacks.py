#############    LAMBDA FUNCTION ON PANDAS ROWS    #############

# Define function
def some_function(row, arg1, arg2):
    return row.some_col * 2


# Create a new columns
df['new_col'] = df.apply(some_function,
						 args=(arg1, arg2),
                         axis=1)

#############   FILTER ROWS BY CONTENTS OF LIST-TYPE COLUMNS   #############

# Example of DataFrame
#   molecule            species
# 0        a              [dog]
# 1        b       [horse, pig]
# 2        c         [cat, dog]
# 3        d  [cat, horse, pig]
# 4        e     [chicken, pig]

# List of items you want to be contained in the list
selection = ['cat', 'dog']

# Solution #1
mask = df.species.apply(lambda x: any(item for item in selection if item in x))
df1 = df[mask]

# Solution #2
df[pd.DataFrame(df.species.tolist()).isin(selection).any(1)]



############# PRINT DATAFRAME TO PDF #############

# SOURCE: https://stackoverflow.com/questions/33155776/export-pandas-dataframe-into-a-pdf-file-using-python
# More hacks in the answers here, hopefully prettier ones. Should try them out sometime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

df = pd.DataFrame(np.random.random((10,3)), columns = ("col 1", "col 2", "col 3"))

#https://stackoverflow.com/questions/32137396/how-do-i-plot-only-a-table-in-matplotlib
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')

#https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
pp = PdfPages("foo.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()

