# Write a function most_repeating_word() that takes a sequence
# of strings as input.The function should return the string that
# contains the greatest number of repeated letters.

# From text-not my solution...hey, I've been away...:)
from collections import Counter
import operator
WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']


#def most_repeating_letter_count(word):
"""Given a non-empty string, counts how many times each letter
    appears in the string, and returns an integer indicating how often
    the most common letter appears."""
    #return Counter(word).most_common(1)[0][1]
    # Counter.most_common returns a list of two-element tuples
    # (value and count) in descending order


#def most_repeating_word(words):
"""Given a list of non-empty strings (words),
    returns the word containing at least one letter that repeats
    more often than any letter in any other word.

    Because sorting in Python is stable, if multiple words have
    the same count, then the first will be returned.
    """
    # return max(words, key=most_repeating_letter_count)
    # Just as you can pass key to sorted, you can also pass it
    # max and use a different sort method.


#print(most_repeating_word(WORDS))

# Beyond the exercise:
# 1. Instead of finding the word with the greatest number of repeated letters,
# find the word with the greatest number of repeated vowels.
# From https://github.com/reuven/python-workout/blob/master/ch03-lists-tuples/e12b1_most_repeated_vowels.py


# from collections import Counter


def most_repeating_vowel_count(word):
    vowels_in_word = ''
    for one_character in word.lower():
        if one_character in 'aeiou':
            vowels_in_word += one_character

    return Counter(vowels_in_word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_vowel_count)


print(most_repeating_word(WORDS))

# 2. Write a program to read /etc/psswd on a Unix computer. The first field
# contains the username, and the final field contains the user's shell, the command
# interpreter. Display the shells in decreasing order of popularity, such that the
# most popular shell is shown first, the second most popular shell second, and so forth.
# From https://github.com/reuven/python-workout/blob/master/ch03-lists-tuples/e12b2_popular_shells.py


def shells_by_popularity(filename):

    shells = Counter(one_line.split(':')[-1].strip()
                     for one_line in open(filename)
                     if not one_line.startswith(('#', '\n')))

    return sorted(shells.items(), key=operator.itemgetter(1), reverse=True)

# 3. For an added challenge, after displaying each shell, also show the usernames
# (sorted alphabetically) who use each of those shells.
# From https://github.com/reuven/python-workout/blob/master/ch03-lists-tuples/e12b3_shells_and_users.py


from collections import defaultdict


def shells_and_users_by_popularity(filename):
    shells = defaultdict(list)
    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue

        username, *rest, shell = one_line.strip().split(':')

        shells[shell].append(username)

    return sorted(shells.items(), key=len)








