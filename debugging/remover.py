import pdb


def remove_vowels(string):
    """ Returns the string without vowels
    """
    vowels = 'aeiou'
    new_string = ''
    for char in string:
        if char not in vowels:
            pdb.set_trace()
            new_string = new_string + char
    return new_string


print(remove_vowels('developer'))
