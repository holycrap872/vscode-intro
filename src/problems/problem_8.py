#!/usr/bin/env python3


def fibonacci(desired_len):
    """
    This function takes a single input: an integer. It then returns a list of
    integers of the given length filled with the Fibonacci numbers.

    :param desired_len: The number of fibonacci numbers to produce
    """
    # Replace the code below with your own code
    if desired_len <= 0:
        return []
    elif desired_len == 1:
        return [1]
    elif desired_len == 2:
        return [1, 1]
    else:
        ret = [1, 1]
        for i in range(2, desired_len):
            ret.append(ret[-1] + ret[-2])
        return ret


assert fibonacci(0) == []
assert fibonacci(-10) == []
assert fibonacci(1) == [1]
assert fibonacci(5) == [1, 1, 2, 3, 5]
assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]
print("Woohoo! All tests have been passed for Problem 8!")
