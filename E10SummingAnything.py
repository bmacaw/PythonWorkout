# Redefine the mysum() function we defined in chapter 1
# such that it can take any number of arguments. The args
# must all be of the same type and know how to respond to
# the + operator. (Thus, the function should work with
# numbers, strings, lists and tuples, but not with sets
# and dicts.) Note: Python 3.9 (Fall 2020) will include
# support for dicts--so note to self: try this! :)


# Author's solution
def mySum(*list_items):
    if not list_items:
        return list_items

    result = list_items[0]

    for list_item in list_items[1:]:
        result += list_item

    return result


print(mySum())  # => ()
print(mySum(10, 20, 30, 40))  # => 100
print(mySum('a', 'b', 'c', 'd'))  # => abcd
print(mySum([10, 20, 30], [40, 50, 60], [70, 80]))  # => [10, 20, 30, 40, 50, 60, 70, 80]


# Beyond the Exercise
# Write a function my_sum_bigger_than() that works the same as mySum(),
# except that it works for an argument that precedes *args. That argument
# indicates the threshold for including an argument in the sum. Thus, calling
# my_sum_bigger_than(10, 5, 20, 30, 6) would return 50 because 5 and 6 aren't
# greater than 10. The function should work with any type and assumes all
# args are same type.



# Write a function, sum_numeric() that takes any number of arguments. If the
# argument is or can be turned into an integer, then it should be added to the
# total. Arguments that can't be handled as integers should be ignored. The
# result is the sum of the numbers. Thus sum_numeric(10, 20, 'a', '30', 'bcd')
# would return 60 (the string '30' is converted into the int 30)

# Write a function that takes a list of dicts and returns a single dict that
# combines all of the keys and values. If a dey appears in more than one
# argument, the value should be a list containing all of the values from the
# arguments.

