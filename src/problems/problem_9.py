#!/usr/bin/env python3


def primes(max_num):
    """
    This function takes a single input: an integer. It then returns all the
    prime numbers less than **or equal to** that number.

    :param max_num: The maximum to check for whether it's prime or not
    """
    # Replace the code below with your own code
    return [2, 3, 5]


assert primes(0) == []
assert primes(1) == []
assert primes(-10) == []
assert primes(10) == [2, 3, 5, 7]
assert primes(13) == [2, 3, 5, 7, 11, 13]
print("Woohoo! All tests have been passed for Problem 9!")
