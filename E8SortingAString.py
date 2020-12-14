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
# Output: ABCabc
#         abc
#         Cab


# Beyond the exercise
# Strings are sequences and can be put wherever other sequences (lists and tuples) can be used.
# sorted() returns a list. In order to get a string, we need to turn the resulting list back
# into a string (use str.()). str.split() and str.join() are two helpful methods to really know.
# Consider variations using str.split(), str.join() and sorted (note-my solutions are all from
# author's solutions...yeah, what a cop-out, right?

# Given the string "Tom Dick Harry," break it into individual words, and then sort those words
# alphabetically. Once they're sorted, print them with commas (,) between the names.


def sort_words(some_string):
    """Given a string containing comma-separated words, return a string with the same
    words, separated by commas, but sorted.
    """

    return ', '.join(one_word for one_word in sorted(some_string.split()))


print(sort_words('Tom Dick Harry'))  # Output: Dick, Harry, Tom


# Which is the last word alphabetically, in a text file?


def last_word_alphabetically(filename):
    """Given the name of a text file, return the word that comes last (alphabetically)
    in that file.
    """

    output = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if one_word > output:
                output = one_word
    return output


print(last_word_alphabetically('wordperlinetest.txt'))  # Output: your


# Which is the longest word in a text file?


def longest_word(filename):
    """Given the name of a text file, return the longest word
    in that file.
    """

    output = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if len(one_word) > len(output):
                output = one_word
    return output


print(longest_word("wordperlinetest.txt"))  # Output: fortunate
