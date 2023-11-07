#!/usr/bin/python3

"""This Python file is used to define
a function named class_to_json."""


def class_to_json(obj):
    """A function that returns the dictionary
    representation of a simple data structure."""
    return obj.__dict__
