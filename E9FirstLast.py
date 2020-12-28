# Write a function firstlast() that takes a sequence (string, list, or tuple)
# and returns the first and last elements of that sequence, in a two-element
# sequence of the same type. Example: firstlast('abc') will return the string ac
# while firstlast([1,2,3,4]) will return the list [1,4].


def firstlast(a_sequence):
    return a_sequence[:1] + a_sequence[-1:]  # Use slices which return a new object of the same type


seq_1 = 'abc'
seq_2 = ['a', 'b', 'c']
seq_3 = ('a', 'b', 'c')
seq_4 = '1b3'
seq_5 = [1, 'b', 3]
seq_6 = (1, 'b', 3)
my_sequences = [seq_1, seq_2, seq_3, seq_4, seq_5, seq_6]
for sequence in my_sequences:
    print(firstlast(sequence))


# ac
# ['a', 'c']
# ('a', 'c')
# 13
# [1, 3]
# (1, 3)

# Beyond the Exercise:
# Write a function that takes a list or tuple of numbers. Return a 2-element
# list containing (respectively) the sum of the even-indexed numbers and the
# sum of the odd-indexed numbers. Example: even_odd_sums([10, 20, 30, 40, 50, 60])
# returns [90, 120]


def even_odd_sums(numbers):
    return [(sum(numbers[0::2])), (sum(numbers[1::2]))]


number_list = [10, 20, 30, 40, 50, 60]
number_tuple = (10, 20, 30, 40, 50, 60)
print(even_odd_sums(number_list))
print(even_odd_sums(number_tuple))


# Expect [90, 120] :D yay!


# Write a function that takes a list or tuple of numbers. Return the result of
# alternately adding or subtracting numbers from each other.
# Example: plus_minus([10, 20, 30, 40, 50, 60]) => 10+20-30+40-50+60, or 50.


def plus_minus(numbers):
    return numbers[0] + (sum(numbers[1::2])) - (sum(numbers[2::2]))


number_list = [10, 20, 30, 40, 50, 60]
number_tuple = (10, 20, 30, 40, 50, 60)
print(plus_minus(number_list))
print(plus_minus(number_tuple))


# Expect 50 :D yay!


# Write a function that partially emulates the built-in zip function, taking
# any number of iterables and returning a list of tuples. Each tuple will
# contain one element from each of the iterables passed to the function.
# Example: my_zip([10, 20, 30], 'abc') => [(10, 'a'), (20, 'b'), (30, 'c)].
# You can return a list (not an iterator) and can assume that all of the
# iterables are of the same length.


def my_zip(*args):  # From solution (first time today!)
    """Takes any number of iterables, returning a list of
    tuples. The tuple at index n will contain the items from
    index n in each iterable. we can assume that all of the iterables
    have the same length.
    """
    return [tuple(a[i] for a in args) for i in range(len(min(args, key=len)))]


print(my_zip([10, 20, 30], 'abc'))  # => [(10, 'a'), (20, 'b'), (30, 'c')]


#
