#!/usr/bin/python3

"""This Python file is used to define
a function for appending a file."""


def append_write(filename="", text=""):
    """A Function that is used to append
    a string to the end of  a UTF8 text file.

    Args:
        filename (str): represents the name of the file.
        text (str): represents the string to append to the file.
    Returns:
        The number of appended characters.
    """

    with open(filename, "a", encoding="utf-8") as fn:
        return fn.write(text)
