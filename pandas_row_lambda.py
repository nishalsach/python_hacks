# Define function
def some_function(row, arg1, arg2):
    return row.some_col * 2


# Create a new columns
df['new_col'] = df.apply(some_function,
						 args=(arg1, arg2),
                         axis=1)