import json

# Opening JSON file
with open('data.json',) as f:
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
  