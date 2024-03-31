#!/usr/bin/env python3


def largest_input(num_1, num_2, num_3):
    """
    This function returns the largest of three inputs.

    :param num_1: The first number
    :param num_2: The second number
    :param num_3: The third number
    """
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_3:
        return num_2
    else:
        return num_3


assert largest_input(1, 2, 3) == 3
assert largest_input(6, 5, 4) == 6
assert largest_input(10, 11, 9) == 11
assert largest_input(10, 1000, 20) == 1000
print("Woohoo! All tests have been passed for Problem 3!")
