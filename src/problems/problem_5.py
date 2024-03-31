#!/usr/bin/env python3


def any_dogs(word_list):
    """
    This function checks a list of words to see if there are any instances of
    the word "dog". If there is, then the function returns "dogs seen".
    Otherwise, the function returns "no dogs".
    """
    for a in word_list:
        if a.lower() == "dog":
            return "dogs seen"
    return "no dogs"


assert any_dogs(["llama", "horse", "dog", "cat"]) == "dogs seen"
assert any_dogs(["Llama", "Horse", "Dog", "cat"]) == "dogs seen"
assert any_dogs(["dog"]) == "dogs seen"
assert any_dogs(["Cat"]) == "no dogs"
assert any_dogs(["cat", "cat", "not sure but not a dog"]) == "no dogs"

print("Woohoo! All tests have been passed for Problem 5!")
