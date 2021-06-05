########## FLATTEN LISTS OS LISTS #############


# Flatten list of lists - https://stackoverflow.com/questions/11264684/flatten-list-of-lists
list_of_lists = [[180.0], [173.8], [164.2], [156.5], [147.2], [138.2]]
flattened = [val for sublist in list_of_lists for val in sublist]




########## CO-OCCURRENCE IN LISTS OF LISTS #############


# A Hack for a problem I seem to encounter deceny regularly

'''
I have a list of lists like :

names =  [['cat', 'fish'], ['cat'], ['fish', 'dog', 'cat'],
 ['cat', 'bird', 'fish'], ['fish', 'bird']]

I want to count number of times that each pair of names mentioned together in the whole list and the output would be like:

{ ['cat', 'fish']: 3, ['cat', 'dog']: 1,['cat','bird']:1
 ['fish','dog'] : 1, ['fish','bird']:2} 

Source: https://stackoverflow.com/questions/42272311/python-co-occurrence-of-two-items-in-different-lists

'''
#### Solution ####

def listOccurences(item, names):
    # item is the list that you want to check, eg. ['cat','fish']
    # names contain the list of list you have.
    set_of_items = set(item) # set(['cat','fish'])
    count = 0
    for value in names:
        if set_of_items & set(value) == set_of_items:
            count+=1
    return count

names =  [['cat', 'fish'], ['cat'], ['fish', 'dog', 'cat'],['cat', 'bird', 'fish'], ['fish', 'bird']]

# Now for each of your possibilities which you can generate
# Chain flattens the list, set removes duplicates, and combinations generates all possible pairs.
permuted_values = list(itertools.combinations(set(itertools.chain.from_iterable(names)), 2))
d = {}
for v in permuted_values:
    d[str(v)] = listOccurences(v, names)
# The key in the dict being a list cannot be possible unless it's converted to a string.
print(d)