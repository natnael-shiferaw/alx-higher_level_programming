#!/usr/bin/python3

"""This Python file is used to define
a function named load_from_json_file."""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file."""

    with open(filename) as fn:
        return json.load(fn)
