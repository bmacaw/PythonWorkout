# Redefine the mysum() function we defined in chapter 1
# such that it can take any number of arguments. The args
# must all be of the same type and know how to respond to
# the + operator. (Thus, the function should work with
# numbers, strings, lists and tuples, but not with sets
# and dicts.) Note: Python 3.9 (Fall 2020) will include
# support for dicts--so note to self: try this! :)


def mySum(*list_items):
    if not list_items:
        return list_items

    result = list_items[0]

    for list_item in list_items[1:]:
        result += list_item

        return result


print(mySum(10, 20, 30, 40))