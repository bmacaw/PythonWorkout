# Write a function most_repeating_word() that takes a sequence
# of strings as input.The function should return the string that
# contains the greatest number of repeated letters.

# From text-not my solution...hey, I've been away...:)
from collections import Counter
import operator
WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    """Given a non-empty string, counts how many times each letter
    appears in the string, and returns an integer indicating how often
    the most common letter appears."""
    return Counter(word).most_common(1)[0][1]
    # Counter.most_common returns a list of two-element tuples
    # (value and count) in descending order


def most_repeating_word(words):
    """Given a list of non-empty strings (words),
    returns the word containing at least one letter that repeats
    more often than any letter in any other word.

    Because sorting in Python is stable, if multiple words have
    the same count, then the first will be returned.
    """
    return max(words, key=most_repeating_letter_count)
    # Just as you can pass key to sorted, you can also pass it
    # max and use a different sort method.


print(most_repeating_word(WORDS))
