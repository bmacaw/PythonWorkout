# This function simulates Python's sum() function
def mySum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output


print(mySum(1, 2, 3))  # Expect 6
# The sum()
print(sum([1, 2, 3]))  # Expect 6
print(mySum(*[1, 2, 3]))  # Expect 6
# print(sum(1, 2, 3))  # Expect 6, but get TypeError: sum() takes at most 2 arguments (3 given)

# "Beyond the Exercise" challenges

# 1. Reimplement mySum so that it adds starting number like sum()
# does with optional second argument. Should default to 0 if no
# second arg


def mySumTwo(numbers, start_num=0):
    output = start_num
    for number in numbers:
        output += number
    return output


print(mySumTwo([1, 2, 3], 4))  # Expect 10
print(mySumTwo([1, 2, 3]))  # Expect 6 YES!!! I'm sooo awesome!

# 2. Write a function that takes a list of numbers and returns the average


def num_ave(numbers):
    output = 0
    count = 0
    for number in numbers:
        output += number
        count += 1
    return output / count


print(num_ave([1, 2, 3]))  # Expect 2.0 Yes! :D I'm so awesome


# 3. Write a function that takes a list of words (strings). It should
# return a tuple containing 3 integers, the length of shortest word, length
# of longest word and the average word length

def word_fun(words):
    shortest = min(len(word) for word in words)
    longest = max(len(word) for word in words)
    total_letter_count = 0
    for word in words:
        letter_count = 0
        for letter in word:
            letter_count += 1
        total_letter_count += letter_count

    letter_ave = total_letter_count / len(words)

    return shortest, longest, letter_ave


print(word_fun(['blue', 'green', 'purple', 'magenta']))  # Expect (4, 7, 5.5) :D
# Write a function that takes a list of numbers, and returns the average


def ave_num(num_list):
    num_count = sum(num_list)
    num_numz = len(num_list)
    return num_count / num_numz

print(ave_num([10, 20, 30, 40, 50]))  # Expect 30.0 :D omg i already did this


# THIS IS NOT A CORRECT SOLUTION YET. The directions were to "write a function that
# takes a list of Python objects. Sum the objects that either are integers or can
# be turned into integers, ignoring the others. Note: Book solution follows*
def is_int(objects):
    sumz = 0
    for object in objects:
        if object is int or object is float:
            sumz += object
        elif object is str:
            pass
    return sumz


print(is_int([2,'pickle',4.0]))  # Expect 6

# * #!/usr/bin/env python3
# """Solution to chapter 1, exercise 2, beyond 4: sum intable"""
#
#
def is_intable(one_item):
     try:
         int(one_item)
         return True
     except ValueError:
         return False


def sum_intable(items):
     """Accepts a list of Python objects.
 Sums those objects that are integers or can be
 turned into integers.
 """

     return sum(one_item
                for one_item in items
                if is_intable(one_item))


print(sum_intable([2, 'pickle', 4.0]))  # Expect 6.0 yes!




