#### LAMBDA FUNCTION ON PANDAS ROWS

# Define function
def some_function(row, arg1, arg2):
    return row.some_col * 2


# Create a new columns
df['new_col'] = df.apply(some_function,
						 args=(arg1, arg2),
                         axis=1)

#### FILTER ROWS BY CONTENTS OF LIST-TYPE COLUMNS

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

