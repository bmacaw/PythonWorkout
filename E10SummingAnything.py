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
def my_sum_bigger_than(threshold_value, *items):
    """Sum items, which should be of the same type.
    Ignore any below the value of threshold.
    The arguments should handle the + operator.
    If passed no arguments, then return an empty tuple.
    """

    if not items:
        return items

    result = 0

    for item in items:
        if item > threshold_value:
             result += item

    return result


print(my_sum_bigger_than(10, 5, 20, 30, 6))  # => 50


# Write a function, sum_numeric() that takes any number of arguments. If the
# argument is or can be turned into an integer, then it should be added to the
# total. Arguments that can't be handled as integers should be ignored. The
# result is the sum of the numbers. Thus sum_numeric(10, 20, 'a', '30', 'bcd')
# would return 60 (the string '30' is converted into the int 30)
def sum_numeric(*args):
    """Sum all argument items, assuming that they
    are integers or can be turned into integers.
    """

    total = 0

    for item in args:
        try:
            total += int(item)
        except ValueError:
            pass
    return total


print(sum_numeric(10, 20, 'a', '30', 'bcd'))  # => 60


# Write a function that takes a list of dicts and returns a single dict that
# combines all of the keys and values. If a dey appears in more than one
# argument, the value should be a list containing all of the values from the
# arguments.
def combine_dicts(*dictionaries):
    """Return a dict, the result of combining all
    elements of args (which should be dicts). If a key
    occurs in more than one, then the value should be a list
    containing all values from the arguments.
    """
    result = {}
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            if key in result:
                try:
                    result[key].append(value)
                except AttributeError:
                    result[key] = [result[key], value]
            else:
                result[key] = value

    return result


dict_1 = {1:'blue', 2: 'red', 3: 'yellow'}
dict_2 = {1: 'blew', 2: 'read'}
print(combine_dicts(dict_1, dict_2))  # => {1: ['blue', 'blew'], 2: ['red', 'read'], 3: 'yellow'}
