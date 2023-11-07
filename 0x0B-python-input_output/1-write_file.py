#!/usr/bin/python3

"""This is a Python file that is used to
Define a function used for file-writing."""


def write_file(filename="", text=""):
    """A function that is used to write
    a string to a UTF8 text file.

    Args:
        filename (str): reprsents the name of the file.
        text (str): represents the text to write to the file.
    Returns:
        returns the number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
