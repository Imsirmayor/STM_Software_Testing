# Exercise: Conditional Statements, Loops, Functions, Maps

# Implement a function called "char_frequency()" which counts the frequency
# of characters in a given string.

def char_frequency(str):
    """Count the frequency of characters in a given string and return this statistics in a Map""" 
    pass 


# Verify implementation

s = "This is a simple string."
expected = {'a': 1, ' ': 4, 'e': 1, 'g': 1, 'i': 4, 'h': 1, 'm': 1, 'l': 1, 'n': 1, 'p': 1, 's': 4, 'r': 1, 'T': 1, '.': 1, 't': 1}
actual = char_frequency(s)
assert expected == actual