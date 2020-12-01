# Translate a series of English words into Pig Latin
# Write a function called pl_sentence that takes a string containing
# several words separated by spaces. Don't have to handle 'real sentences,
# punctuation or capitals. Example: pl_sentence('this is a test translation')
# should output: histay isway away esttay ranslationtay

def pl_sentence(words_string):
    word_list = []
    vowels = 'aeiou'
    for word in words_string.split():
        if word[0] in vowels:
            word_list.append(f'{word}way')
        else:
            word_list.append(f'{word[1:]}ay')

    return ' '.join(word_list)


print(pl_sentence('this is a test translation'))