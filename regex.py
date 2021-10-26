def camel_case_split(some_string):

    '''
    
    Parameters:
    -----------
    some_string: Cmel Cased string

    Returns: 
    -----------
    some_string, with words separated by spaces

    '''
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', some_string)
    return ' '.join([m.group(0) for m in matches])