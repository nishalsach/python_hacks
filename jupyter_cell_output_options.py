#############   CHANGE VIEW OPTIONS FOR GIVEN CELL IN JUPYTER NOTEBOOK #############

with pd.option_context("display.min_rows", 50, "display.max_rows", 100, "display.max_columns", 5, 'display.max_colwidth', -1):
    display(df)



############# MODIFY CELL OUTPUT BEHAVIOUR #############

# Display variables in the output for a cell anywhere they're mentioned (i.e., you don't need them to be on the last line)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

## To set this behaviour for all instances of Jupyter (Notebook and Console), simply create a file ~/.ipython/profile_default/ipython_config.py with the lines below.

## c = get_config()

## # Run all nodes interactively
## c.InteractiveShell.ast_node_interactivity = "all"


############# HIGH RESOLUTION PLOTS FOR MACBOOK SCREEN #############

# High res plot outputs for Macbook Retina models

%config InlineBackend.figure_format ='retina'

#####################