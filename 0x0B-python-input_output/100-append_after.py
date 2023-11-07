#!/usr/bin/python3

"""This Python file is used to Define
a function for text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """A function that is used for inserting
    text after each line that contains a
    given string in a file.

    Args:
        filename (str):represents the name of the file.
        search_string (str): represents the string to be
        searched in the file.
        new_string (str): represents the string to insert.
    """

    Text = ""

    with open(filename) as fn:
        for line in fn:
            Text += line
            if search_string in line:
                Text += new_string

    with open(filename, "w") as w:
        w.write(Text)
