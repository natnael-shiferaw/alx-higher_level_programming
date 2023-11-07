#!/usr/bin/python3

"""This python file is used to Define
a function used for text file-reading."""


def read_file(filename=""):
    """A function that is used to Print
    the contests of a UTF8 text file to stdout."""

    with open(filename, encoding="utf-8") as fn:
        print(fn.read(), end="")
