# Write a Python function (pig_latin) that takes a string as input,
# assumed to be an English word. The function should return the
# translation of this word into Pig Latin.

def pig_latin(english_word_string):
    vowels = 'a', 'e', 'i', 'o', 'u'
    if english_word_string[0] in vowels:
        return english_word_string + 'way'
    else:
        return english_word_string[1:-1] + english_word_string[0].lower() + 'ay'


word_1 = 'Finn'
word_2 = 'airport'
word_3 = 'puppy'
word_4 = 'equine'
print(pig_latin(word_1))
print(pig_latin(word_2))
print(pig_latin(word_3))
print(pig_latin(word_4))

# Beyond the exercise:
# Handle capitalized words


def pig_latin(english_word_string):
    vowels = 'aeiouAEIOU'
    all_caps = english_word_string.upper()
    if english_word_string[0] in vowels:
        if english_word_string == all_caps:
            translation = english_word_string + 'WAY'
        elif english_word_string[0] == english_word_string[0].upper():
            translation = english_word_string + 'way'
        else:
            translation = english_word_string + 'way'
    else:
        if english_word_string == all_caps:
            translation = english_word_string[1:] + english_word_string[0] + 'AY'
        elif english_word_string[0] == english_word_string[0].upper():
            translation = english_word_string[1].upper() + english_word_string[2:]\
                          + english_word_string[0].lower() + 'ay'
        else:
            translation = english_word_string[1:] + english_word_string[0] + 'ay'

    return translation


word_1 = 'Finn'
word_2 = 'Boise airport'
word_3 = 'puppy'
word_4 = 'equine'
word_5 = 'TESLA'
word_6 = 'ACROBAT'
print(pig_latin(word_1))
print(pig_latin(word_2))
print(pig_latin(word_3))
print(pig_latin(word_4))
print(pig_latin(word_5))
print(pig_latin(word_6))

# TODO: Handle Punctuation: if a word ends with punctuation, then
# that punctuation should be shifted to the end of the translated word.

# TODO: Consider an alternative version of Pig Latin