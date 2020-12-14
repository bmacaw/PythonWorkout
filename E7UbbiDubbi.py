# Write a function called ubbi_dubbi that takes a single word (string) as an argument
# and returns a string, the word's translation into Ubbi Dubbi. Example: if the
# function is called with octopus, the function will return the string uboctubopubus.
import string

def ubbi_dubbi(any_word):
    ud_translation = []
    for one_letter in any_word:
        if one_letter in 'aeiou':
            ud_translation.append(f'ub{one_letter}')
        else:
            ud_translation.append(one_letter)
    return ''.join(ud_translation)


word_1 = 'rebecca'
word_2 = 'banana'
word_3 = 'finn'
word_list = [word_1, word_2, word_3]
for word in word_list:
    print(ubbi_dubbi(word))   # Expect and get rubebubeccuba bubanubanuba fubinn

# Beyond the exercise:
# Python has str.replace() and string.translate(), but sometimes have to iterate
# over a string and append modified version of what we want.

# Handle capitalized words
def ubbi_dubbi(any_word):
    ud_translation = []
    for one_letter in any_word:
        if one_letter in 'aeiou':
            ud_translation.append(f'ub{one_letter}')
        else:
            ud_translation.append(one_letter)

    # Note: I took this part from the solution. It's slick imo
    if any_word[0] in string.ascii_uppercase:
        ud_translation[0] = ud_translation[0].capitalize()

    return ''.join(ud_translation)


word_1 = 'Rebecca'
word_2 = 'banana'
word_3 = 'Finn'
word_list = [word_1, word_2, word_3]
for word in word_list:
    print(ubbi_dubbi(word))   # Expect and get Rubebubeccuba bubanubanuba Fubinn
