#!/usr/bin/env python3


def first_and_last_letter(word):
    """
    This function returns the first and last letter of a word. Note: if the
    word is too short, the the function returns "too short".

    :param word: The word to slice
    """
    # Replace the code below with your own code
    if len(word) <= 1:
        return "too short"
    else:
        return word[0] + word[-1]


assert first_and_last_letter("y") == "too short"
assert first_and_last_letter("") == "too short"
assert first_and_last_letter("umbrella") == "ua"
assert first_and_last_letter("yolo") == "yo"
print("Woohoo! All tests have been passed for Problem 2!")
