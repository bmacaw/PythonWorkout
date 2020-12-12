# Translate a series of English words into Pig Latin
# Write a function called pl_sentence that takes a string containing
# several words separated by spaces. Don't have to handle 'real sentences,
# punctuation or capitals. Example: pl_sentence('this is a test translation')
# should output: histay isway away esttay ranslationtay

def pl_sentence(words_string): # From author's solution
    word_list = []
    vowels = 'aeiou'
    for word in words_string.split():
        if word[0] in vowels:
            word_list.append(f'{word}way')
        else:
            word_list.append(f'{word[1:]}ay')

    return ' '.join(word_list)


print(pl_sentence('this is a test translation'))


# Beyond the exercise: # ALL course/author's solutions (none are mine)
# Take a text file, creating (and printing) a nonsensical sentence from the nth
# word on each of the first 10 lines, where n is the line number.
"""Solution to chapter 2, exercise 6, beyond 1: Word per line"""
def word_per_line(filename):
    """Given a text file, return a sentence from the nth word for line n,
    for each of the first 10 lines.
    """
    output = []

    for n, one_line in enumerate(open(filename)):
        words = one_line.split()

        if not words:
            continue

        if n >= 10:
            break

        if n >= len(words):
            output.append(words[-1])
        else:
            output.append(words[n])

    return ' '.join(output)
print(word_per_line("wordperlinetest.txt"))

# Write a function that transposes a list of strings, in which each string contains
# multiple words separated by whitespace. Specifically, it should perform in such a
# way that if you were to pass the list['abc def ghi', 'jkl mno pqr', 'stu vwx yz'] to
# the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']
"""Solution to chapter 2, exercise 6, beyond 2: Tranpose strings"""


def transpose_strings(word_list):
    """Given a list of strings, each of which contains multiple
    words, transpose them.
    """

    return [' '.join(t)
            for t in (zip(*[s.split()
                            for s in word_list]))]


word_list_one = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
print(transpose_strings(word_list_one))

# Read through an Apache logfile. If there is a 404 error--you can just search for
# ' 404 ', if you want--display the IP address, which should be the first element.
"""solution to chapter 2, exercise 6, beyond 3: IP addresses with 404"""


def ips_for_404s(filename):
    """Given the name of an Apache logfile,
    print the IP address where the response code is 404

    """
    for one_line in open(filename):
        if ' 404 ' in one_line:
            print(one_line.split()[0])

# I spent some time finding out about Apache files, but not
# sure how to test, haha. Need sample_apache_file_with_404 :)