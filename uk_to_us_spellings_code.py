# Code written to reproduce and repurpose what I already found online at:
    # https://stackoverflow.com/questions/42329766/python-nlp-british-english-vs-american-english
    # https://gist.github.com/rcortini/0d05417339bc74300ce3a971442a4d3c
    # https://github.com/hyperreality/American-British-English-Translator/blob/master/data/british_spellings.json

    # Credits to the creators of those SO answer and the dictionary!


######### OPTION 1: Use online version of the data #########

import requests

def americanize(string):
    url ="https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/british_spellings.json"
    british_to_american_dict = requests.get(url).json()    

    for british_spelling, american_spelling in british_to_american.items():
        string = string.replace(british_spelling, american_spelling)
  
    return string

def britishize(string):
    url ="https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/american_spellings.json"
    american_to_british_dict = requests.get(url).json()    

    for american_spelling, british_spelling in american_to_british.items():
        string = string.replace(american_spelling, british_spelling)
  
    return string


######### OPTION 2: Use local version of the data #########

# Read in the JSON from wherever it is locally
def replace_all(text, mydict):
    for gb, us in mydict.items():
        text = text.replace(us, gb)
    return text

# Example 
gb_text = "I realise I can see the world in colour but I can't vocalise its splendour"
us_text = replace_all(gb_text, us2gb)



