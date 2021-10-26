# Pathlib stuff
import pathlib

##########  MAKING DIRECTORIES WHEN THEY DON'T EXIST ##############s
if not os.path.isdir(abstracts_destination):
    print('The directory is not present. Creating a new one.')
    os.mkdir(abstracts_destination)

##########  FIND LATEST FILE WITH REGEX PATTERN ##############
folder_path = pathlib.Path('Documents/ProjectName')
list_of_paths = folder_path.glob('*mypattern.csv');      
latest_path = max(list_of_paths, key=lambda p: p.stat().st_ctime)
# Now open with pathlib