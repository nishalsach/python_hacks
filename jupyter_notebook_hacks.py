
#############   CHANGE VIEW OPTIONS FOR GIVEN CELL IN JUPYTER NOTEBOOK #############

with pd.option_context("display.min_rows", 50, "display.max_rows", 100, "display.max_columns", 5, 'display.max_colwidth', -1):
    display(df)

############# STORE JUPYER NOTEBOOK NAME FOR FOLDER CREATION ETC. #############

# Store the name of the current jupyter notebook in a variable nbk_name 

%%javascript
IPython.notebook.kernel.execute('nbk_name = "' + IPython.notebook.notebook_name + '"')

# OR

%%javascript
IPython.notebook.kernel.execute(`nbk_name = '${window.document.getElementById("notebook_name").innerHTML}'`);

### You can later use this to create a folder named for this notebook for data dumps etc.

# Create directory to store files from this python notebook
save_path = '../'+nbk_name+'/'

print(save_path)

if not os.path.exists(save_path):
    os.makedirs(save_path)

############# MODIFY CELL OUTPUT BEHAVIOUR #############

# Display variables in the output for a cell anywhere they're mentioned (i.e., you don't need them to be on the last line)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

## To set this behaviour for all instances of Jupyter (Notebook and Console), simply create a file ~/.ipython/profile_default/ipython_config.py with the lines below.

## c = get_config()

## # Run all nodes interactively
## c.InteractiveShell.ast_node_interactivity = "all"


############# RUN CODE FROM CHOSEN .PY/.IPYNB FILE #############

# Run all code from a chosen python file/ipynb by using a magic command - %run

# Execute and show the output from all code cells of the specified .py/.ipynb file
%run ./some_file.ipynb


############# GLOBAL VARIABLES IN A NOTEBOOK #############

# List all global variables in a notebook

%who <INSERT VARIABLE TYPE (OPTIONAL ARGUMENT)>

############# HIGH RESOLUTION PLOTS FOR MACBOOK SCREEN #############

# High res plot outputs for Macbook Retina models

%config InlineBackend.figure_format ='retina'

#####################


