# Pathlib stuff


##########  MAKING DIRECTORIES WHEN THEY DON'T EXIST ##############s
if not os.path.isdir(abstracts_destination):
    print('The directory is not present. Creating a new one.')
    os.mkdir(abstracts_destination)