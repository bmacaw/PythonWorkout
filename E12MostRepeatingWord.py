# Write a function most_repeating_word() that takes a sequence
# of strings as input.The function should return the string that
# contains the greatest number of repeated letters.

# From text-not my solution...hey, I've been away...:)
from collections import Counter
import operator
WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    # What letter appears the most times, and how often
    # does it appear?
    return Counter(word).most_common(1)[0][1]
    # Counter.most_common returns a list of two-element tuples
    # (value and count) in descending order


def most_repeating_word(words):
    # Just as you can pass key to sorted, you can also pass it
    # max and use a different sort method.
    return max (words, key=most_repeating_letter_count(1)[0][1])


print(most_repeating_word(WORDS))
