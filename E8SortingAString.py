import string

# Write a function strsort(), that takes a single string as its input and returns a string.
# The returned string should contain the same characters as the input, except that its
# characters should be sorted in order, from the lowest Unicode value to the highest Unicode
# value. Example: strsort('cba') => ('abc').


def strsort(one_string):
    # From solution (hey, i'm tired :D)
    return ''.join(sorted(one_string))


str_1 = 'ABCabc'
str_2 = 'cba'
str_3 = 'Cba'
list_o_strings = [str_1, str_2, str_3]
for string in list_o_strings:
    print(strsort(string))


# Beyond the exercise
# Strings are sequences and can be put wherever other sequences (lists and tuples) can be used.
# sorted() returns a list. In order to get a string, we need to turn the resulting list back
# into a string (use str.()). str.split() and str.join() are two helpful methods to really know.
# Consider variations using str.split(), str.join() and sorted:

# TODO:Given the string "Tom Dick Harry," break it into individual words, and then sort those words
# alphabetically. Once they're sorted, print them with commas (,) between the names.


# TODO:Which is the last word alphabetically, in a text file?


# TODO:Which is the longest word in a text file?