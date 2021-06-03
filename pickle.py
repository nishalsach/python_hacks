import pickle

# Dumping
mylist = ['a', 'b', 'c', 'd']
with open('datafile.pkl', 'wb') as fh:
   pickle.dump(mylist, fh)

# Opening
with open('datafile.pkl', 'rb') as fh:
    mylist = pickle.load(fh)