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