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


# Remove author names: Given a string containing an article and
# a separate list of strings containing authors' names, replace all
# names in the article with _characters.
def remove_authors(article, author_list):
    article_with_names_replaced = article

    for name in author_list:
        # I had the gist of this-yay-but got the '_' * part from solution-cool!
        article_with_names_replaced = article_with_names_replaced.replace(name, '_' * len(name))

    return article_with_names_replaced


text = 'This is an incredible article written by three amazing authors, the famous Alice, Bob and Malice.'
author_list = ['Alice', 'Bob', 'Malice']
print(remove_authors(text, author_list)) # returns This is an incredible article written by three amazing
# authors, the famous _____, ___ and ______.

# URL-encode characters: In URL's we often replace special and nonprintable characters
# with a % followed by the character's ASCII value in hexadecimal. For example, if a
# URL is to include a space character ASCII 32, aka 0x20), we replace it with %20. Given
# a string, URL-encode any character that isn't a letter or number. For the purposes of
# this exercise, we'll assume that all characters are indeed in ASCII (i.e., one byte
# long), and not multibyte UTF-8 characters. It might help to know about ord() and hex().

# From author's solution:
# import string


def url_encode(text):
    """Given a string, replace any character that isn't
    a letter or number with % and its two-digit hex code.
    """
    safe_chars = string.ascii_letters + string.digits
    output = []

    for one_character in text:
        if one_character in safe_chars:
            output.append(one_character)
        else:
            output.append(hex(ord(one_character)).replace('0x', '%'))

    return ''.join(output)


my_text = 'Are you a !@#$%^&*() Trumpster?'
print(url_encode(my_text)) # Output: Are%20you%20a%20%21%40%23%24%25%5e%26%2a%28%29%20Trumpster%3f  haha!






