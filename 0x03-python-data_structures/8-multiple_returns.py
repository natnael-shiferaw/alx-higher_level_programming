#!/usr/bin/python3


def multiple_returns(sentence):

    """This program is used to return the length
    of a string and it's first character."""

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
