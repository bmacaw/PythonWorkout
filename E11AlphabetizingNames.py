# Write a function alphabetizing_names() that assumes the existence of a PEOPLE
# constant defined as shown (example p. 40 text). The function should return a list of
# dicts, but sorted by last name and then by first name.

# All author's solutions (b/c I haven't practiced python in a while :D)
import operator

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Holly', 'last': 'Black', 'email': 'holly@blackholly.com'},
          {'first': 'Ernest', 'last': 'Cline', 'email': 'ernest@readyplayertwo.com'}
          ]


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))


print(alphabetize_names(PEOPLE))

# Beyond the Exercise
# Given a sequence of positive and negative numbers, sort them by absolute value.


def sort_absolute(numbers):
    """Given an iterable of numbers, return
    a list of those numbers sorted by absolute value.
    """
    return sorted(numbers, key=abs)


num_list_1 = [-2, 3, -1]
num_list_2 = [-.0003, -.003, .03]
print(sort_absolute(num_list_1))
print(sort_absolute(num_list_2))


# Given a list of strings, sort them according to how many vowels they contain.


def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total


def sort_by_vowel_count(words):
    """Given a list of strings(words), return
    a list of those words sorted by the number of vowels they contain.
    """
    return sorted(words, key=by_vowel_count)


word_list_1 = ['finn', 'rebecca', 'peak']
print(sort_by_vowel_count(word_list_1))


# Given a list of lists, with each list containing zero or more numbers, sort by
# the sum of each inner list's numbers.


def sort_by_sum(list_of_lists):
    """Given a list of lists, in which the inner lists contain
    numbers, return the outer list sorted by each inner list's sum.
    """

    return sorted(list_of_lists, key=sum)


lol_1 = [[1, 2, 3], [4, 5, 6], [-7, -8, -9]]
print(sort_by_sum(lol_1))
