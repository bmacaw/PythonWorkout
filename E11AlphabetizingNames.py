# Write a function alphabetizing_names() that assumes the existence of a PEOPLE
# constant defined as shown (example p. 40 text). The function should return a list of
# dicts, but sorted by last name and then by first name.

# Author's solution (b/c I haven't practiced python in a while :D)
import operator

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Holly', 'last': 'Black', 'email': 'holly@blackholly.com'},
          {'first': 'Ernest', 'last': 'Cline', 'email': 'ernest@readyplayertwo.com'}
          ]


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))


print(alphabetize_names(PEOPLE))