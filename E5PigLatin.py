# Write a Python function (pig_latin) that takes a string as input,
# assumed to be an English word. The function should return the
# translation of this word into Pig Latin.

def limited_pig_latin(english_word_string):
    vowels = 'a', 'e', 'i', 'o', 'u'
    if english_word_string[0] in vowels:
        return english_word_string + 'way'
    else:
        return english_word_string[1:-1] + english_word_string[0].lower() + 'ay'

# Beyond the exercise:
# Handle capitalized words


def pig_latin_caps_too(english_word_string):
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


# Handle Punctuation: if a word ends with punctuation, then
# that punctuation should be shifted to the end of the translated word.


def pig_latin_complete(english_word_string):
    vowels = 'aeiouAEIOU'
    punctuation = ''
    all_caps = english_word_string.upper()

    if english_word_string[-1] in '?!.':
        punctuation = english_word_string[-1]
        english_word_string = english_word_string[:-1]

    if english_word_string[0] in vowels:
        if english_word_string == all_caps:
            translation = english_word_string + 'WAY' + punctuation
        elif english_word_string[0] == english_word_string[0].upper():
            translation = english_word_string + 'way' + punctuation
        else:
            translation = english_word_string + 'way' + punctuation
    else:
        if english_word_string == all_caps:
            translation = english_word_string[1:] + english_word_string[0] + 'AY' + punctuation
        elif english_word_string[0] == english_word_string[0].upper():
            translation = english_word_string[1].upper() + english_word_string[2:]\
                          + english_word_string[0].lower() + 'ay' + punctuation
        else:
            translation = english_word_string[1:] + english_word_string[0] + 'ay' + punctuation

    return translation


# Consider an alternative version of Pig Latin


def my_latin():
    word_list = []
    word_count = 0
    print('Enter five words to translate at the prompt.')
    while word_count < 5:
        my_word = input('Enter a word: ')
        word_list.append(my_word)
        word_count += 1
    my_ending = input('Enter any one syllable three letter (cvc) word ending: ')

    for word in word_list:
        this_word = word
        vowels = 'aeiou'
        punctuation = ''

        if this_word[-1] in '?!.':
            punctuation = this_word[-1]
            this_word = this_word[:-1]

        if this_word[0].lower() in vowels:
            all_caps = this_word.upper()
            v_case = my_ending
            v_u_case = my_ending.upper()

            if this_word == all_caps:
                translation = f'{this_word}{v_u_case}{punctuation}'
            elif this_word[0] == this_word[0].upper():
                translation = f'{this_word}{v_case}{punctuation}'
            else:
                translation = f'{this_word}{v_case}{punctuation}'
        else:
            c_case = my_ending[1:]
            c_u_case = my_ending[1:].upper()
            all_caps = this_word.upper()
            if this_word == all_caps:
                translation = f'{this_word[1:]}{this_word[0].upper()}{c_u_case}{punctuation}'
            elif this_word[0] == this_word[0].upper():
                translation = f'{this_word[1].upper()}{this_word[2:]}' \
                              f'{this_word[0].lower()}{c_case}{punctuation}'
            else:
                translation = f'{this_word[1:]}{this_word[0]}{c_case}{punctuation}'

        print(translation)