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
