def find_needle(haystack):
    
    i=0
    while i < len(haystack):
        if haystack[i] == 'needle':
            return f'found the needle at position {i}'
        i += 1         


find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])