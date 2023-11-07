#!/usr/bin/python3

"""This Python file is used to define
a function named save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """A Function that writes an Object to
    a text file, using a JSON representation."""

    with open(filename, "w") as fn:
        json.dump(my_obj, fn)
