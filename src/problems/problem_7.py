#!/usr/bin/env python3


def look_smart(sentence):
    """
    This function replaces all the words in a sentence that are short (less than
    three letters) with "paradigm shifting" just to look smart.

    :param sentence: The phrase to make smarter
    """
    # Replace the code below with your own code
    smart_sentence = ""
    for word in sentence.split():
        if len(word) <= 3:
            smart_sentence += " paradigm shifting"
        else:
            smart_sentence = smart_sentence + " " + word

    return smart_sentence.strip()


assert look_smart("This seems fun") == "This seems paradigm shifting"
assert look_smart("Hi there Dan") == "paradigm shifting there paradigm shifting"
assert look_smart("This sentence refuses words below length four") == "This sentence refuses words below length four"
assert look_smart("yo") == "paradigm shifting"
assert look_smart("encyclopedia") == "encyclopedia"
print("Woohoo! All tests have been passed for Problem 7!")
