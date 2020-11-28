from decimal import Decimal

# Write a function (run_timing) that asks how long it took for you
# to run 10 km. The function continues to ask how long (in minutes)
# it took for additional runs, until the user presses Enter. At that
# point, the function exits--but only after calculating and displaying
# the average time that the 10 km runs took.
# Example output:
# Enter 10 km run time: 15
# Enter 10 km run time: 20
# Enter 10 km run time: 10
# Enter 10 km run time: <enter>
#
# Average of 15.0, over 3 runs


def run_timing():
    number_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:  # If one_run is an empty string, stop
            break

        number_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_runs

    print(f'Average of {average_time}, over {number_runs} runs')

run_timing()


# Beyond the Exercise
# 1. Write a function that takes a float and two integers (before and after). The
# function should return a float consisting of before digits before the decimal and
# after digits after. Thus, if we call the function with 1234.5678, 2 and 3, the
# return value should be 34.567.

def before_after_dot(f, before, after):
    """Accepts a float, and two integers.

Returns a float containing before digits preceding the decimal point,
and after digits following the decimal point.
"""
    s = str(f)
    i = s.index('.')
    return s[i-before:i+after+1]

print(before_after_dot(1234.5678, 2, 3))

# 2. Write a function that takes two strings from the user, turns them into decimal
# instances, and then prints the floating-point sum of the user's two inputs. In
# other words, make it possible for the user to enter 0.1 and 0.2, and for us to
# get 0.3 back.


def decimal_add(first, second):
    """Accepts two strings, turns them into decimals, and returns a float
representing the sum of these two.
"""
    return float(Decimal(first) + Decimal(second))


print(decimal_add(0.1, 0.2))  # I get 0.30000000000000004, not 0.3, using the course solution...?

