# Flatten list of lists - https://stackoverflow.com/questions/11264684/flatten-list-of-lists
list_of_lists = [[180.0], [173.8], [164.2], [156.5], [147.2], [138.2]]
flattened = [val for sublist in list_of_lists for val in sublist]