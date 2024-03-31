#!/usr/bin/env python3


def roller_coaster_rules(height_ft, height_in):
    """
    This function is in charge of determining whether someone is allowed onto a
    roller coaster. If they are greater than 5'6", then the value "allowed"
    should be returned. Otherwise, "nope" should be returned.

    Hints:
    - If they're 4 feet tall (or shorter), inches don't matter: they're too short.
    - If they're 6 feet tall (or taller), inches don't matter: they're allowed.
    - Only when they're 5 feet tall do we actually have to check the inches part

    :param height_ft: The height of the patron in feet
    :param height_in: The remaining inches of the patron's height
    """
    if height_ft >= 6:
        return "allowed"
    elif height_ft <= 4:
        return "nope"
    elif height_in >= 6:
        return "allowed"
    else:
        return "nope"


assert roller_coaster_rules(4, 1) == "nope"
assert roller_coaster_rules(4, 11) == "nope"
assert roller_coaster_rules(5, 2) == "nope"
assert roller_coaster_rules(5, 5) == "nope"
assert roller_coaster_rules(5, 6) == "allowed"
assert roller_coaster_rules(5, 7) == "allowed"
assert roller_coaster_rules(6, 1) == "allowed"
assert roller_coaster_rules(6, 11) == "allowed"
print("Woohoo! All tests have been passed for Problem 4!")
