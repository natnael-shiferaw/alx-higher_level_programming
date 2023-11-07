#!/usr/bin/python3

"""This Python file is used to define
a function named from_json_string."""
import json


def from_json_string(my_str):
    """A function that returns an
    object (Python data structure) represented
    by a JSON string"""
    return json.loads(my_str)
