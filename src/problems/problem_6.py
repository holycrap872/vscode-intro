#!/usr/bin/env python3


def sum_of_positive_integers_in_list(int_list):
    """
    This function adds all of the positive integers in a list and returns the
    result.

    :param l: The list of numbers
    """
    # Replace the code below with your own code
    s = 0
    for e in int_list:
        if e > 0:
            s = s + e
    return s


assert sum_of_positive_integers_in_list([1, 2, 3, 4]) == 10
assert sum_of_positive_integers_in_list([1, 2, -4, -6, 3, 4]) == 10
assert sum_of_positive_integers_in_list([-5, -1, -2]) == 0
assert sum_of_positive_integers_in_list([]) == 0
assert sum_of_positive_integers_in_list([1, 1, 1, 1, 1, 1, 1]) == 7
print("Woohoo! All tests have been passed for Problem 6!")
