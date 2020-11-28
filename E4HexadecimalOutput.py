# Write a function (hex_output) that takes a hex number and returns the decimal
# equivalent.

def hex_output():
    dec_num = 0
    hex_num = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16 ** power)
    print(dec_num)


hex_output()


# Beyond the Exercise:

# Reimplement the solution for this exercise such that it doesn't use the int
# function at all, but rather uses the built-in ord a chr functions to identify
# the character.
""" Solution to chapter 1, exercise 4, beyond 1: ord_hex"""


def ord_hex_output():
    """Get a hex number to convert. Use ord to turn it into an integer,
    and print the decimal equivalent.
    """

    dec_num = 0
    dec_digit = 0
    hex_num = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hex_num)):
        if 48 <= ord(digit) <= 57:
            dec_digit = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dec_digit = ord(digit) - 87

        dec_num += dec_digit * (16 ** power)
    print(dec_num)


ord_hex_output()

# Write a program that asks the user for their name and then produces
# a "name" triangle": the first letter of their name, then the first
# two letters, then the first three, and so forth, until the entire
# name is written on the final line.
"""Solution to chapter 1, exercise 4 beyond 2: name_triangle"""


def name_triangle():
    """Get the user's name. Print a name triangle, starting
    with the first letter, then the first two letters, etc.
    """

    name = input("Enter your name: ")

    for i in range(len(name)):
        print(name[:i+1])


name_triangle()
